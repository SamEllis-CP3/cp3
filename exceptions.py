#expetions are ways we handle errors created by users, in a way that doesnt break the code
"""
The computer can atomaticly detect zero divions, file not found, type error, index error
"""

class NegativeNumberError(Exception):
    pass

while True:
    try:
        num = int(input("Tel me a number: "))
        

    except (ValueError, TypeError):
        print("That wasnt a whole number!")
        continue
    
    else:
        break
while True:
    try:
        numTwo = int(input("Tell me another number: "))
        if numTwo <= 0:
            raise NegativeNumberError("Cannot Divide By zero")
    except (ValueError, NegativeNumberError):
        print("That wasnt a whole number!")
        continue


    else:
        try:
            print(f'{str(num)} divied {str(numTwo)} equals {num/numTwo}')

        except ZeroDivisionError:
            print("You Cant Divide By zero, try again!")
            continue
        else:
            break
    #finally: 
        
