   # This will be True

value = 5 > 3  
print("Is value true?", value)


# Calculator program
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")


# Using single quotes
text1 = 'Hello, world!'
print(text1)

# Using double quotes
text2 = "Hello, Python!"
print(text2)

# Using triple quotes for multi-line strings
text3 = """This is a
multi-line
string"""
print(text3)
