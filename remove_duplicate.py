def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        my_list = []        
        for num in nums:
            if num in my_list:                
                continue
            else:
                my_list.append(num)   
                counter +=num
        return my_list
l = [1,1,2]
print(removeDuplicates(l))