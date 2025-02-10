# def digits(num):
#     if num < 10:
#         return num
#     return num % 10 + digits(num // 10)
# print(digits(1234))
#
# def bubbles(arr):
#     return b(arr,len(arr)-1)
# def b(arr,end):
#     if not end:
#         return arr
#     for i in range(end):
#         if arr[i] > arr[i+1]:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#     return b(arr,end-1)
#
# l = [1,9,0,8,6,3]
# print(bubbles(l))
#
# def increasing(arr,i = 0):
#     if i == len(arr) - 1:
#         return True
#     if arr[i] > arr[i+1]:
#         return False
#     return increasing(arr,i+1)
# print(increasing(l))






