import os
import traceback
import streamlit as st

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from services.publisher.publisher_common import init_driver
from services.publisher.xiaohongshu_publisher import xiaohongshu_publisher
from services.publisher.douyin_publisher import douyin_publisher
from services.publisher.kuaishou_publisher import kuaishou_publisher
from services.publisher.shipinhao_publisher import shipinhao_publisher
from tools.file_utils import write_to_file, list_files, read_head
from tools.utils import get_must_session_option

last_published_file_name = 'last_published_cn.txt'

all_sites = ['xiaohongshu',
             'douyin',
             'kuaishou',
             'shipinhao',
             ]


def publish_to_platform(platform, driver, video_file, text_file):
    """
    发布到指定平台的封装函数
    """
    try:
        while True:
            ret = globals()[platform + '_publisher'](driver, video_file, text_file)  # 动态调用对应平台的发布函数
            if ret : 
                break
    except Exception as e:
        print(platform, "got error")
        traceback.print_exc()  # 打印完整的异常跟踪信息
        print(e)
    if video_file:
        save_last_published_file_name(os.path.basename(video_file))


def save_last_published_file_name(filename):
    write_to_file(filename, last_published_file_name)

def publish_file():
    driver = init_driver()
    video_file = get_must_session_option('video_publish_content_file', "请选择要发布的视频文件")
    text_file = get_must_session_option('video_publish_content_text', "请选择要发布的内容文件")
    if st.session_state.get("video_publish_enable_douyin"):
        publish_to_platform('douyin', driver, video_file, text_file)

    if st.session_state.get("video_publish_enable_kuaishou"):
        publish_to_platform('kuaishou', driver, video_file, text_file)

    if st.session_state.get("video_publish_enable_xiaohongshu"):
        publish_to_platform('xiaohongshu', driver, video_file, text_file)

    if st.session_state.get("video_publish_enable_shipinhao"):
        publish_to_platform('shipinhao', driver, video_file, text_file)

def publish_all():
    driver = init_driver()
    video_dir = get_must_session_option('video_publish_content_dir', "请设置视频发布内容")
    video_list = list_files(video_dir, '.mp4')
    text_list = list_files(video_dir, '.txt')
    while True:
        # 选择要发布的内容
        print("选择你要发布的视频,输入序号,A:全部,n-m从n到m:")
        for index, file_name in enumerate(video_list):
            print(str(index) + ":" + os.path.basename(file_name))
        print("上次发布的视频是: " + read_head(last_published_file_name))
        file_choice = input("\n请选择: ")
        print("")
        file_path_list = []
        text_path_list = []

        if file_choice == 'A':
            file_path_list = video_list
            text_path_list = text_list
        elif file_choice.isdigit():
            if len(video_list) > int(file_choice) >= 0:
                file_path_list.append(video_list[int(file_choice)])
                text_path_list.append(text_list[int(file_choice)])
            else:
                print("输入的序号不在范围内")
                continue
        else:
            range_list = file_choice.split('-')
            if len(range_list) == 2:
                start = int(range_list[0])
                end = int(range_list[1])
                if start <= end < len(video_list):
                    file_path_list = video_list[start:end + 1]
                    text_path_list = text_list[start:end + 1]
                else:
                    print("输入的序号不在范围内")
                    continue
            else:
                print("输入的序号不在范围内")
                continue

        while True:
            print("选择你要发布的平台:\n")
            print("1. 全部(小红书,抖音,快手,视频号)")
            print("2. 小红书")
            print("3. 抖音")
            print("4. 快手")
            print("5. 视频号")
            print("0. 退出")

            choice = input("\n请选择: ")
            print("")
            for file_path, text_path in zip(file_path_list, text_path_list):
                if choice == "1":
                    publish_to_platform('xiaohongshu', driver, file_path, text_path)
                    publish_to_platform('douyin', driver, file_path, text_path)
                    publish_to_platform('kuaishou', driver, file_path, text_path)
                    publish_to_platform('shipinhao', driver, file_path, text_path)
                elif choice == "2":
                    publish_to_platform('xiaohongshu', driver, file_path, text_path)
                elif choice == "3":
                    publish_to_platform('douyin', driver, file_path, text_path)

                elif choice == "4":
                    publish_to_platform('kuaishou', driver, file_path, text_path)

                elif choice == "5":
                    publish_to_platform('shipinhao', driver, file_path, text_path)
                else:
                    break
            if choice == "0":
                break


if __name__ == '__main__':
    publish_all()