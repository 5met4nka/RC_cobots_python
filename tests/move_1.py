import sys
import time


from API.rc_api import RobotApi

if __name__ == '__main__':
    robot = RobotApi('192.168.0.197', show_std_traceback=True) 

    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))

    robot.motion.scale_setup.set(velocity=0.1, acceleration=0.1)

    # Переводим контроллер робота в состояние "run", робот деактивирует
    # электромеханические тормоза и находится в режиме сервоудержания
    robot.controller_state.set('run', await_sec=120)

    while True:
        # Добавляем точки в ядро управления роботом:
        robot.motion.joint.add_new_waypoint(
           angle_pose=(0, -115, 120, -100, -90, 0),
           speed=10,
           accel=10,
           units='deg'
        )

        # Запускаем перемещение по точкам
        robot.motion.mode.set('move')

        # Ожидаем когда буфер точек будет равен 0
        robot.motion.wait_waypoint_completion(0)

        # Выполняем перемещение по линейно траектории траектории
        robot.motion.linear.add_new_waypoint(
           tcp_pose=((-0.44, -0.16, 0.337, -175, 0, 90)),
           speed=0.2,
           accel=0.2
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
