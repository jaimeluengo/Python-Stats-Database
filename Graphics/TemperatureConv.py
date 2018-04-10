'''
Jaime Luengo Rozas
jl3752
Program to create GUI to convert celsius to Farenheit and viceversa
'''

from graphics import *
def main():
    win = GraphWin("Temperature Converter", 300,200)
    win.setCoords(0.0,0.0,300.0,200.0)

    #Draw the interface
    Text(Point(90,150), "Celsius Temperature").draw(win)
    Text(Point(105,100), "Farenheit Temperature").draw(win)
    input1 = Entry(Point(240,150),5)
    input1.setText("")
    input1.draw(win)

    
    input2 = Entry(Point(240,100),5)
    input2.setText("")
    input2.draw(win)


    rec = Rectangle(Point(100,20), Point(200,70))
    rec.setFill('yellow')
    rec.setOutline('red')
    rec.draw(win)
    button = Text(Point(150,45),"Convert it")
    button.draw(win)

    pressed=False

    while(True):
        #wait
        click = win.getMouse()
        if(click.getX()<200 and click.getY()<70 and click.getX()>100 and click.getY()>20):
            if(not pressed):
                    #convert input
                    i1=input1.getText()
                    if(i1!= ""):
                        c=eval(input1.getText()) # c = celcius
                        f=1.8*c+32 # f = farenheit

                        #display output and change button
                        input2.setText("%0.1f"%f)
                    else:
                        f=eval(input2.getText())
                        c=(f-32)/1.8 

                        #display output and change button
                        input1.setText("%0.1f"%c)
                    button.setText("Quit")
                    pressed=True
            else:
                #wait for click and then quit
                win.close()
                break
main()
