import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 15
TOTAL_PROBLEM = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right= random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

for i in range(TOTAL_PROBLEM):
    expr, answer = generate_problem()
    while True:
        answers = input ("Problem #" + str(i+1)+ ": " +expr + "= " ) 
        if answers == str(answer):
            break
print("Well done Ramanujan!")


    

