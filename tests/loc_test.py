import sys

from API.source.models.classes.enum_classes.state_classes import (
    InComingControllerState as Ics, InComingSafetyStatus as Iss
)
from API.source.ap_interface.motion.coordinate_system import CoordinateSystem
from API.source.features.mathematics.coordinate_system import (
    convert_position_orientation
)
from API.rc_api import RobotApi


if __name__ == 'main':
    robot = RobotApi('192.168.0.73', show_std_traceback=True)
    if (
        robot.safety_status.get() == Iss.fault.name
        or robot.controller_state.get() == Ics.failure.name
    ):
        robot.controller_state.set('off')
    while True:
        robot.motion.scale_setup.set(velocity=0.5, acceleration=0.5)
        robot.controller_state.set('run')
        local_coord_sys_1 = CoordinateSystem((1, 1, 1, 1, 1, 1, 1))
        local_coord_sys_2 = CoordinateSystem((2, 2, 2, 2, 2, 2, 2))
        robot.motion.linear.add_new_waypoint(
            tcp_pose=(
                convert_position_orientation(
                    local_coord_sys_1,
                    (0.1, 0.2, 0.3, 1, 1.5, 2)
                )
            ),
            speed=30,
            accel=10
        )
        robot.motion.wait_waypoint_completion(0)
        robot.motion.linear.get_actual_position()
        robot.motion.linear.get_actual_position(
            coordinate_system=local_coord_sys_1
        )

        robot.motion.linear.add_new_waypoint(
            tcp_pose=(
                convert_position_orientation(
                    local_coord_sys_1,
                    (0.34, 0.14, 0.48, 4, 2, 0.3)
                )
            ),
            speed=30,
            accel=10
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        robot.motion.linear.get_actual_position()
        robot.motion.linear.get_actual_position(
            coordinate_system=local_coord_sys_1
        )
        sys.exit()
