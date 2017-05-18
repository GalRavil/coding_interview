"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column is set to 0
"""

matrix = [[1, 2, 3],
          [4, 0, 6],
          [7, 8, 9],
          [10,11,0]]


#def zeroing_machine(matrix):
#    coordinates = []
#    length = len(matrix)
#    
#    # creating list of coordinates [x,y]
#    for row in matrix:
#        for dig in row:
#            if dig == 0:
#                coordinates.append([matrix.index(row), row.index(dig)])
#    
#    # set to zero rows
#    for row, column in coordinates:
#        matrix[row] = [0 for i in range(length)]
#        
#        # set to zero column
#        for i in range(length):
#            matrix[i][column] = 0
#            
#    return matrix
#    
#    
#print(zeroing_machine(matrix))



class Matrix_processor:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.coordinates = []  # [[row, column], ...]
        
    def set_to_zero(self):
        self.find_all_zeros()
        self.to_zero()
        
        return self.matrix
    
    def find_all_zeros(self):
        for row_count, row in enumerate(matrix):
            for cell_count, cell_value in enumerate(row):
                if cell_value == 0:
                    self.coordinates.append([row_count, cell_count])
                    # [[row, column], ...]
    
    def to_zero(self):
        new_row = [0 for i in range(self.columns)]  # [0,0,0]
        
        # set to zero row
        for row, column in self.coordinates:
            self.matrix[row] = new_row
            
            # set to zero column
            for i in range(self.rows):
                self.matrix[i][column] = 0
    

test = Matrix_processor(matrix)
print(test.set_to_zero())








