class Solution:
    def intToRoman(self, num):
        hash_tab = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 900: 'CM', 400: 'CD', 90: 'XC',
                    40: 'XL', 9: 'IX', 4: 'IV'}
        hash_keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''
        i, j = 0, 0
        while True:
            i = hash_keys[j]
            if num // i != 0:
                res += hash_tab[i]
                num -= i
            else:
                j += 1

            if j >= len(hash_keys) or num == 0:
                break
        return res


s = Solution()
print(s.intToRoman(1994))
