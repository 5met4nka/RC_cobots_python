import threading
from API.rc_api import RobotApi

if __name__ == '__main__':
    robot = RobotApi('127.0.0.1', show_std_traceback=True)
    robot.controller_state.set('run', await_sec=120)
    # Установить скорость для перемещений в simple_joystick
    robot.motion.scale_setup.set(velocity=0.3, acceleration=0.3)
    # запускаем simple_joystick в отдельном потоке
    joystick_thread = threading.Thread(target=robot.motion.simple_joystick)
    joystick_thread.start()
    while True:
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -115, 120, -100, -90, 0),
            speed=70,
            accel=70,
            blend=0,
            units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        robot.motion.linear.add_new_waypoint(
            tcp_pose=(-0.44, -0.16, 0.337, -175, 0, 90),
            speed=0.5,
            accel=0.5,
            orientation_units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
