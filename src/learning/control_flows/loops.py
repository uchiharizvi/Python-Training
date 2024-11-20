from data.dataset import numbers

print("using for loop:")
for num in numbers:#For Loop Print each number
    if num == 6:#if Condition
        print("Breaking the loop at 6!")
        break #Break the flow and exit
    if num % 2 == 0: #If Condition
        print(F"Skipping {num} because it is even.")
        continue #Continue the flow
    print(num)

print("\nUsing while loop:")#While Loop Print numbers until we reach a value > n
i=0
while i<len(numbers):# which is 10
    if numbers[i]>7: #check if current num is > 7
        print("Breaking the loop as number is greater than 7!")
        break
    print(numbers[i]) #print current number
    i+=1 #increment counter

