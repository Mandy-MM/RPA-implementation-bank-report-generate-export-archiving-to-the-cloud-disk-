import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time
from xbot import print

def main(args):
    try:
        process_info = xbot_visual.system.run_or_open(application_path="C:\\Users\\Public.DESKTOP-4UAVD8T\\Desktop\\UClient.exe", command_line_arguments=None, working_folder=None, after_application_launch="continue", is_waitexit_not_more_than=False, timeout_for_exit="10", is_waithwnd_not_more_than=False, timeout_for_hwnd="3", start_as_admin=False, window_style="normal", _block=("NC登入流程", 1, "运行或打开"))
        xbot_visual.image.click(window_kind="currentactivatewindow", window="", template_images=[package.image_selector("图像")], anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", clicks="click", button="left", keys="null", move_mouse=True, timeout="5", delay_after="1", _block=("NC登入流程", 2, "点击图像"))
        用户文本 = xbot_visual.win32.element.get_element(window="0", selector=package.selector("用户文本框"), timeout="20", is_related_parent=False, parent="", _block=("NC登入流程", 3, "获取元素对象(win)"))
        if xbot_visual.workflow.test(operand1=用户文本.get_text(), operator="==", operand2=lambda: "", operator_options="{}", _block=("NC登入流程", 4, "IF 条件")):
            xbot_visual.win32.element.input(window="0", element=package.selector("用户名框"), text="jiqiren", append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("NC登入流程", 5, "填写输入框(win)"))
            xbot_visual.win32.element.input(window="0", element=package.selector("密码文本"), text="yygf230299999", append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("NC登入流程", 6, "填写输入框(win)"))
            xbot_visual.win32.element.click(window="0", element=package.selector("登入按钮"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("NC登入流程", 7, "点击元素(win)"))
        else:
            xbot_visual.win32.element.input(window="0", element=package.selector("密码文本"), text="yygf230299999", append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("NC登入流程", 9, "填写输入框(win)"))
            xbot_visual.win32.element.click(window="0", element=package.selector("登入按钮"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("NC登入流程", 10, "点击元素(win)"))
        #endif
    finally:
        pass
