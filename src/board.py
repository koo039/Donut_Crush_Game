from sparsematrix import SparseMatrix
from candyphotos import CandyPhotos
import pygame


class Board:
    def __init__(self):
        """ when u want change max_row and max_col don't forget to change their in
        sparse martix in insert and delete focntion """
        self.max_row = 10
        self.max_col = 8
        self.cell_size = 50
        self.row_tab = [None] * self.max_row
        self.col_tab = [None] * self.max_col
        self.candies = CandyPhotos.load_photos()

    def display_cont(self):
        # To display the matrix with some colors and zeros
        # O(n) = n^2

        print()
        for i in range(self.max_row):
            cur = self.row_tab[i]
            for j in range(-1, self.max_col + 1):
                if i == self.max_row or j == self.max_col or j == -1:
                    print(" # ", end="")
                    continue
                elif cur is None or cur.j != j:
                    print(" . ", end="")
                    continue
                print(" {} ".format(cur.data), end="")
                cur = cur.nc
            print()
        print(" #  #  #  #  #  #  #  #  #  #  #  # ")

    def insert_new_node(self, i, j, data):
        SparseMatrix.insert_node(self.row_tab, self.col_tab, i, j, data)

    def is_empty(self, row, col):
        cur = self.row_tab[row]
        while cur is not None:
            if cur.j == col:
                return False
            cur = cur.nc
        return True

    def reset(self):
        SparseMatrix.delete_dynamic_arr(self.row_tab, self.col_tab, self.max_row)

    def is_row_full(self, row):
        count = 1
        cur = self.row_tab[row]

        if cur is None:
            return -1

        data = cur.data
        index = cur.j

        while cur.nc is not None:
            if cur.nc.data == data and index == cur.nc.j - count:
                count += 1
                if count == 3:
                    return index
            else:
                data = cur.nc.data
                count = 1
                index = cur.nc.j
            cur = cur.nc

        return -1

    def is_col_full(self, col):
        count = 1
        cur = self.col_tab[col]

        if cur is None:
            return -1

        data = cur.data
        index = cur.i

        while cur.nl is not None:
            if cur.nl.data == data and index == cur.nl.i - count:
                count += 1
                if count == 3:
                    return index
            else:
                data = cur.nl.data
                count = 1
                index = cur.nl.i
            cur = cur.nl

        return -1

    def clear_row(self, row, index):
        cur = self.row_tab[row]
        while cur is not None:
            if cur.j == index:
                SparseMatrix.delete_node(self.row_tab, self.col_tab, row, index)
                SparseMatrix.delete_node(self.row_tab, self.col_tab, row, index+1)
                SparseMatrix.delete_node(self.row_tab, self.col_tab, row, index+2)
                break
            cur = cur.nc

    def clear_col(self, col, index):
        cur = self.col_tab[col]
        while cur is not None:
            if cur.i == index:
                SparseMatrix.delete_node(self.row_tab, self.col_tab, index, col)
                SparseMatrix.delete_node(self.row_tab, self.col_tab, index+1, col)
                SparseMatrix.delete_node(self.row_tab, self.col_tab, index+2, col)
                break
            cur = cur.nl

    def move_col_candy_down(self, col, completed, index):
        if col is None:
            return
        if col.i < index:
            self.move_col_candy_down(col.nl, completed, index)
            SparseMatrix.insert_node(self.row_tab, self.col_tab, col.i + completed, col.j, col.data)
            SparseMatrix.delete_node(self.row_tab, self.col_tab, col.i, col.j)

    def clear_three_candy_row(self):
        completed = 0
        for row in range(self.max_row - 1, -1, -1):
            col_index = self.is_row_full(row)
            if col_index >= 0:
                self.clear_row(row, col_index)
                completed = 1
                if completed == 1:
                    for p in range(3):
                        cur = self.col_tab[col_index + p]
                        self.move_col_candy_down(cur, completed, row)
        return completed

    def clear_three_candy_col(self):
        completed = 0
        for col in range(self.max_col - 1, -1, -1):
            cur = self.col_tab[col]
            row_index = self.is_col_full(col)
            if row_index >= 0:
                self.clear_col(col, row_index)
                completed = 3
                if completed == 3:
                    self.move_col_candy_down(cur, completed, row_index)
        return completed

    def is_inside(self, row, column):
        if row >= 0 and row < self.max_row and column >= 0 and column < self.max_col:
            return True
        return False

    def draw(self, screen):
        for i in range(self.max_row):
            cur = self.row_tab[i]
            for j in range(self.max_col):
                if cur is None or cur.j != j:
                    continue
                else:
                    cell_value = cur.data
                    cell_rect = pygame.Rect(j * self.cell_size + 50, i * self.cell_size + 100, self.cell_size - 1,
                                            self.cell_size - 1)
                    background_image = pygame.image.load(self.candies[cell_value]).convert_alpha()
                    background_image = pygame.transform.smoothscale(background_image, (50, 50))
                    screen.blit(background_image, cell_rect)
                cur = cur.nc
