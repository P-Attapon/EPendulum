from moviepy import ImageSequenceClip
import glob
import re

def numerical_sort(value):
    return [int(s) if s.isdigit() else s for s in re.split('([0-9]+)', value)]

def make_video(frame_folder, save_name, fps=1000):  # Set FPS here
    frames = []
    for image_path in sorted(glob.glob(f"{frame_folder}/*.PNG"), key=numerical_sort):
        frames.append(image_path)

    # Create video using moviepy with specified frame rate (fps)
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(save_name, codec="libx264")

# Paths
E0_path = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\E0"
saveE0 = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\GIF_result\E0.mp4"

# E10_path = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\E10"
# saveE10 = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\GIF_result\E10.mp4"
# EP_path = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\EPerturb"
# saveEP = r"C:\Users\Salay\PycharmProjects\PythonProject\pendulum_result\GIF_result\EP.mp4"

# Create video files with very high FPS
# make_video(E10_path, saveE10, fps=120)  # 10,000 FPS for video
# make_video(EP_path, saveEP, fps=120)
make_video(E0_path, saveE0, fps=120)

