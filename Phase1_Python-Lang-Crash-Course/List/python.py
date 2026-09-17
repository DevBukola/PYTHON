first_list = [1,2,3,4,5]

first_list.append(6) #adds 6 to the end of the list.
print(first_list)
print(len(first_list))

# first_list.append(7,8,) #does not WORK!apend takes only one argument, and two was given. "Extend" to the rescues.
# print(first_list)

first_list.append([1,1,2,2])
print(first_list)
print(len(first_list))


first_list.extend([7,8,9,10])
print(first_list)
print(len(first_list));

'''
While append and extend add to the end of the list. Append to add one item to the end of the list because even doing .append([2,3,4]) still sees the addem numbers as one, just like doing .append(2), extend adds more than one item to the end of the list. But what if we want to add an item to the beginning or the middle? We use "insert".
'''

first_list.insert(2, "Hey!");
print(first_list)

first_list.insert(-1, "The end!")
print(first_list)

first_list.insert(0, ["Welcome!", "Yes"])
print(first_list)

names = ["Oluwabukola", "Daniel", "Kings", "Oluwatoyin", "Olajide", "Grace"]
names.sort()
print(names)

names.clear()
print(names)

"""
Pop removes the item at the given position in the list, and returns it. if no index is specified, removes and returns last item in the list.
"""
names2 = ["Oluwabukola", "Daniel", "Kings", "Oluwatoyin", "Olajide", "Grace", "Bright"]
print(names2.pop()) 
print(names2.pop(1))

"""
Remove removes the first item from the list whose value is x. Throws ValueError if the item is not found. Best to use if you want to remove an item but you don' know the position.
"""

digits = [1,2,3,4,5,6,6,6]
digits.remove(2)
print(digits)
digits.remove(6)
print(digits)
# digits.remove(8)
# print(digits)

digits2 = [1,6,2,3,4,5,6,7]
print(digits2.index(2))

#index allows us to specify start and end.
print(digits2.index(6, 3)) #find the index of 6 from index 3 
# print(digits2.index(3, 5, 7)) #find index of 8 between the index of 5 and 7.

#count returns the number of times x appears in the list.

print(digits2.count(2))
print(digits2.count(6))

digits2.reverse()
print(digits2)

digits2.sort()
print(digits2)

words = ["Coding", "is", "fun!"]
sentence = ' '.join(words)
print(sentence)
print(words)

#SLICE
digits3 = [1,2,3,4,5,6,7,8,9]
print(digits3[1:])
print(digits3[4:])
print(digits3[:3])
print(digits3[2:5])
print(digits3[:-3])
print(digits3[1: -1])
print(digits3[0:-1:2])
print(digits3[3::2])
print(digits3[:2:-1])




