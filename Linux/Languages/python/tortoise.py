def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    pasada = 0
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        print("pasada" + str(pasada))
        print (hare)
        print (tortoise)
        if tortoise == hare:
            break
        pasada += 1
        
    
    ptr1 = nums[0]
    ptr2 = tortoise

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

print("duplicate: "+str(findDuplicate([1,4,5,6,1])))