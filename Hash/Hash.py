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

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))