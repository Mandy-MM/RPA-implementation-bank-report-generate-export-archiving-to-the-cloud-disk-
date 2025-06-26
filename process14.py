import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time
from xbot import print

def main(args):
    try:
        loop_index = -1
        while True:
            loop_index += 1
            if xbot_visual.image.exist(window_kind="screen", window="", exist_mode="exist", template_images=[package.image_selector("编辑路径")], is_find_all_images=False, _block=("如果可编辑", 2, "IF 图像存在")):
                _xbot_retry_time = 0
                while _xbot_retry_time <= 2:
                    try:
                        xbot_visual.image.click(window_kind="screen", window=None, template_images=[package.image_selector("编辑路径")], anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", clicks="click", button="left", keys="null", move_mouse=True, timeout="10", delay_after="1", _block=("如果可编辑", 3, "点击图像"))
                        _xbot_retry_time = 4
                    except Exception as e:
                        if _xbot_retry_time == 2:
                            raise e
                        else:
                            xbot_visual.programing.log(type='info',text=e,_block=("如果可编辑", 3,"点击图像"))
                        _xbot_retry_time += 1
                        time.sleep(1)
                if xbot_visual.win32.window.contains_element(window="0", content_type="contains_element", element=package.selector("路径编辑框"), _block=("如果可编辑", 4, "IF 窗口包含")):
                    break
                #endif
            #endif
        #endloop
    finally:
        pass
