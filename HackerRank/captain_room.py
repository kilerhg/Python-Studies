'''
>> The Captain's Room 

Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of
members per group where ≠

.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear

times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of

and the room number list.

Input Format

The first line consists of an integer,
, the size of each group.
The second line contains the unordered elements of the room number list.

# Example Inputs

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

# Example Output
8
'''
ex_input = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 '

size_group = int(5)
array = str(ex_input).strip().split(' ')

# size_group = int(input(""))
# array = str(input("")).strip().split(' ')

array = list(map(int, array))

all_elements = set(array)

for element in all_elements:
    if not array.count(element) > 1:
        print(element)

