def two_sum(nums, target):
    for i in range(0, len(nums)):
        print(len(nums))
        for j in range(0, len(nums)):
            print(j, i)
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                print(nums[i], nums[j])
                print('done')
                return [i,j]
    return None


def two_sum(nums, target):
    m = {}
    for i in range(0, len(nums)):
        num = nums[i]
        diff = target - num
        print(diff)
        if str(diff) not in m:
            m[str(num)] = i
        else:
            return m[str(diff)], i 
    return m
print(two_sum([3,2,4], 6))
