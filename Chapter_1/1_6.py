"""
Given an image represented by an NxN matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degrees. 
Can you do this in place? 
"""

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def rotate_matrix_clockwise(matrix):
    return list(zip(*reversed(matrix)))
    
print(rotate_matrix_clockwise(matrix))



# Explanation:
# you can make shallow reversed copy using [::-1]
# but to rotate in place use:
#reversed_ = reversed(matrix)
#[ [7, 8, 9],
#  [4, 5, 6],
#  [1, 2, 3] ]


# * - makes each sublist in the original list a separate argument to zip() 
# (i.e., unpacks the list)

#zip() - takes one item from each argument and makes a list (well, a tuple) 
#from those, and repeats until all the sublists are exhausted. 
#This is where the transposition actually happens
#list(zip(*reversed_))

def rotate_matrix_counterclockwise(matrix):
    return list(reversed(list(zip(*matrix))))

print(rotate_matrix_counterclockwise(matrix))