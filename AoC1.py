### advent of code day 1 2023
### have to grab first number, and last number 
### from each string , adf3adga9ad2 would == 32
###                  , kdfa7adjk == 77 
### add all numbers together for total result

'''
get file
read file by lines
store lines
get list
read list by lines
read lines pull 1st number
if only 1 number, store
if 2 numbers, store
if more than 3 numbers, take first and last, store
add all == answer
'''



import re

total_sum = 0

with open('AoC.txt', 'r') as f:
    for line in f:
        numbers = re.findall(r'\d+', line)
        if numbers:
            first_num = int(numbers[0])
            last_num = int(numbers[-1]) if len(numbers) > 1 else first_num
            total_sum += int(f"{first_num}{last_num}")

print("Total Sum:", total_sum) 
