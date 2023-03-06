
nums = [1,2,3,4,5]

# imperative code - what you want, how to do what you want

# not valid Python
# for (x=0; x<len(nums); x=x+1):
#     nums[x]


# count = len(nums)
# counter = 0

# while counter < count:
#     print(nums[counter])
#     counter = counter + 1

# declarative - what you want

# very pythonic way
for num in nums:
    print(num)


def double(x):
    print(f"in double: {x}")
    return x * 2

# more imperative
# double_nums = []

# for num in nums:
#     double_nums.append(double(num))

double_nums_gen = map(double, nums)

for num in double_nums_gen:
    print("in for loop gen")
    print(num)

double_nums = [ double(num) for num in nums ]

for num in double_nums:
    print("in for loop list")
    print(num)

double_nums_gen = ( double(num) for num in nums )

for num in double_nums_gen:
    print("in for loop gen comp")
    print(num)

# double_nums = list(double_nums_gen)

# double_nums = [ double(num) for num in nums ]


# print(nums)
# print(double_nums)







