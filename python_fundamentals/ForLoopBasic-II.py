# #Biggie Size 
# def biggie_size(list):
#     for i in range(len(list)):
#         if list[i]>0:
#             list[i]='big'
#     return list
# print(biggie_size([-1, 3, 5, -5]))


#Count Positives
# def count_positives(list):
#     count = 0
#     for num in list:
#         if num > 0:
#             count += 1
#     list[len(list)-1] = count
#     return list
# print(count_positives([-1,1,1,1])) # print [-1,1,1,3]
# print(count_positives([1,6,-4,-2,-7,-2])) # print [1,6,-4,-2,-7,2]


#Sum Total
# def sum_total(list):
#     sum = 0
#     for val in list:
#         sum += val
#     return sum
# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))


#Average
# def avg(list):
#     sum = 0
#     for val in list:
#         sum += val
#     return (sum/len(list))
# print(avg([1,2,3,4]))


#Length
# def length(list):
#     return len(list)
# print(length([37,2,1,-9]))
# print(length([]))

#Minimum
# def minimum(list):
#     if len(list) == 0:
#         return False
#     minInt = list[0]
#     for val in list:
#         if val<minInt:
#             minInt = val
#     return minInt
# print(minimum([37,2,1,-9]))
# print(minimum([]))

# #Maximum
# def maximum(list):
#     if len(list) == 0:
#         return False
#     else:
#         return max(list)

# print(maximum([37,2,1,-9]))
# print(maximum([]))

#Ultimate Analysis
# def ultimate_analysis(list):
#     myDictonary = {'sumTotal': 0, 'average': 0, 'minimum': list[0], 'maximun': list[0],
#                     'length': len(list)}
#     for val in list:
#         if myDictonary['minimum']<val:
#             myDictonary['minimum'] = val
#         if myDictonary['maximun']>val:
#             myDictonary['maximun'] = val
#         myDictonary['sumTotal']+= val
#         myDictonary['average']=myDictonary['sumTotal']/len(list)
#     return myDictonary
# print(ultimate_analysis([37,2,1,-9]))


#Reverse List
def reverse_list(list):
    list.reverse()
    return list
list = [37, 2, 1, -9]
print(reverse_list(list)) 




