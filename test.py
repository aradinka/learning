nums = [2, 7, 11, 15]
target = 9

res = {}
for i in range(len(nums)):
	print(f"i: {i}, num: {nums[i]}")
	if nums[i] in res:
		hasil = [res[nums[i]], i]
	else:
		res[target-nums[i]] = i

print(hasil)
print(res)
