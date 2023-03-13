# Выводит родителя до всех его потомков (прямой обход)
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


# Выводит потомков, а затем родителя (обратный обход)
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


# выводит левого потомка, затем родителя, затем правого потомка (центральный обход)
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)
