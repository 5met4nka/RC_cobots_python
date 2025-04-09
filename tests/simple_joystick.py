from API.rc_api import RobotApi


if __name__ == '__main__':
    robot = RobotApi('192.168.0.190', show_std_traceback=True)
    robot.controller_state.set('off')
    robot.controller_state.set('run', await_sec=120)
    robot.motion.simple_joystick()
