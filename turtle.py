import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_win.setup(500, 500)


def draw_spiral(my_turtle, line_len):
    if line_len <= 0:             # works till length is greater than 0
        return
    else:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len-10)   # recursive call


draw_spiral(my_turtle, 160)
