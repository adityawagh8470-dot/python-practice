#
# digits = input("Enter digits: ")
#
# phone = {
#     "2": "abc",
#     "3": "def",
#     "4": "ghi",
#     "5": "jkl",
#     "6": "mno",
#     "7": "pqrs",
#     "8": "tuv",
#     "9": "wxyz"
# }
# #
# # result = [""]
# # for d in digits:
# #     temp = []
# #     for r in result:
# #         for ch in phone[d]:
# #             temp.append(r + ch)
# #     result = temp
# # print(result)
#
#
# result = [""]
# for d in digits:
#     temp = []
#     for r in result:
#         for ch in phone[d]:
#             temp.append(r + ch)
#     result = temp
# print(result)

# #
digit = input("enter the number : ")
#
phone = {
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
for d in digit:
    temp = []
    for r in result:
        for ch in phone[d]:
            temp.append( r + ch)
    result = temp
print(result)


# x = int(input("enter the number : "))
# n = abs(x)
# rev = 0
# while n>0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n//10
#
# if x<0:
#     rev = -rev
#
# if x< -2**31 or x> 2**31 -1:
#     print(0)
# else:
#     print(rev)