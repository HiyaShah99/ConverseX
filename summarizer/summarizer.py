# summarizer.py



# summarizer.py

import os
import whisper
import moviepy.editor as mp
import cv2
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
import torch
from textwrap import wrap
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load models only once
whisper_model = whisper.load_model("base")
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_audio(video_path, audio_path="temp_audio.mp3"):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return audio_path

def extract_keyframes(video_path, interval=5):
    cap = cv2.VideoCapture(video_path)
    frames = []
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        if count % (fps * interval) == 0:
            frames.append(frame)
        count += 1
    cap.release()
    return frames

def caption_image(image_np):
    image_pil = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
    inputs = blip_processor(image_pil, return_tensors="pt").to(device)
    out = blip_model.generate(**inputs)
    caption = blip_processor.decode(out[0], skip_special_tokens=True)
    return caption

def save_to_pdf(text, filename="video_summary.pdf"):
    filename = os.path.join(os.path.dirname(__file__), filename)
    c = canvas.Canvas(filename, pagesize=letter)

    width, height = letter
    y = height - 40
    for line in wrap(text, 100):
        c.drawString(40, y, line)
        y -= 14
        if y < 40:
            c.showPage()
            y = height - 40
    c.save()

def run_summarizer(video_path):
    audio_path = extract_audio(video_path)
    result = whisper_model.transcribe(audio_path)
    transcript_text = result['text']

    # Short summary from transcript (2–3 lines)
    try:
        short_summary = summarizer(transcript_text[:1024], max_length=60, min_length=25, do_sample=False)[0]['summary_text']
    except Exception as e:
        short_summary = "Summary generation failed."

    frames = extract_keyframes(video_path)
    captions = [caption_image(frame) for frame in frames]
    visual_summary = "\n".join([f"{i+1}. {cap}" for i, cap in enumerate(captions)])

    # Combine for PDF
    combined_text = f"""VIDEO SUMMARY (Text):\n{short_summary}\n\nVISUAL SUMMARY:\n{visual_summary}"""
    save_to_pdf(combined_text)

    return {
        "summary": short_summary,
        "transcript": transcript_text,
        "visual_summary": visual_summary,
        "pdf_file": os.path.join(os.path.dirname(__file__), "video_summary.pdf")
    }

# import os
# import whisper
# import moviepy.editor as mp
# import cv2
# from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration
# import torch
# from textwrap import wrap
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# device = "cuda" if torch.cuda.is_available() else "cpu"

# # Load models only once
# whisper_model = whisper.load_model("base")
# blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

# def extract_audio(video_path, audio_path="temp_audio.mp3"):
#     video = mp.VideoFileClip(video_path)
#     video.audio.write_audiofile(audio_path)
#     return audio_path

# def extract_keyframes(video_path, interval=5):
#     cap = cv2.VideoCapture(video_path)
#     frames = []
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     count = 0
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret: break
#         if count % (fps * interval) == 0:
#             frames.append(frame)
#         count += 1
#     cap.release()
#     return frames

# def caption_image(image_np):
#     image_pil = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
#     inputs = blip_processor(image_pil, return_tensors="pt").to(device)
#     out = blip_model.generate(**inputs)
#     caption = blip_processor.decode(out[0], skip_special_tokens=True)
#     return caption

# def save_to_pdf(text, filename="video_summary.pdf"):
#     filename = os.path.join(os.path.dirname(__file__), filename)
#     c = canvas.Canvas(filename, pagesize=letter)

#     width, height = letter
#     y = height - 40
#     for line in wrap(text, 100):
#         c.drawString(40, y, line)
#         y -= 14
#         if y < 40:
#             c.showPage()
#             y = height - 40
#     c.save()

# def run_summarizer(video_path):
#     audio_path = extract_audio(video_path)
#     result = whisper_model.transcribe(audio_path)
#     transcript_text = result['text']

#     frames = extract_keyframes(video_path)
#     captions = [caption_image(frame) for frame in frames]
#     visual_summary = "\n".join([f"{i+1}. {cap}" for i, cap in enumerate(captions)])

#     # Combine for PDF
#     combined_text = f"""TRANSCRIPT:\n{transcript_text[:1500]}\n\nVISUAL SUMMARY:\n{visual_summary}"""
#     save_to_pdf(combined_text)

#     return {
#     "transcript": transcript_text,
#     "visual_summary": visual_summary,
#     "pdf_file": os.path.join(os.path.dirname(__file__), "video_summary.pdf")
#     }



# # -*- coding: utf-8 -*-
# """summarizer

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1Js9As_ASYO9rl6ThzVBQ2021FuyCPjDZ
# """

# !pip install yt-dlp whisper openai reportlab

# !pip install openai whisper transformers torch torchvision timm opencv-python reportlab pytorch-lightning -q
# !sudo apt install -y ffmpeg

# from google.colab import files
# uploaded = files.upload()

# import os
# video_path = list(uploaded.keys())[0]
# print(f"Uploaded: {video_path}")

# !pip install git+https://github.com/openai/whisper.git
# !sudo apt install -y ffmpeg

# import whisper
# import moviepy.editor as mp

# def extract_audio(video_path, audio_path="temp_audio.mp3"):
#     video = mp.VideoFileClip(video_path)
#     video.audio.write_audiofile(audio_path)
#     return audio_path

# audio_path = extract_audio(video_path)

# # This line should now work after a correct installation
# model = whisper.load_model("base")
# result = model.transcribe(audio_path)
# transcript_text = result['text']

# print("Transcription complete (first 500 chars):")
# print(transcript_text[:500])

# # Extract Keyframes (Simple Sampling)
# import cv2

# def extract_keyframes(video_path, interval=5):
#     cap = cv2.VideoCapture(video_path)
#     frames = []
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

#     count = 0
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret: break
#         if count % (fps * interval) == 0:
#             frames.append(frame)
#         count += 1
#     cap.release()
#     return frames

# frames = extract_keyframes(video_path, interval=5)
# print(f"Extracted {len(frames)} keyframes.")

# # BLIP: Caption Keyframes (Visual Summary)
# from PIL import Image
# from transformers import BlipProcessor, BlipForConditionalGeneration
# import torch

# device = "cuda" if torch.cuda.is_available() else "cpu"

# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

# def caption_image(image_np):
#     image_pil = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))
#     inputs = processor(image_pil, return_tensors="pt").to(device)
#     out = blip_model.generate(**inputs)
#     caption = processor.decode(out[0], skip_special_tokens=True)
#     return caption

# captions = [caption_image(frame) for frame in frames]
# visual_summary = "\n".join([f"{i+1}. {cap}" for i, cap in enumerate(captions)])

# print("📸 Image Summary:")
# print(visual_summary)

# # Combine & Summarize into PDF
# from textwrap import wrap
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# combined_text = f"""TRANSCRIPT:\n{transcript_text[:1500]}\n\nVISUAL SUMMARY:\n{visual_summary}"""

# def save_to_pdf(text, filename="video_summary.pdf"):
#     c = canvas.Canvas(filename, pagesize=letter)
#     width, height = letter
#     y = height - 40
#     for line in wrap(text, 100):
#         c.drawString(40, y, line)
#         y -= 14
#         if y < 40:
#             c.showPage()
#             y = height - 40
#     c.save()

# save_to_pdf(combined_text)
# print("PDF generated: video_summary.pdf")

# # Download PDF
# from google.colab import files
# files.download("video_summary.pdf")

