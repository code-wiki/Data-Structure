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
    def checkBalancedParanthesis(self, str):
        paranthesisStack = []
        paranthesisStackIndex = -1

        for elem in str:
            if (elem == '{' or elem == '[' or elem == '('):
                paranthesisStack.append(elem)
                paranthesisStackIndex += 1

            elif (elem == '}' or elem == ']' or elem == ')'):
                topStackElem = paranthesisStack[paranthesisStackIndex]

                if (paranthesisStackIndex == -1):
                    return False
                if(topStackElem == '{' and (elem == ']' or elem == ')')):
                    return False
                if(topStackElem == '[' and (elem == '}' or elem == ')')):
                    return False
                if(topStackElem == '(' and (elem == ']' or elem == '}')):
                    return False
                else:
                    paranthesisStack.pop(paranthesisStackIndex)
                    paranthesisStackIndex = paranthesisStackIndex - 1
        return True


if __name__ == "__main__":
    string = raw_input()
    result = Solution().checkBalancedParanthesis(string)
    if (result):
        print "Balanced Paranthesis"
    else:
        print "Not Balanced Paranthesis"
