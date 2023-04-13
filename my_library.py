#This is my library that I will import in my new python file to make a calculator!
def helpMenu():
    print("Choose operation: \n\na/A.Addition \nm/M.Multiplication \ns/s.Substraction \nd/D.Division \ne/D.Exit program\n")
    
def getUserInput(kind):
    flag = True
    if kind == "l":
        while flag == True:
            operation_selection = input("Enter the operation type:")
            if operation_selection in ["a","A","m","M","s","S","d","D","e","E"]:
                flag = False
            else:
                print("Invalid Input.try again")
    
    elif kind == "n":
        while flag == True:
            try:
                operation_selection = float(input('...>>>:'))
                flag = False
                
            except:
                print("Invalid Input. Try again!")
    return operation_selection

def try_calculation(operation_type):
    print("The operation chosen is:",operation_type)
    print("Please Enter the first number:")
    num1 = getUserInput('n')

    if operation_type == "a" or operation_type == "A":
        symb = "+"
        print("Enter the second number:")
        num2 = getUserInput("n")
        answer = num1 + num2
        
    elif operation_type == "m" or operation_type == "M":
        symb = "x"
        print("Enter the second number:")
        num2 = getUserInput("n")
        answer = num1 * num2

    elif operation_type == "s" or operation_type == "S":
        symb = "-"
        print("Enter the second number:")
        num2 = getUserInput("n")
        answer = num1 - num2
        
    elif operation_type == "d" or operation_type == "D":
        symb = "/"
        test = True
        while test == True:
            print("Enter the second number:")
            num2 = getUserInput("n")
            if num2 == 0:
                print("Invalid input.Try again because you can not devide by zero")
            else:
                test = False
        answer = num1 / num2
    
    
    result = str(num1)+' '+ symb + ' ' + str(num2) +'  ' + "=" + '  ' + str(answer)
    print(f"The answer of:{num1} {symb} {num2} is : {answer}")
    return result
