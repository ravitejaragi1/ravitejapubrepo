if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
    arrSort = list(arr) 

    arrSort.sort()

    res = [*set(arrSort)]
 
    print(res[-2])