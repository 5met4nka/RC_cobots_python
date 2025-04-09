import sys

from API.source.models.classes.enum_classes.state_classes import (
    InComingControllerState as Ics, InComingSafetyStatus as Iss
)
from API.rc_api import RobotApi


if __name__ == '__main__':
    robot = RobotApi('192.168.0.197', show_std_traceback=True)
    if (
        robot.safety_status.get() == Iss.fault.name
        or robot.controller_state.get() == Ics.failure.name
    ):
        robot.controller_state.set('off')
    robot.controller_state.set('run', await_sec=120)
    while True:
        glob_pose_rad = robot.motion.linear.get_actual_position(
            orientation_units='rad'
        )
        glob_pose_deg = robot.motion.linear.get_actual_position()
        CTI = robot.tool.get()
        print(f'CTI - {CTI}')
        print(
            f'GLOB_POSE_RAD - {glob_pose_rad}\n'
            f'GLOB_POSE_DEG - {glob_pose_deg}'
        )
        sys.exit()
