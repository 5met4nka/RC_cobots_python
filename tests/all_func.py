import sys
import logging
from API.rc_api import RobotApi
from API.source.models.classes.enum_classes.state_classes import (
    InComingControllerState as Ics, InComingSafetyStatus as Iss
)

if __name__ == '__main__':

    # Создаем точку входа для управления роботом и настройки логирования
    robot = RobotApi(
        '192.168.0.53',
        enable_logger=True,
        log_std_level=logging.INFO,
        enable_logfile=True,
        logfile_level=logging.INFO
    )
    # Проверка состояния на наличие ошибки и попытка сброса ошибки
    if (
        robot.safety_status.get() == Iss.fault.name
        or robot.controller_state.get() == Ics.failure.name
    ):
        robot.controller_state.set('off')

    # Задать параметры инструмента
    # Установка координат ЦТИ
    robot.tool.set((0, 0, 0, 0, 0, 0), units='deg')
    # Установка нагрузки инструмента
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))

    # Задать ограничения ускорения и скорости, устанавливаем множитель (до 1)
    robot.motion.scale_setup.set(velocity=1, acceleration=1)

    # Перевод робота в состояние run, подача питания и включение режима
    # сервоудержания
    robot.controller_state.set('run', await_sec=120)

    # В бесконечном цикле создаем основное тело программы управления
    while True:

        # Задаем точки перемещения joint
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -90, 0, -90, 0, 0),
            speed=20,
            accel=20,
            blend=0,
            units='deg'
        )
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -120, 120, -90, -90, 0),
            speed=20,
            accel=20,
            blend=0,
            units='deg'
        )
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -90, 0, -90, 0, 0),
            speed=20,
            accel=20,
            blend=0.5,
            units='deg'
        )
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -120, 120, -90, -90, 0),
            speed=20,
            accel=20,
            blend=0.5,
            units='deg'
        )

        # Запускаем перемещение по добавленным точкам
        robot.motion.mode.set('move')

        # Ожидаем пока робот выполнит перемещения (скрипт находится в ожидании)
        robot.motion.wait_waypoint_completion(0)

        # Установим параметры скорости и ускорения для всех точек
        robot.motion.set_motion_config(
            units='deg',
            joint_speed=30,
            joint_acceleration=30,
            linear_speed=1,
            linear_acceleration=1
        )
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -90, 0, -90, 0, 0)
        )
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -120, 120, -90, -90, 0)
        )
        robot.motion.joint.jog_once(0, '+')

        # Запускаем окно для перемещения
        robot.motion.simple_joystick()
        input('')
        sys.exit
