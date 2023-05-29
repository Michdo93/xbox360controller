import pygame

# JOYBUTTONDOWN / JOYBUTTONUP
A_BUTTON = 0
B_BUTTON = 1
X_BUTTON = 2
Y_BUTTON = 3
LEFT_BUMPER = 4
RIGHT_BUMPER = 5
BACK_BUTTON = 6
START_BUTTON = 7
L_STICK_IN = 8
R_STICK_IN = 9
GUIDE_BUTTON = 10

# JOYHATMOTION
DPAD_RELEASED = (0, 0)
DPAD_UP = (0, 1)
DPAD_DOWN = (0, -1)
DPAD_LEFT = (-1, 0)
DPAD_RIGHT = (1, 0)

# JOYAXISMOTION
LEFT_STICK_X_AXIS = 0
LEFT_STICK_Y_AXIS = 1
RIGHT_STICK_X_AXIS = 2
RIGHT_STICK_Y_AXIS = 3
LT_STICK = 4
RT_STICK = 5

class Controller(object):
    def __init__(self):
        # Initialisation of Pygame and the controller
        pygame.init()
        pygame.joystick.init()

        # Check whether a controller is connected
        if pygame.joystick.get_count() == 0:
            print("No controller found.")
            pygame.quit()
            exit()

        # Selecting the first controller
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def controll_loop(self):
        # Main loop
        while True:
            # Query events
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    # Movement of the axes
                    if event.axis == LEFT_STICK_X_AXIS:
                        # Axis 0 (X-axis of the left stick)
                        left_x_axis = event.value
                        print("X axis: ", left_x_axis)

                        if left_x_axis < -0.5:
                            print("left joystick moved to the left")
                        elif left_x_axis > 0.5:
                            print("left joystick moved to the right")
                    elif event.axis == LEFT_STICK_Y_AXIS:
                        # Axis 1 (Y-axis of the left stick)
                        left_y_axis = event.value
                        print("Y axis: ", left_y_axis)

                        if left_y_axis < -0.5:
                            print("left joystick moved upwards")
                        elif left_y_axis > 0.5:
                            print("left joystick moved downwards")
                    elif event.axis == RIGHT_STICK_X_AXIS:
                        # Axis 2 (X-axis of the right stick)
                        right_x_axis = event.value
                        print("X axis: ", right_x_axis)

                        if right_x_axis < -0.5:
                            print("right joystick moved to the left")
                        elif right_x_axis > 0.5:
                            print("right joystick moved to the right")
                    elif event.axis == RIGHT_STICK_Y_AXIS:
                        # Axis 3 (Y-axis of the right stick)
                        right_y_axis = event.value
                        print("Y axis: ", right_y_axis)

                        if right_y_axis < -0.5:
                            print("right joystick moved upwards")
                        elif right_y_axis > 0.5:
                            print("right joystick moved downwards")
                    elif event.axis == LT_STICK:
                        # Axis 4 (LT button)
                        lt_axis = event.value
                        print("LT axis: ", lt_axis)
                    elif event.axis == RT_STICK:
                        # Axis 5 (RT button)
                        rt_axis = event.value
                        print("RT axis: ", rt_axis)

                elif event.type == pygame.JOYBUTTONDOWN:
                    # button pressed
                    if event.button == A_BUTTON:
                        # Button 0 (A button)
                        print("A button pressed")
                    elif event.button == B_BUTTON:
                        # Button 1 (B button)
                        print("B button pressed")
                    elif event.button == X_BUTTON:
                        # Button 2 (X button)
                        print("X button pressed")
                    elif event.button == Y_BUTTON:
                        # Button 3 (Y button)
                        print("Y button pressed")
                    elif event.button == LEFT_BUMPER:
                        # Button 4 (Left bumper)
                        print("Left bumper button pressed")
                    elif event.button == RIGHT_BUMPER:
                        # Button 5 (Right bumper)
                        print("Right button pressed")
                    elif event.button == BACK_BUTTON:
                        # Button 6 (Back button)
                        print("Back button pressed")
                    elif event.button == START_BUTTON:
                        # Button 7 (Start button)
                        print("Start button pressed")
                    elif event.button == L_STICK_IN:
                        # Button 8 (L-Stick in)
                        print("L-Stick in pressed")
                    elif event.button == R_STICK_IN:
                        # Button 9 (R-Stick in)
                        print("R-Stick in button pressed")
                    elif event.button == GUIDE_BUTTON:
                        # Button 10 (Guide button)
                        print("Guide button pressed")

                elif event.type == pygame.JOYBUTTONUP:
                    # button released
                    if event.button == A_BUTTON:
                        # Button 0 (A button)
                        print("A button released")
                    elif event.button == B_BUTTON:
                        # Button 1 (B button)
                        print("B button released")
                    elif event.button == X_BUTTON:
                        # Button 2 (X button)
                        print("X button released")
                    elif event.button == Y_BUTTON:
                        # Button 3 (Y button)
                        print("Y button released")
                    elif event.button == LEFT_BUMPER:
                        # Button 4 (Left bumper)
                        print("Left bumper button released")
                    elif event.button == RIGHT_BUMPER:
                        # Button 5 (Right bumper)
                        print("Right button released")
                    elif event.button == BACK_BUTTON:
                        # Button 6 (Back button)
                        print("Back button released")
                    elif event.button == START_BUTTON:
                        # Button 7 (Start button)
                        print("Start button released")
                    elif event.button == L_STICK_IN:
                        # Button 8 (L-Stick in)
                        print("L-Stick in released")
                    elif event.button == R_STICK_IN:
                        # Button 9 (R-Stick in)
                        print("R-Stick in button released")
                    elif event.button == GUIDE_BUTTON:
                        # Button 10 (Guide button)
                        print("Guide button released")

                # Check dpad/hat event
                elif event.type == pygame.JOYHATMOTION:
                    dpad = self.joystick.get_hat(0)

                    if dpad == DPAD_RELEASED:
                        print("dpad released")
                    elif dpad == DPAD_UP:
                        print("dpad up pressed")
                    elif dpad == DPAD_DOWN:
                        print("dpad down pressed")
                    elif dpad == DPAD_LEFT:
                        print("dpad left pressed")
                    elif dpad == DPAD_RIGHT:
                        print("dpad right pressed")
            # Waiting time to reduce CPU load
            pygame.time.wait(10)
