from API.rc_api import RobotApi
from API.source.ap_interface.motion.coordinate_system import CoordinateSystem
from API.source.features.mathematics.coordinate_system import (
    calculate_plane_from_points
)


if __name__ == '__main__':
    robot = RobotApi('192.168.0.190', show_std_traceback=True)
    robot.tool.set(tool_end_point=(-0.00115, 0.00164, 0.14612, 0, 0, 0))
    robot.controller_state.set('off')
    robot.controller_state.set('run', await_sec=120)
    calculated_coordinate_system = calculate_plane_from_points(
        pO=[-0.62949, -0.48229, 0.00739],
        pX=[-0.28411, -0.11155, 0.00842],
        pY=[-0.14781, -0.92954, 0.00827],
    )
    robot._logger.info(calculated_coordinate_system)
    user_coordinate_system = CoordinateSystem(calculated_coordinate_system)
    # Установить скорость для перемещений в simple_joystick
    robot.motion.simple_joystick(coordinate_system=user_coordinate_system)
