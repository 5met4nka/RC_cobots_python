from API.rc_api import RobotApi
from API.source.ap_interface.motion.coordinate_system import CoordinateSystem


if __name__ == '__main__':
    robot = RobotApi('192.168.0.190', show_std_traceback=True)
    robot.controller_state.set('off')
    robot.controller_state.set('run', await_sec=120)
    # устанавливаем пользовательскую систему координат
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
    robot.motion.simple_joystick(coordinate_system=user_coordinate_system)
