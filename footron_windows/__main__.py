import time

import vgamepad as vg
import msvcrt as m

gamepad1 = vg.VX360Gamepad()
gamepad2 = vg.VX360Gamepad()

while True:
    gamepad1.reset()
    gamepad1.update()
    keyp = m.getch()
    # Handle ctrl-c
    if keyp == b"\x03":
        del gamepad1
        break

    if keyp == b"x":
        gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        # gamepad1.update()
        # time.sleep(0.05)
        # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        # gamepad1.update()
        # continue

    if keyp == b"f":
        gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        # gamepad1.update()
        # time.sleep(0.05)
        # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        # gamepad1.update()
        # continue

    if keyp == b"y":
        gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        # gamepad1.update()
        # time.sleep(0.05)
        # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        # gamepad1.update()
        # continue

    if keyp == b"b":
        gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        # gamepad1.update()
        # time.sleep(0.05)
        # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        # gamepad1.update()
        # continue

    elif keyp == b"w":
        print("up")
        gamepad1.left_joystick(0, 32767)
    elif keyp == b"s":
        print("down")
        gamepad1.left_joystick(0, -32767)
    elif keyp == b"a":
        print("left")
        gamepad1.left_joystick(-32767, 0)
    elif keyp == b"d":
        print("right")
        gamepad1.left_joystick(32767, 0)
    elif keyp == b"W":
        print("up")
        gamepad2.left_joystick(0, 32767)
    elif keyp == b"S":
        print("down")
        gamepad2.left_joystick(0, -32767)
    elif keyp == b"A":
        print("left")
        gamepad2.left_joystick(-32767, 0)
    elif keyp == b"D":
        print("right")
        gamepad2.left_joystick(32767, 0)
    elif keyp == b"\xe0":
        keyp = m.getch()
        if keyp == b"H":
            print("kup")
            gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            gamepad1.update()
            # time.sleep(0.05)
            # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        elif keyp == b"P":
            print("kdown")
            gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            gamepad1.update()
            # time.sleep(0.05)
            # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        elif keyp == b"K":
            print("kleft")
            gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            gamepad1.update()
            # time.sleep(0.05)
            # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        elif keyp == b"M":
            print("kright")
            gamepad1.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            gamepad1.update()
            # time.sleep(0.05)
            # gamepad1.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
    else:
        print(keyp)

    gamepad1.update()
    gamepad2.update()
    time.sleep(0.05)
