"""Initial Try, did not work: runtime error"""
def addNode(node, place):
    """
    :type node: TreeNode
    :type place: int
    :rtype: None 
    """
    if node:
        if place > node.val:
            if node.right == None:
                node.right = TreeNode(place)
            else:
                addNode(node.right, place)
        if place < node.val:
            if node.left == None:
                node.left = TreeNode(place)
            else:
                addNode(node.left, place) 

    if len(nums) % 2 != 0:
        middle = len(nums) // 2
        root = TreeNode(nums[len(nums) // 2])
        start = middle - 1
        end = middle + 1
    else:
        start = (len(nums) / 2) - 1 
        root = TreeNode(nums[start])
        start -= 1 
        end = (len(nums) / 2)
        
    while(start != -1 and end != len(nums)):
        addNode(root, nums[start])
        addNode(root, nums[end])
        start -= 1
        end += 1
    return root