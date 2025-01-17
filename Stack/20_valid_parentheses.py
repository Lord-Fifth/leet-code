class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in parentheses:
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False