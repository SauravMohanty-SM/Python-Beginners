arr1 = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]

arr2 = [[1,2,3],
    [7 ,8,9],
    [4 ,5,6]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(arr1)):  

    for j in range(len(arr1[0])):
        result[i][j] = arr1[i][j] + arr2[i][j]
 
for r in result:
    print(r)