# User prompt with option for F or C
# This progam allows conversion to either Fahrenheit or Centigrade


print('Hello Human')
myname = input('What is your name?')

def menu():
    print('\n1. Celsius to Fahrenheit')
    print('2. Fahrenheit to Celsius')
    print('3. Done with conversions')
    pick = int(input('What temperature conversion do you need: '))
    return pick

def toC(f) :
    return int((f-32)/1.8)

def toF(c) :
    return int(c * 1.8 + 32)
    
def main():
    choose = menu()
    print(str(choose))
    while choose != 3:
        if choose == 1:
            #  C to F
            c = eval(input('Enter degrees Celsius: '))
            print(str(c) + ' degrees Celsius = ' + str(toF(c)) + ' degrees Fahrenheit')
        elif choose == 2:
            # F to C
            f = eval(input('Enter degrees Fahrenheit: '))
            print(str(f) + ' degrees Fahrenheit = ' + str(toC(f)) + ' degrees Celsius')
        else:
            print('Invalid Entry')
        choose = menu()
    print('Good-bye ' + myname)
main()
