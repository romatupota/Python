def maximal(element):
    max_namber = element[0]
    for i in element:
        if i > max_namber:
            max_namber = i
    
    print(max_namber)

nums1 = [11, 34, 3, 75,134]
max1 = maximal(nums1)

nums2 = [67, 46, 36, 377, 2]
max2 = maximal(nums2)
