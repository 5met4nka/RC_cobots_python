from API.rc_api import RobotApi
from API.source.models.classes.enum_classes.state_classes import (
    InComingControllerState as Ics, InComingSafetyStatus as Iss
)

if __name__ == '__main__':
    robot = RobotApi('192.168.0.190', show_std_traceback=True)
    if (
        robot.safety_status.get() == Iss.fault.name
        or
        robot.controller_state.get() == Ics.failure.name
    ):
        robot.controller_state.set('off')
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))

    robot.motion.scale_setup.set(velocity=0.2, acceleration=0.2)

    robot.controller_state.set('run', await_sec=120)

    while True:
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -115, 120, -100, -90, 0),
            speed=70,
            accel=70,
            blend=0,
            units='deg'
        )
        robot.motion.linear.add_new_waypoint(
            tcp_pose=(-0.44, -0.16, 0.337, -175, 0, 90),
            speed=0.5,
            accel=0.5,
            orientation_units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
