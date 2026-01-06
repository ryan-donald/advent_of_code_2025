def evaluate_expression(expr, operator):
    if operator == '+':
        sum = 0
        for num in expr:
            sum += num
        return sum
    elif operator == '*':
        result = 1
        for num in expr:
            result *= num
        return result
    else:
        raise ValueError("unsupported operator")

lines = []
idx = 0 
with open('day_6/input.txt') as f:
    while True:
        data = f.readline().strip()

        if not data:
            break
        data = data.split(' ')
        while '' in data:
            data.remove('')

        # print(data)

        if idx == 0:
            for i in range(len(data)):
                lines.append([data[i]])
            idx += 1
        else:
            for i in range(len(data)):
                lines[i].append(data[i])

sum = 0
for line in lines:
    expr = [int(x) for x in line[:-1]]
    operator = line[-1]
    # print(expr, operator)
    result = evaluate_expression(expr, operator)
    sum+=result

print(f'part 1: {sum}')

# part 2
with open('day_6/input.txt') as f:
    data = f.readlines()

idx = -1
expressions = []
temp = []
# construct expressions column-wise as per the new problem
for i in range(len(data[-1])):
    if data[-1][i] == '\n':
        break
    # increment idx only if not space i.e. it is an operator, start of new expression
    if data[-1][i] != ' ':
        expressions.append(temp)
        temp = []
        temp.append(data[-1][i]) # operator
        idx += 1
    
    num = ''
    for j in range(len(data)-1):
        num += data[j][i]
    if num != '    ':
        temp.append(num)
    
# add last expression, only adds when a new operator is found, last expression is missed
expressions.append(temp)

expressions.pop(0)
        
sum = 0
for line in expressions:
    expr = [int(x) for x in line[1:]]
    operator = line[0]
    print(expr, operator)
    result = evaluate_expression(expr, operator)
    sum+=result

print(f'part 2: {sum}')