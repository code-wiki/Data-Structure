# Hi, here's your problem today. This problem was recently asked by Uber:

# Imagine you are building a compiler.
# Before running any code, the compiler must check that the parentheses in the program are balanced.
# Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.


class Solution:
    def __init__(self):
        self.balancedParanthesisMsg = "Balanced Paranthesis"
        self.nonBalancedParanthesisMsg = "Non Balanced Paranthesis"
        self.stringContainsParanthesis = False

    def checkBalancedParanthesis(self, str):
        paranthesisStack = []
        paranthesisStackIndex = -1

        if (len(str) == 0 or str == ""):
            return "Empty String Provided"

        for elem in str:
            if (elem == '{' or elem == '[' or elem == '('):
                self.stringContainsParanthesis = True
                paranthesisStack.append(elem)
                paranthesisStackIndex += 1

            elif (elem == '}' or elem == ']' or elem == ')'):
                self.stringContainsParanthesis = True
                topStackElem = paranthesisStack[paranthesisStackIndex]

                if (paranthesisStackIndex == -1):
                    return self.balancedParanthesisMsg
                if(topStackElem == '{' and (elem == ']' or elem == ')')):
                    return self.balancedParanthesisMsg
                if(topStackElem == '[' and (elem == '}' or elem == ')')):
                    return self.balancedParanthesisMsg
                if(topStackElem == '(' and (elem == ']' or elem == '}')):
                    return self.balancedParanthesisMsg
                else:
                    paranthesisStack.pop(paranthesisStackIndex)
                    paranthesisStackIndex = paranthesisStackIndex - 1

        if(self.stringContainsParanthesis == False):
            return "String Does Not Contain Paranthesis"
        else:
            return self.balancedParanthesisMsg


if __name__ == "__main__":
    string = raw_input()
    result = Solution().checkBalancedParanthesis(string)
    print result
