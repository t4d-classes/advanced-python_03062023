
# setting the value of nums
# nums - variable declaration and assignment
# nums = [1,2,3,4]

# getting the value of nums
# nums - being evaluated as part of an expression
# double_nums = [ n * 2 for n in nums ]


nums = [1,2,3,4]

# print(nums) # print([1,2,3,4])
# * is used in an expression, it is unpacking
# print(*nums) # unpacking, print(1,2,3,4)

# a,b,c,d = nums
# print(a,b,c,d)

# * in declaration or assignment is packing
a,b,*c = nums # a: first element, b: second element, c: list of remaining elements
print(a,b,c)

# # val is declaration and assigment
# def do_it(val):
#     print(val)

# g = 3
# h = 4

# # g is an expression to be evaluated before the function call
# do_it(g)

# * packing
# def do_it(a,b,*c):
#     print(a,b,c)


# * is unpacking
# do_it(*[1,2,3,4])

nums1 = list(range(5))
nums2 = list(range(5))

nums3 = [ *nums1, *nums2 ]

print(nums3)
