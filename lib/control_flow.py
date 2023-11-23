#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass
    username = username.lower()
    admin_password = '12345'
    
    # try :
    #     password = int(password)
    # except :
    #     return('Invalid password format')
    
    if username == 'admin' and password == admin_password :
        return('Access granted')
    else :
        return('Access denied')

def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40 :
        return("It's brisk out there!")
    elif temperature > 40 and temperature < 60 :
        return("It's a little chilly out there!")
    elif temperature > 85 :
        return("It's too dang hot out there!")
    else :
        return("It's perfect out there!")

def fizzbuzz(num):
    # your code here
    pass
    if num % 3 == 0 and num % 5 == 0 :
        return("FizzBuzz")
    elif num % 3 == 0 :
        return("Fizz")
    elif num % 5 == 0 :
        return("Buzz")
    else :
        return(num)

def calculator(operation, num1, num2):
    # your code here
    pass
    if operation in ('+', '-', '*', '/'):
        if operation == '+':
            return(num1 + num2) 
        elif operation == '-':
            return(num1 - num2)
        elif operation == '*':
            return(num1 * num2)
        elif operation == '/':
            if num2 != 0:
                return(num1 / num2)
            else:
                return 'Cannot divide by zero!'
    else:
        print('Invalid operation!')
        return None
