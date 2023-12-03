class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        new_num1=num1[::-1]
        new_num2=num2[::-1]
        number1=0
        number2=0
        for i in range(len(num1)):
            number1+=(int(new_num1[i]))*10**i
        for i in range(len(num2)):
            number2+=(int(new_num2[i]))*10**i
        return str(number1*number2)


