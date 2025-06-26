import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time
from xbot import print

def main(args):
    try:
        # process.run
        # win32.element.click
        桌面路径 = xbot_visual.dir.get_special_dir(special_dir_name="DesktopDirectory", _block=("main", 3, "获取系统文件夹路径"))
        公司名称和路径 = xbot_visual.excel.launch(launch_way="open", driver_way="auto_check", open_filename=lambda: 桌面路径+'\测试.xlsx', save_filename="", isvisible=True, ignoreformula=False, password=None, write_password=None, update_links=False, _block=("main", 4, "打开/新建Excel"))
        账户执行情况 = xbot_visual.excel.launch(launch_way="open", driver_way="auto_check", open_filename=lambda: 桌面路径+'\执行情况.xlsx', save_filename="", isvisible=True, ignoreformula=False, password=None, write_password=None, update_links=False, _block=("main", 5, "打开/新建Excel"))
        公司名称列表 = xbot_visual.list.create(_block=("main", 6, "新建列表"))
        执行情况excel行索引 = xbot_visual.programing.variable(value=lambda: 2
        , _block=("main", 7, "设置变量"))
        for 当前循环公司, 当前循环公司excel行号, _ in xbot_visual.excel.loop_data_from_workbook_with_return_item_location(workbook=公司名称和路径, loop_way="loop_range", range=None, begin_row_num=None, end_row_num=None, begin_column_name=None, end_column_name=None, has_header_row=False, range_begin_row_num="2", range_begin_column_name="E", range_end_row_num="-1", range_end_column_name="E", sheet_name="", using_text=False, text_cols="", clear_space=False, _block=("main", 8, "循环Excel内容")):
            当前循环路径 = xbot_visual.excel.read_data_from_workbook(workbook=账户执行情况, read_way="cell", range=None, cell_row_num=当前循环公司excel行号, cell_column_name="AC", area_begin_row_num=None, area_begin_column_name=None, area_end_row_num=None, area_end_column_name=None, row_row_num=None, get_display_text=False, has_header_row=False, column_column_name=None, sheet_name="", using_text=False, text_cols="", clear_space=False, _block=("main", 9, "读取Excel内容"))
            xbot_visual.win32.element.click(window="0", element=package.selector("查询按钮_余额表界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 10, "点击元素(win)"))
            公司名称 = xbot_visual.text.extract_content_from_text(text=lambda: str(当前循环公司), extract_way="custom", regular_pattern=lambda: "^\\['(.*)\'\\]$", just_get_first=True, ignore_case=False, _block=("main", 11, "从文本中提取内容"))
            xbot_visual.win32.element.input(window="0", element=package.selector("公司查找框_查询界面"), text=lambda: 公司名称, append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("main", 12, "填写输入框(win)"))
            win_wait_result = xbot_visual.win32.element.wait(window="0", element=package.selector("选择公司_查询界面"), state="appear", iswait=True, timeout="10", _block=("main", 13, "等待元素(win)"))
            if xbot_visual.win32.window.contains_element(window="0", content_type="not_contains_element", element=package.selector("选择公司_查询界面"), _block=("main", 14, "IF 窗口包含")):
                xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="A", begin_row_num="1", begin_column_name="", content=lambda: 公司名称, sheet_name="", write_as_text_cols=None, _block=("main", 15, "写入内容至Excel工作表"))
                xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="C", begin_row_num="1", begin_column_name="", content=lambda: "未下载：原因：未找到公司", sheet_name="", write_as_text_cols=None, _block=("main", 16, "写入内容至Excel工作表"))
                try:
                    __contains_xbot_ai_module__ = False
                    from xbot_ai.web import WebBrowser as xbot_ai_browser
                    xbot_ai_browser(None)
                    __contains_xbot_ai_module__ = True
                except:
                    pass
                执行情况excel行索引 = xbot_visual.process.invoke_module(module="magic_activities.mb95vf67m", package=__name__, function="increment_variable", params={
                    "variable_value": lambda: 执行情况excel行索引,
                }, _block=("main", 17, "变量自增1"))
                continue
            #endif
            xbot_visual.list.append_or_insert(lst=公司名称列表, insert_way="append", index="0", elem=公司名称, _block=("main", 20, "列表插入一项"))
            xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("main", 21, "键盘输入"))
            # process.run
            # process.run
            xbot_visual.win32.element.click(window="0", element=package.selector("账户查询按钮_查询界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 24, "点击元素(win)"))
            当前公司的账户选择按钮相似元素列表 = xbot_visual.win32.element.get_all_elements(window="0", selector=package.selector("账户选择按钮列表_账户界面"), operation="element", attribute_name=None, timeout="20", output_with_element_count=False, _block=("main", 25, "获取相似元素列表(win)"))
            current_datetime = xbot_visual.datetime.now(_block=("main", 26, "获取当前日期时间"))
            当月日期年月 = xbot_visual.datetime.to_string(datetime=current_datetime, format="%Y-%m", _block=("main", 27, "日期时间转换为文本"))
            上月最后一天日期 = xbot_visual.process.run(process="xbot_extensions.shadowbot_datatime.process2", package=__name__, inputs={
                "humanized_string": "上月最后一天",
                "formatting_string": "YYYY-MM-DD",
                "without_zeros": False,
                }, outputs=[
                "formatted_string",
            ], _block=("main", 28, "常用日期"))
            _, 具体日期 = xbot_visual.datetime.add(datetime=current_datetime, timeway="decrease", duration="1", unit="month", output_text=True, _block=("main", 29, "增加/减少时间"))
            上个月日期年月 = xbot_visual.datetime.to_string(datetime=具体日期, format="%Y-%m", _block=("main", 30, "日期时间转换为文本"))
            币种 = xbot_visual.win32.element.get_all_elements(window="0", selector=package.selector("币种列表_相似元素组"), operation="text", attribute_name=None, timeout="20", output_with_element_count=False, _block=("main", 31, "获取相似元素列表(win)"))
            账户名称列表文本 = xbot_visual.win32.element.get_all_elements(window="0", selector=package.selector("账户名称列表_相似元素组"), operation="text", attribute_name=None, timeout="20", output_with_element_count=False, _block=("main", 32, "获取相似元素列表(win)"))
            for 当前循环要选择的账户名称文本 in xbot_visual.workflow.list_iterator(list=账户名称列表文本, loop_start_index="0", loop_end_index="-1", output_with_index=False, _block=("main", 33, "ForEach列表循环")):
                xbot_visual.win32.element.click(window="0", element=package.selector("账户查询按钮_查询界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 34, "点击元素(win)"))
                账户名称索引_index = xbot_visual.list.get_index(lst=账户名称列表文本, elem=当前循环要选择的账户名称文本, _block=("main", 35, "获取列表指定项的位置"))
                当前币种名称 = xbot_visual.programing.variable(value=lambda: 币种[账户名称索引_index]
                , _block=("main", 36, "设置变量"))
                xbot_visual.win32.element.click(window="0", element=package.selector("全部选择/清除按钮_账户界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 37, "点击元素(win)"))
                xbot_visual.win32.element.click(window="0", element=package.selector("全部选择/清除按钮_账户界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 38, "点击元素(win)"))
                for loop_index in xbot_visual.workflow.range_iterator(start="0", stop=lambda: len(账户名称列表文本), step="1", _block=("main", 39, "For次数循环")):
                    if xbot_visual.image.exist(window_kind="currentactivatewindow", window="", exist_mode="exist", template_images=[package.image_selector("勾选成功图像_账户界面")], is_find_all_images=False, _block=("main", 40, "IF 图像存在")):
                        xbot_visual.image.click(window_kind="currentactivatewindow", window="", template_images=[package.image_selector("勾选成功图像_账户界面")], anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", clicks="click", button="left", keys="null", move_mouse=True, timeout="5", delay_after="1", _block=("main", 41, "点击图像"))
                    else:
                        break
                    #endif
                #endloop
                xbot_visual.win32.element.input(window="0", element=package.selector("账户搜索框"), text=当前循环要选择的账户名称文本, append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("main", 46, "填写输入框(win)"))
                xbot_visual.win32.element.click(window="0", element=package.selector("勾选按钮"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 47, "点击元素(win)"))
                xbot_visual.win32.element.click(window="0", element=package.selector("确定账户按钮"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="custom", sudoku_part="MiddleLeft", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 48, "点击元素(win)"))
                xbot_visual.win32.element.input(window="0", element=package.selector("截止日期输入框_查询界面"), text=上月最后一天日期, append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("main", 49, "填写输入框(win)"))
                xbot_visual.win32.element.click(window="0", element=package.selector("确定按钮_查询界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 50, "点击元素(win)"))
                xbot_visual.programing.sleep(random_number=False, seconds="3", start_number="1", stop_number="5", _block=("main", 51, "等待"))
                截止日期相似元素列表_文本 = xbot_visual.win32.element.get_all_elements(window="0", selector=package.selector("截止日期_余额表_相似元素组"), operation="text", attribute_name=None, timeout="20", output_with_element_count=False, _block=("main", 52, "获取相似元素列表(win)"))
                审批人列表 = xbot_visual.win32.element.get_all_elements(window="0", selector=package.selector("审批人_相似元素组"), operation="text", attribute_name=None, timeout="20", output_with_element_count=False, _block=("main", 53, "获取相似元素列表(win)"))
                for 数据界面截止日期_当前循环行日期 in xbot_visual.win32.element.iter_all_elements(window="0", selector=package.selector("截止日期_余额表_相似元素组"), operation="element", attribute_name=None, loop_start_index="0", loop_end_index="-1", timeout="20", output_with_index=False, _block=("main", 54, "循环相似元素(win)")):
                    截止日期列表_index = xbot_visual.list.get_index(lst=截止日期相似元素列表_文本, elem=lambda: 数据界面截止日期_当前循环行日期.get_text(), _block=("main", 55, "获取列表指定项的位置"))
                    if xbot_visual.workflow.multiconditional_judgment(relation="and", conditionals=[{"operand1": lambda: 数据界面截止日期_当前循环行日期.get_text()[:7],"operand2": 上个月日期年月,"operator": "=="},{"operand1": lambda: 审批人列表[截止日期列表_index],"operand2": lambda: "","operator": "!="}], _block=("main", 56, "IF 多条件")):
                        xbot_visual.win32.element.click(window="0", element=数据界面截止日期_当前循环行日期, clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 57, "点击元素(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("余额调节表按钮_余额表界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 58, "点击元素(win)"))
                        win_wait_result = xbot_visual.win32.window.wait_window(window_type="window_selector", window="", selector=package.selector("打印界面"), handle="", title="", handle_checked=False, class_name="", wait_way="appear", use_timeout=True, timeout="20", _block=("main", 59, "等待窗口"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("打印按钮_余额表界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 60, "点击元素(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("输出按钮_打印预览界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 61, "点击元素(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("单选按钮_输出到PDF文件_打印预览界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 62, "点击元素(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("选择目标文件按钮_输出界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 63, "点击元素(win)"))
                        xbot_visual.win32.element.input(window="0", element=package.selector("文件名输入框_保存界面"), text=lambda: 桌面路径+'\\余额调节表\\', append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("main", 64, "填写输入框(win)"))
                        xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("main", 65, "键盘输入"))
                        if xbot_visual.workflow.test(operand1=账户名称索引_index, operator="==", operand2="0", operator_options="{}", _block=("main", 66, "IF 条件")):
                            xbot_visual.win32.element.click(window="0", element=package.selector("新建文件夹按钮_打印界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 67, "点击元素(win)"))
                            xbot_visual.win32.send_keys(keys="{BACKSPACE}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("main", 68, "键盘输入"))
                            xbot_visual.win32.send_keys(keys=lambda: 公司名称+'-'+上个月日期年月, hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("main", 69, "键盘输入"))
                            xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("main", 70, "键盘输入"))
                        #endif
                        xbot_visual.win32.element.input(window="0", element=package.selector("文件名输入框_保存界面"), text=lambda: 公司名称+'-'+上个月日期年月+'\\'+公司名称+'-'+当前循环要选择的账户名称文本+'-'+当前币种名称+'-'+数据界面截止日期_当前循环行日期.get_text() + '.pdf', append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("main", 72, "填写输入框(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("保存按钮_保存界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 73, "点击元素(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("确定Y按钮_输出界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 74, "点击元素(win)"))
                        xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("main", 75, "等待"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("确定按钮_导出界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 76, "点击元素(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("关闭按下按钮_打印界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 77, "点击元素(win)"))
                        xbot_visual.win32.element.click(window="0", element=package.selector("返回按钮_余额表界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 78, "点击元素(win)"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="A", begin_row_num="1", begin_column_name="", content=lambda: 公司名称, sheet_name="", write_as_text_cols=None, _block=("main", 79, "写入内容至Excel工作表"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="B", begin_row_num="1", begin_column_name="", content=当前循环要选择的账户名称文本, sheet_name="", write_as_text_cols=None, _block=("main", 80, "写入内容至Excel工作表"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="C", begin_row_num="1", begin_column_name="", content=lambda: "已下载", sheet_name="", write_as_text_cols=None, _block=("main", 81, "写入内容至Excel工作表"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="D", begin_row_num="1", begin_column_name="", content=lambda: "√", sheet_name="", write_as_text_cols=None, _block=("main", 82, "写入内容至Excel工作表"))
                        try:
                            __contains_xbot_ai_module__ = False
                            from xbot_ai.web import WebBrowser as xbot_ai_browser
                            xbot_ai_browser(None)
                            __contains_xbot_ai_module__ = True
                        except:
                            pass
                        执行情况excel行索引 = xbot_visual.process.invoke_module(module="magic_activities.mb95vf67m", package=__name__, function="increment_variable", params={
                            "variable_value": lambda: 执行情况excel行索引,
                        }, _block=("main", 83, "变量自增1"))
                        break
                    elif xbot_visual.workflow.test(operand1=lambda: 审批人列表[截止日期列表_index], operator="==", operand2=lambda: "", operator_options="{}", _block=("main", 85, "Else IF")):
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="A", begin_row_num="1", begin_column_name="", content=lambda: 公司名称, sheet_name="", write_as_text_cols=None, _block=("main", 86, "写入内容至Excel工作表"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="B", begin_row_num="1", begin_column_name="", content=当前循环要选择的账户名称文本, sheet_name="", write_as_text_cols=None, _block=("main", 87, "写入内容至Excel工作表"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="C", begin_row_num="1", begin_column_name="", content=lambda: "未下载，原因：账户当月未审核", sheet_name="", write_as_text_cols=None, _block=("main", 88, "写入内容至Excel工作表"))
                        try:
                            __contains_xbot_ai_module__ = False
                            from xbot_ai.web import WebBrowser as xbot_ai_browser
                            xbot_ai_browser(None)
                            __contains_xbot_ai_module__ = True
                        except:
                            pass
                        执行情况excel行索引 = xbot_visual.process.invoke_module(module="magic_activities.mb95vf67m", package=__name__, function="increment_variable", params={
                            "variable_value": lambda: 执行情况excel行索引,
                        }, _block=("main", 89, "变量自增1"))
                        break
                    elif xbot_visual.workflow.test(operand1=截止日期相似元素列表_文本, operator="==", operand2=lambda: "", operator_options="{}", _block=("main", 91, "Else IF")):
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="A", begin_row_num="1", begin_column_name="", content=lambda: 公司名称, sheet_name="", write_as_text_cols=None, _block=("main", 92, "写入内容至Excel工作表"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="B", begin_row_num="1", begin_column_name="", content=当前循环要选择的账户名称文本, sheet_name="", write_as_text_cols=None, _block=("main", 93, "写入内容至Excel工作表"))
                        xbot_visual.excel.write_data_to_workbook(workbook=账户执行情况, write_range="area", write_way="append", write_column_way="override", row_num=执行情况excel行索引, column_name="C", begin_row_num="1", begin_column_name="", content=lambda: "未下载：原因：账户当月无数据", sheet_name="", write_as_text_cols=None, _block=("main", 94, "写入内容至Excel工作表"))
                        try:
                            __contains_xbot_ai_module__ = False
                            from xbot_ai.web import WebBrowser as xbot_ai_browser
                            xbot_ai_browser(None)
                            __contains_xbot_ai_module__ = True
                        except:
                            pass
                        执行情况excel行索引 = xbot_visual.process.invoke_module(module="magic_activities.mb95vf67m", package=__name__, function="increment_variable", params={
                            "variable_value": lambda: 执行情况excel行索引,
                        }, _block=("main", 95, "变量自增1"))
                        break
                    #endif
                #endloop
                xbot_visual.win32.element.click(window="0", element=package.selector("查询按钮_余额表界面"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 99, "点击元素(win)"))
            #endloop
        #endloop
        index索引 = xbot_visual.programing.variable(value=lambda: 0
        , _block=("main", 102, "设置变量"))
        for 当前循环路径, 当前循环公司excel行号, _ in xbot_visual.excel.loop_data_from_workbook_with_return_item_location(workbook=公司名称和路径, loop_way="loop_range", range=None, begin_row_num=None, end_row_num=None, begin_column_name=None, end_column_name=None, has_header_row=False, range_begin_row_num="2", range_begin_column_name="AC", range_end_row_num="-1", range_end_column_name="AC", sheet_name="", using_text=False, text_cols="", clear_space=False, _block=("main", 103, "循环Excel内容")):
            process_info = xbot_visual.system.run_or_open(application_path="C:\\Users\\Public.DESKTOP-4UAVD8T\\AppData\\Local\\Filez\\zBox\\zBox_client.exe", command_line_arguments=None, working_folder=None, after_application_launch="continue", is_waitexit_not_more_than=False, timeout_for_exit="10", is_waithwnd_not_more_than=False, timeout_for_hwnd="3", start_as_admin=False, window_style="normal", _block=("main", 104, "运行或打开"))
            _ = xbot_visual.process.run(process="process15", package=__name__, inputs={
                }, outputs=[
            ], _block=("main", 105, "调用流程"))
            xbot_visual.programing.sleep(random_number=False, seconds="2", start_number="1", stop_number="5", _block=("main", 106, "等待"))
            路径 = xbot_visual.text.extract_content_from_text(text=lambda: str(当前循环路径), extract_way="custom", regular_pattern=lambda: "^\\['(.*)\'\\]$", just_get_first=True, ignore_case=False, _block=("main", 107, "从文本中提取内容"))
            image_wait_result = xbot_visual.image.wait(window_kind="screen", window=None, wait_mode="appear", template_images=[package.image_selector("编辑路径")], is_wait_all_images=False, iswait=True, timeout="20", _block=("main", 108, "等待图像"))
            _ = xbot_visual.process.run(process="process14", package=__name__, inputs={
                }, outputs=[
            ], _block=("main", 109, "调用流程"))
            xbot_visual.win32.element.click(window="0", element=package.selector("路径编辑框"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 110, "点击元素(win)"))
            xbot_visual.win32.element.input(window="0", element=package.selector("路径编辑框"), text=lambda: 路径, append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("main", 111, "填写输入框(win)"))
            xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("main", 112, "键盘输入"))
            if xbot_visual.image.exist(window_kind="screen", window="", exist_mode="exist", template_images=[package.image_selector("找不到path")], is_find_all_images=False, _block=("main", 113, "IF 图像存在")):
                xbot_visual.programing.log(type="info", text="错误/找不到公司", _block=("main", 114, "打印日志"))
                break
            #endif
            if xbot_visual.image.exist(window_kind="screen", window=None, exist_mode="exist", template_images=[package.image_selector("不小心勾选到")], is_find_all_images=False, _block=("main", 117, "IF 图像存在")):
                xbot_visual.win32.element.click(window="0", element=package.selector("上方"), clicks="click", button="left", keys="null", delay_after="1", anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", move_mouse=True, simulate=True, timeout="20", _block=("main", 118, "点击元素(win)"))
            #endif
            网盘循环中公司名称文本 = xbot_visual.list.get_elem(lst=公司名称列表, index=lambda: index索引, _block=("main", 120, "获取列表指定位置项"))
            xbot_visual.win32.element.input(window="0", element=package.selector("文件名(N):"), text=lambda: 桌面路径+'\\余额调节表\\'+网盘循环中公司名称文本+'-'+上个月日期年月, append=False, simulate=True, save_to_clipboard=False, input_type="simulate", contains_hotkey=False, force_ime_ENG=False, send_key_delay="50", focus_timeout="1000", delay_after="1", click_before_input=True, anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", timeout="20", _block=("main", 121, "填写输入框(win)"))
            xbot_visual.win32.send_keys(keys="{ENTER}", hardware_driver_input=False, force_ime_eng=False, contains_hotkey=True, send_key_delay="50", delay_after="1", _block=("main", 122, "键盘输入"))
            xbot_visual.programing.sleep(random_number=False, seconds="1", start_number="1", stop_number="5", _block=("main", 123, "等待"))
            if xbot_visual.win32.window.contains_element(window="0", content_type="contains_element", element=package.selector("窗格"), _block=("main", 124, "IF 窗口包含")):
                xbot_visual.image.click(window_kind="screen", window="", template_images=[package.image_selector("图像2")], anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", clicks="click", button="left", keys="null", move_mouse=True, timeout="5", delay_after="1", _block=("main", 125, "点击图像"))
            #endif
            try:
                __contains_xbot_ai_module__ = False
                from xbot_ai.web import WebBrowser as xbot_ai_browser
                xbot_ai_browser(None)
                __contains_xbot_ai_module__ = True
            except:
                pass
            index索引 = xbot_visual.process.invoke_module(module="magic_activities.mb95vf67m", package=__name__, function="increment_variable", params={
                "variable_value": lambda: index索引,
            }, _block=("main", 127, "变量自增1"))
        #endloop
    finally:
        pass
