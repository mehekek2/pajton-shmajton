
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
#result2 tu se sprema transponirana matrica
result2 = [[0,0,0], 
       	  [0,0,0]]

for i in range(len(X)):
   
   for j in range(len(Y[0])):
       
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
print(" ")
for r in result:
   print(r)


#==========TRANSPONIRANJE===================
print("TRANSPONIRANA")
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
print(" ")
for r in result:
   print(r)
