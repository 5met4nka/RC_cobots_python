import sys

from API.source.models.classes.enum_classes.state_classes import (
    InComingControllerState as Ics, InComingSafetyStatus as Iss
)
from API.source.ap_interface.motion.coordinate_system import CoordinateSystem
from API.source.features.mathematics.coordinate_system import (
    convert_position_orientation
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
        robot.motion.scale_setup.set(velocity=0.1, acceleration=0.1)
        robot.tool.set(tool_end_point=(0, 0, 0.14329, 0, 0, 0))
        local_coord_sys_1 = CoordinateSystem(
            position_orientation=(
                (-0.7332, -0.4838, -0.0198, 3.138, 0, 0.8195)
            )
        )
        new_point = (
            convert_position_orientation(
                local_coord_sys_1,
                (0.1, 0.1, 0.1, 0, 0, 0),
                orientation_units='deg'
            )
        )
        print(new_point)
        robot.motion.linear.add_new_waypoint(
            tcp_pose=,
            speed=0.1,
            accel=0.1,
            orientation_units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        glob_pose_rad = robot.motion.linear.get_actual_position(
            orientation_units='rad'
        )
        local_pose_rad = robot.motion.linear.get_actual_position(
            coordinate_system=local_coord_sys_1,
            orientation_units='rad'
        )
        glob_pose_deg = robot.motion.linear.get_actual_position()
        local_pose_deg = robot.motion.linear.get_actual_position(
            coordinate_system=local_coord_sys_1
        )
        print(
            f'GLOP_POSE_RAD = {glob_pose_rad}\n'
            f'LOCAL_POSE_RAD =  {local_pose_rad}'
        )
        print(
            f'GLOB_POSE_DEG = {glob_pose_deg}\n'
            f'LOCAL_POSE_DEG = {local_pose_deg}'
        )
        sys.exit()
