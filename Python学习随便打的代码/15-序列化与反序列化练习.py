# 1.打开中文字符的文档时,会出现乱码,python自带的打开文件是否可以指定文字编码?还是只能用相关函数?
# 可以  encoding  函数(.encode())也可以指定

"""
编写程序查找最长的单词
输入文档: res/test.txt
题目说明:
Input file
test.txt
Output file
['general-purpose,', 'object-oriented,']
"""
import string


def longest_word(filename):
    # your code here
    lines = ''
    with open(filename, 'r+', encoding='utf-8') as f:  # r+ 读写模式
        lines = f.readlines()
    s = str(lines)
    for i in string.punctuation:
        s = s.replace(i, ' ')
    return max(s.split(), key=len)

print(longest_word('test.txt'))  # wonderful

