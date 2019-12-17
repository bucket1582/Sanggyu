import turtle as t
from fireworks import Firework, g
from math import pi, cos, sin
from random import uniform, random
from time import sleep

# settings
fps = 60

screen = t.Screen()
consolefont = ("궁서", 100, "normal")
draw = t.Turtle()

mainText = "졸업 축하드려요!"

def init():
    '''
    init
        initializing the game
    '''
    global screen, fps, draw

    # Screen Settings
    screen.setup(1920, 1080, 0, 0)
    screen.setworldcoordinates(0, 0, 1920, 1080)
    screen.tracer(0, 0)
    screen.title("상규 선배 졸업 축하!")
    screen.ontimer(scene1, 1000//fps) # Update Function
    screen.bgcolor('#000000')
    tSetting(draw)
    for i in range(6):
        Firework([uniform(0, 1920), 0], 20, uniform(pi/6,5*pi/6), 1, (uniform(0.3,1), uniform(0.3,1), uniform(0.3,1)), 4)
    screen.listen()

def tSetting(tur):
    tur.ht()
    tur.speed(0)
    tur.pu()
    tur.color("#FFFFFF")

def scene1():
    global screen, draw
    Firework.processing()
    for f in Firework.fireworks:
        draw.color(f.c)
        draw.goto(f.p)
        draw.dot()
    if len(Firework.fireworks) == 0:
        scene1Fin()
    else:
        screen.update()
        screen.ontimer(scene1, 1000//fps)

def scene1Fin():
    screen.listen()
    draw.color("#FFFFFF")
    draw.goto(960, 540)
    draw.pd()
    text = "상규 선배!"
    for i in range(len(text)):
        draw.write(text[:i+1], move = False, align = "center", font = consolefont)
        screen.update()
        sleep(0.3)
        draw.undo()
    draw.write(mainText, move = False, align = "center", font = consolefont)
    screen.update()
    sleep(0.1)
    draw.pu()
    scene2()

def scene2():
    global screen, draw, fps, mainText
    draw.clear()
    draw.goto(960, 540)
    color = [(1.0, 0, 0), (0, 1.0, 0), (0, 0, 1.0), (1.0, 1.0, 0), (1.0, 1.0, 1.0), (0, 0, 0)]
    for i in range(len(color)):
        draw.color(color[i])
        draw.goto(1920/len(color)*i, 0)
        draw.begin_fill()
        draw.goto(1920/len(color)*i, 1080)
        draw.goto(1920/len(color)*(i + 1), 1080)
        draw.goto(1920/len(color)*(i + 1), 0)
        draw.end_fill()
        screen.update()
        sleep(0.1)
    sleep(0.1)
    scene3()

def scene3():
    global screen, draw, fps, mainText
    draw.clear()
    screen.bgcolor("#000000")
    draw.goto(960, 540)
    draw.color("#FFFFFF")
    for i in mainText:
        draw.write(i, move = False, align = "center", font = consolefont)
        sleep(0.2)
        draw.undo()
    screen.bgcolor("#FFFFFF")
    text = "상규선배!"
    velocity = 90
    accel = -5
    draw.color("#000000")
    for i in range(len(text)):
        for t in range(int(-2*velocity/accel)):
            draw.goto(1920/len(text)*(i + 0.5), velocity * t + 0.5 * accel * (t**2))
            draw.write(text[i], move = False, align = "center", font = consolefont)
            sleep(0.02)
            draw.undo()

    for t in range(int(-velocity/accel)):
        draw.goto(960, velocity * t + 0.5 * accel * (t**2))
        draw.write(mainText, move = False, align = "center", font = consolefont)
        sleep(0.02)
        draw.undo()

    for t in range(int(-velocity/accel), int(-2*velocity/accel)):
        draw.color("#000000")
        if t != int(-velocity/accel):
            draw.goto(0, velocity * (t-1) + 0.5 * accel * ((t-1)**2))
            draw.begin_fill()
            draw.goto(1920, velocity * (t-1) + 0.5 * accel * ((t-1)**2))
            draw.goto(1920, velocity * t + 0.5 * accel * (t**2))
            draw.goto(0, velocity * t + 0.5 * accel * (t**2))
            draw.goto(0, velocity * (t-1) + 0.5 * accel * ((t-1)**2))
            draw.end_fill()
        else:
            draw.goto(0, 1080)
            draw.begin_fill()
            draw.goto(1920, 1080)
            draw.goto(1920, velocity * t + 0.5 * accel * (t**2))
            draw.goto(0, velocity * t + 0.5 * accel * (t**2))
            draw.goto(0, 1080)
            draw.end_fill()
        draw.color("#FFFFFF")
        draw.goto(960, velocity * t + 0.5 * accel * (t**2))
        draw.write(mainText, move = False, align = "center", font = consolefont)
        sleep(0.02)
        draw.undo()
    screen.bgcolor("#000000")
    sleep(0.1)
    scene4()

def scene4():
    global screen, draw, fps, mainText
    draw.clear()
    xIter = 12
    yIter = 7
    for y in range(yIter - 1, -1, -1):
        for x in range(xIter):
            draw.goto(1920/xIter*(x + 0.5), 1080/yIter*(y + 0.5))
            draw.write("상", move = False, align = "center", font = consolefont)
            sleep(0.05)
    for k in range(2):
        sleep(0.2)
        draw.clear()
        screen.bgcolor("#FFFFFF")
        draw.color("#000000")
        for y in range(yIter - 1, -1, -1):
            for x in range(xIter):
                draw.goto(1920/xIter*(x + 0.5), 1080/yIter*(y + 0.5))
                draw.write("규", move = False, align = "center", font = consolefont)
        sleep(0.2)
        draw.clear()
        screen.bgcolor("#000000")
        draw.color("#FFFFFF")
        for y in range(yIter - 1, -1, -1):
            for x in range(xIter):
                draw.goto(1920/xIter*(x + 0.5), 1080/yIter*(y + 0.5))
                draw.write("상", move = False, align = "center", font = consolefont)
    sleep(0.2)
    draw.clear()
    screen.bgcolor("#FFFFFF")
    draw.color("#000000")
    for y in range(yIter - 1, -1, -1):
        for x in range(xIter):
            draw.goto(1920/xIter*(x + 0.5), 1080/yIter*(y + 0.5))
            draw.write("규", move = False, align = "center", font = consolefont)
    sleep(0.2)
    draw.clear()
    screen.bgcolor("#000000")
    draw.color("#FFFFFF")
    text = "선배 축 졸업"
    for i in range(len(text)):
        draw.goto(1920/len(text)*(i + 0.5), 540)
        draw.write(text[i], move = False, align = "center", font = consolefont)
    sleep(1)
    velocity = 45
    accel = -5
    for t in range(30):
        for i in range(len(text)):
            draw.goto(1920/len(text)*(i + 0.5), 540 + velocity * t + 0.5 * accel * (t**2))
            draw.write(text[i], move = False, align = "center", font = consolefont)
        sleep(0.01)
    sleep(0.3)
    scene5()

def scene5():
    global screen, draw, fps, mainText
    draw.clear()
    draw.goto(960, 540)
    color = [(1.0, 0, 0), (0, 1.0, 0), (0, 0, 1.0), (1.0, 1.0, 0), (1.0, 1.0, 1.0), (0, 0, 0)]
    for i in range(len(color)):
        draw.color(color[i])
        draw.goto(1920/len(color)*i, 0)
        draw.begin_fill()
        draw.goto(1920/len(color)*i, 1080)
        draw.goto(1920/len(color)*(i + 1), 1080)
        draw.goto(1920/len(color)*(i + 1), 0)
        draw.end_fill()
        screen.update()
        sleep(0.1)
    sleep(0.1)
    scene6()

def scene6():
    global screen, draw, mainText, consolefont, fps
    draw.clear()
    screen.bgcolor("#FFFFFF")
    draw.color("#000000")
    text = ["선배님,", "한 해 동안", "수고 많으셨습니다.", "3학년인데도", "불구하고,", "바쁘신 와중에도", \
            "동아리에 열심히", "참여해주시고,", "저희에게 많은", "가르침을 주셔서", "감사합니다.", \
            "1학기에", "정보의 날이니", "과학의 날이니", "해서 너무", "많은 일을", "벌인 것이", \
            "아닌가하고", "사죄를", "올립니다.", "(꾸벅)", "이제 학교를", "떠나서", "사회인이", \
            "되실 텐데요.", "아직 저는 어려서", "그게 부러워보이기만", "합니다.", "(웃음)", \
            "사회에 나가신", "후에도", "한결같으시면", "좋겠네요.", "앞으로", "좋은 일만이", \
            "함께 하기를", "그리고", "더 행복하시기를", "바랍니다.", "학교를 떠나는", "선배님의 뒤에서", \
            "9기", "송영진 올림"]
    draw.goto(960, 540)
    for t in text:
        draw.write(t, move = False, align = "center", font = consolefont)
        sleep(0.2*len(t))
        draw.undo()
    scene7()

def scene7():
    global screen, draw, fps, mainText
    draw.clear()
    draw.goto(960, 540)
    color = [(1.0, 0, 0), (0, 1.0, 0), (0, 0, 1.0), (1.0, 1.0, 0), (1.0, 1.0, 1.0), (0, 0, 0)]
    for i in range(len(color)):
        draw.color(color[i])
        draw.goto(1920/len(color)*i, 0)
        draw.begin_fill()
        draw.goto(1920/len(color)*i, 1080)
        draw.goto(1920/len(color)*(i + 1), 1080)
        draw.goto(1920/len(color)*(i + 1), 0)
        draw.end_fill()
        screen.update()
        sleep(0.1)
    sleep(0.1)
    finale()

def finale():
    global screen, draw, fps, mainText
    draw.clear()
    screen.bgcolor("#FFFFFF")
    iteration = 100
    for c in range(0, iteration):
        colorSet = (1/iteration * (iteration - c), 1/iteration * c, 0)
        draw.color(colorSet)
        draw.goto(960/iteration * c, 0)
        draw.begin_fill()
        draw.goto(960/iteration * c, 1080)
        draw.goto(960/iteration * (c+1), 1080)
        draw.goto(960/iteration * (c+1), 0)
        draw.goto(960/iteration * c, 0)
        draw.end_fill()
        sleep(0.01)
        screen.update()

    for c in range(0, iteration):
        colorSet = (0, 1/iteration * (iteration - c), 1/iteration * c)
        draw.color(colorSet)
        draw.goto(960/iteration * c + 960, 0)
        draw.begin_fill()
        draw.goto(960/iteration * c + 960, 1080)
        draw.goto(960/iteration * (c+1) + 960, 1080)
        draw.goto(960/iteration * (c+1) + 960, 0)
        draw.goto(960/iteration * c + 960, 0)
        draw.end_fill()
        sleep(0.01)
        screen.update()
    sleep(0.2)
    screen.bye()
    print("시청해주셔서 감사합니다.")
          
if __name__=="__main__":
    init()
    screen.mainloop()
