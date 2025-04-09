from API.rc_api import RobotApi

if __name__ == '__main__':
    robot = RobotApi('192.168.0.197')
    robot.controller_state.set('run', await_sec=120)

    while True:
        print('Inputs before set')
        print(robot.io.digital.get_input_functions(0))
        print(robot.io.digital.get_input_functions(2))
        print(robot.io.digital.get_input_functions())

        input()

        robot.io.digital.set_input_function(index=0, function='hold')
        robot.io.digital.set_input_function(index=1, function='move')
        robot.io.digital.set_input_function(index=2, function='pause')

        input()

        print('Inputs after set')
        print(robot.io.digital.get_output_functions(0))
        print(robot.io.digital.get_output_functions(2))
        print(robot.io.digital.get_output_functions())

        input()

        print('Outputs before set')
        print(robot.io.digital.get_output_functions(0))
        print(robot.io.digital.get_output_functions(2))
        print(robot.io.digital.get_output_functions())

        input()

        robot.io.digital.set_output_function(0, 'error_signal_true')
        robot.io.digital.set_output_function(1, 'no_move_signal_false')
        robot.io.digital.set_output_function(2, 'warning_signal_true')

        input()

        print('Outputs after set')
        print(robot.io.digital.get_output_functions(0))
        print(robot.io.digital.get_output_functions(2))
        print(robot.io.digital.get_output_functions())
