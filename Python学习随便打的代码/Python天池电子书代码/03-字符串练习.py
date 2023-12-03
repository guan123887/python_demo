"""
. 字符串函数回顾
a. 怎么批量替换字符串中的元素？
b. 怎么把字符串按照空格进⾏拆分？
c. 怎么去除字符串⾸位的空格？
"""


#1.
#a.怎么批量替换字符串中的元素？
str='I love I am I' #We love We am We
print(str.replace('I','We'))
#b.怎么把字符串按照空格进⾏拆分？
str1='I love here'
print(str1.split());    #['I', 'love', 'here']
#c. 怎么去除字符串⾸位的空格？
str3=' I LOVE HERE   '
print(str3.lstrip())    #'I LOVE HERE   '



#2.实现isdigit
#实现函数isdigit， 判断字符串里是否只包含数字0~9
def isdigit(str):
    return str.isnumeric();
str='12345s'
print(isdigit(str))

#3.给定一个字符串 s ，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000
class Solution:
    def longestPalindrome(self,str):
        pass

sol=Solution()
s1='babad'
s2='cbbd'
print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))





