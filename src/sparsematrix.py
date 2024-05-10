""" This represents a node in a sparse matrix data structure.
 Contains the implementation of the Node class and methods
  for node manipulation such as adding, removing, or accessing nodes."""


class Node:
    def __init__(self, i, j, data):
        self.data = data
        self.i = i
        self.j = j
        self.nc = None
        self.nl = None


class SparseMatrix:

    """ Create new node to insert it in sparse matrix. """
    @classmethod
    def create_new_node(cls, i, j, data):
        new_node = Node(i, j, data)
        return new_node

    """ Insert the node into the matrix with the correct links to other nodes or tabs.
                    ---O(n) = linear (n)--- """

    @classmethod
    def insert_node(cls, row_tab, col_tab, i, j, data):
        if i >= 10 or j >= 8:
            print("This index doesn't exist!")
        elif cls.is_exist(row_tab, i, j):
            print("This position is allocated!")
        else:
            if row_tab[i] is None and col_tab[j] is None:
                node = cls.create_new_node(i, j, data)
                col_tab[j] = node
                row_tab[i] = node
            elif row_tab[i] is None:
                cur1 = col_tab[j]
                node = cls.create_new_node(i, j, data)
                row_tab[i] = node
                if col_tab[j].i < i:
                    while cur1.nl is not None and cur1.nl.i < node.i:
                        cur1 = cur1.nl

                    node.nl = cur1.nl
                    cur1.nl = node
                else:
                    row_tab[i].nl = col_tab[j]
                    col_tab[j] = row_tab[i]
            elif col_tab[j] is None:
                cur = row_tab[i]
                node = cls.create_new_node(i, j, data)
                col_tab[j] = node
                if row_tab[i].j < j:
                    while cur.nc is not None and cur.nc.j < node.j:
                        cur = cur.nc

                    node.nc = cur.nc
                    cur.nc = node
                else:
                    col_tab[j].nc = row_tab[i]
                    row_tab[i] = col_tab[j]
            else:
                cur2 = col_tab[j]
                node = cls.create_new_node(i, j, data)
                if col_tab[j].i < i:
                    while cur2.nl is not None and cur2.nl.i < node.i:
                        cur2 = cur2.nl
                    node.nl = cur2.nl
                    cur2.nl = node
                else:
                    node.nl = col_tab[j]
                    col_tab[j] = node
                cur2 = row_tab[i]
                if row_tab[i].j < j:
                    while cur2.nc is not None and cur2.nc.j < node.j:
                        cur2 = cur2.nc
                    node.nc = cur2.nc
                    cur2.nc = node
                else:
                    node.nc = row_tab[i]
                    row_tab[i] = node

    """ Delete the node from the matrix and link the previous and next nodes to the appropriate adjacent node.
                        --- O(n) = linear (n) --- """

    @classmethod
    def delete_node(cls, row_tab, col_tab, i, j):

        if i >= 10 or j >= 8:
            print("this index don't exist!")
        elif cls.is_exist(row_tab, i, j) == 0:
            print("This position not exist")
        else:
            cur = col_tab[j]
            cur1 = None
            cura = row_tab[i]
            cura1 = None

            while cur.i != i:
                cur1 = cur
                cur = cur.nl

            while cura.j != j:
                cura1 = cura
                cura = cura.nc

            if cur.nc is None and cur.nl is None:
                if cur1 is None:
                    col_tab[j] = None
                else:
                    cur1.nl = None
                if cura1 is None:
                    row_tab[i] = None
                else:
                    cura1.nc = None
                del cur
            elif cur.nl is None:
                if cur1 is None:
                    col_tab[j] = None
                else:
                    cur1.nl = None
                if cura1 is None:
                    row_tab[i] = cura.nc
                else:
                    cura1.nc = cura.nc
                del cur
            elif cur.nc is None:
                if cur1 is None:
                    col_tab[j] = cur.nl
                else:
                    cur1.nl = cur.nl
                if cura1 is None:
                    row_tab[i] = None
                else:
                    cura1.nc = None
                del cur
            else:
                if cur1 is None:
                    col_tab[j] = cur.nl
                else:
                    cur1.nl = cur.nl
                if cura1 is None:
                    row_tab[i] = cura.nc
                else:
                    cura1.nc = cura.nc
                del cur

    """ This function is used to deleting all nodes from the matrix.
                            --- O(n) = n2 ---   """

    @classmethod
    def delete_dynamic_arr(cls, row_tab, col_tab, max_row):
        for i in range(max_row):
            cur = row_tab[i]
            while cur is not None:
                cur1 = cur
                cur = cur.nc
                cls.delete_node(row_tab, col_tab, i, cur1.j)

    """ To check this index exist on matrix or not
                    --- O(n) = n ---   """
    @classmethod
    def is_exist(cls, row_tab, i, j):

        c = 0

        cur = row_tab[i]
        while cur is not None:
            if cur.j == j:
                c = 1
                break
            cur = cur.nc

        return c
