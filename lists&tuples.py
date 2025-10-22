# WAP to ask the user to enter names of their  3 favorite movies & store them it in list

list = []

mov = input("Enter your Favourite movie :")
list.append(mov)
mov = input("Enter your Favourite movie :")
list.append(mov)
mov = input("Enter your Favourite movie :")
list.append(mov)

print(list)

"""
list.append(input("Enter your 1st Favourite movie :"))
list.append(input("Enter your 2nd Favourite movie :"))
list.append(input("Enter your 3rd  Favourite movie :"))

print(list)
"""

## WAP to check if a list contains a palindrome of elements .(Hint use copy() method)
## [1,2,3,2,1]    [1,'abc','abc',1] -> palindromes

list = [1,2,3,2,1]

copy_list = list.copy()
copy_list.reverse()

if(list == copy_list):
    print("Given list is Palindrome")
else:
    print("Given list is not Palindrome")

## WAP to count the number of students with the "A" grade in the fallowing tuple

tup = ("C","D","A","A","B","B","A")
count = tup.count("A")
print(count)

## Store the above values in the list & sort them from "A" to "D"

list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)