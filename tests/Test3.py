import time

from API.rc_api import RobotApi
if __name__ == '__main__':
    # Подключаемся к управляющему сокету и устанавливаем необходимый уровень
    # логирования
    robot = RobotApi('10.10.10.10', show_std_traceback=True)
    robot.safety_status.get()
    while True:
        robot.motion.joint.add_new_waypoint([30.776481628417987, -70.65135955810547, 90.0480651855469, -71.02764129638672, -176.9684600830078, 189.9752426147461],
                                            speed=30,
                                            accel=30,
                                            blend=0,
                                            units='deg')
        robot.motion.joint.add_new_waypoint(
            [25.60501098632812, -70.65204620361328, 90.0480651855469, -71.02592468261719, -176.9681167602539, 189.97421264648438],
            speed=30,
            accel=30,
            blend=0,
            units='deg')
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(1)