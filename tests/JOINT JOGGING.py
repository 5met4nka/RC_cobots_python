import time
import logging

from API.rc_api import RobotApi


if __name__ == '__main__':
    robot = RobotApi(
        '192.168.10.10',
        enable_logger=True,
        log_std_level=logging.DEBUG,
        enable_logfile=True, logfile_level=logging.INFO
    )
    robot.controller_state.set('off')
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))
    robot.motion.scale_setup.set(velocity=0.5, acceleration=0.5)
    robot.controller_state.set('run', await_sec=120)
    while True:
        robot.motion.joint.jog_once(0, '+')
        time.sleep(0.01)
        robot.motion.joint.jog_once(4, '+')
        time.sleep(0.01)
        input()
