# #Count-down
# def countdown(y):
#     new_list = []
#     for i in range(y, -1, -1):
#         new_list.append(i)
#     return new_list
# print(countdown(5))


# #Print and Return
# def print_return(list):
#     print(list[0])
#     return list[1]
# print (print_return([5,50]))

#First Plus Length
def first_plus_length(list):
    return list[0] + len(list)
list = [1, 2, 3, 4, 5]
result = first_plus_length(list)
print(result)  


#values_greater_than_second
# def values_greater_than_second(list):
#     if len(list)<2:
#         return False
#     newList = []
#     # greaterThan = list[1]
#     for val in list:
#         if val>list[1]:
#             newList.append(val)
#     print(len(newList))    
#     return newList
# print(values_greater_than_second([5,2,3,2,1,4]))
# print(values_greater_than_second([1]))


#This Length, That Value
def length_and_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_and_value(4,7))
print(length_and_value(6,2))