

def diagonalSum(mat):
    sum = 0
    if len(mat) == 0:
        return sum

    n = len(mat)
    for i in range(0, n):
        left = mat[i][i]
        right = mat[i][n-1-i]
        sum += left + right
    return sum if n%2==0 else sum - mat[n//2][n//2]

if __name__=="__main__":
    # mat = [[1,2,3],[4,5,6],[7,8,9]]
    # mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    mat = [[5]]
    print(diagonalSum(mat))
