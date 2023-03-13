# Реализация бинарного дерева в Python.

class Node:   # Создаём класс для объекта (вершины дерева)
    def __init__(self, data): # В инициализаторе передаём данные, которые будут храниться в вершине.
        self.data = data
        self.left = self.right = None # В каждой вершине указатели left и right по умолчанию None.


class Tree:   # Создаём класс для работы со всем деревом.
    def __init__(self):
        self.root = None   # Указатель root по умолчанию None.

# Т.о. создано пустое бинарное дерево, для которого еще нужно определить методы для работы с ним.

    def __find(self, node, parent, value): # Метод для поиска вершины, к кот. будет цепляться нов.объект
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:   # Рекурсия для прохождения по левой ветви.
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:   # Рекурсия для прохождения по правой ветви.
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):   # Метод для добавления новых вершин. В метод передаём объекты класса Node.
        if self.root is None: # Проверка наличия объектов в дереве. Если root принимает значение None,
# значит в бинарном дереве нет ни одного объекта.
            self.root = obj   # В этом случае новая вершина добавляется как корневая.
            return obj        # Иначе нам надо добавить объект к существующей вершине:

        s, p, fl_find = self.__find(self.root, None, obj.data)   # Ищем вершину.

        if not fl_find and s:
            if obj.data < s.data:   # Если значение меньше значения в s, добавляем его слева.
                s.left = obj
            else:
                s.right = obj       # Иначе - добавляем значение справа.

        return obj

    def show_tree(self, node):   # Отображение бинарного дерева в глубину.
        if node is None:
            return

        self.show_tree(node.right)
        print(node.data)
        self.show_tree(node.left)

    def show_wide_tree(self, node):   # Отображение бинарного дерева в ширину.
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, s, p):   # Удаление листовой вершины:
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):   # Удаление вершины с одним потомком:
        if p.left == s:
            if s.left is None:         # (Переопределяем вершины)
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):   # Метод находит минимальное значение в правом поддереве:
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def del_node(self, key):   # Метод удаляет вершину. Key определяет значение вершины.
        s, p, fl_find = self.__find(self.root, None, key)   # Ищем вершину, которую будем удалять.

        if not fl_find:
            return None

        if s.left is None and s.right is None:   # В случае удаления листовой вершины:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:  # В случае наличия одного потомка:
            self.__del_one_child(s, p)
        else:                                    # В случае наличия двух потомков:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


v = [10, 5, 7, 16, 13, 2, 20]
# v = [20, 5, 24, 2, 16, 11, 18]

t = Tree()
for x in v:
    t.append(Node(x))

t.del_node(5)
t.show_wide_tree(t.root)
