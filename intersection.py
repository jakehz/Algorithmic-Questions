class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inters = []
        for num in nums1:
            if num in nums2:
                inters.append(num)
                del nums2[nums2.index(num)]
        return inters