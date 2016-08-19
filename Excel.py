import sys
class Excel:
    def __init__(self):
            self.lst = [[0 for x in range(4)] for y in range(4)]
    #Spreadsheet initializing
    def default(self):
        self.cell = self.Cell("1")
        self.lst[0][0] = "1"
        self.lst[0][1] = "2*" + str(self.lst[0][2])
        self.lst[0][2] = "4*" + str(self.lst[0][3])
        self.lst[0][3] = "4"
        self.lst[1][0] = "7"
        self.lst[1][1] = "2*" + str(self.lst[0][0])
        self.lst[1][2] = str(self.lst[0][0]) + "+" + str(self.lst[2][0])
        self.lst[1][3] = str(self.lst[0][0]) + "+" + str(self.lst[0][1]) + "+" + str(self.lst[0][2])
        self.lst[2][0] = "9"
        self.lst[2][1] = "1"
        self.lst[2][2] = "2"
        self.lst[2][3] = str(self.lst[0][2]) + "+" + str(self.lst[0][1])
        self.lst[3][0] = "7"
        self.lst[3][1] = str(self.lst[0][2]) + "+" + str(self.lst[0][3])
        self.lst[3][2] = str(self.lst[0][0]) + "+" + str(self.lst[0][3])
        self.lst[3][3] = str(self.lst[0][1]) + "+" + str(self.lst[0][2])
        #Dictionary for storing indices having formulas as keys and formulas as values
        self.dict = {'0,1': str(self.lst[0][2]),
                    '1,1': str(self.lst[0][0]),
                    '1,2': str(self.lst[0][0]) + "+" + str(self.lst[2][0]),
                    '1,3': str(self.lst[0][0]) + "+" + str(self.lst[0][1]) + "+" + str(self.lst[0][2]),
                    '2,3': str(self.lst[0][2]) + "+" + str(self.lst[0][1]),
                    '3,1': str(self.lst[0][2]) + "+" + str(self.lst[0][3]),
                    '3,2': str(self.lst[0][0]) + "+" + str(self.lst[0][3]),
                    '3,3': str(self.lst[0][1]) + "+" + str(self.lst[0][2])
        }
    #Function for evaluating spreadsheet cells
    def evaluate_sheet(self):
        temp_lst = [[0 for x in range(4)] for y in range(4)]
        for i in range(int(len(self.lst))):
            for j in range(int(len(self.lst))):
             temp_lst[i][j] = self.evalution(self.lst[i][j])
        return temp_lst

    #Function for displaying sheet
    def displaySheet(self):
        for i in range(int(len(self.lst))):
            for j in range(int(len(self.lst))):
                sys.stdout.write(str(self.lst[i][j])+"   ")
            sys.stdout.write('\n')

    def displayArray(self,lst):
        for i in range(int(len(lst))):
            for j in range(int(len(lst))):
                sys.stdout.write(str(lst[i][j]) + "   ")
            sys.stdout.write('\n')


    #Push Operation For Stack
    def push_stack(self,stackArr, ele):
        stackArr.append(ele)

    # Pop Operation For Stack
    def pop_stack(self,stackArr):
        return stackArr.pop()

    def isOperand(self,who):
        if not self.isOperator(who) and who != '(' and who != ')':
            return 1
        return 0

    def isOperator(self,who):
        if who == '+' or who == '-' or who == '*' or who == '/' or who \
                == '^':
            return 1
        return 0

    def topStack(self,stackArr):
        return stackArr[len(stackArr) - 1]

    def isEmpty(self,stackArr):
        if len(stackArr) == 0:
            return 1
        return 0

    def prcd(self,who):
        if who == '^':
            return 5
        if who == '*' or who == '/':
            return 4
        if who == '+' or who == '-':
            return 3
        if who == '(':
            return 2
        if who == ')':
            return 1

    def ip(self,infixStr, postfixStr=[], retType=0):
        postfixStr = []
        stackArr = []
        postfixPtr = 0
        tempStr = infixStr
        infixStr = []
        infixStr = self.strToTokens(tempStr)
        for x in infixStr:
            if self.isOperand(x):
                postfixStr.append(x)
                postfixPtr = postfixPtr + 1
            if self.isOperator(x):
                if x != '^':
                    while not self.isEmpty(stackArr) and self.prcd(x) \
                            <= self.prcd(self.topStack(stackArr)):
                        postfixStr.append(self.topStack(stackArr))
                        self.pop_stack(stackArr)
                        postfixPtr = postfixPtr + 1
                else:
                    while not self.isEmpty(stackArr) and self.prcd(x) \
                            < self.prcd(self.topStack(stackArr)):
                        postfixStr.append(self.topStack(stackArr))
                        self.pop_stack(stackArr)
                        postfixPtr = postfixPtr + 1
                self.push_stack(stackArr, x)
            if x == '(':
                self.push_stack(stackArr, x)
            if x == ')':
                while self.topStack(self.stackArr) != '(':
                    postfixStr.append(self.pop_stack(stackArr))
                    postfixPtr = postfixPtr + 1
                    self.pop_stack(stackArr)

        while not self.isEmpty(stackArr):
            if self.topStack(stackArr) == '(':
                self.pop_stack(stackArr)
            else:
                postfixStr.append(self.pop_stack(stackArr))

        returnVal = ''
        for x in postfixStr:
            returnVal += x

        if retType == 0:
            return returnVal
        else:
            return postfixStr

    def strToTokens(self,str):
        strArr = []
        strArr = str
        tempStr = ''
        tokens = []
        tokens_index = 0
        count = 0
        for x in strArr:
            count = count + 1
            if self.isOperand(x):
                tempStr += x
            if self.isOperator(x) or x == ')' or x == '(':
                if tempStr != '':
                    tokens.append(tempStr)
                    tokens_index = tokens_index + 1
                tempStr = ''
                tokens.append(x)
                tokens_index = tokens_index + 1
            if count == len(strArr):
                if tempStr != '':
                    tokens.append(tempStr)
        return tokens

    def PostfixSubEval(self,num1, num2, sym):
        (num1, num2) = (float(num1), float(num2))
        if sym == '+':
            returnVal = num1 + num2
        if sym == '-':
            returnVal = num1 - num2
        if sym == '*':
            returnVal = num1 * num2
        if sym == '/':
            returnVal = num1 / num2
        if sym == '^':
            returnVal = pow(num1, num2)
        return returnVal

    def PostfixEval(self,postfixStr):
        temp = postfixStr
        postfixStr = []
        postfixStr = temp
        stackArr = []
        for x in postfixStr:
            if self.isOperand(x):
                self.push_stack(stackArr, x)
            else:
                temp = self.topStack(stackArr)
                self.pop_stack(stackArr)
                pushVal = self.PostfixSubEval(self.topStack(stackArr), temp, x)
                self.pop_stack(stackArr)
                self.push_stack(stackArr, pushVal)
        return self.topStack(stackArr)

    def evalution(self,expression_str):
        self.ipe = self.ip(expression_str);
        self.eval = self.PostfixEval(self.ipe)
        return self.eval

    #Cell Class
    class Cell:
        def __init__(self,expression_str):
            self.expression_str = expression_str

#Excel object instantiation
excel = Excel()
#Excel default spreadsheet is loaded in excel object
excel.default()
#Default excel sheet is displayed without updated cell values
excel.displaySheet()
#Excel sheet is evaluated and returned and stored in another 2d array
a = excel.evaluate_sheet()
#BUG -- Excel sheet after updating expressions is displayed,yet it not updates the cells
excel.displayArray(a)



