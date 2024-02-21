# Codex解释器
一个由python构建的简单解释器,在这里的描述是最Codex的新版本


2024.2.21 pyvav 正式改为 Codex


.vav是Codex的文件,打开编码utf-8


Codex语法

#cprint函数:


  用于打印示例cprint hello world!
  
                    ^
                    |这里有空格

#变量赋值:


  Codex的数据类型有两个str,int。使用方法：

  
  str:

  
    cbl[hello] = 'hello world!'

    
    cprint cbl[hello]<--使用cprint打印变量

    
    #输出：hello world!

    
  int:

  
    int[a] = 1

    
    int[b] = 1

    
    add int[a],int[b]<--add 是加法计算，js 函数可进行任意计算。

    
    输出：2

    

#计算


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

      

#执行时间:在代码开头加上@time,结尾加@stop



  

#exit:用于终止程序

  



#osname:系统名称,使用python os创造

  

#注释


  在注释开头加'!'

  
  例:

  
    !变量赋值

    
    cbl[h] = 'hello world'

    
    cprint cbl[h]



    
#ntime:now time



  
#gy():关于



#input: <--新增的函数,类型为str


input[提示,要储存到的变量]

        
例:

        
            input[>>>|,a]

            
            cprint cbl[a]

            
输入:hello world

            
输出:hello world




#bprint


这个函数用法与cprint一样,但是标准输出,因此不会空行,用于解决cprint不能把str类型与str变量一起打印问题


例:


              cbl[name] = 'xinhaitianze.';
              cbl[age] = ' 12 ';
              bprint My name is ;
              cprint cbl[name];
              bprint I'm;
              bprint cbl[age];
              bprint years old.;
              ！代码说明：在Codex代码中结尾加'；'，是合法的，这是因为bprint,cprint打印时有可能有空格在结尾如cprint hello ;加';'是为了代码可读性。

    
输出：


              My name is xinhaitianze.
              I'm 12 years old.


#js[算式或数学判断,变量名]类型:int


例:


              js[1+1,nam]
              cprint int[nam]
              输出:2

              js[1+1==2,nam1]
              cprint int[name1]
              输出:True

              js[1*1>2,nam2]
              cprint int[nam2]
              输出:False

              
Codex的运算符: +加|-减|*乘|/除


!= 不等于


== 等于
