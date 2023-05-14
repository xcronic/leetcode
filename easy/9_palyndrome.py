import console_color as console_color

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        
        digits = []
        n = x
        while n:
            digits.append(n % 10)
            n //= 10

        for i in range(len(digits) // 2):
            if digits[i] != digits[-(i + 1)]:
                return False
            
        return True
        


def main():
    solution = Solution()
    
    test_cases = [
        (1,True),
        (11,True),
        (12,False),
        (88,True),
        (86,False),
        (121,True),
        (122,False),
        (-121,False),
        (0,True),
        (12321,True),
        (12324,False),
    ]
    
    for test_case in test_cases:
        result = solution.isPalindrome(test_case[0])
        color = console_color.ConsoleColor.RED
        if test_case[1] == result:
            color = console_color.ConsoleColor.GREEN
        console_color.print_colored(f"{test_case[0]} => {result}, expected result is {test_case[1]}", color)
            

if __name__ == "__main__":
    main()
