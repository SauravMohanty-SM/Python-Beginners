arr1 = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

arr2 = [[4, 9, 14, 4],
    [9, 4, 3, 14],
    [0, 3, 1, 8]]

multiply = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
  
for i in range(len(arr1)): 
    for j in range(len(arr2[0])):
        for k in range(len(arr2)):
            multiply[i][j] += arr1[i][k] * arr2[k][j]
  
for r in multiply:
    print(r)