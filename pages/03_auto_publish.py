import os

import streamlit as st

from config.config import driver_types
from pages.common import common_ui
from services.publish.open_test import start_all_pages,start_tiktok_pages,start_youtube_pages,start_xiaohongshu_pages
from tools.tr_utils import tr

# 获取当前脚本的绝对路径
script_path = os.path.abspath(__file__)

# 脚本所在的目录
script_dir = os.path.dirname(script_path)

default_bg_music_dir = os.path.join(script_dir, "../bgmusic")
default_bg_music_dir = os.path.abspath(default_bg_music_dir)


def test_publish_video():
    start_all_pages()


def start_publish_tiktok():
    start_tiktok_pages()

def start_publish_youtube():
    start_youtube_pages()

def start_publish_xiaohongshu():
    start_xiaohongshu_pages()

common_ui()

st.markdown("<h1 style='text-align: center; font-weight:bold; font-family:comic sans ms; padding-top: 0rem;'> \
            AI搞钱工具</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;padding-top: 0rem;'>视频批量自动发布工具</h2>", unsafe_allow_html=True)

# 选择要发布的视频目录
video_container = st.container(border=True)
with video_container:
    st.subheader(tr("Video Auto Public Config"))
    st.selectbox(label=tr("Driver Type"), options=driver_types, format_func=lambda x: driver_types.get(x),
                 key="video_publish_driver_type")
    if st.session_state.get("video_publish_driver_type") == 'chrome':
        st.text_input(label=tr("Driver Location"), key="video_publish_driver_location",
                      help=tr("Download the driver from https://googlechromelabs.github.io/chrome-for-testing/"))
        st.text_input(label=tr("Driver Debugger Address"), value="127.0.0.1:9222", key="video_publish_debugger_address")
    if st.session_state.get("video_publish_driver_type") == 'firefox':
        st.text_input(label=tr("Driver Location"), key="video_publish_driver_location",
                      help=tr("Download the driver from https://github.com/mozilla/geckodriver/releases"))
        st.text_input(label=tr("Driver Debugger Address"), value="127.0.0.1:2828", key="video_publish_debugger_address")
    st.text_input(label=tr("Video Content Dir"), key="video_publish_content_dir")


video_container = st.container(border=True)
with video_container:
    st.warning(tr("Click the test button, one new page will be opened, if not, that means your config has some error."))
    st.button(label=tr("Test Publish"), type="primary", on_click=test_publish_video)

video_container = st.container(border=True)
with video_container:
    st.warning(tr("Make sure your env is ready, before start publish"))
    st.subheader(tr("Video Publish"))
    llm_columns = st.columns(3)
    with llm_columns[0]:
        st.button(label=tr("tiktok"), type="primary", on_click=start_publish_tiktok)
    with llm_columns[1]:
        st.button(label=tr("youtube"), type="primary", on_click=start_publish_youtube)
    with llm_columns[2]:
        st.button(label=tr("xiaohongshu"), type="primary", on_click=start_publish_xiaohongshu)
