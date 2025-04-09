from time import sleep

from API.rc_api import RobotApi


# функция для сброса работы скрипта по 0 индексу
# если у нас блокирующий метод ожидания сигнала, то в строке
# while not robot.motion.check_waypoint_completion()
# заменяем robot.motion.check_waypoint_completion() на ожидание сигнала
def wait_wp_and_input_reset(robot: RobotApi):
    while not robot.motion.check_waypoint_completion():
        if robot.io.digital.get_input(index=0):
            robot.motion.mode.set('hold')
            while robot.io.digital.get_input(index=0):
                sleep(0.001)
            return True
        sleep(0.001)


if __name__ == '__main__':
    robot = RobotApi('192.168.0.67', show_std_traceback=True)
    # назначаем на 1 индекс действие для продолжения выполнения скрипта
    # в случае столкновения
    robot.io.digital.set_input_function(1, 'move')
    # на выход 0 назначаем сигнал в случае остановки движения робота
    # (индикация при столкновении робота с препятствием)
    robot.io.digital.set_output_function(0, 'no_move_signal_true')
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))
    robot.controller_state.set('run', await_sec=120)
    while True:
        robot.motion.joint.add_new_waypoint(
           angle_pose=(0, -115, 120, -100, -90, 0),
           speed=70,
           accel=70,
           units='deg'
        )
        robot.motion.linear.add_new_waypoint(
           tcp_pose=((-0.44, -0.16, 0.337, -175, 0, 90)),
           speed=1,
           accel=1
        )
        robot.motion.linear.add_new_waypoint(
           tcp_pose=((-0.54, -0.26, 0.537, -175, 0, 90)),
           speed=1,
           accel=1
        )
        robot.motion.mode.set('move')
        # все блокирующие методы ожидания в коде (wait_waypoint_completion()
        #  и wait_input()) заменяем на ранее добавленную новую функцию,
        # в случаем возврата True сбрасываем цикл
        if wait_wp_and_input_reset(robot):
            continue
        sleep(0.01)
