from tkinter import *
main_window=Tk()
width=900
height=600
paddleW=20
paddleH=100
left_speed=0
right_speed=0
main_speed=5
ball_speed=[2,1]
initial_ball_speed=[2,1]
ball_radius=10
acc=3
Player1_score=0
Player2_score=0
main_canvas=Canvas(main_window,width=width,height=height,bg='black')
main_canvas.pack()
main_canvas.focus_set()
left_paddle=main_canvas.create_rectangle(0,0,paddleW,paddleH,fill='white')
right_paddle=main_canvas.create_rectangle(width-paddleW,height-paddleH,width,height,fill='white')
middle_line=main_canvas.create_line(width/2,0,width/2,height,fill='white',width=1)
ball=main_canvas.create_oval(width/2-ball_radius,height/2-ball_radius,width/2+ball_radius,height/2+ball_radius,fill='white')
p1score=main_canvas.create_text(width/4,20,text=Player1_score,font=30,fill='blue')
p2score=main_canvas.create_text(width-width/4,20,text=Player2_score,font=30,fill='red')
def ball_movement():
    global ball_speed,Player1_score,Player2_score,acc
    if main_canvas.coords(ball)[2]==width-paddleW:
        if (main_canvas.coords(right_paddle)[1]<(main_canvas.coords(ball)[3]-ball_radius)<main_canvas.coords(right_paddle)[3]):
            ball_speed=[acc*(-ball_speed[0]),ball_speed[1]]
            acc=1
        else:
            Player1_score+=1
            main_canvas.itemconfig(p1score,text=Player1_score)
            #ball_respawn()
    if main_canvas.coords(ball)[0]==paddleW:
        if (main_canvas.coords(left_paddle)[1]<(main_canvas.coords(ball)[1]+ball_radius)<main_canvas.coords(left_paddle)[3]):
            ball_speed=[acc*(-ball_speed[0]),ball_speed[1]]
            acc=1
        else:
            Player2_score+=1
            main_canvas.itemconfig(p2score,text=Player2_score)
            #ball_respawn()
    if main_canvas.coords(ball)[1]==0:
        ball_speed=[ball_speed[0],-ball_speed[1]]
    if main_canvas.coords(ball)[3]==height:
        ball_speed=[ball_speed[0],-ball_speed[1]]
    main_canvas.move(ball,ball_speed[0],ball_speed[1])

def ball_respawn(event):
    global initial_ball_speed,ball_speed,acc
    main_canvas.coords(ball,width/2-ball_radius,height/2-ball_radius,width/2+ball_radius,height/2+ball_radius)
    initial_ball_speed=[-initial_ball_speed[0],-initial_ball_speed[1]]
    ball_speed=[initial_ball_speed[0],initial_ball_speed[1]]
    acc=3


def animation():
    paddle_movement()
    ball_movement()

    main_window.after(10, animation)

def paddle_movement():
    global left_speed, right_speed, main_speed
    if main_canvas.coords(left_paddle)[1] == 0 and left_speed == -main_speed:
        left_speed = 0
    elif main_canvas.coords(left_paddle)[3] == height and left_speed == main_speed:
        left_speed = 0
    else:
        main_canvas.move(left_paddle, 0, left_speed)
    if main_canvas.coords(right_paddle)[1] == 0 and right_speed == -main_speed:
        right_speed = 0
    elif main_canvas.coords(right_paddle)[3] == height and right_speed == main_speed:
        right_speed = 0
    else:
        main_canvas.move(right_paddle, 0, right_speed)


def change_speed(event):
    global left_speed, right_speed, main_speed
    if event.keysym == 's':
        if left_speed in [-main_speed, 0]:
            left_speed = left_speed + main_speed
    if event.keysym == 'w':
        if left_speed in [0, main_speed]:
            left_speed = left_speed - main_speed
    if event.keysym == 'Down':
        if right_speed in [-main_speed, 0]:
            right_speed = right_speed + main_speed
    if event.keysym == 'Up':
        if right_speed in [0, main_speed]:
            right_speed = right_speed - main_speed


main_canvas.bind('<KeyPress>', change_speed)
main_canvas.bind("<space>",ball_respawn)
animation()
main_window.mainloop()
