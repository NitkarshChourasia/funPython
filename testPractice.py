

def rotateList(nums : list[int], k: int) -> None:
    #a = nums[-3:]
    #b = nums[:-3]
    #nums1 = a + b
    nums = nums[-k:]  + nums[:-k]

    #print(a)
    #print(b)
    #print(nums)
    print(nums)



print(rotateList([1,2,3,4,5,6,7], 3))