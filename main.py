import pandas
import turtle
screen = turtle.Screen()
screen.setup(1000, 600)
image = 'georgie49 (1).gif'
screen.addshape(image)
turtle.shape(image)
qalaqebi = {
    'city' : ['afxazeti', 'samegrelo', 'guria', 'awara', 'rawa', 'imereti', 'samcxe javaxeti', 'qvemo qartli', 'shida qartli', 'zemo qartli', 'mcxeta tianeti', 'tbilisi', 'kaxeti'],
    'x' : [-299, -181, -189, -195, -44, -66, -57, 148, 68, 84, 206, 212, 330],
    'y' : [143, 59, -74, -131, 63, -37, -150, -171, -71, 8, -16, -122, -98]
}
var = pandas.DataFrame(qalaqebi)
var.to_csv('Georgia.csv')
data = pandas.read_csv('Georgia.csv')
score = 0
guessed= []
notguessed = []
data2 = {
    'city': notguessed,
}

print(data2)
while score < 14:
    question = screen.textinput(f"{score} / 13", 'ჩაწერე ქალაქი')
    if question in str(data['city']):
        jim = turtle.Turtle()
        jim.shape("circle")
        jim.penup()
        jim.speed('fastest')
        jim.shapesize(0.2, 0.2)
        variable = data[data['city'] == question]
        jim.setpos(int(variable.x), int(variable.y))
        print(str(question))
        jim.write(question)
        jim.forward(-10)
        score += 1
        print(question)
        guessed.append(question)
    if question == "exit":
        for i in data.city:
            if not(i in guessed):
                notguessed.append(i)
        varr = pandas.DataFrame(notguessed)
        varr.to_csv('you should revise this shit dude')
        break




