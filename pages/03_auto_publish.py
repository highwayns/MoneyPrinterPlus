import os

import streamlit as st

from config.config import driver_types, my_config, save_config, test_config
from pages.common import common_ui
from services.publisher.open_test import start_all_pages
from services.publisher.publish_video import publish_all, publish_file
from tools.tr_utils import tr
import threading
from streamlit.runtime.scriptrunner import add_script_run_ctx

from tools.utils import get_file_map_from_dir

# 获取当前脚本的绝对路径
script_path = os.path.abspath(__file__)

# 脚本所在的目录
script_dir = os.path.dirname(script_path)


def get_tags(my_type):
    test_config(my_config, "publisher", my_type)
    if 'tags' not in my_config['publisher'][my_type]:
        # 设置默认值
        my_config['publisher'][my_type]['tags'] = []
        save_config()
        return ""
    else:
        return " ".join(my_config['publisher'][my_type]['tags'])


def set_tags(my_type, state_key):
    common_prefix = st.session_state.get(state_key)
    test_config(my_config, "publisher", my_type)
    my_config['publisher'][my_type]['tags'] = common_prefix.split()
    save_config()


def get_content_location():
    test_config(my_config, "publisher")
    if 'content_location' not in my_config['publisher']:
        # 默认''
        my_config['publisher']['content_location'] = ''
        save_config()
        return ''
    else:
        return my_config['publisher']['content_location']


def set_content_location(state_key):
    use_common = st.session_state.get(state_key)
    test_config(my_config, "publisher")
    my_config['publisher']['content_location'] = use_common
    save_config()


def get_driver_location():
    test_config(my_config, "publisher")
    if 'driver_location' not in my_config['publisher']:
        # 默认''
        my_config['publisher']['driver_location'] = ''
        save_config()
        return ''
    else:
        return my_config['publisher']['driver_location']


def set_driver_location(state_key):
    use_common = st.session_state.get(state_key)
    test_config(my_config, "publisher")
    my_config['publisher']['driver_location'] = use_common
    save_config()


def get_auto():
    test_config(my_config, "publisher")
    if 'auto_publish' not in my_config['publisher']:
        # 默认True
        my_config['publisher']['auto_publish'] = True
        save_config()
        return True
    else:
        return my_config['publisher']['auto_publish']


def set_auto(state_key):
    use_common = st.session_state.get(state_key)
    test_config(my_config, "publisher")
    my_config['publisher']['auto_publish'] = use_common
    save_config()


def get_enable(my_type):
    test_config(my_config, "publisher", my_type)
    if 'enable' not in my_config['publisher'][my_type]:
        # 默认True
        my_config['publisher'][my_type]['enable'] = True
        save_config()
        return True
    else:
        return my_config['publisher'][my_type]['enable']


def set_enable(my_type, state_key):
    use_common = st.session_state.get(state_key)
    test_config(my_config, "publisher", my_type)
    my_config['publisher'][my_type]['enable'] = use_common
    save_config()


def get_enable_kuaishou(my_type):
    test_config(my_config, "publisher", "kuaishou", my_type)
    if 'enable' not in my_config['publisher']['kuaishou'][my_type]:
        # 默认True
        my_config['publisher']['kuaishou'][my_type]['enable'] = True
        save_config()
        return True
    else:
        return my_config['publisher']['kuaishou'][my_type]['enable']


def set_enable_kuaishou(my_type, state_key):
    use_common = st.session_state.get(state_key)
    test_config(my_config, "publisher", "kuaishou", my_type)
    my_config['publisher']['kuaishou'][my_type]['enable'] = use_common
    save_config()


def get_kuaishou_value(my_type, kuaishou_key):
    test_config(my_config, "publisher", "kuaishou", my_type)
    if kuaishou_key not in my_config['publisher']['kuaishou'][my_type]:
        # 默认True
        my_config['publisher']['kuaishou'][my_type][kuaishou_key] = ""
        save_config()
        return ''
    else:
        return my_config['publisher']['kuaishou'][my_type][kuaishou_key]


def set_kuaishou_value(my_type, kuaishou_key, state_key):
    use_common = st.session_state.get(state_key)
    test_config(my_config, "publisher", "kuaishou", my_type)
    my_config['publisher']['kuaishou'][my_type][kuaishou_key] = use_common
    save_config()


def get_title_prefix(my_type):
    test_config(my_config, "publisher", my_type)
    if 'title_prefix' not in my_config['publisher'][my_type]:
        # 设置默认值
        my_config['publisher'][my_type]['title_prefix'] = ""
        save_config()
        return ""
    else:
        return my_config['publisher'][my_type]['title_prefix']


def set_title_prefix(my_type, state_key):
    common_prefix = st.session_state.get(state_key)
    test_config(my_config, "publisher", my_type)
    my_config['publisher'][my_type]['title_prefix'] = common_prefix
    save_config()


def get_collection_name(my_type):
    test_config(my_config, "publisher", my_type)
    if 'collection' not in my_config['publisher'][my_type]:
        # 设置默认值
        my_config['publisher'][my_type]['collection'] = ""
        save_config()
        return ""
    else:
        return my_config['publisher'][my_type]['collection']


def set_collection_name(my_type, state_key):
    common_collection = st.session_state.get(state_key)
    test_config(my_config, "publisher", my_type)
    my_config['publisher'][my_type]['collection'] = common_collection
    save_config()


def test_publish_video():
    t = threading.Thread(target=start_all_pages)
    add_script_run_ctx(t)
    t.start()



def start_publish_video():
    t = threading.Thread(target=publish_file)
    add_script_run_ctx(t)
    t.start()

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
                      value=get_driver_location(), on_change=set_driver_location,
                      args=('video_publish_driver_location',),
                      help=tr("Download the driver from https://googlechromelabs.github.io/chrome-for-testing/"))
        st.text_input(label=tr("Driver Debugger Address"), value="127.0.0.1:9222", key="video_publish_debugger_address")
    if st.session_state.get("video_publish_driver_type") == 'firefox':
        st.text_input(label=tr("Driver Location"), key="video_publish_driver_location",
                      value=get_driver_location(), on_change=set_driver_location,
                      args=('video_publish_driver_location',),
                      help=tr("Download the driver from https://github.com/mozilla/geckodriver/releases"))
        st.text_input(label=tr("Driver Debugger Address"), value="127.0.0.1:2828", key="video_publish_debugger_address")
    st.text_input(label=tr("Video Content Dir"), key="video_publish_content_dir",
                  value=get_content_location(), on_change=set_content_location, args=('video_publish_content_dir',))
    video_list = get_file_map_from_dir(st.session_state["video_publish_content_dir"], ".mp4")
    st.selectbox(label=tr("Video File"), key="video_publish_content_file",
                 options=video_list, format_func=lambda x: video_list[x])
    file_list = get_file_map_from_dir(st.session_state["video_publish_content_dir"], ".txt")
    st.selectbox(label=tr("Text File"), key="video_publish_content_text",
                 options=file_list, format_func=lambda x: file_list[x])

# 视频网站配置区
video_config_container = st.container(border=True)
with video_config_container:
    st.subheader(tr("Video Site Config"))
    st.checkbox(label=tr("Auto Publish"), key="video_publish_auto_publish",
                value=get_auto(), on_change=set_auto, args=('video_publish_auto_publish',))
    st.checkbox(label=tr("Use Common Config"), key="video_publish_use_common_config",
                value=get_enable('common'), on_change=set_enable, args=('common', 'video_publish_use_common_config'))
    if st.session_state.get("video_publish_use_common_config"):
        st_columns = st.columns(3)
        with st_columns[0]:
            st.text_input(label=tr("Title Prefix"), key="video_publish_title_prefix",
                          value=get_title_prefix('common'), on_change=set_title_prefix,
                          args=('common', 'video_publish_title_prefix'))
        with st_columns[1]:
            st.text_input(label=tr("Collection Name"), key="video_publish_collection_name",
                          value=get_collection_name('common'), on_change=set_collection_name,
                          args=('common', 'video_publish_collection_name'))
        with st_columns[2]:
            st.text_input(label=tr("Tags"), key="video_publish_tags",
                          value=get_tags('common'), on_change=set_tags,
                          args=('common', 'video_publish_tags'))
    st.subheader(tr("Douyin Config"))
    st.checkbox(label=tr("Enable douyin"), key="video_publish_enable_douyin",
                value=get_enable("douyin"), on_change=set_enable, args=('douyin', 'video_publish_enable_douyin'))
    if not st.session_state.get("video_publish_use_common_config"):
        st_columns = st.columns(3)
        with st_columns[0]:
            st.text_input(label=tr("Title Prefix"), key="video_publish_douyin_title_prefix",
                          value=get_title_prefix('douyin'), on_change=set_title_prefix,
                          args=('douyin', 'video_publish_douyin_title_prefix'))
        with st_columns[1]:
            st.text_input(label=tr("Collection Name"), key="video_publish_douyin_collection_name",
                          value=get_collection_name('douyin'), on_change=set_collection_name,
                          args=('douyin', 'video_publish_douyin_collection_name'))
        with st_columns[2]:
            st.text_input(label=tr("Tags"), key="video_publish_douyin_tags",
                          value=get_tags('douyin'), on_change=set_tags,
                          args=('douyin', 'video_publish_douyin_tags'))
    st.subheader(tr("Kuaishou Config"))
    st.checkbox(label=tr("Enable kuaishou"), key="video_publish_enable_kuaishou",
                value=get_enable('kuaishou'), on_change=set_enable,
                args=('kuaishou', 'video_publish_enable_kuaishou'))
    if not st.session_state.get("video_publish_use_common_config"):
        st_columns = st.columns(3)
        with st_columns[0]:
            st.text_input(label=tr("Title Prefix"), key="video_publish_kuaishou_title_prefix",
                          value=get_title_prefix('kuaishou'), on_change=set_title_prefix,
                          args=('kuaishou', 'video_publish_kuaishou_title_prefix'))
        with st_columns[1]:
            st.text_input(label=tr("Collection Name"), key="video_publish_kuaishou_collection_name",
                          value=get_collection_name('kuaishou'), on_change=set_collection_name,
                          args=('kuaishou', 'video_publish_kuaishou_collection_name'))
        with st_columns[2]:
            st.text_input(label=tr("Tags"), key="video_publish_kuaishou_tags",
                          value=get_tags('kuaishou'), on_change=set_tags,
                          args=('kuaishou', 'video_publish_kuaishou_tags'))
    st.checkbox(label=tr("Enable kuaishou domain"), key="video_publish_enable_kuaishou_domain",
                value=get_enable_kuaishou('domain'), on_change=set_enable_kuaishou,
                args=('domain', 'video_publish_enable_kuaishou_domain'))
    st_columns = st.columns(2)
    with st_columns[0]:
        st.text_input(label=tr("Domain Level1"), key="video_publish_kuaishou_domain_level1",
                      value=get_kuaishou_value('domain', 'level1'), on_change=set_kuaishou_value,
                      args=('domain', 'level1', 'video_publish_kuaishou_domain_level1'))
    with st_columns[1]:
        st.text_input(label=tr("Domain Level2"), key="video_publish_kuaishou_domain_level2",
                      value=get_kuaishou_value('domain', 'level2'), on_change=set_kuaishou_value,
                      args=('domain', 'level2', 'video_publish_kuaishou_domain_level2'))
    st.subheader(tr("shipinhao Config"))
    st.checkbox(label=tr("Enable shipinhao"), key="video_publish_enable_shipinhao",
                value=get_enable('shipinhao'), on_change=set_enable,
                args=('shipinhao', 'video_publish_enable_shipinhao'))
    if not st.session_state.get("video_publish_use_common_config"):
        st_columns = st.columns(3)
        with st_columns[0]:
            st.text_input(label=tr("Title Prefix"), key="video_publish_shipinhao_title_prefix",
                          value=get_title_prefix('shipinhao'), on_change=set_title_prefix,
                          args=('shipinhao', 'video_publish_shipinhao_title_prefix'))
        with st_columns[1]:
            st.text_input(label=tr("Collection Name"), key="video_publish_shipinhao_collection_name",
                          value=get_collection_name('shipinhao'), on_change=set_collection_name,
                          args=('shipinhao', 'video_publish_shipinhao_collection_name'))
        with st_columns[2]:
            st.text_input(label=tr("Tags"), key="video_publish_shipinhao_tags",
                          value=get_tags('shipinhao'), on_change=set_tags,
                          args=('shipinhao', 'video_publish_shipinhao_tags'))
    st.subheader(tr("Xiaohongshu Config"))
    st.checkbox(label=tr("Enable xiaohongshu"), key="video_publish_enable_xiaohongshu",
                value=get_enable('xiaohongshu'), on_change=set_enable,
                args=('xiaohongshu', 'video_publish_enable_xiaohongshu'))
    if not st.session_state.get("video_publish_use_common_config"):
        st_columns = st.columns(3)
        with st_columns[0]:
            st.text_input(label=tr("Title Prefix"), key="video_publish_xiaohongshu_title_prefix",
                          value=get_title_prefix('xiaohongshu'), on_change=set_title_prefix,
                          args=('xiaohongshu', 'video_publish_xiaohongshu_title_prefix'))
        with st_columns[1]:
            st.text_input(label=tr("Collection Name"), key="video_publish_xiaohongshu_collection_name",
                          value=get_collection_name('xiaohongshu'), on_change=set_collection_name,
                          args=('xiaohongshu', 'video_publish_xiaohongshu_collection_name'))
        with st_columns[2]:
            st.text_input(label=tr("Tags"), key="video_publish_xiaohongshu_tags",
                          value=get_tags('xiaohongshu'), on_change=set_tags,
                          args=('xiaohongshu', 'video_publish_xiaohongshu_tags'))

video_container = st.container(border=True)
with video_container:
    st.warning(tr("Click the test button, one new page will be opened, if not, that means your config has some error."))
    st.button(label=tr("Test Publish"), type="primary", on_click=test_publish_video)

video_container = st.container(border=True)
with video_container:
    st.warning(tr("Make sure your env is ready, before start publish"))
    st.subheader(tr("Video Publish"))
    st.button(label=tr("Start Publish"), type="primary", on_click=start_publish_video)
#    llm_columns = st.columns(3)
#    with llm_columns[0]:
#        st.button(label=tr("tiktok"), type="primary", on_click=start_publish_tiktok)
#    with llm_columns[1]:
#        st.button(label=tr("youtube"), type="primary", on_click=start_publish_youtube)
#    with llm_columns[2]:
#        st.button(label=tr("xiaohongshu"), type="primary", on_click=start_publish_xiaohongshu)
