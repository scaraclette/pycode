# Hints:
# 17: If you just cleared the rows and columns as you found 0s,
#     you'd likely wind up clearing the whole matrix.
#     Try finding the cells with zeros first before making any changes to the 
#     matrix
# 74: Can you use O(N) additional space instead of O(N^2)?
#     What information do you really need from the list of cells that are zero?
# 102: You probably need some data storage to maintain a list of the rows and 
#      columns that need to be zeroed. Can you reduce the additional space
#      usage to O(1) by using the matrix itself for data storage?
import unittest

def zero_matrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    rows = set()
    cols = set()

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0


    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()