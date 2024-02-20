# pyvav
一个由python构建的简单解释器

pyvav语法

cprint函数:
  用于打印示例cprint hello world!
                   ^
                   |这里有空格

变量赋值:
  pyvav的数据类型有两个str,int。使用方法：
  str:
    cbl[hello] = 'hello world!'
    cprint cbl[hello]<--使用cprint打印变量
    #输出：hello world!
  int:
    int[a] = 1
    int[b] = 1
    add int[a],int[b]<--add 是加法计算，js 函数可进行任意计算。
    输出：2

计算
  add 加法
  sub 减法
  mul 乘法
  div 除法
  divz 除法(保留整数)
  示例:
      变量赋值
      int[a] = 1
      int[b] = 1
      int[c] = 2
      加
      add int[a],int[b]
      减
      sub int[c],int[a]
      乘
      mul int[c],int[c]
      除
      div int[b],int[c]

执行时间
  在代码开头加上@time,结尾加@stop

exit
  用于终止程序

osname
  系统名称,使用python os创造

注释
  在注释开头加!
  例:
    !变量赋值
    cbl[h] = 'hello world'
    cprint cbl[h]
ntime
  now time
gy()
  关于
