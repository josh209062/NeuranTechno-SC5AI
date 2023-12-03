import glob
import streamlit as st
import wget
from PIL import Image
import torch
import cv2
import os
import time
from io import *
from streamlit import session_state
import subprocess
import pandas as pd
from collections import Counter
import numpy as np
import av

st.set_page_config(
    page_title="Remilk Go: Milk Detection",
    page_icon="🥛",
    layout="wide"
)

cfg_model_path = 'models/best.pt'
model = None
confidence = .10


def image_input(data_src):
    img_file = None
    if data_src == 'Sample data':
        # get all sample images
        img_path = glob.glob('data/sample_images/*')
        img_slider = st.slider("Select a test image.",
                               min_value=1, max_value=len(img_path), step=1)
        img_file = img_path[img_slider - 1]
    else:
        img_bytes = st.file_uploader(
            "Upload an image", type=['png', 'jpeg', 'jpg'])
        if img_bytes:
            img_file = "data/uploaded_data/upload." + \
                img_bytes.name.split('.')[-1]
            Image.open(img_bytes).save(img_file)

    if img_file:
        col1, col2 = st.columns(2)
        with col1:
            st.image(img_file, caption="Selected Image")
        with col2:
            img, results = infer_image(img_file)
            st.image(img, caption="Model prediction")
            detected_obj = results.pandas().xyxy[0]['name']
            unique, counts = np.unique(detected_obj, return_counts=True)
            detected_products = dict(zip(unique, counts))

        df = pd.DataFrame(list(detected_products.items()),
                          columns=['Product Name', 'Row Of Product'])
        df['Count of Products'] = df['Row Of Product'] * 5

        st.table(df)


def video_input(data_src):
    vid_file = None
    if data_src == 'Sample data':
        vid_file = "data/sample_videos/sample.mp4"
    else:
        vid_bytes = st.file_uploader(
            "Upload a video", type=['mp4', 'mpv', 'avi'])
        if vid_bytes:
            vid_file = "data/uploaded_data/upload." + \
                vid_bytes.name.split('.')[-1]
            with open(vid_file, 'wb') as out:
                out.write(vid_bytes.read())

    if vid_file:
        cap = cv2.VideoCapture(vid_file)
        custom_size = st.sidebar.checkbox("Custom frame size")
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if custom_size:
            width = st.sidebar.number_input(
                "Width", min_value=120, step=20, value=width)
            height = st.sidebar.number_input(
                "Height", min_value=120, step=20, value=height)

        fps = 0
        st1, st2, st3 = st.columns(3)
        with st1:
            st.markdown("## Height")
            st1_text = st.markdown(f"{height}")
        with st2:
            st.markdown("## Width")
            st2_text = st.markdown(f"{width}")
        with st3:
            st.markdown("## FPS")
            st3_text = st.markdown(f"{fps}")

        st.markdown("---")
        output = st.empty()
        prev_time = 0
        curr_time = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                st.write("Can't read frame, stream ended? Exiting ....")
                break
            frame = cv2.resize(frame, (width, height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output_img, results = infer_image(frame)
            output.image(output_img)
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time
            st1_text.markdown(f"**{height}**")
            st2_text.markdown(f"**{width}**")
            st3_text.markdown(f"**{fps:.2f}**")
        cap.release()


def infer_image(img, size=None):
    model.conf = confidence
    result = model(img, size=size) if size else model(img)
    result.render()
    image = Image.fromarray(result.ims[0])
    return image, result


@st.cache_resource
def load_model(path, device):
    model_ = torch.hub.load('WangRongsheng/BestYOLO',
                            'custom', path=path, force_reload=True)
    model_.to(device)
    print("model to ", device)
    return model_


@st.cache_resource
def download_model(url):
    model_file = wget.download(url, out="models")
    return model_file


def main():
    # global variables
    global model, confidence, cfg_model_path

    st.title("🥛 Remilk Go: Various of milk Types Detection for Automated Smart Retail Monitoring System 🥛")
    st.sidebar.write("Wellcome to Remilk Go 🥛")
    st.sidebar.write("")

    st.sidebar.title("⚙️ Settings")
    st.sidebar.write("Please Configure Settings")

    # upload model

    # check if model file is available
    if not os.path.isfile(cfg_model_path):
        st.warning(
            "Model file not available!!!, please added to the model folder.", icon="⚠️")
    else:
        # device options
        if torch.cuda.is_available():
            device_option = st.sidebar.radio(
                "Select Device", ['cpu', 'cuda'], disabled=False, index=0, label_visibility="collapsed")
        else:
            device_option = "cpu"

        # load model
        model = load_model(cfg_model_path, device_option)

        # input options
        input_option = st.sidebar.selectbox(
            "Select Activity: ", ['🎪 Home', '📷 Detect Via Image', '🎬 Detect Via Video'], index=0)
        st.sidebar.markdown("---")

        # confidence slider
        if (input_option == '📷 Detect Via Image') or (input_option == '🎬 Detect Via Video'):
            confidence = st.sidebar.slider(
                '👁‍🗨 Confidence Level', min_value=0.1, max_value=0.8, value=.10)

            # custom classes
            if st.sidebar.checkbox("🛠 Custom Classes"):
                model_names = list(model.names.values())
                assigned_class = st.sidebar.multiselect(
                    "Select Classes", model_names, default=[model_names[0]])
                classes = [model_names.index(name) for name in assigned_class]
                model.classes = classes
            else:
                model.classes = list(model.names.keys())
            st.sidebar.markdown("---")

        # input src option

        if input_option == '📷 Detect Via Image':
            data_src = st.sidebar.radio("Select input source: ", [
                'Sample data', 'Upload your own data'])
            image_input(data_src)
        elif input_option == '🎬 Detect Via Video':
            data_src = st.sidebar.radio("Select input source: ", [
                'Sample data', 'Upload your own data'])
            video_input(data_src)
        elif input_option == '🎪 Home':
            html_temp_home1 = """<div style="background-color:#6D7B8D;padding:10px">
                                            <h4 style="color:white;text-align:center;">
                                            Frisian Flag Milk Product Detection</h4>
                                            </div>
                                            </br>"""
            st.markdown(html_temp_home1, unsafe_allow_html=True)
            st.write("""
                    Feature of this App: 

                    1. Feature to detect Frisian Flag product by Image

                    2. Feature to detect Frisian Flag product by Video

                    """)
            st.write(" ")
            st.write(" ")
            st.write(" ")

            st.write("# 👨‍💼 Team Profile")
            st.write("### NeuranTechno Team - Startup Campus")
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                pass
            with col2:
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.image("assets/logoKM.png")
            with col4:
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.write(" ")
                st.image("assets/logoSC.png")
            with col5:
                pass
            with col3:
                st.image(
                    "assets/logoNT.png")
            st.write(" ")
            st.write("**Supervisor**  - M. Haswin Anugrah Pratama")
            st.write("**Facilitator** - Ni Luh Nitya Ayu Laksmi")
            st.write(" ")
            st.write("**_Team_**: ")
            st.write(
                "**1. Reynaldi Tangkearung (Leader)**      - Universitas Dipa Makassar")
            st.write(
                "**2. Joshua Immanuel Fransisko Manurung** - Universitas Sumatera Utara")
            st.write(
                "**3. Dhea Amanda Ramadhan**               - Universitas Riau")
            st.write("**4. Moh. Daril Anwar**              - Universitas Trunojoyo")
            st.write(
                "**5. Nirmala Arumningtyas**               - Universitas PGRI Yogyakarta")
            st.write(
                "**6. Purnomo Hernaoli**                   - Universitas Sebelas Maret")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            # st.write(model.names)

        st.sidebar.markdown("---")
        st.sidebar.image("assets/logoNT.png")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
