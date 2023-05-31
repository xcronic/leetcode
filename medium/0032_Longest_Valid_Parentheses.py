import os
import console_color as console_color

class Solution(object):
    def longestValidParentheses(self, s):
        if len(s) == 0:
            return 0
        
        stack = []
        current_stack_element = 0
        result = 0

        for char in s:
            if char == '(':
                stack.append(current_stack_element)
                current_stack_element = 0
            elif len(stack) > 0:
                current_stack_element += stack.pop() + 2
                result = max(result, current_stack_element)
            else:
                current_stack_element = 0
        
        return result

            
def main():
    os.system('clear')
    solution = Solution()
    
    test_cases = [
        ("(())", 4),
        ("())()())", 4),
        ("(()(", 2), 
        ("(()(((()", 2),
        ("()(()(((()", 2),
        ("()(()()(((()", 4),
        (")()())", 4),
        ("())()", 2),
        ("()(()", 2),
        ("()(())", 6),
        ("()((())", 4),
        ("(", 0),
        ("((((", 0),
        (")", 0),
        (")(((", 0),
        (")()", 2),
        ("(()", 2),
        ("())", 2),
        ("()(", 2),
        ("()()", 4),
        ("()()()()", 8),
        ("((())", 4),
        ("((())))", 6),
    ]
    
    print("**************************")

    for test_case in test_cases:
        result = solution.longestValidParentheses(test_case[0])
        color = console_color.ConsoleColor.RED
        if test_case[1] == result:
            color = console_color.ConsoleColor.GREEN
        console_color.print_colored(f"\"{test_case[0]}\" => \"{result}\", expected result is \"{test_case[1]}\"", color)
            

if __name__ == "__main__":
    main()
