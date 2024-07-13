import re

def explain_token(token,language):
    if token.isdigit():
        return f"'{token}' is a number."
    
    
    elif token in ["auto","const","extern","register","signed","sizeof","static","typedef",
                    "unsigned","virtual","delete","inline","mutable","new","java.io","throw","interface","False","True","None",
                    "and","as","from","global","in","is","lambda","not","or"
                    ,"raise","with","yield"]:
       return f"'{token}' this ({language} Syntax): 'it is a keyword."
   
   
    elif token in ["include"]:
        return f"'{token}' ({language} Syntax): 'it is use to specify/include the libraries."
    
    elif token in ["System.in"]:
        return f"'{token}'({language} Syntax): 'input stream class."
    elif token in ["System.out"]:
        return f"'{token}' ({language} Syntax): 'print stream class."
    elif token in ["import.java.util.Scanner"]:
        return f"'{token}' ({language} Syntax): 'it's provide meathod for reading input of different datatype from various sources ."
    elif token in ["this"]:
        return f"'{token}' ({language} Syntax): 'this is a reference variable that refers to the current object.."
    elif token in ["try","except","finally","catch"]:
        return f"'{token}' ({language} Syntax): 'block can be used to ensure that certain cleanup or resource release operations are always executed, regardless of whether an exception occurs."
    elif token in ["throws"]:
        return f"'{token}' ({language} Syntax): 'it is used in meathod declaration to indicate that the method may throw one or more specified exceptions."
    elif token in ["import matplotlib.pyplot as plt"]:
        return f"'{token}'({language} Syntax): 'it is used for creating static,interactive and animated visulizations."
     
    elif token in ["args","args[]"]:
        return f"'{token}' ({language} Syntax): 'It is used for parameter passed to the main method." 
    elif token in ["String","Strings[]"]:
        return f"'{token}' ({language} Syntax): 'it represents sequences of character."
    
    elif token in ["def"]:
        return f"'{token}' ({language} Syntax): 'define a function in Python:."  
    elif token in ["numpy"]:
        return f"'{token}'  ({language} Syntax): 'for numerical computing." 
    elif token in ["pandas"]:
        return f"'{token}'  ({language} Syntax): 'for data manupulation and analysis."
    elif token in ["list"]:
        return f"'{token}' ({language} Syntax): 'collection of elements,ordered and mutable,represented by square bracket."
    elif token in ["dict"]:
        return f"'{token}' ({language} Syntax): 'collection of key value pairs unorderd and mutable,represented by curly bracket."
    elif token in ["tuple"]:
        return f"'{token}'  ({language} Syntax): 'collection of elements ordered and immutable,represented by parentheses."
    
    elif token in ["+", "-", "*", "/", "%", "++", "--"]:
        return f"'{token}'  ({language} Syntax): 'Arithmatic operators."
    elif token in ["<", ">", "=", "==", "!=", "<=", ">="]:
        return f"'{token}' ({language} Syntax): 'Relational operators."
    elif token in ["&&", "||", "!"]:
        return f"'{token}'  ({language} Syntax): 'Logical operators."
    elif token in ["+=", "-=", "*=", "/=", "%="]:
        return f"'{token}' ({language} Syntax): 'Assignment operators."
    elif token in ["?:"]:
        return f"'{token}'  ({language} Syntax): 'Turney operators."

    elif token in ["[", "]"]:
        return f"'{token}'  ({language} Syntax): 'Is commonly used to define arrays or lists."
    elif token in ["(", ")"]:
        return f"'{token}' ({language} Syntax): 'Is used for mathematical expressions and function calls."
    elif token in ["{", "}"]:
        return f"'{token}'  ({language} Syntax): 'Is used to define dictionaries and code blocks."

    elif token in ["if", "ifelse", "else", "elseif", "elif", "switch", "case"]:
        return f"'{token}'  ({language} Syntax): 'Conditional Statements"
    elif token in ["default"]:
        return f"'{token}'  ({language} Syntax): 'It is used to define a block of code to be executed if none of the specified cases match the value of the expression."
    elif token in ["break"]:
        return f"'{token}'  ({language} Syntax): 'It is used to terminate the execution of the switch block."
    elif token in ["continue"]:
        return f"'{token}'  ({language} Syntax): 'It is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration."
    elif token in ["return"]:
        return f"'{token}' ({language} Syntax): 'It is used to end the execution of the function and return a value to the user."
    elif token in ["goto"]:
        return f"'{token}'  ({language} Syntax): 'These statements allow jumping to a labeled section of code."

    elif token in [ "std","std:","std::"]:
        return f"'{token}' ({language} Syntax): 'It is used for standard input and output."
    elif token in ["scanf","cin","::cin",":cin","std::cin","Scanner","input"]:
        return f"'{token}' ({language} Syntax): 'This Function is commanly use for taking input from the user."
    elif token in ["printf","cout","::cout",":cout","std::cout","System.out.println","System.out.print","print"]:
        return f"'{token}' ({language} Syntax): 'This function is use to display the output."

    elif token in ["for", "while", "do", "do-while"]:
        return f"'{token}'  ({language} Syntax): 'It used to execute a block of code repeatedly until a certain condition is met."

    elif token in ["stdio.h", "stdlib.h", "math.h", "cstdlib", "cmath", "java.util", "java.lang", "java.math", "math"]:
        return f"'{token}'  ({language} Syntax): 'It commanly used libraries."
    elif token in ["iostream"]:
        return f"'{token}'  ({language} Syntax): 'It is a header file that provides functionality for input and output operations."

    elif token in ["int", "short", "long"]:
        return f"'{token}'  ({language} Syntax): 'It is a data type which takes general integer values."
    elif token in ["float", "double"]:
        return f"'{token}'  ({language} Syntax): 'It is a data type which takes fractional numbers."
    elif token in ["char", "string", "str"]:
        return f"'{token}'  ({language} Syntax): 'It is a data type which takes characters and strings."
    elif token in ["bool", "boolean"]:
        return f"'{token}'  ({language} Syntax): 'It is a data type which represents true and false values."
    elif token in ["void"]:
        return f"'{token}'  ({language} Syntax): 'Used in function return type when function does not return a value."
    elif token in ["array"]:
        return f"'{token}'  ({language} Syntax): 'It is a collection of elements with the same data type."
    elif token in ["pointer", "pointers"]:
        return f"'{token}'  ({language} Syntax): 'It is used to store the memory location of variables."
    elif token in ["struct", "structure"]:
        return f"'{token}'  ({language} Syntax): 'It is used to group the variables under a single name.'"
    elif token in ["union"]:
        return f"'{token}' ({language} Syntax): 'It is used to store different data types in"
    
    #new addedddddddd
    elif token in ["sqrt"]:
        return f"'{token}' ({language} Syntax): 'Returns the square root "
    elif token in ["pow"]:
        return f"'{token}' ({language} Syntax): 'Returns x raised to the power of y"
    elif token in ["fabs"]:
        return f"'{token}' ({language} Syntax): ' Returns the absolute value"
    elif token in ["ceil"]:
        return f"'{token}' ({language} Syntax): 'Returns the smallest integer greater than or equal "
    elif token in ["floor"]:
        return f"'{token}' ({language} Syntax): 'Returns the largest integer less than or equal" 
    elif token in ["sin","cos","tan"]:
        return f"'{token}' ({language} Syntax): 'Returns the trigonometric sine, cosine, and tangent of x"
    
    elif token in ["Math.sqrt"]:
        return f"'{token}' ({language} Syntax): 'Returns the square root"
    elif token in ["Math.pow"]:
        return f"'{token}' ({language} Syntax): 'Returns x raised to the power of y"
    elif token in ["Math.abs"]:
        return f"'{token}' ({language} Syntax): 'Returns the absolute value."
    elif token in ["Math.ceil"]:
        return f"'{token}' ({language} Syntax): 'Returns the smallest integer greater than or equal."
    elif token in ["Math.floor"]:
        return f"'{token}' ({language} Syntax): 'Returns the largest integer less than or equal "
    elif token in ["Math.sin","Math.cos","Math.tan"]:
        return f"'{token}' ({language} Syntax): 'Returns the trigonometric sine, cosine, and tangent"
    
    elif token in ["math.sqrt"]:
        return f"'{token}' ({language} Syntax): 'Returns the square root"
    elif token in ["math.pow"]:
        return f"'{token}' ({language} Syntax): 'Returns x raised to the power of y"
    elif token in ["math.abs"]:
        return f"'{token}' ({language} Syntax): 'Returns the absolute value."
    elif token in ["math.ceil"]:
        return f"'{token}' ({language} Syntax): 'Returns the smallest integer greater than or equal."
    elif token in ["math.floor"]:
        return f"'{token}' ({language} Syntax): 'Returns the largest integer less than or equal "
    elif token in ["math.sin","math.cos","math.tan"]:
        return f"'{token}' ({language} Syntax): 'Returns the trigonometric sine, cosine, and tangent"
    
    elif token in ["abstract"]:
        return f"'{token}' ({language} Syntax): 'It provide a blueprint but are not implemented directly, allowing subclasses to provide their own implementation"
    elif token in ["class"]:
        return f"'{token}' ({language} Syntax): 'A blueprint for creating objects that define properties (attributes) and behaviors (methods) shared by all objects of that type."
    elif token in ["extends"]:
        return f"'{token}' ({language} Syntax): 'Indicates that a class is inheriting properties and behaviors from another class "
    elif token in ["import"]:
        return f"'{token}' ({language} Syntax): 'Allows you to access functionality defined in other modules or packages, making it available in the current module or program."
    elif token in ["super"]:
        return f"'{token}' ({language} Syntax): 'It allows access to methods or constructors of the superclass within the subclass."
    elif token in ["pass"]:
        return f"'{token}' ({language} Syntax): 'It is used as a placeholder indicating that no action should be taken, allowing code to pass through without any effect"
    
    else:
        return f"'{token}' is a special symbol or identifier or variable or string."