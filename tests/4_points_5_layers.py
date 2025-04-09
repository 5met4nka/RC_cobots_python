import sys

from API.rc_api import RobotApi
from API.source.ap_interface.motion.coordinate_system import CoordinateSystem
from API.source.features.mathematics.coordinate_system import (
    convert_position_orientation
)


if __name__ == '__main__':
    count = 0
    box_size = 0.2

    point_1 = [0, 0, 0, 0, 0, 0]
    point_2 = [0.5, 0, 0, 0, 0, 0]
    point_3 = [0, 0.5, 0, 0, 0, 0]
    point_4 = [0.5, 0.5, 0, 0, 0, 0]

    robot = RobotApi('192.168.0.190', show_std_traceback=True)
    robot.controller_state.set('off')
    robot.controller_state.set('run')
    robot.motion.set_motion_config(linear_speed=150, linear_acceleration=150)
    robot.motion.scale_setup.set(velocity=1, acceleration=1)
    robot.tool.set(tool_end_point=(-0.00115, 0.00164, 0.14612, 0, 0, 0))
    user_coordinate_system = CoordinateSystem(
        [
            -0.6268585854335833,
            -0.481927454358517,
            0.00739,
            179.9295,
            -0.1177,
            44.1798
        ]
    )

    while count < 5:
        count += 1

        converted_point = convert_position_orientation(
            coordinate_system=user_coordinate_system,
            position_orientation=point_1,
        )
        print(
            f'слой - {count}\n'
            f'converted - {converted_point}'
        )
        robot.motion.linear.add_new_waypoint(
            tcp_pose=convert_position_orientation(
                coordinate_system=user_coordinate_system,
                position_orientation=point_1,
            )
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        # здесь выполняем какие-то действия

        robot.motion.linear.add_new_waypoint(
            tcp_pose=convert_position_orientation(
                coordinate_system=user_coordinate_system,
                position_orientation=point_2
            )
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)

        robot.motion.linear.add_new_waypoint(
            tcp_pose=convert_position_orientation(
                coordinate_system=user_coordinate_system,
                position_orientation=point_3
            )
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)

        robot.motion.linear.add_new_waypoint(
            tcp_pose=convert_position_orientation(
                coordinate_system=user_coordinate_system,
                position_orientation=point_4
            )
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)

        user_coordinate_system.set(
            [
                -0.6268585854335833,
                -0.481927454358517,
                0.00739 + count*box_size,
                179.9295,
                -0.1177,
                44.1798
            ]
        )

    sys.exit()
