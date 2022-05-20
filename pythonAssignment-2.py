orig_list= [[1,
1,
3, 2], [9,
8,
8, 1], [0,
4,
5, 0,
0, 1,
4]]fori in
range(0,
3):list1= orig_list[i]setlist=
list(set(list1))forj in
setlist:n= list1.count(j)ifn >
1:print(j,
" --> ", n)

# 2) Merging 2 lists given
list3 = []
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
for i in list1:
    for j in list2:
        list3.append(i + j)
print("List 1 is - ", list1)
print("List 2 is - ", list2)
print("Merged list is - ", list3)



# 3) Extending a nested list

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
print("Original list is - ", list1)
sub_list = ["h", "i", "j"]
print("Sublist to be added is - ", sub_list)
for i in sub_list:
    list1[2][1][2].append(i)
print("After adding sublist - ", list1)


# Mapping 2 lists as a dictionary
Keys = ['Ten', 'Twenty', 'Thirty']
Value = [10, 20, 30]

dictionary = dict(zip(Keys, Value))
print("Keys list - ", Keys)
print(("Values list - ", Value))
print("Dictionary - ", dictionary)


# 5) Merging 2 dictionary

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
print("Dictionary 1 - ", dict1)
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print("Dictionary 2 - ", dict2)
dict1.update(dict2)
print("Merged dictionary is - ", dict1)


# rename key 'city' to 'location'
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
print("Original List is - ", sampleDict)
sampleDict["Location"] = sampleDict["city"]
del sampleDict["city"]
print("Dictionary after changing city to location - ", sampleDict)


# converting dictionary to list

original_dictionary = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print("Original dictionary - ", original_dictionary)
res_list = []
for key, val in original_dictionary.items():
    res_list.append([key] + val)
print("Dictionary converted to list - ", res_list)


