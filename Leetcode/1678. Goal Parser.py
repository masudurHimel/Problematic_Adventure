class Solution:
    def interpret(self, command):
        _ = command.replace("()", "o")
        return _.replace("(al)", "al")


s = Solution()
print(s.interpret("G()(al)"))