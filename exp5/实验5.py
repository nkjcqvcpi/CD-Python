import re


class Expression:
    def __init__(self):
        self.raw = input('请输入表达式：')
        self.format_expression = re.sub(' ', '', self.raw)
        self._expression = []
        self.result = 0

    def format(self):
        for item in [i for i in re.split('(-\d+\.?\d*)', self.format_expression) if i]:
            if len(self._expression) == 0 and re.search('^-\d+\.?\d*$', item):
                self._expression.append(item)
            elif len(self._expression) > 0 and re.search('[+\-*/(]$', self._expression[-1]):
                self._expression.append(item)
            else:
                self._expression += [i for i in re.split('([+\-*/()])', item) if i]

    def calculate(self):
        num_stack = []
        op_stack = []
        for e in self._expression:
            if e not in ['+', '-', '*', '/', '(', ')']:
                num_stack.append(float(e))
            else:
                while True:
                    if len(op_stack) == 0:
                        op_stack.append(e)
                        break
                    tag = self.decision(op_stack[-1], e)
                    if tag == -1:
                        op_stack.append(e)
                        break
                    elif tag == 0:
                        op_stack.pop()
                        break
                    elif tag == 1:
                        num2 = num_stack.pop()
                        num1 = num_stack.pop()
                        num_stack.append(self.calc(num1, num2, op_stack.pop()))
        while len(op_stack) != 0:
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num_stack.append(self.calc(num1, num2, op_stack.pop()))
        self.result = num_stack[0]

    @staticmethod
    def calc(n1, n2, operator):
        if operator == "+":
            return n1 + n2
        elif operator == "-":
            return n1 - n2
        elif operator == "*":
            return n1 * n2
        elif operator == "/":
            return n1 / n2
        else:
            return 0

    @staticmethod
    def decision(tail_op, now_op):
        rate1 = ['+', '-']
        rate2 = ['*', '/']
        rate3 = ['(']
        rate4 = [')']
        if tail_op in rate1:
            op = -1 if now_op in rate2 or now_op in rate3 else 1
        elif tail_op in rate2:
            op = -1 if now_op in rate3 else 1
        elif tail_op in rate3:
            op = 0 if now_op in rate4 else -1
        else:
            op = -1
        return op


if __name__ == '__main__':
    exp = Expression()
    exp.format()
    print('输入为：', exp.format_expression)
    exp.calculate()
    print('结果：', exp.result)
