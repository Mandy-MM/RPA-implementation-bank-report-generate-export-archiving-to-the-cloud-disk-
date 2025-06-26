import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time
from xbot import print

def main(args):
    try:
        xbot_visual.programing.sleep(random_number=False, seconds="1", start_number="1", stop_number="5", _block=("网盘登入流程", 1, "等待"))
        if xbot_visual.win32.window.contains_element(window="0", content_type="contains_element", element=package.selector("网盘登录界面"), _block=("网盘登入流程", 2, "IF 窗口包含")):
            xbot_visual.win32.element.click(window="0", element=package.selector("企业登录账号输入框"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("网盘登入流程", 3, "点击元素(win)"))
            xbot_visual.win32.element.input(window="0", element=package.selector("企业登录账号输入框"), text="cwgx@yuyuantm.com.cn", append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("网盘登入流程", 4, "填写输入框(win)"))
            xbot_visual.win32.element.input(window="0", element=package.selector("网盘密码输入框"), text="Abc123456!", append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("网盘登入流程", 5, "填写输入框(win)"))
            xbot_visual.win32.element.click(window="0", element=package.selector("网盘登 录按钮"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("网盘登入流程", 6, "点击元素(win)"))
        #endif
    finally:
        pass
