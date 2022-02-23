n=int(input('enter number'))
for i in range(1,n):
    for k in range(n-i,0,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end="   ")
    print('\n')
for i in range(1,n+1):
    for j in range(1,i,1):
        print(" ",end=" ")
    for k in range(n-i+1,0,-1):
        print('*',end="   ")
    print("\n")
Output:
enter number
5
        *   


      *   *   

    *   *   *   

  *   *   *   *   

*   *   *   *   *   

  *   *   *   *   

    *   *   *   

      *   *   
        
        *
