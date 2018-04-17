# # -*- coding:utf-8 -*-
"""
利用Python定义了二叉树的结点类，前序、中序、后序遍历，以及建立一棵二叉搜索树、插入一个元素、删除一个元素、查找一个元素
链式存储的数据一般用递归的方式遍历，结构简单，逻辑清晰
递归往往都可以用循环展开，以迭代的形式实现，因为没有了递归函数调用的开销，在计算机中迭代效率更高，速度更快
"""
# 定义二叉树的结点类
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# 计算一棵二叉树的深度
# 思想：递归的方法，树的深度=max(左子树深度,右子树深度)+1
def TreeDepth(root): # 递归实现
    if root== None:
        return 0
    left = TreeDepth(root.left)
    right = TreeDepth(root.right)
    return max(left+1,right+1)

def TreeDepth_iter(root): # 非递归实现，利用二叉树的层序遍历，记录一共有多少层，即树的深度
    if root == None:
        return 0
    width = 0 # 记录当前层的宽度
    depth = 0 # 每遍历一层，树的高度+1
    queue = [root] # 利用队列保存每一层的结点
    while(len(queue)!=0): # 当所有结点遍历完后，停止
        width = len(queue) # 队列里只保存当前层的结点
        depth+=1
        while(width!=0): # 把上一层所有结点弹出
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            width -= 1
    return depth

# 计算一个二叉树的广度
# 思想：采用二叉树的层序遍历，利用队列保存每一层的结点并记录结点数
def TreeWidth(root):
    if root == None:
        return 0
    curwidth = 0 # 记录当前层的宽度
    lastwidth = 1 # 记录上一层的宽度
    maxwidth = 1 # 记录最大宽度
    queue = [root] # 利用队列保存每一层的结点
    while(len(queue)!=0): # 当所有结点遍历完后，停止
        while(lastwidth!=0): # 把上一层所有结点弹出
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            lastwidth -= 1
        curwidth = len(queue)
        if curwidth>maxwidth:
            maxwidth = curwidth
        lastwidth = curwidth
    return maxwidth

# 采用递归中序遍历一个二叉树，得到的序列是一个有序序列
def inorder(root):
    if root == None:
        return None # 递归终止条件
    inorder(root.left)
    print('%s '%root.val,end='')
    inorder(root.right)

# 采用递归前序遍历一个二叉树
def preorder(root):
    if root == None:
        return None # 递归终止条件
    print('%s ' % root.val, end='')
    preorder(root.left)
    preorder(root.right)

# 采用递归后序遍历一个二叉树
def postorder(root):
    if root == None:
        return None # 递归终止条件
    postorder(root.left)
    postorder(root.right)
    print('%s ' % root.val, end='')

# 采用迭代层序遍历一个二叉树，层序遍历需要借助辅助存储队列，不能递归实现，只能迭代循环
def levelorder(root):
    if root == None:
        return None
    queue = [root]
    while(len(queue)!=0):
        temp = queue.pop(0)
        print('%s '%temp.val,end='')
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

# 插入一个元素进BST二叉树，插入一个元素的时间复杂度等同于查找一个元素，为O(logn)
def bst_append(root, val):
    # 首先找插入元素的位置，即新结点加入的位置
    while(root != None and root.val != val):
        if (val<root.val and root.left!=None):
            root = root.left
        elif (val>root.val and root.right!=None):
            root = root.right
        else:
            break
    # 如果BST含有重复元素，则返回
    if (root == None or root.val==val):
        return False
    # 创建新结点保存新元素
    new_node = TreeNode(val)
    if val<root.val:
        root.left = new_node
    elif val>root.val:
        root.right = new_node
    return True

# 建立一棵二叉搜索树BST，建立整个树时间复杂度为O(nlogn)，相当于是二叉排序，将任意一个数组变为有序的二叉树，
# 其中序遍历是一个从小到大的有序序列
def bst_init(List):
    if len(List) == 0:
        return None
    root = TreeNode(List[0])
    for i in range(1,len(List)):
        bst_append(root, List[i])
    return root

# 迭代实现在一个BST中查找元素，时间复杂度与插入一个元素相同，都是O(logn)
def bst_find_iter(root,val):
    while(root and root.val!=val):
        if val>root.val:
            root = root.right
        elif val<root.val:
            root = root.left
    return root

# 在一个BST查找元素，递归实现，递归需要间接地用到栈
def bst_find_recur(root,val):
    if root.val>val:
        return bst_find_recur(root.left,val)
    elif root.val<val:
        return bst_find_recur(root.right,val)
    return root

# 删除一个BST搜索树的结点，需要分为三种情况：
# 1、待删除结点无子结点，直接删除；
# 2、待删除结点有一个子结点，用其子结点继承删除结点；
# 3、待删除结点有两个子结点，先找到删除结点的前驱结点，用其继承删除结点，然后将前驱结点的子结点链接到其父结点
def bst_erase(root, val):
    """root is the BST, val is the number to be erased
    """
    # 先找到要删除结点的位置，调用查找函数
    f = None # 待删除结点的父结点
    d = root # 待删除结点
    while(d and d.val != val):
        f = d
        if d.val>val:
            d = d.left
        else:
            d = d.right

    if d == None: # 不存在该数值
        return 0

    # 待删除结点有两个子结点
    if (d.left and d.right):
    # 找到中序遍历的前驱结点
        f = d # 前驱结点的父结点
        p = d.left # 前驱结点
        while(p.right): # 找到没有右子结点的，即为前驱结点
            f = p
            p = p.right
        d.val = p.val # 将p的值赋给待删除结点
        if (f == d):
            d.left = p.left
        else:
            f.right = p.left

    # 待删除结点没有子结点
    if root == d:
        return -1 # 待删除结点是只有一个根结点的BST
    if (d.left == None and d.right == None):
        if (d==f.left):
            f.left = None
        elif (d == f.right):
            f.right = None

    # 待删除结点有一个子结点
    else:
    # 用其子结点继承该删除结点
        if d.left:
            p = d.left
        else:
            p = d.right
        d.val = p.val
        d.left = p.left
        d.right = p.right
    return 1 # 返回删除结点的个数，0、-1或1

# 二叉树是最常用的数据结构，其采用链式存储结构，遍历一般使用递归，无需辅助存储空间，间接用到了栈
# 如果使用循环遍历，则需要辅助存储空间
# 但是，堆是一种特殊的完全二叉树，其一般用数组存储而非链式结构，遍历采用循环迭代

# 测试
num = [10,5,12,4,7] # 输入数组
root = bst_init(num) # 建立一棵二叉搜索树
print(TreeDepth(root))
print(TreeDepth_iter(root))
preorder(root) # 前序遍历
# levelorder(root)
# print(bst_find_recur(root,5).val) # 查找某个元素
# print(bst_erase(root, 10))
