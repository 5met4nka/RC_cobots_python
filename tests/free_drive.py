from API.rc_api import RobotApi
from API.source.features.tools import sleep


if __name__ == '__main__':
    robot = RobotApi('192.168.0.53', show_std_traceback=True)
    robot.controller_state.set('run', await_sec=120)
    # Установка нагрузки инструмента,
    # некорректно заданная нагрузка может привести к неадекватной работе в
    # режиме free_drive
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))

    # Выставляем таймер в секундах, free_drive использовать только в рамках
    # данной функции
    for i in sleep(200):
        robot.motion.free_drive()
