import os
import console_color as console_color

class Solution(object):
    def trap(self, height):
        
        stack = []
        result = 0

        for (i, cur_h) in enumerate(height):
            if i > 0:
                delta_right = 0
                step_delta = cur_h - height[i-1]
                go_down = step_delta < 0
                go_up = step_delta > 0
                if go_down:
                    stack_value = (i, -step_delta)
                    stack.append(stack_value)
                elif go_up:
                    if len(stack) == 0:
                        continue
                    stack_value = stack[-1]
                    stack_value_h = height[stack_value[0]-1]
                    stack_delta = cur_h - stack_value_h
                    if stack_delta <= 0: # current is lower
                        water_h = step_delta - delta_right
                        result += water_h * (i - stack_value[0])
                        delta_right = 0
                        if stack_delta == 0:
                            stack.pop()
                        else:
                            new_stack_value = (stack_value[0], stack_value[1] - water_h)
                            stack[-1] = new_stack_value
                    elif stack_delta > 0: # current is higher
                        prev_max_found = True

                        while stack_delta > 0:
                            if len(stack) > 0:
                                result += stack_value[1] * (i - stack_value[0])
                                delta_right += stack_value[1]
                                stack.pop()
                                if len(stack) > 0:
                                    stack_value = stack[-1]
                                    stack_value_h = height[stack_value[0]-1]
                                    stack_delta = cur_h - stack_value_h
                            else:
                                prev_max_found = False
                                break
                        
                        if prev_max_found:
                            water_h = step_delta - delta_right
                            result += water_h * (i - stack_value[0])
                            new_stack_value = (stack_value[0], stack_value[1] - water_h)
                            stack[-1] = new_stack_value
        
        return result

            
def main():
    os.system('clear')
    solution = Solution()
    
    test_cases = [
        ([0,9,3,2,1,4,6,5,7,8,11], 36),
        ([0,1,3,1,0,2,4], 6),
        ([4,2,0,3,2,5], 9),
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ]
    
    print("**************************")

    for test_case in test_cases:
        result = solution.trap(test_case[0])
        color = console_color.ConsoleColor.RED
        if test_case[1] == result:
            color = console_color.ConsoleColor.GREEN
        console_color.print_colored(f"\"{test_case[0]}\" => \"{result}\", expected result is \"{test_case[1]}\"", color)
            

if __name__ == "__main__":
    main()
