# 1.怎么查出通过 from xx import xx导⼊的可以直接调⽤的⽅法？
## sys.path

"""
了解Collection模块，编写程序以查询给定列表中最常见的元素。
题目说明:
输入: language = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python','PHP', 'Python']
输出: Python
"""

"""
Input file
language = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python','PHP', 'Python']
Output file
Python
"""
from collections import Counter
language = ['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python','PHP', 'Python']
def most_element(language):
    """ Return a list of lines after inserting a word in a specific line. """
    # your code here
    word_counts = Counter(language)
    top_one = word_counts.most_common()
    return top_one[0][0]

print(most_element(language))