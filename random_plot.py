from random import random, choice, randint
import turtle as t

WIDTH = 800
HEIGHT = 400

t.setup(WIDTH, HEIGHT)
t.bgcolor('black')
t.color('white')
t.speed(0)

def draw_lane(lane):
    """ Draws the upper and lower bounds of the random lane, 
    to form a strip with a width expressed in pixels by 
    the 'lane' parameter and centered on the center 
    of the surface """

    t.width(2)

    # Upper limit
    t.up()
    t.goto(-WIDTH, lane//2)
    t.down()
    t.forward(WIDTH*2)

    # Lower limit
    t.up()
    t.goto(-WIDTH, -lane//2)
    t.down()
    t.forward(WIDTH*2)

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

    - angle_range : Angular freedom of movement (in degrees) 
    of the turtle. This value should not be greater than 
    or equal to 180 to avoid backtracking. An error will 
    be displayed if any
    """

    # Errors
    if lane//2 <= step:
        raise ValueError("'lane' // 2 must be strictly greater than 'step'")
    if angle_range > 180:
        raise ValueError("'angle_range' must be less than 180 or equal")

    draw_lane(lane) # Draw the upper and lower limits
    t.width(1)

    # Places the turtle on the far left of the surface (center)
    t.up()
    t.goto(-WIDTH, 0)
    t.down()

    pos_hist = [] # Coordinate history

    # As long as the turtle does not reach the right end 
    # of the surface
    while t.pos()[0] <= WIDTH/2:
        # Random angular orientation
        hdg = choice([randint(0,angle_range//2), randint(360-(angle_range//2),360)])
        
        # Curve color
        if 0 <= hdg <= angle_range//2: # Increasing curve
            t.pencolor('lime')
        else: # Decreasing or stagnant curve
            t.pencolor('red')

        # The next step will exceed the upper limit
        if t.pos()[1] + step >= lane//2:
            init_hdg = hdg
            hdg = (hdg - 30) % 360 # HDG angle lowering
            t.setheading(hdg)
            t.forward(step+0)
            #print(f"---- HDG CORRECTION TOP. INITIAL HDG : {init_hdg} ----")

        # The next step will exceed the lower limit
        elif t.pos()[1] - step <= -lane//2:
            init_hdg = hdg
            hdg = (hdg + 30) % 360 # HDG angle uppering
            t.setheading(hdg)
            t.forward(step+0)
            #print(f"---- HDG CORRECTION BOTTOM. INITIAL HDG : {init_hdg} ----")

        # The next step crosses no limits
        else:
            t.setheading(hdg)
            t.forward(step)

        pos_hist.append(t.pos())
        #print(f'HDG : {t.heading()} | POS : {t.pos()}')

    print("FINISH")
    print("STEPS : ", len(pos_hist))

run(lane=100, step=10, angle_range=90)

t.exitonclick()