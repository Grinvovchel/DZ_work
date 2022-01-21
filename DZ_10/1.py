class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for line in self.my_list:
            for i in line:
                print(f"{i:4}", end="")
            print()
        return ''


    def __add__(self, other):
        for i in range(len(self.my_list)):
            for k in range(len(other.my_list[i])):
                self.my_list[i][k] = self.my_list[i][k] + other.my_list[i][k]
        return Matrix.__str__(self)


mat = Matrix([[7, 5, 4], [-1, 3, 7], [8, 1, -4], [2, 1, -1]])
mat2 = Matrix([[3, -1, -2], [4, 3, 4], [6, 2, 8], [5, 2, 5]])
print(mat.__add__(mat2))