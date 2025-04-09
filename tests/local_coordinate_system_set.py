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
    robot = RobotApi('192.168.0.73', show_std_traceback=True)
    if (
        robot.safety_status.get() == Iss.fault.name
        or robot.controller_state.get() == Ics.failure.name
    ):
        robot.controller_state.set('off')
    while True:
        robot.motion.scale_setup.set(velocity=0.2, acceleration=0.2)
        robot.controller_state.set('run')
        local_coord_sys_1 = CoordinateSystem(
            (0.11998, 0.35375, 0.45203, -0.1740, 0.4166, 0.3759), 'rad'
        )
        robot.motion.linear.add_new_waypoint(
            tcp_pose=(
                convert_position_orientation(
                    local_coord_sys_1,
                    (-0.70025, -0.70337, 0.00627, -0.5948, -0.2205, -0.2766)
                )
            ),
            speed=1,
            accel=10,
            units='rad'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        glob_pose = robot.motion.linear.get_actual_position(units='rad')
        robot.motion.linear.get_actual_position(units='rad')
        local_pose = robot.motion.linear.get_actual_position(
            coordinate_system=local_coord_sys_1, units='rad'
        )
        print(glob_pose, local_pose)
        sys.exit()
