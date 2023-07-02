ex = input()
nums = ex.split('-')
result = 0 if nums[0] == '' else eval('+'.join(map(str, map(int, nums[0].split('+')))))
for num in nums[1:]:
  result -= eval('+'.join(map(str, map(int, num.split('+')))))
print(result)