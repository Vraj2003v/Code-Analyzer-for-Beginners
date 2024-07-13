from flask import Flask, render_template, request
import re
import ast
import subprocess
from token_explainer import explain_token  # Ensure this module is implemented correctly
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

app = Flask(__name__)

def break_code(code):
    token_matches = re.finditer(r'[\w.]+|[^\s\w]', code)
    unique_tokens = set()
    tokens = []
    for match in token_matches:
        token = match.group(0)
        if token not in unique_tokens:
            tokens.append(token)
            unique_tokens.add(token)
    return tokens

def check_syntax(code, language):
    if language == 'python':
        try:
            ast.parse(code)
            return True, ""
        except SyntaxError as e:
            return False, f"Syntax error at line {e.lineno}: {e.msg}"
    return True, ""

def run_code(language, code, user_inputs=None):
    try:
        if language == 'python':
            python_executable = 'python3' if subprocess.run(['python3', '--version'], 
                                                            capture_output=True).returncode == 0 else 'python'
            result = subprocess.run([python_executable, '-c', code], input=user_inputs, capture_output=True,
                                    text=True)
            stdout, stderr = result.stdout, result.stderr

        elif language == 'c':
            filename = 'temp_code.c'
            executable = 'temp_code.exe'
            with open(filename, 'w') as f:
                f.write(code)
            compile_cmd = ['gcc', filename, '-o', executable]
            compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)
            if compile_result.returncode != 0:
                return False, compile_result.stderr  # Capture and return compilation errors
            result = subprocess.run([executable], input=user_inputs, capture_output=True, text=True)
            stdout, stderr = result.stdout, result.stderr

        elif language == 'c++':
            filename = 'temp_code.cpp'
            executable = 'temp_code.exe'
            with open(filename, 'w') as f:
                f.write(code)
            compile_cmd = ['g++', filename, '-o', executable]
            compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)
            if compile_result.returncode != 0:
                return False, compile_result.stderr  # Capture and return compilation errors
            result = subprocess.run([executable], input=user_inputs, capture_output=True, text=True)
            stdout, stderr = result.stdout, result.stderr

        elif language == 'java':
            filename = 'TempCode.java'
            with open(filename, 'w') as f:
                f.write(code)
            compile_result = subprocess.run(['javac', filename], capture_output=True, text=True)
            if compile_result.returncode != 0:
                return False, compile_result.stderr  # Capture and return compilation errors
            result = subprocess.run(['java', 'TempCode'], input=user_inputs, capture_output=True, text=True)
            stdout, stderr = result.stdout, result.stderr

        else:
            return False, f"Unsupported language: {language}"

        if stderr:
            return False, stderr  # Capture and return runtime errors
        return True, stdout

    except Exception as e:
        return False, str(e)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    language = request.form['language'].lower()
    code = request.form['code']
    user_inputs = request.form['user_inputs'] if 'user_inputs' in request.form else None
    
    is_valid_syntax, syntax_error_message = check_syntax(code, language)
    if not is_valid_syntax:
        return render_error(syntax_error_message)
    
    success, output = run_code(language, code, user_inputs)
    if not success:
        return render_error(output)
    
    try:
        tokens = break_code(code)
        token_explanations = {token: explain_token(token, language) for token in tokens}
        
        lexer = get_lexer_by_name(language)
        formatter = HtmlFormatter(linenos=True, cssclass="source")
        highlighted_code = highlight(code, lexer, formatter)
        css = formatter.get_style_defs('.source')
        
        token_classes = {token: 'token-highlight' for token in tokens}
        
        return render_template('result.html', token_explanations=token_explanations, highlighted_code=highlighted_code, css=css, token_classes=token_classes, output=output)
    
    except ClassNotFound:
        error_message = f"The language '{language}' is not supported for syntax highlighting."
        return render_error(error_message)
    
    except ValueError as ve:
        error_message = str(ve)
        return render_error(error_message)
    
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return render_error(error_message)

def render_error(message):
    return render_template('error.html', error_message=message)

if __name__ == "__main__":
    app.run(debug=True)