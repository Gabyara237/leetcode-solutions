class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list=[]
        i=0
        j=0
        new_list_size= len(nums1)+len(nums2)

        while i< len(nums1) and j< len(nums2):
            
            if nums1[i]<nums2[j]:
                new_list.append(nums1[i])
                i+=1
            else:
                new_list.append(nums2[j])
                j+=1
        
        if i< len(nums1):
            new_list.extend(nums1[i:])
        
        if j<len(nums2):
            new_list.extend(nums2[j:])

        index= new_list_size//2

        if new_list_size%2==0:

            median= (new_list[index-1]+ new_list[index])/2
        else:
            median= float(new_list[index])

        return median



        