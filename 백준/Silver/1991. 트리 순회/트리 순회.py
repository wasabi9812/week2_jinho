import sys

N = int(sys.stdin.readline())
binary_trees = []
tree_dict = {}

for i in range(N):
    node, left, right = sys.stdin.readline().split()
    tree_dict[node] = (left, right)

pretemp = []

def preorder(node):
    if node == '.':  # 자식이 없는 경우는 바로 return
        return
    pretemp.append(node)  # 자기 노드 실행
    preorder(tree_dict[node][0])  # 왼쪽 자식 실행
    preorder(tree_dict[node][1])  # 오른쪽 자식 실행

preorder('A')  # 일반적으로 루트는 'A'로 시작
print(*pretemp, sep ='')


intemp = []

def inordrer(node):
    if node =='.':
        return
    inordrer(tree_dict[node][0])
    intemp.append(node)
    inordrer(tree_dict[node][1])
    
inordrer('A')
print(*intemp, sep ='')



posttemp = []

def postorder(node):
    if node =='.':
        return
    postorder(tree_dict[node][0])
    postorder(tree_dict[node][1])
    posttemp.append(node)
    
postorder('A')
print(*posttemp, sep ='')