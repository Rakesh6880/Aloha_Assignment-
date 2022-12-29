n=list(map(str,input().split('.')))
for i in n:
    if i>'255':
        continue
    else:
        print('false')
        exit(0)
print('true')
