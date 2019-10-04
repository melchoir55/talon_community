# From https://github.com/talonvoice/examples
from talon_plugins import eye_mouse
from talon.voice import Context
from talon import cron


def enable_for_three_seconds():
    eye_mouse.control_mouse.enable()
    cron.after('3s', eye_mouse.control_mouse.disable)

ctx = Context("eye_control")
ctx.keymap(
    {
        "debug overlay": lambda m: eye_mouse.debug_overlay.toggle(),
        "control mouse": lambda m: eye_mouse.control_mouse.toggle(),
        "camera overlay": lambda m: eye_mouse.camera_overlay.toggle(),
        "run calibration": lambda m: eye_mouse.calib_start(),
        "snap": lambda m: enable_for_three_seconds()
    }
)
