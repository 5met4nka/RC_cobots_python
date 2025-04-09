import sys

from API.rc_api import RobotApi


if __name__ == '__main__':
    robot = RobotApi('127.0.0.1', show_std_traceback=True)

    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))
    robot.controller_state.set('off')
    robot.motion.scale_setup.set(velocity=1, acceleration=1)

    robot.controller_state.set('run', await_sec=120)

    while True:
        robot.motion.joint.add_new_waypoint(
            tcp_pose=(
                0.37303676787432796,
                0.250042915592268,
                0.8882177250512572,
                -150.42526386121557,
                15.5250049850496004,
                90.055355272203126
            ),
            speed=15,
            accel=15,
            units='deg'
        )
        robot.motion.joint.add_new_waypoint(
            tcp_pose=(
                0.27303676787432796,
                0.450042915592268,
                0.5882177250512572,
                -179.42526386121557,
                1.5250049850496004,
                12.055355272203126
            ),
            speed=15,
            accel=15,
            units='deg'
        )
        robot.motion.joint.add_new_waypoint(
            tcp_pose=(
                0.77303676787432796,
                0.20042915592268,
                0.1882177250512572,
                120.42526386121557,
                0.5250049850496004,
                0.055355272203126
            ),
            speed=15,
            accel=15,
            units='deg'
        )
        robot.motion.joint.add_new_waypoint(
            tcp_pose=(
                0.5303676787432796,
                -0.60042915592268,
                0.5882177250512572,
                0.42526386121557,
                -70.5250049850496004,
                -30.055355272203126
            ),
            speed=15,
            accel=15,
            units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        print(robot.motion.linear.get_actual_position())

        sys.exit()
