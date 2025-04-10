# Импортируем класс RobotApi
from API.rc_api import RobotApi
if __name__ == '__main__':
    # Подключаемся к управляющему сокету и устанавливаем необходимый уровень
    # логирования
    robot = RobotApi('192.168.31.11', show_std_traceback=True)
    # Устанавливаем текущую нагрузку на фланце в конфигурацию системы
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))
    # Ограничиваем общую скорость перемещения
    robot.motion.scale_setup.set(velocity=1, acceleration=1)
    # Переводим контроллер робота в состояние "run", робот деактивирует
    # электромеханические тормоза и находится в режиме сервоудержания
    robot.controller_state.set('run', await_sec=120)
    while True:
        # Добавляем точки в ядро управления роботом:
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -115, 120, -100, -90, 0),
            speed=10,
            accel=10,
            blend=0,
            units='deg'
        )
        # Запускаем перемещение по точкам
        robot.motion.mode.set('move')
        # Ожидаем, когда буфер точек будет равен 0
        robot.motion.wait_waypoint_completion(0)
        # Выполняем перемещение по линейно траектории
        robot.motion.linear.add_new_waypoint(
            tcp_pose=(-0.44, -0.16, 0.337, -175, 0, 90),
            speed=0.2,
            accel=0.2
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        # Устанавливаем высокий сигнал на цифровом выходе 5
        robot.io.digital.set_output(5, True)
        # Ожидаем высокий сигнал на цифровом входе 1
        robot.io.digital.wait_input(1, True)
        # Возвращаем робота в 1 точку
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -115, 120, -100, -90, 0),
            speed=10,
            accel=10,
            blend=0,
            units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
