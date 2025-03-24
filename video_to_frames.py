import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread

def extract_frames(video_path, output_folder, frame_interval):
    """
    Extracts frames from a video file and saves them as images.
    
    Parameters:
        video_path (str): Path to the input video file.
        output_folder (str): Folder where extracted frames will be saved.
        frame_interval (int): Extract every 'frame_interval' frames.
    """
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        messagebox.showerror("Error", f"Could not open video: {video_path}")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0
    saved_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frames += 1
            status_label.config(text=f"Processing... Saved {saved_frames} frames")
            root.update_idletasks()

        frame_count += 1

    cap.release()
    messagebox.showinfo("Completed", f"Extraction done! Total frames saved: {saved_frames}")
    status_label.config(text="Extraction Completed")

def browse_video():
    """Open a file dialog to select a video file."""
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov;*.mkv")])
    if file_path:
        video_entry.delete(0, tk.END)
        video_entry.insert(0, file_path)

def browse_output_folder():
    """Open a file dialog to select an output directory."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder_path)

def start_extraction():
    """Start the frame extraction process in a separate thread."""
    video_path = video_entry.get()
    output_folder = output_entry.get()
    try:
        frame_interval = int(frame_interval_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for frame interval.")
        return

    if not video_path or not os.path.exists(video_path):
        messagebox.showerror("Error", "Please select a valid video file.")
        return
    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder.")
        return

    status_label.config(text="Processing...")
    Thread(target=extract_frames, args=(video_path, output_folder, frame_interval), daemon=True).start()

# GUI Setup
root = tk.Tk()
root.title("Video to Frames Extractor")
root.geometry("500x300")

# Video File Selection
tk.Label(root, text="Select Video File:").pack()
video_entry = tk.Entry(root, width=50)
video_entry.pack()
tk.Button(root, text="Browse", command=browse_video).pack()

# Output Folder Selection
tk.Label(root, text="Select Output Folder:").pack()
output_entry = tk.Entry(root, width=50)
output_entry.pack()
tk.Button(root, text="Browse", command=browse_output_folder).pack()

# Frame Interval Selection
tk.Label(root, text="Frame Extraction Interval:").pack()
frame_interval_entry = tk.Entry(root, width=10)
frame_interval_entry.insert(0, "10")
frame_interval_entry.pack()

# Start Button
tk.Button(root, text="Start Extraction", command=start_extraction, bg="green", fg="white").pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Waiting for input...", fg="blue")
status_label.pack()

# Run GUI
root.mainloop()
