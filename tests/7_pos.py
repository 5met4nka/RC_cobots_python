import sys
from API.rc_api import RobotApi
from API.source.models.classes.enum_classes.state_classes import (
    InComingControllerState as Ics, InComingSafetyStatus as Iss
)


if __name__ == '__main__':
    robot = RobotApi('192.168.0.190', show_std_traceback=True)
    if robot.safety_status.get() == (
        Iss.fault.name
    ) or (
        robot.controller_state.get() == Ics.failure.name
    ):
        robot.controller_state.set('off')
    robot.payload.set(mass=0, tcp_mass_center=(0, 0, 0))
    robot.motion.scale_setup.set(velocity=1, acceleration=1)
    robot.controller_state.set('run', await_sec=120)
    while True:
        robot.motion.joint.add_new_waypoint(
            angle_pose=(0, -120, 120, -90, -90, 0),
            speed=100,
            accel=10,
            blend=0,
            units='deg'
        )
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion(0)
        sys.exit()
