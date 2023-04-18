from random import random, choice, randint
import turtle as t

# Surface size
WIDTH = 800
HEIGHT = 600

# Make window not resizable
screen = t.Screen()
screen.cv._rootwindow.resizable(False, False)

t.setup(WIDTH, HEIGHT) # Set surface size
t.title("Random plot") # Window title
t.bgcolor('black') # Background color
t.color('white') # Default line color
t.speed(0) # Turtle speed

def draw_strip(strip):
    """ Draws the upper and lower bounds of the strip.
    This function can be executed depending on the state 
    of the 'show_strip' boolean parameter in the 'run' function """

    t.width(2)

    # Upper limit
    t.up()
    t.goto(-WIDTH, strip//2)
    t.down()
    t.forward(WIDTH*2)

    # Lower limit
    t.up()
    t.goto(-WIDTH, -strip//2)
    t.down()
    t.forward(WIDTH*2)

def show_info(strip, step, angle_range):
    """ Shows the validated parameters on the surface, 
    above the upper limit. This function can be executed 
    depending on the state of the 'info' boolean parameter 
    in the 'run' function """

    txt = f"Strip length : {strip} | Step Length : {step} | Angle range : {angle_range}"
    t.up()
    t.goto(0, (strip//2)+4)
    t.write(txt, font=("Arial", 10, "normal"))

def run(strip=100, step=10, angle_range=100, info=False, 
    show_strip=True):

    """ Starts the random graph inside the fixed strip, 
    until reaching the right edge of the surface.

    - strip : Width (in pixels) of the band delimiting 
    the random graph. In order to ensure that the limits 
    are not exceeded, the whole half of the 'strip' value 
    must be strictly greater than 'step'. An error will 
    be displayed if any

    - step : Step length (in pixels) between each change 
    of direction (heading)

    - angle_range : Angular freedom of movement (in degrees) 
    of the turtle. This value should not be greater than 
    or equal to 180 to avoid backtracking. An error will 
    be displayed if any

    - info : Display of textual information on the surface 
    regarding validated parameters

    - show_strip : Display of upper and lower limits
    """

    # Errors
    if strip//2 <= step:
        raise ValueError("'strip' // 2 must be strictly greater than 'step'")
    if angle_range > 180:
        raise ValueError("'angle_range' must be less than 180 or equal")

    # Display of information related to parameters
    if info:
        show_info(strip, step, angle_range)

    # Display of strip lines
    if show_strip:
        draw_strip(strip) # Draw the upper and lower limits

    t.width(1) # Line thickness

    # Places the turtle on the far left of the surface (center)
    # Starting point of the graph
    t.up()
    t.goto(-WIDTH, 0)
    t.down()

    pos_hist = [] # Coordinates history

    # while = As long as the turtle does not reach the right end 
    # of the surface
    while t.pos()[0] <= WIDTH/2:
        # Random angular orientation
        hdg = choice([randint(0,angle_range//2), randint(360-(angle_range//2),360)])
        
        # Line color
        # The color of each path changes depending on whether 
        # it is ascending or descending and this based on 
        # the orientation of the turtle via the recovery 
        # of its heading value 'hdg'.
        if 0 <= hdg <= angle_range//2: # Increasing curve
            t.pencolor('lime')
        else: # Decreasing or stagnant curve
            t.pencolor('red')

        # Heading correction
        # The next step will exceed the upper limit
        if t.pos()[1] + step >= strip//2:
            init_hdg = hdg
            hdg = (hdg - 30) % 360 # HDG angle lowering
            t.setheading(hdg)
            t.forward(step+0)
            #print(f"---- HDG CORRECTION TOP. INITIAL HDG : {init_hdg} ----")
        
        # Heading correction
        # The next step will exceed the lower limit
        elif t.pos()[1] - step <= -strip//2:
            init_hdg = hdg
            hdg = (hdg + 30) % 360 # HDG angle uppering
            t.setheading(hdg)
            t.forward(step+0)
            #print(f"---- HDG CORRECTION BOTTOM. INITIAL HDG : {init_hdg} ----")

        # No heading correction
        # The next step crosses no limits
        else:
            t.setheading(hdg)
            t.forward(step)

        pos_hist.append(t.pos())
        #print(f'HDG : {t.heading()} | POS : {t.pos()}')

    print("FINISH")
    print("STEPS : ", len(pos_hist))

run(strip=200, step=50, angle_range=100, info=True, show_strip=True)

t.exitonclick()