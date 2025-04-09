import time

from API.rc_api import RobotApi
from API.source.core.exceptions.data_validation_error.generic_error import (
    AddWaypointError, FunctionTimeOutError
)


if __name__ == '__main__':
    robot_ip = '192.168.0.63'
    robot = RobotApi(
        robot_ip, ignore_controller_exceptions=True, show_std_traceback=True
    )
    robot.controller_state.set('off', await_sec=60)
    robot.controller_state.set('run', await_sec=60)

    while True:
        try:
            robot.motion.joint.add_new_waypoint(
                angle_pose=(0, -115, 120, -100, -90, 0),
                speed=70,
                accel=70,
                blend=0,
                units='deg'
            )
            robot.motion.linear.add_new_waypoint(
                tcp_pose=(-0.44, -0.16, 0.337, -175, 0, 90),
                speed=0.5,
                accel=0.5,
                orientation_units='deg'
            )
            robot.motion.mode.set('move')
        except (AddWaypointError, FunctionTimeOutError):
            pass
        if robot.controller_state.get() != 'run':
            try:
                robot.controller_state.set('off', await_sec=1)
                robot.controller_state.set('run', await_sec=10)
            except FunctionTimeOutError:
                pass
        time.sleep(0.01)
