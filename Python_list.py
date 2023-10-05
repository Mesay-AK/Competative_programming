if __name__ == '__main__':
    N = int(input())
    myList=[]
    for i in range(N):
        inp=input().split(" ")
        if inp[0]== 'insert':
            myList.insert(int(inp[1]),int(inp[2]))
        elif inp[0]=='print':
            print(myList)
        elif inp[0]=='remove':
            myList.remove(int(inp[1]))
        elif inp[0]=='append':
            myList.append(int(inp[1]))
        elif inp[0]=='sort':
            myList.sort()
        elif inp[0]=='pop':
            myList.pop()
        elif inp[0]=='reverse':
            myList.reverse()
