print('i love %s')
print('i love %s'%"lixiao")
print('i am %d years old'%18)
print('i am %d years old, i am %s'%(18,'minlei'))
s = 'i love {}'.format('lixiao')
print(s)
s = 'i am {1}, i love {0}, {1} hate the dog'.format('lixiao','wangjun')
print(s)
# format 格式限定符 有着丰富的格式限定符，语法是{}中带：号
# 填充与对齐 填充经常跟对齐一起使用 ^ < > 分别是居中、左对齐、右对齐，后面带宽度
# ：号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{0}, {1}'.format('kzc', 18))
print('{:>8}'.format('189'))
print('{:0>8}'.format(189))
print('{:a>8}'.format('189'))
# 精度与类型f:精度常跟类型f一起使用
print('{:.2f}'.format(321.33345))
# 其中.2表示长度为2 的精度，f表示float类型  还有其他类型： 主要就是进制了，b、d、o、x 分别是二、十、八、十六进制
print('{:,}'.format(1234567890)) # 逗号，还能用来做金额的千位分隔符：

