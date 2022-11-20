import pprint

matrix = [
        [1,0,3,4,5],
        [1,2,3,4,5],
        [1,2,3,0,5],
        [1,2,3,4,0],
]
# For pretty printing
pp = pprint.PrettyPrinter(indent=4, width=len(matrix[0]) *5, compact=True)


def zero_matrix(matrix):
    ROW = len(matrix)
    COL = len(matrix[0])
    seen = set()

    for r in range(ROW):
        for c in range(COL):
            if matrix[r][c] == 0 and (r, c) not in seen:
                cc = 0
                while cc < COL:
                    matrix[r][cc] = 0
                    seen.add((r, cc))
                    cc +=1
                rr = 0 
                while rr < ROW:
                    matrix[rr][c] = 0
                    seen.add((rr, c))
                    rr +=1

    return matrix




print('before')

pp.pprint(matrix)
zero_matrix(matrix)

print('after')
pp.pprint(matrix)
