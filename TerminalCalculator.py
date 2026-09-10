
#User Inputs
firstNum = int(input("What's your first number?: "))
secondNum = int(input("What's your second number?: "))
operation = input("What's the operation you want to use? use the following symbols + - / *: ")


#performs the operations that the user inputted
match operation:
    case "+":
        answer = firstNum + secondNum
    case "-":
        answer = firstNum - secondNum
    case "/":
        answer = firstNum / secondNum
    case "*":
        answer = firstNum * secondNum
    case _:
        operation = input("Please provide a valid input. Again the symbols are + - / *: ")

print("Your Answer is: " + str(answer))

#Outputs the Results