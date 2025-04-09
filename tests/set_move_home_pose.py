import sys
from time import sleep

from API.rc_api import RobotApi


if __name__ == '__main__':
    robot = RobotApi('192.168.0.204', show_std_traceback=True)
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))
    robot.controller_state.set('run', await_sec=120)
    while True:

        home_pose = robot.motion.get_home_pose(units='rad')
        print('OLD HOME POSE:', home_pose)
        print(robot.motion.set_home_pose((0, -88, 0, -88, 0, 0)))
        print('NEW_HOME_POSE: ', robot.motion.get_home_pose())
        robot.motion.move_to_home_pose()
        robot.motion.wait_waypoint_completion()
        print('ACTUAL POSE: ', robot.motion.joint.get_actual_position())
        sleep(0.01)
        sys.exit()
