from time import sleep
from threading import Thread, main_thread

from API.rc_api import RobotApi


take_top = [0.4926321425469745, -0.22941067744686422, 0.17632334166034475, -178.22410138680934, -1.331937084906622, -45.216746230492944]
take_bottom = [0.4917190704738804, -0.22854473009042015, 0.03801219650008253, -178.23077716941378, -1.1384636656288696, -45.211678022651405]
drop_top = [0.4926386228022661, 0.023424199924316203, 0.17326210535478714, -178.2126853894406, -1.3384159839612462, -45.0675176691534]
drop_bottom = [0.4925096930992017, 0.023383708836229748, 0.03077205068045341, -178.22694579614236, -1.324376940732378, -45.075276226458314]


if __name__ == '__main__':
    robot = RobotApi('192.168.0.145', show_std_traceback=True)
    robot.controller_state.set('off')
    robot.controller_state.set('run')
    robot.io.digital.set_output(index=0, value=False)
    # robot.motion.scale_setup.set(velocity=0.5, acceleration=0.5)
    robot.motion.set_motion_config(
        linear_speed=3,
        linear_acceleration=10,
        joint_speed=120,
        joint_acceleration=240
    )

    robot.io.digital.set_output(index=1, value=False)

    def conveyer_control(robot: RobotApi):
        while True:
            if robot.io.digital.get_input(index=0):
                robot.io.digital.set_output(index=1, value=False)
            else:
                if not robot.io.digital.get_output(index=1):
                    robot.io.digital.set_output(index=1, value=True)
            sleep(0.001)

    conveyer_controller_thread = Thread(
        target=conveyer_control,
        kwargs={'robot': robot}
    )
    conveyer_controller_thread.start()

    while True:
        robot.motion.joint.add_new_waypoint(tcp_pose=take_top)
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion()
        # robot.io.digital.set_output(index=1, value=True)
        robot.io.digital.wait_input(index=0, value=True)
        # robot.io.digital.set_output(index=1, value=False)
        robot.motion.linear.add_new_waypoint(tcp_pose=take_bottom)
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion()
        robot.io.digital.set_output(index=0, value=True)
        sleep(1)
        robot.motion.linear.add_new_waypoint(tcp_pose=take_top)
        robot.motion.linear.add_new_waypoint(tcp_pose=drop_top)
        robot.motion.linear.add_new_waypoint(tcp_pose=drop_bottom)
        robot.motion.mode.set('move')
        robot.motion.wait_waypoint_completion()
        robot.io.digital.set_output(index=0, value=False)
        sleep(1)
