from graphics import *
win = GraphWin('Calculator', 600, 600)
win.setBackground("lightgray")

#  operation showing screen
screen_text = Entry(Point(300, 60), 20)
screen_text.setText("0")
screen_text.draw(win)


TextList = ["AC", "7", "4", "1", "0", "+/-", "8", "5", "2", "0", "%", "9", "6", "3", "^", "/", "x", "-", "+", "="]
n = 0

for p in range(0, 451, 150):
    x = p
    z = x + 150
    for m in range(100, 501, 100):
        y = m
        t = y + 100
        Text_calc = Text(Point(x+75, y+50), TextList[n])
        Rect = Rectangle(Point(x, y), Point(z, t))
        Rect.setOutline("black")
        Rect.draw(win)
        Text_calc.draw(win)
        n += 1

Rectan = Rectangle(Point(0, 500), Point(300, 600))
Rectan.setFill("lightgray")

txt = Text(Point(150, 550), "0")

Rectan.draw(win)
txt.draw(win)

result = ""
result_2 = ""
listOfOperators = ['*', '/', '+', '-', '%', '**']
listOfOperands = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def Result():
    if result[-1] in listOfOperators:
        if int(eval(result[:-1])) == float(eval(result[-1])):
            screen_text.setText(str(int(eval(result[:-1]))))
        else:
            screen_text.setText(str(float(eval(result[:-1]))))
    else:
        if int(eval(result)) == float(eval(result)):
            screen_text.setText(str(int(eval(result))))
        else:
            screen_text.setText(str(float(eval(result))))


#  Looping through inputs
while True:
    try:
        a = win.getMouse()
        b = a.getX()
        c = a.getY()
    except:
        win.close()
        break
    #  AC
    if 0 < b < 150 and 100 < c < 200:
        screen_text.setText("0")
        result = ""
        result_2 = ""

    #  7
    elif 0 < b < 150 and 200 < c < 300:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "7"
            result_2 += "7"
            screen_text.setText(result_2)
        else:
            result += "7"
            result_2 += "7"
            screen_text.setText(result_2)

    #  4
    elif 0 < b < 150 and 300 < c < 400:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "4"
            result_2 += "4"
            screen_text.setText(result_2)
        else:
            result += "4"
            result_2 += "4"
            screen_text.setText(result_2)

    #  1
    elif 0 < b < 150 and 400 < c < 500:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "1"
            result_2 += "1"
            screen_text.setText(result_2)
        else:
            result += "1"
            result_2 += "1"
            screen_text.setText(result_2)

    #  0
    elif 0 < b < 300 and 500 < c < 600:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "0"
            result_2 += "0"
            screen_text.setText(result_2)
        else:
            result += "0"
            result_2 += "0"
            if len(result) > 1 and result[-len(result)] == "0":
                result = ""
                result_2 = ""
                screen_text.setText("0")
            elif len(result) > 1:
                screen_text.setText(result_2)

    #  +/-
    elif 150 < b < 300 and 100 < c < 200:
        if bool(result) == False or result[-1] in listOfOperators:
            screen_text.setText("0")
            result = ""
            result_2 = ""
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(-eval(result[:-1]))
            result = "(" + str(-eval(result[:-1])) + ")"
        else:
            result_2 = str(-eval(result_2))
            screen_text.setText(result_2)
            result = "(" + str(-eval(result)) + ")"

    #  8
    elif 150 < b < 300 and 200 < c < 300:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "8"
            result_2 += "8"
            screen_text.setText(result_2)
        else:
            result += "8"
            result_2 += "8"
            screen_text.setText(result_2)

    #  5
    elif 150 < b < 300 < c < 400:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "5"
            result_2 += "5"
            screen_text.setText(result_2)
        else:
            result += "5"
            result_2 += "5"
            screen_text.setText(result_2)

    #  2
    elif 150 < b < 300 and 400 < c < 500:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "2"
            result_2 += "2"
            screen_text.setText(result_2)
        else:
            result += "2"
            result_2 += "2"
            screen_text.setText(result_2)

    #  %
    elif 300 < b < 450 and 100 < c < 200:
        if bool(result) == False or result[-1] in listOfOperators:
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(str(eval(result[:-1])))
            result_2 = ""
            result = "(" + str(eval(result[:-1])) + ")" + "%"
        else:
            Result()
            result_2 = ""
            result = "(" + result + ")" + "%"

    #  9
    elif 200 < c < 300 < b < 450:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "9"
            result_2 += "9"
            screen_text.setText(result_2)
        else:
            result += "9"
            result_2 += "9"
            screen_text.setText(result_2)

    #  6
    elif 300 < b < 450 and 300 < c < 400:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "6"
            result_2 += "6"
            screen_text.setText(result_2)
        else:
            result += "6"
            result_2 += "6"
            screen_text.setText(result_2)

    #  3
    elif 300 < b < 450 and 400 < c < 500:
        if bool(result) == True and (result[-1] == "=" or result[-1] in listOfOperands):
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == ")":
            result = str(eval(result)) + "3"
            result_2 += "3"
            screen_text.setText(result_2)
        else:
            result += "3"
            result_2 += "3"
            screen_text.setText(result_2)

    #  **
    elif 300 < b < 450 and 500 < c < 600:
        if bool(result) == False or result[-1] in listOfOperators:
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(str(eval(result[:-1])))
            result_2 = ""
            result = "(" + str(eval(result[:-1])) + ")" + "**"
        else:
            Result()
            result_2 = ""
            result = "(" + result + ")" + "**"

    #  /
    elif 450 < b < 600 and 100 < c < 200:
        if bool(result) == False or result[-1] in listOfOperators:
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(str(eval(result[:-1])))
            result_2 = ""
            result = "(" + str(eval(result[:-1])) + ")" + "/"
        else:
            Result()
            result_2 = ""
            result = "(" + result + ")" + "/"

    #  x
    elif 450 < b < 600 and 200 < c < 300:
        if bool(result) == False or result[-1] in listOfOperators:
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(str(eval(result[:-1])))
            result_2 = ""
            result = "(" + str(eval(result[:-1])) + ")" + "*"
        else:
            Result()
            result_2 = ""
            result = "(" + result + ")" + "*"

    #  -
    elif 450 < b < 600 and 300 < c < 400:
        if bool(result) == False or result[-1] in listOfOperators:
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(str(eval(result[:-1])))
            result_2 = ""
            result = "(" + str(eval(result[:-1])) + ")" + "-"
        else:
            Result()
            result_2 = ""
            result = "(" + result + ")" + "-"

    #  +
    elif 450 < b < 600 and 400 < c < 500:
        if bool(result) == False or result[-1] in listOfOperators:
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(str(eval(result[:-1])))
            result_2 = ""
            result = "(" + str(eval(result[:-1])) + ")" + "+"
        else:
            Result()
            result_2 = ""
            result = "(" + result + ")" + "+"

    #  =
    elif 450 < b < 600 and 500 < c < 600:
        if bool(result) == False or result[-1] in listOfOperators:
            result = ""
            result_2 = ""
            screen_text.setText("0")
        elif bool(result) == True and result[-1] == "=":
            screen_text.setText(str(eval(result[:-1])))
            result_2 = ""
            result = "(" + str(eval(result[:-1])) + ")" + "="
        elif result[-2:] == "/0":
            screen_text.setText("0")
            result = ""
            result_2 = ""
        else:
            Result()
            result_2 = ""
            result += "="
