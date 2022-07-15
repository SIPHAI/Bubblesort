Lower = int(input("Enter the Lowest range Value :"))
Upper = int(input("Enter the Upper range Value :"))

print("The Prime numbers in range are :")
for num in range (Lower, Upper+1):
    if num >1:
        for i in range (2,num):
            if(num % i) == 0:
                break
        else:
            print("/t",num)
           
# First, we will take the input:  
# lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
# upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
# print ("The Prime Numbers in the range are: ")  
# for number in range (lower_value, upper_value + 1):  
#     if number > 1:  
#         for i in range (2, number):  
#             if (number % i) == 0:  
#                 break  
#         else:  
#             print (number)  
