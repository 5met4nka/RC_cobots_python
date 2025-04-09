from API.rc_api import RobotApi

if __name__ == '__main__':
    robot = RobotApi('192.168.0.63')
    robot.controller_state.set('run', await_sec=120)

    while True:
        robot.io.digital.wait_any_input()
        if robot.io.digital.get_input(0):
            robot._logger.info('Index 0 has been changed')
        if robot.io.digital.get_input(1):
            robot._logger.info('Index 1 has been changed')
        input()
