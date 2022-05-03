# 无重复子串 双指针 + 哈希表
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/pythonha-xi-biao-shuang-zhi-zhen-by-leet-9hw1/

def intToRoman(self, num: int) -> str:
    dicts = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL'
        , 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} # 哈希表的创建
    temp = num
    res = ""
    for i in dicts:
        if temp // i > 0: #
            count = temp // i # 得到 商值
            res += dicts[i] * count
            temp = temp % i # 得到余数
    return res

def groupAnagrams(strs) : # https://leetcode-cn.com/problems/group-anagrams/solution/python3-99-by-meng-zhi-hen-n/
    dict = {}
    for i in strs:
        key = tuple(sorted(i))
        dict[key] = dict.get(key, []) + [i] # dict.get(key, value)的用法 ,key不存在时，返回默认的value
    return list(dict.values())

def longestConsecutive(nums): # 学会去掉代码中多余的东西很重要
    dict = {}
    listtemp =  []
    num_set = set(nums)
    maxval = 0
    for item in num_set:
        if item - 1 not in num_set:
            curnum = item
            curval = 1
            while curnum + 1 in num_set:
                curval += 1
                curnum += 1
            maxval = max(maxval, curval)
    return maxval

# LRU cache 哈希表 加 双向链表


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))