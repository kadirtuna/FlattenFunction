import FlattenFunction
import ListReverserFunction

#Two sample ragged nested lists to be flatted and reversed!
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list2 = [[1, 2], [3, 4], [[5, [6, 10, 16]], 7]]

print("Original list1 : ", list1)
print("Flatten version of list1 : ", list(FlattenFunction.flatten(list1)))
list(ListReverserFunction.listReverserFunc(list1))
print("Reversed version of list1 : ", list1)

print("----------------------------------------------")
print("Original list2 : ", list2)
print("Flatten version of list2 : ", list(FlattenFunction.flatten(list2)))
list(ListReverserFunction.listReverserFunc(list2))
print("Reversed version of list2 : ", list2)