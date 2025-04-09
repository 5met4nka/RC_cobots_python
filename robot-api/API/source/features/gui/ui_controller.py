from __future__ import annotations
from tkinter import Tk
from typing import TYPE_CHECKING

from API.source.ap_interface.motion.coordinate_system import CoordinateSystem
from API.source.features.gui.view import _WindowUI
from API.source.features.gui.key_handler import KeyHandler
from API.source.features.gui.bindings import Binding, Sequences
from API.source.features.mathematics.coordinate_system import (
    convert_position_orientation
)
from API.source.models.classes.enum_classes.various_types import (
    JogParamInTCP
)
from API.source.models.classes.data_classes.command_templates import (
    MOTION_SETUP
)
from API.source.models.classes.enum_classes.various_types import (
    AngleUnitTypes, GUICoordinateSystem, MotionTypes
)
from API.source.models.constants import (
    JOYSTICK_ACCEL_MAX_DEG_SEC, JOYSTICK_ACCEL_MAX_RAD_SEC,
    JOYSTICK_SPEED_MAX_DEG_SEC, JOYSTICK_SPEED_MAX_RAD_SEC,
)

if TYPE_CHECKING:
    from API.source.ap_interface.motion.linear_motion import LinearMotion
    from API.source.ap_interface.motion.joint_motion import JointMotion
    from API.source.ap_interface.motion.motion_host import Motion
    from API.source.features.gui.bindings import RTDGroup


class SimpleJoystickUI(Tk):
    def __init__(
        self,
        linear_jog_func: LinearMotion.jog_once,
        joint_jog_func: JointMotion.jog_once,
        joint_set_jog_param_in_tcp: JointMotion.set_jog_param_in_tcp,
        act_linear_pose: LinearMotion.get_actual_position,
        act_joint_pose: JointMotion.get_actual_position,
        free_drive: Motion.free_drive,
        mode_set_func: Motion.mode.set,
        add_new_waypoint: JointMotion.add_new_waypoint,
        add_new_offset: LinearMotion.add_new_offset,
        scale_setup: Motion.scale_setup.set,
        coordinate_system: CoordinateSystem | None
    ):
        super().__init__()
        self.ui = _WindowUI(self, coordinate_system)
        self.key_handler = KeyHandler(self)
        self.act_l_pose = act_linear_pose
        self.act_j_pose = act_joint_pose
        self.joint_set_jog_param_in_tcp = joint_set_jog_param_in_tcp
        self.mode_set = mode_set_func
        self.add_new_waypoint = add_new_waypoint
        self.add_new_offset = add_new_offset
        self.scale_setup = scale_setup
        self.units = MOTION_SETUP.units
        self.coordinate_system = coordinate_system
        self.current_coordinate_system = (
            self.ui.coordinate_system_combobox.get()
        )

        self.binds = []
        self.binds.append(Binding('empty', None, Sequences.empty))
        self.binds.append(
            Binding(
                'x_min',
                self.ui.x_min_btn.connect(linear_jog_func, 'X', '-'),
                Sequences.x_min
            )
        )
        self.binds.append(
            Binding(
                'x_max',
                self.ui.x_max_btn.connect(linear_jog_func, 'X', '+'),
                Sequences.x_max
            )
        )
        self.binds.append(
            Binding(
                'y_min',
                self.ui.y_min_btn.connect(linear_jog_func, 'Y', '-'),
                Sequences.y_min
            )
        )
        self.binds.append(
            Binding(
                'y_max',
                self.ui.y_max_btn.connect(linear_jog_func, 'Y', '+'),
                Sequences.y_max
            )
        )
        self.binds.append(
            Binding(
                'z_min',
                self.ui.z_min_btn.connect(linear_jog_func, 'Z', '-'),
                Sequences.z_min
            )
        )
        self.binds.append(
            Binding(
                'z_max',
                self.ui.z_max_btn.connect(linear_jog_func, 'Z', '+'),
                Sequences.z_max
            )
        )
        self.binds.append(
            Binding(
                'rx_min',
                self.ui.rx_min_btn.connect(linear_jog_func, 'Rx', '-'),
                Sequences.rx_min
            )
        )
        self.binds.append(
            Binding(
                'rx_max',
                self.ui.rx_max_btn.connect(linear_jog_func, 'Rx', '+'),
                Sequences.rx_max
            )
        )
        self.binds.append(
            Binding(
                'ry_min',
                self.ui.ry_min_btn.connect(linear_jog_func, 'Ry', '-'),
                Sequences.ry_min
            )
        )
        self.binds.append(
            Binding(
                'ry_max',
                self.ui.ry_max_btn.connect(linear_jog_func, 'Ry', '+'),
                Sequences.ry_max
            )
        )
        self.binds.append(
            Binding(
                'rz_min',
                self.ui.rz_min_btn.connect(linear_jog_func, 'Rz', '-'),
                Sequences.rz_min
            )
        )
        self.binds.append(
            Binding(
                'rz_max',
                self.ui.rz_max_btn.connect(linear_jog_func, 'Rz', '+'),
                Sequences.rz_max
            )
        )
        self.binds.append(
            Binding(
                'j0_min',
                self.ui.j0_min_btn.connect(joint_jog_func, 0, '-'),
                Sequences.j0_min
            )
        )
        self.binds.append(
            Binding(
                'j0_max',
                self.ui.j0_max_btn.connect(joint_jog_func, 0, '+'),
                Sequences.j0_max
            )
        )
        self.binds.append(
            Binding(
                'j1_min',
                self.ui.j1_min_btn.connect(joint_jog_func, 1, '-'),
                Sequences.j1_min
            )
        )
        self.binds.append(
            Binding(
                'j1_max',
                self.ui.j1_max_btn.connect(joint_jog_func, 1, '+'),
                Sequences.j1_max
            )
        )
        self.binds.append(
            Binding(
                'j2_min',
                self.ui.j2_min_btn.connect(joint_jog_func, 2, '-'),
                Sequences.j2_min
            )
        )
        self.binds.append(
            Binding(
                'j2_max',
                self.ui.j2_max_btn.connect(joint_jog_func, 2, '+'),
                Sequences.j2_max
            )
        )
        self.binds.append(
            Binding(
                'j3_min',
                self.ui.j3_min_btn.connect(joint_jog_func, 3, '-'),
                Sequences.j3_min
            )
        )
        self.binds.append(
            Binding(
                'j3_max',
                self.ui.j3_max_btn.connect(joint_jog_func, 3, '+'),
                Sequences.j3_max
            )
        )
        self.binds.append(
            Binding(
                'j4_min',
                self.ui.j4_min_btn.connect(joint_jog_func, 4, '-'),
                Sequences.j4_min
            )
        )
        self.binds.append(
            Binding(
                'j4_max',
                self.ui.j4_max_btn.connect(joint_jog_func, 4, '+'),
                Sequences.j4_max
            )
        )
        self.binds.append(
            Binding(
                'j5_min',
                self.ui.j5_min_btn.connect(joint_jog_func, 5, '-'),
                Sequences.j5_min
            )
        )
        self.binds.append(
            Binding(
                'j5_max',
                self.ui.j5_max_btn.connect(joint_jog_func, 5, '+'),
                Sequences.j5_max
            )
        )
        for group in self.ui.rtd_groups:
            sequence_str = (
                'ctrl_j_c' if group.type_ == MotionTypes.JOINT else 'ctrl_l_c'
            )
            self.binds.append(
                Binding(
                    sequence_str,
                    group.copy_btn.connect(self.copy_rtd, group.type_),
                    getattr(Sequences, sequence_str)
                )
            )
        self.binds.append(
            Binding(
                'move',
                self.ui.move_btn.connect(self.move),
                Sequences.move
            )
        )
        self.binds.append(
            Binding(
                'move',
                self.ui.move_btn.connect_release(self.stop),
                Sequences.move
            )
        )
        self.binds.append(
            Binding(
                'offset',
                self.ui.shift_btn.connect(self.shift),
                Sequences.offset
            )
        )
        self.binds.append(
            Binding(
                'offset',
                self.ui.shift_btn.connect_release(self.stop),
                Sequences.offset
            )
        )
        self.binds.append(
            Binding(
                'free_drive',
                self.ui.free_drive_btn.connect(free_drive),
                Sequences.free_drive
            )
        )
        self.ui.free_drive_switch.bind(
            '<ButtonRelease>', self.set_free_drive
        )
        self.bind('<Button>', self.click_handler)
        self.ui.coordinate_system_combobox.bind(
            '<<ComboboxSelected>>', self.set_current_coordinate_system
        )
        self.ui.orientation_units_combobox.bind(
            '<<ComboboxSelected>>', self.set_orientation_units_combobox_value
        )
        self.ui.speed_scale.bind(
            '<ButtonRelease-1>', self.set_speed_scale_value
        )
        self.task = self.after(100, self.update_rtd)
        self.protocol('WM_DELETE_WINDOW', self.close_window)
        if self.units == 'rad':
            self.ui.orientation_units_combobox.set(AngleUnitTypes.RAD)
        scale_setup(
            velocity=self.ui.speed_scale.get(),
            acceleration=self.ui.speed_scale.get()
        )
        self.mainloop()

    def click_handler(self, _):
        if self.key_handler.sequence:
            self.key_handler.clear_sequence()
            self.release_all()

    def copy_rtd(self, type_: RTDGroup.type_):
        self.clipboard_clear()
        self.clipboard_append(
            str(self.act_j_pose())
            if type_ == MotionTypes.JOINT else str(self.act_l_pose(self.units))
        )

    def set_current_coordinate_system(self, event):
        self.current_coordinate_system = (
            self.ui.coordinate_system_combobox.get()
        )
        if self.current_coordinate_system == GUICoordinateSystem.CTI:
            self.joint_set_jog_param_in_tcp(JogParamInTCP.TRUE)
        else:
            self.joint_set_jog_param_in_tcp(JogParamInTCP.FALSE)

    def set_free_drive(self, event):
        checkbox_value = self.ui.enabled.get()
        if checkbox_value == 1:
            self.ui.free_drive_btn.set_pressed()
        else:
            self.ui.free_drive_btn.set_released()

    def set_orientation_units_combobox_value(self, event):
        self.units = (
            'deg'
            if self.ui.orientation_units_combobox.get() == AngleUnitTypes.DEG
            else 'rad'
        )

    def set_speed_scale_value(self, event):
        scale_value = self.ui.speed_scale.get()
        self.scale_setup(
            velocity=scale_value, acceleration=scale_value
        )

    def get_entry_data(self, motion_type):
        entry_group = (
            self.ui.move_entry_group
            if motion_type == MotionTypes.JOINT
            else self.ui.offset_entry_group
        )
        for group in entry_group:
            return [float(entry.get()) for entry in group.entries]

    def move(self):
        tcp_pose = self.get_entry_data(MotionTypes.JOINT)
        if self.current_coordinate_system == GUICoordinateSystem.LOCAL:
            tcp_pose = convert_position_orientation(
                coordinate_system=self.coordinate_system,
                position_orientation=tcp_pose,
                orientation_units=self.units
            )
        speed, accel = (
            JOYSTICK_SPEED_MAX_DEG_SEC, JOYSTICK_ACCEL_MAX_DEG_SEC
        ) if self.units == 'deg' else (
            JOYSTICK_SPEED_MAX_RAD_SEC, JOYSTICK_ACCEL_MAX_RAD_SEC
        )
        self.add_new_waypoint(
            tcp_pose=tcp_pose,
            speed=speed,
            accel=accel,
            units=self.units
        )
        self.mode_set('move')

    def shift(self):
        act_l_pose = self.act_l_pose(self.units)
        if self.current_coordinate_system == GUICoordinateSystem.LOCAL:
            act_l_pose = convert_position_orientation(
                coordinate_system=self.coordinate_system,
                position_orientation=act_l_pose,
                orientation_units=self.units,
                to_local=True
            )
        self.add_new_offset(
            waypoint=act_l_pose,
            offset=self.get_entry_data(MotionTypes.LINEAR),
            coordinate_system=(
                self.coordinate_system
                if self.current_coordinate_system == GUICoordinateSystem.LOCAL
                else None
            ),
            orientation_units=self.units
        )
        self.mode_set('move')

    def stop(self):
        self.mode_set('hold')

    def update_rtd(self):
        act_l_pose = self.act_l_pose(self.units)
        if self.current_coordinate_system == GUICoordinateSystem.LOCAL:
            act_l_pose = convert_position_orientation(
                coordinate_system=self.coordinate_system,
                position_orientation=act_l_pose,
                orientation_units=self.units,
                to_local=True
            )
        elif self.current_coordinate_system == GUICoordinateSystem.CTI:
            act_l_pose = [0] * 6
        for group in self.ui.rtd_groups:
            pose = (
                self.act_j_pose(self.units)
                if group.type_ == MotionTypes.JOINT else act_l_pose
            )
            for i in range(len(group.labels)):
                group.labels[i].config(text=str(round(pose[i], 5)))
        self.task = self.after(50, self.update_rtd)

    def release_all(self):
        for binding in self.binds:
            if binding.button and binding.button.is_pressed():
                binding.button.set_released(None)

    def close_window(self):
        self.after_cancel(self.task)
        self.destroy()
