
def largestPalindrome(num1, num2):
    list = []
    for i in range(num1, num2):
        for x in range(num1, num2):
            number = str(i * x)
            pivot = int(len(number)/2)
            string1 = number[0:pivot]
            string2 = number[pivot:len(number)]
            if string1 == string2[::-1]:
                list.append(int(string1 + string2))
        
    
    return max(list)
    



def reverse(string):
    return string[::-1]

def max(list):
    highest = list[0]
    for i in list:
        if(i > highest):
            highest = i
    return i

print(largestPalindrome(900,999))