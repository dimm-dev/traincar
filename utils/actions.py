from controllers.racecontroller import Action

def translate_action(action):
    accel_x = 0
    accel_y = 0
    if action == Action.Accelerate:
        accel_y += 1
    if action == Action.Slowdown:
        accel_y -= 1
    if action == Action.ShiftLeft:
        accel_x -= 3
    if action == Action.ShiftRight:
        accel_x += 3

    return accel_x, accel_y
