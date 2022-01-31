class Solution:
    def defangIPaddr(self, address):
        return address.replace('.', '[.]')


s = Solution()
print(s.defangIPaddr("255.100.50.0"))
