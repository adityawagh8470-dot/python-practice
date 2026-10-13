Digit = input("enter the digits : ")
Phone = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}

result = [""]
for d in Digit:
    temp = []
    for r in result:
        for ch in Phone[d]:
            temp.append(r + ch)
    result = temp
print(result)

#
# digit = input("enter the number : ")
# #
# phone = {
#     "2":"abc",
#     "3":"def",
#     "4":"ghi",
#     "5":"jkl",
#     "6":"mno",
#     "7":"pqrs",
#     "8":"tuv",
#     "9":"wxyz"
# }
#
# result = [""]
# for d in digit:
#     temp = []
#     for r in result:
#         for ch in phone[d]:
#             temp.append( r + ch)
#     result = temp
# print(result)
