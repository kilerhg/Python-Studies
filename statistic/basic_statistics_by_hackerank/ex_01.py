'''
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT

Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output

43900.6
44627.5
4978


[ ] - Median
[ ] - Mean
[ ] - Mode


'''


STDIN = int(input())
#  10
list_values = list(map(float, input().split()))
# 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
sorted_values = sorted(list_values) 
mean = sum(sorted_values)/STDIN

if len(sorted_values) % 2 != 0:
    median = sorted_values[round(len(sorted_values)/2)-1]
else:
    median = sum(sorted_values[round(len(sorted_values)/2)-1:round(len(sorted_values)/2)+1])/2

list_all_qtd = {line:list_values.count(line) for line in list_values}

num_mode = max(list_all_qtd.items(), key=lambda x: x[1])[1] 

list_modes = list(filter(lambda x: x[1] == num_mode, list_all_qtd.items())) # Getting the list of numbers with the same mode
if len(list_modes) > 1: # verify if there is more than one number with the same mode
    mode = min(list_modes, key=lambda x: x[0])[0]
else:
    mode = list_modes[0][0]
    
print(mean)
# 43900.6
print(median)
# 44627.5
print(mode)
# 4978.0
