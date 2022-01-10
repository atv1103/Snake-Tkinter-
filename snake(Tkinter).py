from tkinter import *
import time
import random

# main window settings
root = Tk()
root.title("Snake Tkinter")
game_running = True
game_width = 620
game_height = 480
snake_frame = 10
virtual_game_x = game_width // snake_frame
virtual_game_y = game_height // snake_frame
root.resizable(False, False)  # prohibition of resizing window
root.configure(bg="white")
root.wm_attributes("-topmost", 1) # game window in front of the other windows
canvas = Canvas(root, width=game_width, height=game_height, bd=0, highlightthickness=0)
canvas.pack()
root.update()

# snake form settings
snake_color = "green"
snake_position_x = virtual_game_x // 2  # start position X
snake_position_y = virtual_game_y // 2  # start position Y
snake_x_navigate = 0
snake_y_navigate = 0
snake_list = []
snake_size = 3

# food settings
food_color1 = "orange"
food_color2 = "brown"
food_list = []
food_quantity = 10
for i in range(food_quantity):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x * snake_frame, y * snake_frame, x * snake_frame + snake_frame, y * snake_frame + snake_frame, fill=food_color2)
    id2 = canvas.create_oval(x * snake_frame + 2, y * snake_frame + 2, x * snake_frame + snake_frame - 2, y * snake_frame + snake_frame - 2, fill=food_color1)
    food_list.append([x, y, id1, id2])
#print(food_list)

def snake_paint_frame(canvas, x, y):  # snake visual form
    global snake_list
    id1 = canvas.create_rectangle(x * snake_frame, y * snake_frame, x * snake_frame + snake_frame, y * snake_frame + snake_frame, fill=snake_color)
    id2 = canvas.create_rectangle(x * snake_frame + 2, y * snake_frame + 2, x * snake_frame + snake_frame - 2, y * snake_frame + snake_frame - 2, fill=snake_color)
    snake_list.append([x, y, id1, id2])
    #print(snake_list)

snake_paint_frame(canvas, snake_position_x, snake_position_y)  # snake start position

def check_can_we_delete_snake_frame():  # when moving, delete last snake frame
    if len(snake_list) >= snake_size:
        temp_frame = snake_list.pop(0)
        #print(temp_frame)
        canvas.delete(temp_frame[2])
        canvas.delete(temp_frame[3])

def check_if_snake_eat_food():  # when snake found food frame
    global snake_size
    for i in range(len(food_list)):
        if food_list[i][0] == snake_position_x and food_list[i][1] == snake_position_y:
            snake_size += 1
            canvas.delete(food_list[i][2])
            canvas.delete(food_list[i][3])

def game_over():  # game over settings
    global game_running
    game_running = False

def check_border():  # when snake touch window border
    if snake_position_x > virtual_game_x or snake_position_x < 0 or snake_position_y > virtual_game_y or snake_position_y < 0:
        game_over()

# when snake touch self frames border
def check_touch_snake_frame(future_x, future_y):
    global game_running
    if not (snake_x_navigate == 0 and snake_y_navigate == 0):
        for i in range(len(snake_list)):
            if snake_list[i][0] == future_x and snake_list[i][1] == future_y:
                #print("OMG!")
                game_running = False

def snake_move(event):  # snake move
    global snake_position_x
    global snake_position_y
    global snake_x_navigate
    global snake_y_navigate
    if event.keysym == "Up":
        snake_x_navigate = 0
        snake_y_navigate = -1
        check_can_we_delete_snake_frame()
    elif event.keysym == "Down":
        snake_x_navigate = 0
        snake_y_navigate = 1
        check_can_we_delete_snake_frame()
    elif event.keysym == "Left":
        snake_x_navigate = -1
        snake_y_navigate = 0
        check_can_we_delete_snake_frame()
    elif event.keysym == "Right":
        snake_x_navigate = 1
        snake_y_navigate = 0
        check_can_we_delete_snake_frame()
    snake_position_x += snake_x_navigate
    snake_position_y += snake_y_navigate
    snake_paint_frame(canvas, snake_position_x, snake_position_y)  # snake move position

canvas.bind_all("<Left>", snake_move)
canvas.bind_all("<Right>", snake_move)
canvas.bind_all("<Up>", snake_move)
canvas.bind_all("<Down>", snake_move)

while game_running:  # endless move
    check_can_we_delete_snake_frame()
    check_if_snake_eat_food()
    check_border()
    check_touch_snake_frame(
        snake_position_x + snake_x_navigate, snake_position_y + snake_y_navigate)
    snake_position_x += snake_x_navigate
    snake_position_y += snake_y_navigate
    snake_paint_frame(canvas, snake_position_x, snake_position_y)
    root.update_idletasks()
    root.update()
    time.sleep(0.2)

def function_nothing(event):  # when game over snake don't move
    pass
canvas.bind_all("<Left>", function_nothing)
canvas.bind_all("<Right>", function_nothing)
canvas.bind_all("<Up>", function_nothing)
canvas.bind_all("<Down>", function_nothing)


root.mainloop()
