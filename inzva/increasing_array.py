input()
nums = input().split(" ")
increasing = sorted(nums)
moves=0

while nums != increasing:
    loc = nums.index(min(nums))
    moves += loc
    nums.pop(loc)
    increasing.pop(0)
print(moves)