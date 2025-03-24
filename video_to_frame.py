import cv2
import os

# Input and output paths
video_folder = 'videos'       # Folder with video files
output_root = 'frames'        # Root folder to save extracted frames
os.makedirs(output_root, exist_ok=True)

# Get all video files from the input folder
video_files = [f for f in os.listdir(video_folder) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

for video_file in video_files:
    video_path = os.path.join(video_folder, video_file)
    video_name = os.path.splitext(video_file)[0]
    output_dir = os.path.join(output_root, video_name)
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_file}")
        continue

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Extracted {frame_count} frames from '{video_file}' into '{output_dir}'")

print("All videos processed.")
