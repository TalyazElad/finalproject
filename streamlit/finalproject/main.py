import cv2
import os
import streamlit as st
import niqe_runner
from brisque_new import compute_score
import warnings

# Ignore all warnings
warnings.simplefilter("ignore")

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    os.makedirs(video_name, exist_ok=True)
    frame_count = 0
    niqe_sum = 0
    pique_sum = 0
    brisque_sum = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame_name = f"{video_name}_frame{frame_count}.jpg"
            cv2.imwrite(os.path.join(video_name, frame_name), frame)
            frame_count += 1
            niqe_sum += float(niqe_runner.runner(os.path.join(video_name, frame_name)))
            pique_sum += float(niqe_runner.pique_runner(os.path.join(video_name, frame_name)))
            brisque_sum += float(compute_score(os.path.join(video_name, frame_name)))
        else:
            break
    cap.release()
    st.success(f"Frames saved to folder {video_name}")
    niqe_avg = niqe_sum/frame_count
    pique_avg = pique_sum/frame_count
    brisque_avg = brisque_sum/frame_count
    st.success(f"niqe score : {niqe_avg}, pique score : {pique_avg}, brisque score : {brisque_avg}")

def main():
    st.title("Video quality evaluation")

    uploaded_file = st.file_uploader("Select an MP4 video file", type="mp4")

    if uploaded_file is not None:
        video_path = "uploaded.mp4"
        with open(video_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        extract_frames(video_path)
        os.remove(video_path)

if __name__ == "__main__":
    main()

# import io
# import multiprocessing
# import os
# import time
#
# import cv2
# import numpy as np
# import streamlit as st
# import torch
# from piq import brisque, niqe, piqe
#
#
# def extract_frames(video_path):
#     cap = cv2.VideoCapture(video_path)
#     video_name = st.secrets["upload_folder"]
#     os.makedirs(video_name, exist_ok=True)
#     frame_count = 0
#     niqe_sum = 0
#     brisque_sum = 0
#     piqe_sum = 0
#
#     frames = []
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if ret:
#             frames.append(frame)
#             frame_count += 1
#         else:
#             break
#     cap.release()
#
#     if not frames:
#         st.error("No frames found in the video")
#         return
#
#     st.success(f"Extracted {len(frames)} frames from the video")
#
#     def compute_scores(frame):
#         niqe_score = niqe(torch.from_numpy(np.transpose(frame, (2, 0, 1))).float(), data_range=1.0)
#         brisque_score = brisque(torch.from_numpy(np.transpose(frame, (2, 0, 1))).float(), data_range=1.0)
#         piqe_score = piqe(torch.from_numpy(frame).permute(2, 0, 1).unsqueeze(0), data_range=1.0)
#         return niqe_score.item(), brisque_score.item(), piqe_score.item()
#
#     with multiprocessing.Pool() as pool:
#         results = pool.map(compute_scores, frames)
#         niqe_scores, brisque_scores, piqe_scores = zip(*results)
#
#     niqe_avg = sum(niqe_scores) / frame_count
#     brisque_avg = sum(brisque_scores) / frame_count
#     piqe_avg = sum(piqe_scores) / frame_count
#     st.success(f"niqe score : {niqe_avg}, brisque score : {brisque_avg}, piqe score : {piqe_avg}")
#
#
# def main():
#     st.title("Video quality evaluation")
#
#     uploaded_file = st.file_uploader("Select an MP4 video file", type="mp4")
#
#     if uploaded_file is not None:
#         video_bytes = uploaded_file.read()
#         video_path = io.BytesIO(video_bytes)
#         st.secrets["upload_folder"] = f"uploaded_{int(time.time())}"
#         extract_frames(video_path)
#         st.secrets.pop("upload_folder", None)
#
#
# if __name__ == "__main__":
#     main()
