'''
test_var = False

if(test_var == True):
    print("okay")
else:
    print("this is not true")

number_a = 500.6
number_b = 100.4
if(number_a > number_b):
    print(number_a,"is bigger than",number_b)
else:
    print(number_b,"is bigger than",number_a)


# name = input("what's your name? ")

# print("your name is",name)

def Multiply(num1,num2):
    result = num1*num2
    return result

temp = Multiply(2,5)
print(">>",temp)
'''

text = float("1665.5")

print(text*52.5)

action = input("?")
num1 = float(input('number 1'))
num2 = float(input('number 2'))
result = 0

if(action == '+'):
    result = num1+num2
elif(action == '*'):
    result = num1*num2
else:
    print('this not a number')


print(result)



number = 515.5
text = "1235.2"
number += float(text)
text += str(number)
