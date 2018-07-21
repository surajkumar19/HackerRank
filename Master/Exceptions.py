n=int(input())
for i in range(n):
    try:
        
        a=[x for x in input().split()]
        print(int(a[0])//int(a[1]))
    except ZeroDivisionError as e:
        print('Error Code:',e)
    except ValueError as e:
        print('Error Code:',e)