import random


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# RANDOM GENERATION OF A BINARY TREE
nums = set()
for _ in range(14):
    nums.add(random.randint(0,100))
nums = list(nums)
print(nums)

root = Node(nums[0])

for value in nums:
    node = root
    while True:
        if value > node.val and not node.right is None:
            node = node.right
        elif value < node.val and not node.left is None:
            node = node.left
        else:
            break

    if value > node.val:
        node.right = Node(value)
    elif value < node.val:
        node.left = Node(value)


inp = int(input("Enter a number that needs to be found "))

path = ""
not_found = False
node = root
while node.val != inp:
    if inp > node.val:
        node = node.right
        path += "1/"
    elif inp < node.val:
        node = node.left
        path += "0/"
    if node is None:
        print(f"{inp} is not inside the binary tree")
        not_found = True
        break
if not not_found:
    print(f"The value can be found at {path}")
