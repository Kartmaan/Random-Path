from random import random, choice, randint
import turtle as t

WIDTH = 800
HEIGHT = 400
t.setup(WIDTH, HEIGHT)
t.bgcolor('black')
t.color('white')

def draw_lane(lane):
    """ Draws the upper and lower bounds of the random lane, 
    to form a strip with a width expressed in pixels by 
    the 'lane' parameter and centered on the center 
    of the surface """

    # Upper limit
    t.up()
    t.goto(-HEIGHT, lane//2)
    t.down()
    t.forward(WIDTH)

    # Lower limit
    t.up()
    t.goto(-HEIGHT, -lane//2)
    t.down()
    t.forward(WIDTH)

def run(lane=100, step=10, angle_range=100):
    """ Starts the random plot in the fixed band, 
    until reaching the right edge of the surface.

    - lane : Width (in pixels) of the band delimiting 
    the random path. In order to ensure that the limits 
    are not exceeded, the whole half of the 'lane' value 
    must be strictly greater than 'step'. An error will 
    be displayed if any

    - step : Step length (in pixels) between each change 
    of direction (heading)

    - angle_range : Freedom of movement (in degrees) 
    of the turtle. This value should not be greater than 
    or equal to 180 to avoid backtracking. An error will 
    be displayed if any
    """

    # Errors
    if lane//2 <= step:
        raise ValueError("'lane' // 2 must be strictly greater than 'step'")
    if angle_range > 180:
        raise ValueError("'angle_range' must be less than 180 or equal")

    draw_lane(lane)

    # Places the turtle on the far left of the surface, 
    # in the center
    t.up()
    t.goto(-HEIGHT, 0)
    t.down()

    pos_hist = [] # Location history

    while t.pos()[0] <= WIDTH/2:
        hdg = choice([randint(0,angle_range//2), randint(360-(angle_range//2),360)])

        if t.pos()[1] + step >= lane//2:
            init_hdg = hdg
            hdg = (hdg - 30) % 360
            t.setheading(hdg)
            t.forward(step+0)
            #print(f"---- HDG CORRECTION TOP. INITIAL HDG : {init_hdg} ----")

        elif t.pos()[1] - step <= -lane//2:
            init_hdg = hdg
            hdg = (hdg + 30) % 360
            t.setheading(hdg)
            t.forward(step+0)
            #print(f"---- HDG CORRECTION BOTTOM. INITIAL HDG : {init_hdg} ----")

        else:
            t.setheading(hdg)
            t.forward(step)

        pos_hist.append(t.pos())
        #print(f'HDG : {t.heading()} | POS : {t.pos()}')

    print("FINISH")
    print("STEPS : ", len(pos_hist))

run(lane=50, step=10, angle_range=120)

t.exitonclick()