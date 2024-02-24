# https://pypi.tuna.tsinghua.edu.cn/simple
# -*- coding: utf-8 -*-

"""
Copyright [2024] [xinhaitianze]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
#中文声明:
"""
版权所有 [2024] [新海田泽]

根据 Apache 许可证 2.0 版（“许可证”）获得许可;
除非遵守本许可，否则您不得使用此文件。
您可以在以下位置获取许可证的副本

http://www.apache.org/licenses/LICENSE-2.0

除非适用法律要求或书面同意，
否则软件根据许可证分发的“按原样”分发，
不作任何明示或暗示的保证或条件。
有关管理权限的特定语言，请参阅许可证下的限制。
"""

from colorama import Fore,init
import sys
import time
import operator
import re
import os
import main
import pygame
import pyttsx3

pygame.init()

def play(music_file, num=1):
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(num)
        while pygame.mixer.music.get_busy():
            continue
    except pygame.error as e:
        print(f"PyvavError:Error playing music: {e}")
    except KeyboardInterrupt:
        pygame.mixer.music.stop()

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def busy():
    print(pygame.mixer.music.get_busy())

def stop():
    pygame.mixer.music.stop()

def unpuse():
    pygame.mixer.music.unpause()

def yl(y):
    pygame.mixer.music.set_volume(y)

def pos(num):
    pygame.mixer.music.set_pos(num)

with open('code.vav', 'r', encoding='utf-8') as fi:
    fi = fi.read()
    code = fi

# code = input('>>>|')


bm = ''
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



def op(n1, n2):
    with open(n1, n2, encoding=bm) as f:
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


def encoding(s):
    global bm
    bm = s

def cs(word, string):
    return len(re.findall(r'\b{}\b'.format(re.escape(word)), string))#检查词语出现次数

def jcs(text):
    return  isinstance(text,int)

def jci(text):
    return  isinstance(text,str)

h = 0
variable = {}
int1 = {}
user_input = ''
hs = {}
hsm = []

for line in code.splitlines():
    if 'import ' in line:
        h = h + 1
        l = line[7:]
        with open(l, 'r', encoding='utf-8') as mk:
            mk_content = mk.read()
            new_content = mk_content
            new_content = f'\n{new_content}\n'
            # 替换原始代码中的行
            code = code.replace(line, new_content)
            print(code)


for line in code.splitlines():
    line = line.rstrip(';')
    if line[:4] == '    ':
        pass
    elif 'cprint ' in line:
        h = h + 1
        c = line[7:]
        try:
            if 'cbl[' in line:
                s = line[11:-1]  # 使用切片删除尾部的 ']'
                cprint(variable[s])
            elif 'int[' in line:
                s = line[11:-1]  # 使用切片删除尾部的 ']'
                cprint(int1[s])
            else:
                cprint(c)
        except KeyError as e:
            # 直接打印错误消息，不需要尝试切片
            cprint('')
            cprint(f'line {h}', 'red')
            cprint(line, 'red')
            cprint('^' * len(line), 'red')
            # 获取KeyError的异常信息，通常是未定义的键名
            undefined_name = str(e)
            cprint(f"CodexError: name {undefined_name} is not defined\n", 'red')
            break

    elif 'bprint ' in line:
        h = h + 1
        c = line[7:]
        try:
            if 'cbl[' in line:
                s = line[11:-1]  # 使用切片删除尾部的 ']'
                sys.stdout.write(variable[s])
            elif 'int[' in line:
                s = line[11:-1]  # 使用切片删除尾部的 ']'
                sys.stdout.write(int1[s])
            else:
                sys.stdout.write(c)
        except KeyError as e:
            # 直接打印错误消息，不需要尝试切片
            cprint('')
            cprint(line, 'red')
            cprint('^' * len(line), 'red')
            # 获取KeyError的异常信息，通常是未定义的键名
            undefined_name = str(e)
            cprint(f"CodexError: name {undefined_name} is not defined\n", 'red')
            break

    elif 'sleep ' in line:
        h = h + 1
        s = line[6:]
        time.sleep(eval(s))
    elif 'add ' in line:
        bm = line.replace('add ', '').split(",")
        bm = bm[2]
        try:
            c = line[4:]
            h = h + 1
            m = cs('int[', line)
            # print(m)
            if m == 2:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                n1 = n1[:4] + '"' + n1[4:]
                n1 = n1[:-1] + '"' + n1[-1:]
                n2 = n2[:4] + '"' + n2[4:]
                n2 = n2[:-1] + '"' + n2[-1:]
                n1 = n1.replace('int', 'int1')
                n2 = n2.replace('int', 'int1')
                m1 = operator.add(int(eval(n1)), int(eval(n2)))
                int1[bm] = m1
            elif m == 1:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                if 'int[' in n1:
                    n1 = n1[:4] + '"' + n1[4:]
                    n1 = n1[:-1] + '"' + n1[-1:]
                    n1 = n1.replace('int', 'int1')
                    m1 = operator.add(int(eval(n1)), int(n2))
                    int1[bm] = m1
                elif 'int[' in n2:
                    n2 = n2[:4] + '"' + n2[4:]
                    n2 = n2[:-1] + '"' + n2[-1:]
                    n2 = n2.replace('int', 'int1')
                    m1 = operator.add(int(eval(n1)), int(n2))
                    int1[bm] = m1
            else:
                if check_numbers_with_comma(c):
                    numbers = c.split(',')
                    n1 = eval(numbers[0])  # 第一个数字
                    n2 = eval(numbers[1])  # 第二个数字
                    m1 = operator.add(int(eval(n1)), int(n2))
                    int1[bm] = m1
                else:
                    cprint('')
                    cprint(line, 'red')
                    cprint(f'^^^\nline {h}', 'red')
                    cprint("CodexError:The statement needs two numbers, and no characters other than numbers appear.\n",
                           'red')
                    break

        except SyntaxError:
            cprint('')
            cprint(line, 'red')
            cprint(f'^^^\nline {h}', 'red')
            cprint("CodexError:The input is incorrect.\n", 'red')
            break
    elif 'sub ' in line:
            bm = line.replace('sub  ', '').split(",")
            bm = bm[2]
            try:
                c = line[4:]
                h = h + 1
                m = cs('int[', line)
                # print(m)
                if m == 2:
                    numbers = c.split(',')
                    n1 = numbers[0]
                    n2 = numbers[1]
                    n1 = n1[:4] + '"' + n1[4:]
                    n1 = n1[:-1] + '"' + n1[-1:]
                    n2 = n2[:4] + '"' + n2[4:]
                    n2 = n2[:-1] + '"' + n2[-1:]
                    n1 = n1.replace('int', 'int1')
                    n2 = n2.replace('int', 'int1')
                    m1 = operator.sub(int(eval(n1)), int(n2))
                    int1[bm] = m1
                elif m == 1:
                    numbers = c.split(',')
                    n1 = numbers[0]
                    n2 = numbers[1]
                    if 'int[' in n1:
                        n1 = n1[:4] + '"' + n1[4:]
                        n1 = n1[:-1] + '"' + n1[-1:]
                        n1 = n1.replace('int', 'int1')
                        m1 = operator.sub(int(eval(n1)), int(n2))
                        int1[bm] = m1
                    elif 'int[' in n2:
                        n2 = n2[:4] + '"' + n2[4:]
                        n2 = n2[:-1] + '"' + n2[-1:]
                        n2 = n2.replace('int', 'int1')
                        m1 = operator.sub(int(eval(n1)), int(n2))
                        int1[bm] = m1
                else:
                    if check_numbers_with_comma(c):
                        numbers = c.split(',')
                        n1 = eval(numbers[0])  # 第一个数字
                        n2 = eval(numbers[1])  # 第二个数字
                        m1 = operator.sub(int(eval(n1)), int(n2))
                        int1[bm] = m1
                    else:
                        cprint('')
                        cprint(line, 'red')
                        cprint(f'^^^\nline {h}', 'red')
                        cprint(
                            "CodexError:The statement needs two numbers, and no characters other than numbers appear.\n",
                            'red')
                        break

            except SyntaxError:
                cprint('')
                cprint(line, 'red')
                cprint(f'^^^\nline {h}', 'red')
                cprint("CodexError:The input is incorrect.\n", 'red')
                break
    elif 'mul ' in line:
                bm = line.replace('mul ', '').split(",")
                bm = bm[2]
                c = line[4:]
                h = h + 1
                m = cs('int[', line)
                try:

                    # print(m)
                    if m == 2:
                        numbers = c.split(',')
                        n1 = numbers[0]
                        n2 = numbers[1]
                        n1 = n1[:4] + '"' + n1[4:]
                        n1 = n1[:-1] + '"' + n1[-1:]
                        n2 = n2[:4] + '"' + n2[4:]
                        n2 = n2[:-1] + '"' + n2[-1:]
                        n1 = n1.replace('int', 'int1')
                        n2 = n2.replace('int', 'int1')
                        m1 = operator.mul(int(eval(n1)), int(n2))
                        int1[bm] = m1
                    elif m == 1:
                        numbers = c.split(',')
                        n1 = numbers[0]
                        n2 = numbers[1]
                        if 'int[' in n1:
                            n1 = n1[:4] + '"' + n1[4:]
                            n1 = n1[:-1] + '"' + n1[-1:]
                            n1 = n1.replace('int', 'int1')
                            m1 = operator.mul(int(eval(n1)), int(n2))
                            int1[bm] = m1
                        elif 'int[' in n2:
                            n2 = n2[:4] + '"' + n2[4:]
                            n2 = n2[:-1] + '"' + n2[-1:]
                            n2 = n2.replace('int', 'int1')
                            m1 = operator.mul(int(eval(n1)), int(n2))
                            int1[bm] = m1
                    else:
                        if check_numbers_with_comma(c):
                            numbers = c.split(',')
                            n1 = eval(numbers[0])  # 第一个数字
                            n2 = eval(numbers[1])  # 第二个数字
                            m1 = operator.mul(int(eval(n1)), int(n2))
                            int1[bm] = m1
                        else:
                            cprint('')
                            cprint(line, 'red')
                            cprint(f'^^^\nline {h}', 'red')
                            cprint(
                                "CodexError:The statement needs two numbers, and no characters other than numbers appear.\n",
                                'red')
                            break

                except SyntaxError:
                    cprint('')
                    cprint(line, 'red')
                    cprint(f'^^^\nline {h}', 'red')
                    cprint("CodexError:The input is incorrect.\n", 'red')
                    break
    elif 'div ' in line:
                    c = line[4:]
                    h = h + 1
                    m = cs('int[', line)
                    bm = line.replace('div ', '').split(",")
                    bm = bm[2]
                    try:
                        c = line[4:]
                        h = h + 1
                        m = cs('int[', line)
                        # print(m)
                        if m == 2:
                            numbers = c.split(',')
                            n1 = numbers[0]
                            n2 = numbers[1]
                            n1 = n1[:4] + '"' + n1[4:]
                            n1 = n1[:-1] + '"' + n1[-1:]
                            n2 = n2[:4] + '"' + n2[4:]
                            n2 = n2[:-1] + '"' + n2[-1:]
                            n1 = n1.replace('int', 'int1')
                            n2 = n2.replace('int', 'int1')
                            m1 = operator.truediv(int(eval(n1)), int(n2))
                            int1[bm] = m1
                        elif m == 1:
                            numbers = c.split(',')
                            n1 = numbers[0]
                            n2 = numbers[1]
                            if 'int[' in n1:
                                n1 = n1[:4] + '"' + n1[4:]
                                n1 = n1[:-1] + '"' + n1[-1:]
                                n1 = n1.replace('int', 'int1')
                                m1 = operator.truediv(int(eval(n1)), int(n2))
                                int1[bm] = m1
                            elif 'int[' in n2:
                                n2 = n2[:4] + '"' + n2[4:]
                                n2 = n2[:-1] + '"' + n2[-1:]
                                n2 = n2.replace('int', 'int1')
                                m1 = operator.truediv(int(eval(n1)), int(n2))
                                int1[bm] = m1
                        else:
                            if check_numbers_with_comma(c):
                                numbers = c.split(',')
                                n1 = eval(numbers[0])  # 第一个数字
                                n2 = eval(numbers[1])  # 第二个数字
                                m1 = operator.truediv(int(eval(n1)), int(n2))
                                int1[bm] = m1
                            else:
                                cprint('')
                                cprint(line, 'red')
                                cprint(f'^^^\nline {h}', 'red')
                                cprint(
                                    "CodexError:The statement needs two numbers, and no characters other than numbers appear.\n",
                                    'red')
                                break

                    except SyntaxError:
                        cprint('')
                        cprint(line, 'red')
                        cprint(f'^^^\nline {h}', 'red')
                        cprint("CodexError:The input is incorrect.\n", 'red')
                        break
#truediv
    elif 'divz ' in line:
        bm = line.replace('divz ', '').split(",")
        bm = bm[2]
        try:
            c = line[5:]
            h = h + 1
            m = cs('int[', line)
            # print(m)
            if m == 2:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                n1 = n1[:4] + '"' + n1[4:]
                n1 = n1[:-1] + '"' + n1[-1:]
                n2 = n2[:4] + '"' + n2[4:]
                n2 = n2[:-1] + '"' + n2[-1:]
                n1 = n1.replace('int', 'int1')
                n2 = n2.replace('int', 'int1')
                m1 = operator.floordiv(int(eval(n1)), int(eval(n2)))
                int1[bm] = m1
            elif m == 1:
                numbers = c.split(',')
                n1 = numbers[0]
                n2 = numbers[1]
                if 'int[' in n1:
                    n1 = n1[:4] + '"' + n1[4:]
                    n1 = n1[:-1] + '"' + n1[-1:]
                    n1 = n1.replace('int', 'int1')
                    m1 = operator.floordiv(int(eval(n1)), int(n2))
                    int1[bm] = m1
                elif 'int[' in n2:
                    n2 = n2[:4] + '"' + n2[4:]
                    n2 = n2[:-1] + '"' + n2[-1:]
                    n2 = n2.replace('int', 'int1')
                    m1 = operator.floordiv(int(n1), int(eval(n2)))
                    int1[bm] = m1
            else:
                if check_numbers_with_comma(c):
                    numbers = c.split(',')
                    n1 = eval(numbers[0])  # 第一个数字
                    n2 = eval(numbers[1])  # 第二个数字
                    m1 = operator.floordiv(n1, n2)
                    int1[bm] = m1
                else:
                    cprint('')
                    cprint(line, 'red')
                    cprint(f'^^^^\nline {h}', 'red')
                    cprint(
                        "CodexError:The statement needs two numbers, and no characters other than numbers appear.\n",
                        'red')
                    break

        except SyntaxError:
            cprint('')
            cprint(line, 'red')
            cprint(f'^^^^\nline {h}', 'red')
            cprint("CodexError:The input is incorrect.\n", 'red')
            break

#floordiv

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
        # print(str)

    elif 'int[' in line:
        h = h + 1
        start_bracket = line.find('[')
        end_bracket = line.find(']')
        if start_bracket != -1 and end_bracket != -1 and start_bracket < end_bracket:
            brackets_content = line[start_bracket + 1:end_bracket]  # 加1是为了排除开括号自身

            # 提取单引号及其内容
        start_quote = line.split("=")
        if len(start_quote) >= 2:
            # 提取等号后面的内容（第二部分，索引为1）
            value_after_equals = start_quote[1].strip()  # 使用strip移除可能的空白字符
            int1[brackets_content] = value_after_equals
            # print(int)
        else:
            cprint(f'\nline{h}', 'red')
            cprint(line, 'red')
            cprint('^' * len(line), 'red')
            cprint('CodexError:invalid syntax', 'red')
            break

    elif 'open|' in line:
        h = h + 1
        o = line[5:]
        file = o.split(',')
        n1 = file[0]
        n2 = file[1]
        if not n1 or not n2:
            cprint(f'\nline{h}', 'red')
            cprint(line, 'red')
            cprint('^' * len(line), 'red')
            cprint('CodexError:Two parameters are required', 'red')
            break
        else:
            try:
                op(n1, n2)
            except FileNotFoundError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint('CodexError:The file path is incorrect or the file does not exist.', 'red')
                break
            except PermissionError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("CodexError:You don't have enough permissions to read or write to the file.", 'red')
                break
            except IsADirectoryError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("CodexError:You're trying to open a directory, not a file.", 'red')
                break
            except TypeError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("CodexError:The arguments of the open| function are incorrect.", 'red')
                break
            except ValueError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("CodexError:The file mode is incorrect or not supported.", 'red')
                break
            except OSError:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint("CodexError:Operating system-related errors.", 'red')
                break
    elif 'osname' in line:
        h = h + 1
        cprint(os.name)
    elif 'gy()' in line:
        h = h + 1
        cprint('Codex1.4.0\n2022~2024\n开发者:新海田沢', 'blue')
    elif '@time' in line:
        h = h + 1
        kaishi()
    elif '@stop' in line:
        h = h + 1
        stop()
    elif 'ntime' in line:
        h = h + 1
        time1()
    elif 'exit' in line:
        h = h + 1
        break
    elif 'input[' in line:
        h = h + 1
        line = line[6:]
        line = line.replace(']', '')
        numbers = line.split(',')
        n1 = numbers[0]
        n2 = numbers[1]
        print(n1, end="", flush=True)
        # 从标准输入读取一行
        user_input = sys.stdin.readline().strip()
        variable[n2] = user_input
        # 返回用户输入的字符串
        # print(user_input)
    elif 'intsr[' in line:
        h = h + 1
        line = line[6:]
        line = line.replace(']', '')
        numbers = line.split(',')
        n1 = numbers[0]
        n2 = numbers[1]
        print(n1, end="", flush=True)
        # 从标准输入读取一行
        user_input = sys.stdin.readline().strip()
        int1[n2] = int(user_input)

    elif 'js[' in line:
        h = h + 1
        pattern = r'js\[(.*?),(.*?)\]'  # 修改了正则表达式以匹配 'js['

        # 使用 re.search() 来搜索匹配项
        match = re.search(pattern, line)
        if 'int[' in line:
            # 提取算式和变量名
            expression = match.group(1)  # 第一个捕获组，即算式部分
            variable_name = match.group(2)  # 第二个捕获组，即变量名部分

            # 尝试计算算式的结果
            try:
                result = eval(expression)
                # 将结果存入字典，以变量名为键
                int1[variable_name] = result
            except Exception as e:
                # 如果计算出现错误，打印错误信息
                cprint('')
                cprint(f'line {h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint(f"CodexErrorError evaluating expression '{expression}': {e}", 'red')
                break
        else:
            # 提取算式和变量名
            expression = match.group(1)  # 第一个捕获组，即算式部分
            variable_name = match.group(2)  # 第二个捕获组，即变量名部分

            # 尝试计算算式的结果
            try:
                result = eval(expression)
                # 将结果存入字典，以变量名为键
                int1[variable_name] = result
            except Exception as e:
                # 如果计算出现错误，打印错误信息
                cprint('')
                cprint(f'line {h}', 'red')
                cprint(line,'red')
                cprint('^' * len(line), 'red')
                cprint(f"CodexErrorError evaluating expression '{expression}': {e}", 'red')
                break


    elif 'encoding|' in line:
        h = h + 1
        line = line[9:]
        encoding(line)

    elif '/k' in line:
        h = h + 1
        cprint('')

    elif 'play[' in line:
        line = line.replace('play[', '').replace(']', '').split(',')
        #print(line)
        wj = line[0]
        yl = int(line[1])
        #print(yl)
        play(wj,yl)

    elif 'stop_music' in line:
        stop()

    elif 'busy' in line:
        busy()

    elif 'def ' in line:
        h = h + 1
        parts = line.split()
        ddd = parts[1] if len(parts) > 1 else None
        #print(ddd)

        line = line.replace('(', ' ').replace(')', '').replace(':', '').split(" ")
        #print(f'函数名:{line}')
        pattern = r'def (.*?)end'
        code = code.replace(ddd,'').replace('    ','')
        matches = re.findall(pattern,code, re.DOTALL)
        #print(f'代码:{matches}')
        hs[line[1]] = matches[0]
        #print(hs)
        #print(line[1])
        hsm.append(line[1]+'()')
        #print(f'已有函数:{hsm}')
    elif 'loop ' in line:
        h = h + 1
        line = line.replace('{', '')[5:]
        #print(line)
        if line == 'True':
            pattern = r'loop (.*?)}'
            code = code.replace('    ', '').replace('True{', '')
            matches = re.findall(pattern, code, re.DOTALL)
            #print(matches)
            while True:
                main.codex(matches[0])

    elif 'jci[' in line:
        h += 1
        line = line[4:].replace(']', '')
        #print(line)
        print(jci(line))
    elif 'jcs' in line:
        h += 1
        line = line[4:].replace(']', '')
        # print(line)
        print(jcs(line))




    else:
        h = h + 1
        if line == '':
            pass
        elif line == '}':
            pass
        elif line == 'end':
            pass
        elif line[0] == '!':
            pass
        elif '()' in line:
            if line in hsm:
                line = line.replace('()', '')
                g = hs[line]
                #print(g)
                main.codex(g)
            else:
                cprint(f'\nline{h}', 'red')
                cprint(line, 'red')
                cprint('^' * len(line), 'red')
                cprint('CodexError:This function does not exist', 'red')
                break
        else:
            cprint(f'\nline{h}', 'red')
            cprint(line, 'red')
            cprint('^' * len(line), 'red')
            cprint('CodexError:invalid syntax', 'red')
            break
