Here’s documentation for the script that extracts frames from every video in a folder and saves them in organized subfolders:

---

# 📄 Video Frame Extractor - Python Script Documentation

## 📝 Description

This Python script reads all video files from a specified folder, extracts each frame from every video, and saves the frames as `.jpg` images in corresponding subdirectories under a common `frames/` output directory. Each video gets its own folder named after the video file (without the extension).

Useful for:
- Preprocessing data for computer vision tasks
- Creating image datasets from video sources
- Manual frame-by-frame video inspection

---

## 📁 Folder Structure

```
project/
├── video_frame_extractor.py     # <--- This script
├── videos/                      # <--- Input folder (place your videos here)
│   ├── video1.mp4
│   ├── video2.avi
│   └── ...
└── frames/                      # <--- Output folder (created automatically)
    ├── video1/
    │   ├── frame_0000.jpg
    │   └── ...
    └── video2/
        ├── frame_0000.jpg
        └── ...
```

---

## 🔧 Requirements

- Python 3.x
- OpenCV library (`cv2`)

### Installation
```bash
pip install opencv-python
```

---

## 🚀 How It Works

1. **Specify Input and Output Folders**:
   - `video_folder`: where your video files are stored
   - `output_root`: where extracted frames will be saved

2. **Collect All Video Files**:
   - Looks for files with video extensions: `.mp4`, `.avi`, `.mov`, `.mkv`.

3. **For Each Video**:
   - Opens the video using OpenCV
   - Creates a subfolder in `frames/` named after the video
   - Reads frames one by one and saves each as a `.jpg`

4. **Output**:
   - Frames are saved with names like `frame_0000.jpg`, `frame_0001.jpg`, etc.

---

## 🧠 Key Functions and Features

- `os.listdir()` — Gets all filenames in the `videos/` folder.
- `cv2.VideoCapture()` — Opens each video for frame reading.
- `cap.read()` — Grabs frames until the video ends.
- `cv2.imwrite()` — Saves each frame as an image.
- `os.makedirs()` — Creates directories if they don’t already exist.

---

## 📌 Notes

- The script processes all video formats listed in the extension check.
- Frames are saved in JPEG format with zero-padded numbers for ordering.
- If a video cannot be opened, it will print an error and skip it.

---

## ✅ Example Usage

```bash
python video_frame_extractor.py
```

Make sure your `videos/` folder is in the same directory or update the `video_folder` variable with the correct path.

---

Let me know if you’d like a command-line version or to extend it with Nth-frame extraction, resizing, or grayscale conversion!