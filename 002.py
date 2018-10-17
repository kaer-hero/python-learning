gendar = input('请输入你的性别：')
print('你输入的性别是：{}'.format(gendar))
for name in ['zhangsan', 'lisi', 'wangerma']:
    print(name)
for row in range(1,10):
    for  col in range(1,row+1):
        print(col*row, end=' ')
    print('\n')

for row in range(1,10):
    for  col in range(1,row+1):
        print('{:<2}'.format(col*row), sep=" ", end=' ')
    print('\n')