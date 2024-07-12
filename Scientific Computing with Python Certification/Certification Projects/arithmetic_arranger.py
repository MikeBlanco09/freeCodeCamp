problems = ["3 + 855", "988 + 40"]

def arithmetic_arranger(problems, show_answers=False):

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    #Checks if there are 5 problems or less.
    if len(problems) > 5:
        return ("Error: Too many problems.")
    
    for problem in problems:       
        for char in problem:
            ##Checks if there are any "*" or "/" arithmetic operators.
            if char in "*/":
                return ("Error: Operator must be '+' or '-'.")
            
            elif char in "+-":
                operator_index = problem.find(char)
                first_operand = problem[:operator_index - 1]
                second_operand = problem[operator_index + 2:]
                #Checks if there are any alphabetic characters in the first operand.
                for i in (first_operand + second_operand):
                    if i.isalpha():
                        return ("Error: Numbers must only contain digits.")
                
                first_length = len(first_operand)
                second_length = len(second_operand)
                
                #Checks if both operands have 4 digits or less.
                if max(first_length,second_length) > 4:
                    return ("Error: Numbers cannot be more than four digits.")
                
                result = f"{eval(first_operand + char + second_operand)}"
                result_length = len(result)

                if first_length >= second_length:
                    first_line.append(f"  {first_operand}")
                    second_line.append(f"{char} {' ' * (first_length - second_length)}{second_operand}")
                    third_line.append(f"--{'-' * first_length}")
                    fourth_line.append(f"{' ' * (max(first_length + 2,result_length) - result_length)}{result}")
                else:
                    first_line.append(f"{' ' * (second_length + 2 - first_length)}{first_operand}")
                    second_line.append(f"{char} {second_operand}")
                    third_line.append(f"--{'-' * second_length}") 
                    fourth_line.append(f"{' ' * (max(second_length + 2,result_length) - result_length)}{result}")


    if show_answers == True:
        return (f"{'    '.join(first_line)}\n{'    '.join(second_line)}\n{'    '.join(third_line)}\n{'    '.join(fourth_line)}")
    else:
        return (f"{'    '.join(first_line)}\n{'    '.join(second_line)}\n{'    '.join(third_line)}")


                
                
                

def main():
    print(arithmetic_arranger(problems,True))

main()