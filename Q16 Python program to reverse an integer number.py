number = int (input('Type a integer number:') )

# print(number)
reverse = 0

while number!=0:
    remainder = number % 10
    reverse = reverse*10 + remainder
    number = number//10
print('Reverse integer number:', reverse)