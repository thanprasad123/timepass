import tkinter as tk
import random
rows=25
cols=25
tile_size=25
 

window_width=rows*tile_size
window_height=cols*tile_size

#gmae window
window=tk.Tk()
window.title("snake game")
window.resizable(False,False)
canvas=tk.Canvas(window,width=window_width,height=window_height,bg="black",borderwidth=0,highlightthickness=0)
canvas.pack()
window.update()


#centre the window on the screen
window.width=window.winfo_width()
window.height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
snake_x = tile_size * 5
snake_y = tile_size * 5

snake_body = [(snake_x, snake_y)]

velocity_x = 1
velocity_y = 0

def place_food():
    fx = random.randint(0, cols - 1) * tile_size
    fy = random.randint(0, rows - 1) * tile_size
    return (fx, fy)

food = place_food()
 
def change_direction(event):
    global velocity_x, velocity_y
    key = event.keysym

    if key == "Up" and velocity_y != 1:
        velocity_x = 0
        velocity_y = -1
    elif key == "Down" and velocity_y != -1:
        velocity_x = 0
        velocity_y = 1
    elif key == "Left" and velocity_x != 1:
        velocity_x = -1
        velocity_y = 0
    elif key == "Right" and velocity_x != -1:
        velocity_x = 1
        velocity_y = 0

window.bind("<KeyPress>", change_direction)


# ------------ GAME LOOP ------------
def update():
    global snake_x, snake_y, food

    # move snake head
    snake_x += velocity_x * tile_size
    snake_y += velocity_y * tile_size
    new_head = (snake_x, snake_y)

    # wall collision
    if (snake_x < 0 or snake_x >= window_width or
        snake_y < 0 or snake_y >= window_height):
        return game_over()

    # self collision
    if new_head in snake_body:
        return game_over()

    # insert new head
    snake_body.insert(0, new_head)

    # food collision
    if new_head == food:
        food = place_food()
    else:
        snake_body.pop()

    draw()
    window.after(100, update)


# ------------ DRAW GAME ------------
def draw():
    canvas.delete("all")

    # draw food
    fx, fy = food
    canvas.create_rectangle(fx, fy, fx + tile_size, fy + tile_size, fill="red")

    # draw snake
    for (x, y) in snake_body:
        canvas.create_rectangle(x, y, x + tile_size, y + tile_size, fill="lime")


# ------------ GAME OVER ------------
def game_over():
    canvas.create_text(
        window_width / 2,
        window_height / 2,
        text="GAME OVER",
        fill="white",
        font=("Arial", 30)
    )


update()
window.mainloop()
