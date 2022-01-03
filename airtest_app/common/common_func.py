from common.desired_caps import *
from config.caps import *

from poco.exceptions import PocoNoSuchNodeException,PocoTargetTimeout
from assertpy import assert_that
import xlrd
import allure
import yaml


#检测文件夹是否建立
def check_file(file_dir):
    if not os.path.exists(file_dir):
        print(file_dir)
        os.mkdir(file_dir)

#截图功能
def Snapshot(dirname,element):
    dirname=SCRE_DIR+'/'+dirname
    check_file(dirname)
    file_name=dirname+'/'+element+'.png'
    snapshot(file_name,msg=element)
    return file_name

#截图并allure加载截图
def attach_snap(dirname,element):
    sleep(0.3)
    file_name=Snapshot(dirname,element)
    logging.info("截图："+element)
    allure.step("截图："+element)
    allure.attach.file(file_name, name=element,attachment_type=allure.attachment_type.JPG)

#xls文件读取
def get_excel(filename):
    # 打开指定路径的Excel文件
    file_name=DATA_DIR+'/'+filename
    ex = xlrd.open_workbook(file_name)
    # 通过索引查找sheet
    sheet = ex.sheet_by_index(0)
    # 定义1个空列表，用于存放控件信息
    dat = []
    # 遍历表格的每一行数据，将每行的控件信息构建成1个字典添加到列表中
    for row in range(sheet.nrows):
        cells=sheet.row_values(row)
        # print(cells)
        data={'element':cells[1],'attributes':cells[2],'position':cells[3]}
        dat.append(data)
    return dat

#获取xls文件，处理控件信息
def handle_poco(filename,element):
    sleep(0.5)
    list=get_excel(filename)
    for li in list:
        if li.get('element')==element:
            # logging.info("获取元素："+element)
            # allure.step("获取元素："+element)
            if li.get('attributes')=='text':
                return poco(text=li.get('position'))
            elif li.get('attributes')=='name':
                return poco(li.get('position'))

#poco元素点击
def handle_poco_click(filename,dirname,element,back=None):
    logging.info("点击元素：" + element)
    allure.step("点击元素：" + element)
    handle_poco(filename, element).click()
    sleep(0.5)
    attach_snap(dirname,element) #截图
    if back=='BACK':
        keyevent("BACK")


# #断言
# def asser_ele(filename,element,ele):
#     value = handle_poco(filename, element).attr('text')
#     try:
#         assert_equal(value, ele, '元素为' + element)
#         # handle_poco(filename, element).click()
#     except AssertionError:
#         print("元素" + element + "断言失败")

#assertpy断言库，判断是否包含元素的文本
def asser_ele_in(filename,element,ele):
    value=handle_poco(filename,element).get_text()
    print(value)
    try:
        assert_that(value).contains(ele)
    except AssertionError:
        print('元素不存在：'+ele)


# 根据相对坐标来点击元素下方的元素
def handle_poco_click_down(filename,dirname,element,back=None):
    logging.info("点击_" + element+"_下方的元素")
    allure.step("点击_" + element+"_下方的元素")
    handle_poco(filename, element).focus([1, 2]).click() #点击元素
    attach_snap(dirname,element+"_下方的元素") #截图
    if back=='BACK':
        keyevent("BACK")


#图片识别处理
def handle_air(dirname,element,back=None):
    filename=PIC_DIR+'/'+dirname+'/'+element+'.png'
    logging.info("点击元素："+element)
    allure.step("点击元素："+element)
    touch(Template(filename))
    sleep(1)
    attach_snap(dirname,element)  # 截图
    if back=='BACK':
        keyevent("BACK")


#判断元素是否存在
def ele_exists(filename,dirname,element,back=None):
    ele=handle_poco(filename,element)
    logging.info("判断元素是否存在：" + element)
    allure.step("判断元素是否存在：" + element)
    sleep(3)
    try:
        ele.click()
        attach_snap(dirname, element)  # 截图
        if back == 'BACK':
            keyevent("BACK")
    except PocoNoSuchNodeException:
        Snapshot(dirname,"不存在"+element)

#等待元素出现
def waitloading(filename,dirname,element,back=None):
    ele = handle_poco(filename, element)
    logging.info("等待元素出现：" + element)
    allure.step("等待元素出现：" + element)
    try:
        ele.wait_for_appearance(timeout=5)
        ele.click()
        sleep(0.5)
        if back == 'BACK':
            keyevent("BACK")
    except PocoTargetTimeout:
        Snapshot(dirname,"未出现"+element)
        if back == 'BACK':
            keyevent("BACK")

#获取最新报告
def latest_report():
    report_dir=REPORT_DIR
    lists=os.listdir(report_dir)
    lists.sort(key=lambda fn:os.path.getatime(report_dir+'/'+fn))
    logging.info('获取最新报告')
    file=os.path.join(report_dir,lists[-1])
    return file

#元素向左滑
def swip_left(filename,element):
    logging.info("向左滑动：" + element)
    allure.step("向左滑动：" + element)
    ele=handle_poco(filename, element)
    ele.swipe([-1, 0])
    sleep(1)

#元素向上滑
def swip_up(filename,element):
    logging.info("向上滑动：" + element)
    allure.step("向上滑动：" + element)
    ele=handle_poco(filename, element)
    ele.swipe([0, -1])
    sleep(1)

#元素向下滑
def swip_down(filename,element):
    logging.info("向下滑动：" + element)
    allure.step("向下滑动：" + element)
    ele=handle_poco(filename, element)
    ele.swipe([0, 1])
    sleep(1)

#上传头像
def upload_snap():
    poco("android.widget.FrameLayout").offspring("com.android.gallery3d:id/fragment_container").offspring(
        "com.android.gallery3d:id/list_albumset").child("com.android.gallery3d:id/gallery_statelist_view")[0].offspring(
        "com.android.gallery3d:id/album_cover_image").click()
    poco(desc="图片7, 2021年8月11日上午10:07").click()
    poco("com.android.gallery3d:id/head_select_right").click()


#读取yaml文件
def get_yaml():
    filename=DATA_DIR+'/data.yaml'
    with open(filename) as f:
        datas=yaml.safe_load(f)
    # print(datas)
    return datas


# 获取当前屏幕分辨率,点击相对坐标元素
def click_resolving(x,y,back=None):
    width = G.DEVICE.display_info['width']
    height = G.DEVICE.display_info['height']
    x1 = x * width
    y1 = y * height
    sleep(0.3)
    touch([x1, y1])
    sleep(2)
    if back == 'BACK':
        keyevent("BACK")
        sleep(1)


if __name__ == '__main__':
    get_yaml()