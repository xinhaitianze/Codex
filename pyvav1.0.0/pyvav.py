from colorama import Fore, Back, Style, init
import sys
import time
import operator
import re
import pygame
import os

"""
code = '''
!sleep 2;
cprint hello world!;
add 1,1;
sub 2,1;
mul 2,2;
div 0,1;
js 1+1*2;
cbl[a] = 'hello world!';
cbl[b] = 'hello pyvav';
int[s] = open1|cs.py,r;
cprint cbl[a];
cprint cbl[b];
cprint int[s];
!aaaaaaaaaaaaaaaaa
open|cs.py,r;
osname;


'''
"""
with open('cs.vav','r',encoding='utf-8') as fi:
    fi = fi.read()
    code = fi

#code = input('>>>|')

def print(text):
    sys.stdout.write(f'{text}\n')
    sys.stdout.flush()

def cprint(text, color='x'):
    init(autoreset=True)  # 启用自动重置颜色
    if color == 'red':
        print(Fore.RED + text)
    elif color == 'green':
        print(Fore.GREEN + text)
    elif color == 'yellow':
        print(Fore.YELLOW + text)
    elif color == 'blue':
        print(Fore.BLUE + text)
    elif color == 'magenta':
        print(Fore.MAGENTA + text)
    elif color == 'cyan':
        print(Fore.CYAN + text)
    elif color == 'white':
        print(Fore.WHITE + text)
    elif color == 'reset':
        print(Fore.RESET + text)
    elif color == 'x':
        print(text)
    else:
        print(color + text)

def check_numbers_with_comma(s):
    # 正则表达式模式：匹配一个或多个数字，后面跟着一个逗号，再后面跟着一个或多个数字
    pattern = r'^\d+,\d+$'
    # 使用re.match检查字符串是否匹配模式
    match = re.match(pattern, s)
    # 如果匹配成功，返回True；否则返回False
    return bool(match)


def play_music(yl, wj, cs=1):
    pygame.init()
    pygame.mixer.music.set_volume(yl)  # 设置音量，范围是0.0到1.0
    pygame.mixer.music.load(wj)
    pygame.mixer.music.play(cs)

def stop_music():
    pygame.mixer.music.stop()

def music_busy():
    pygame.mixer.music.get_busy()

def op(n1,n2):
    with open(n1, n2,encoding='utf-8') as f:
        f = f.read()
        cprint(f)
        return f


def time1():
    time_tuple = time.strptime("%Y-%m-%d %H:%M:%S")
    cprint(time_tuple)
    return time_tuple

start_time = ''
def kaishi():
    global start_time
    start_time = time.process_time()

def stop():
    global start_time
    end_time = time.process_time()

    # 计算并打印消耗的 CPU 时间
    elapsed_time = end_time - start_time
    print(f"CPU time used: {elapsed_time} seconds")


def ima(jikan):
    time_tuple = time.strptime(jikan)
    cprint(time_tuple)
    return time_tuple
h = 0
variable = {}
int1 = {}
for line in code.splitlines():
    line = line.rstrip(';')
    lines_without_empty = [line for line in line.splitlines() if line]
    line = '\n'.join(lines_without_empty)
    if 'cprint ' in line:
        c = line[7:]
        #str[a]
        if 'cbl[' in line:
            s = line[11:]
            s = s.rstrip(']')
            cprint(variable[s])
        elif 'int[' in line:
            s = line[11:]
            s = s.rstrip(']')
            cprint(int1[s])
        else:
            cprint(c)
    elif 'sleep ' in line:
        h = h + 1
        s = line[6:]
        time.sleep(eval(s))
    elif 'add ' in line:
        try:
            c = line[4:]
            h = h + 1
            if 'int[' in line:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                n1 = n1[:4] + '"' + n1[4:]
                n1 = n1[:-1] + '"' + n1[-1:]
                n2 = n2[:4] + '"' + n2[4:]
                n2 = n2[:-1] + '"' + n2[-1:]
                n1 = n1.replace('int', 'int1')
                n2 = n2.replace('int','int1')
                cprint(operator.add(int(eval(n1)),int(eval(n2))))
            else:
                if check_numbers_with_comma(c):
                    numbers = c.split(',')
                    n1 = eval(numbers[0])  # 第一个数字
                    n2 = eval(numbers[1])  # 第二个数字
                    cprint(operator.add(n1, n2))
                else:
                    cprint('')
                    cprint(line,'red')
                    cprint(f'^^^\nline {h}','red')
                    cprint("PyvavError:The statement needs two numbers, and no characters other than numbers appear.\n",'red')
                    break
        except SyntaxError:
            cprint('')
            cprint(line, 'red')
            cprint(f'^^^\nline {h}', 'red')
            cprint("PyvavError:The input is incorrect.\n", 'red')
            break
    elif 'sub ' in line:
        try:
            c = line[4:]
            h = h + 1
            if 'int[' in line:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                n1 = n1[:4] + '"' + n1[4:]
                n1 = n1[:-1] + '"' + n1[-1:]
                n2 = n2[:4] + '"' + n2[4:]
                n2 = n2[:-1] + '"' + n2[-1:]
                n1 = n1.replace('int', 'int1')
                n2 = n2.replace('int', 'int1')
                cprint(operator.sub(int(eval(n1)), int(eval(n2))))
            else:
                if check_numbers_with_comma(c):
                    numbers = c.split(',')
                    n1 = eval(numbers[0])  # 第一个数字
                    n2 = eval(numbers[1])  # 第二个数字
                    cprint(operator.sub(n1, n2))
                else:
                    cprint('')
                    cprint(line, 'red')
                    cprint(f'^^^\nline {h}', 'red')
                    cprint("PyvavError:The statement needs two numbers, and no characters other than numbers appear.\n",
                           'red')
                    break
        except SyntaxError:
            cprint('')
            cprint(line, 'red')
            cprint(f'^^^\nline {h}', 'red')
            cprint("PyvavError:The input is incorrect.\n", 'red')
            break
    elif 'mul ' in line:
        try:
            c = line[4:]
            h = h + 1
            if 'int[' in line:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                n1 = n1[:4] + '"' + n1[4:]
                n1 = n1[:-1] + '"' + n1[-1:]
                n2 = n2[:4] + '"' + n2[4:]
                n2 = n2[:-1] + '"' + n2[-1:]
                n1 = n1.replace('int', 'int1')
                n2 = n2.replace('int', 'int1')
                cprint(operator.mul(int(eval(n1)), int(eval(n2))))
            else:
                if check_numbers_with_comma(c):
                    numbers = c.split(',')
                    n1 = eval(numbers[0])  # 第一个数字
                    n2 = eval(numbers[1])  # 第二个数字
                    cprint(operator.mul(n1, n2))
                else:
                    cprint('')
                    cprint(line, 'red')
                    cprint(f'^^^\nline {h}', 'red')
                    cprint("PyvavError:The statement needs two numbers, and no characters other than numbers appear.\n",
                           'red')
                    break
        except SyntaxError:
            cprint('')
            cprint(line, 'red')
            cprint(f'^^^\nline {h}', 'red')
            cprint("PyvavError:The input is incorrect.\n", 'red')
            break
    elif 'div ' in line:
        try:
            c = line[4:]
            h = h + 1
            if 'int[' in line:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                n1 = n1[:4] + '"' + n1[4:]
                n1 = n1[:-1] + '"' + n1[-1:]
                n2 = n2[:4] + '"' + n2[4:]
                n2 = n2[:-1] + '"' + n2[-1:]
                n1 = n1.replace('int', 'int1')
                n2 = n2.replace('int', 'int1')
                cprint(operator.truediv(int(eval(n1)), int(eval(n2))))
            else:
                if check_numbers_with_comma(c):
                    numbers = c.split(',')
                    n1 = eval(numbers[0])  # 第一个数字
                    n2 = eval(numbers[1])  # 第二个数字
                    cprint(operator.truediv(n1, n2))
                else:
                    cprint('')
                    cprint(line, 'red')
                    cprint(f'^^^\nline {h}', 'red')
                    cprint("PyvavError:The statement needs two numbers, and no characters other than numbers appear.\n",
                           'red')
                    break
        except SyntaxError:
            cprint('')
            cprint(line, 'red')
            cprint(f'^^^\nline {h}', 'red')
            cprint("PyvavError:The input is incorrect.\n", 'red')
            break

    elif 'divz ' in line:
        try:
            c = line[4:]
            h = h + 1
            if 'int[' in line:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                n1 = n1[:4] + '"' + n1[4:]
                n1 = n1[:-1] + '"' + n1[-1:]
                n2 = n2[:4] + '"' + n2[4:]
                n2 = n2[:-1] + '"' + n2[-1:]
                n1 = n1.replace('int', 'int1')
                n2 = n2.replace('int', 'int1')
                cprint(operator.floordiv(int(eval(n1)), int(eval(n2))))
            else:
                if check_numbers_with_comma(c):
                    numbers = c.split(',')
                    n1 = eval(numbers[0])  # 第一个数字
                    n2 = eval(numbers[1])  # 第二个数字
                    cprint(operator.floordiv(n1, n2))
                else:
                    cprint('')
                    cprint(line, 'red')
                    cprint(f'^^^\nline {h}', 'red')
                    cprint("PyvavError:The statement needs two numbers, and no characters other than numbers appear.\n",
                           'red')
                    break
        except SyntaxError:
            cprint('')
            cprint(line, 'red')
            cprint(f'^^^\nline {h}', 'red')
            cprint("PyvavError:The input is incorrect.\n", 'red')
            break

    elif 'js ' in line:
        c = line[3:]
        h = h + 1
        print(eval(c))

    elif 'cbl[' in line:
        h = h + 1
        start_bracket = line.find('[')
        end_bracket = line.find(']')
        if start_bracket != -1 and end_bracket != -1 and start_bracket < end_bracket:
            brackets_content = line[start_bracket + 1:end_bracket]  # 加1是为了排除开括号自身
            pass

            # 提取单引号及其内容
        start_quote = line.find("'")
        end_quote = line.find("'", start_quote + 1)
        if start_quote != -1 and end_quote != -1 and start_quote < end_quote:
            quoted_string = line[start_quote + 1:end_quote]  # 加1是为了排除开引号自身
            variable[brackets_content] = quoted_string

            # 如果需要提取双引号及其内容（确保字符串中存在双引号）
        start_double_quote = line.find("\"")
        end_double_quote = line.find("\"", start_double_quote + 1)
        if start_double_quote != -1 and end_double_quote != -1 and start_double_quote < end_double_quote:
            double_quoted_string = line[start_double_quote + 1:end_double_quote]  # 加1是为了排除开引号自身
            variable[brackets_content] = double_quoted_string
        #print(str)

    elif 'int[' in line:
        h = h + 1
        start_bracket = line.find('[')
        end_bracket = line.find(']')
        if start_bracket != -1 and end_bracket != -1 and start_bracket < end_bracket:
            brackets_content = line[start_bracket + 1:end_bracket]  # 加1是为了排除开括号自身
            pass

            # 提取单引号及其内容
        start_quote = line.split("=")
        if len(start_quote) >= 2:
            # 提取等号后面的内容（第二部分，索引为1）
            value_after_equals = start_quote[1].strip()  # 使用strip移除可能的空白字符
            int1[brackets_content] = value_after_equals
            #print(int)
        else:
            cprint(f'\nline{h}', 'red')
            cprint(line, 'red')
            cprint('^' * len(line), 'red')
            cprint('PyvavError:invalid syntax', 'red')
            break

    elif 'play_music(' in line:
        h = h + 1
        p = line[10:]
        play_music(1,p)

    elif 'stop_music()' == line:
        stop_music()

    elif 'music_busy' == line:
        music_busy()

    elif 'open|' in line:
        o = line[5:]
        file = o.split(',')
        n1 = file[0]
        n2 = file[1]
        if not n1 or not n2:
            cprint(f'\nline{h}', 'red')
            cprint(line, 'red')
            cprint('^' * len(line), 'red')
            cprint('PyvavError:Two parameters are required', 'red')
            break
        else:
            try:
                op(n1, n2)
            except FileNotFoundError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint('PyvavError:The file path is incorrect or the file does not exist.', 'red')
            except PermissionError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("PyvavError:You don't have enough permissions to read or write to the file.", 'red')
            except IsADirectoryError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("PyvavError:You're trying to open a directory, not a file.", 'red')
            except TypeError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("PyvavError:The arguments of the open| function are incorrect.", 'red')
            except ValueError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("PyvavError:The file mode is incorrect or not supported.", 'red')
            except OSError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("PyvavError:Operating system-related errors.", 'red')
    elif 'osname' in line:
        cprint(os.name)
    elif 'gy()' in line:
        cprint('pyvav1.0.0\n2022~2024','blue')
    elif '@time' in line:
        kaishi()
    elif '@stop' in line:
        stop()
    elif 'ntime' in line:
        time1()
    elif 'exit' in line:
        break
    elif 'input[' in line:
        line  = line[6:]
        line = line.replace(']', '')
        numbers = line.split(',')
        n1 = numbers[0]
        n2 = numbers[1]
        print(n1,end="",flush=True)
        # 从标准输入读取一行
        user_input = sys.stdin.readline().strip()
        variable[n2] = user_input
    else:
        if line == '':
            pass
        elif line[0] == '!':
            pass
        else:
            cprint(f'\nline{h}','red')
            cprint(line,'red')
            cprint('^'*len(line),'red')
            cprint('PyvavError:invalid syntax','red')
            break
