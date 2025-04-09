import sys

from API.rc_api import RobotApi


if __name__ == '__main__':
    robot = RobotApi('192.168.0.63', show_std_traceback=True)
    # При ошибке по безопасности сбросить с помощью перевода контроллера в
    # состояние off
    robot.controller_state.set('off')
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))
    robot.motion.scale_setup.set(velocity=1, acceleration=1)
    robot.controller_state.set('run', await_sec=120)

    while True:
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -90, 0, -90, 0, 0),
            speed=12,
            accel=5,
            blend=0,
            units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        sys.exit()
