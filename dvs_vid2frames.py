import cv2
import os
import argparse
import matplotlib.pyplot as plt

def read_frame_times(frames_filename):
    frames_file = open(frames_filename, 'r')
    lines = frames_file.readlines()

    frame_times = []
    
    for line in lines:
        if not line.startswith('#'):
            frame_times.append(float(line.split()[1]))

    return frame_times

def write_frames(ip_video_path, frames_filename, op_dir):
    frame_times = read_frame_times(frames_filename)
    video_capture = cv2.VideoCapture(ip_video_path)
    
    for index, time in enumerate(frame_times):
        video_capture.set(cv2.CAP_PROP_POS_MSEC, time*1000)
        success, image = video_capture.read()
        if success:
            image = cv2.medianBlur(image, 9)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            png_filename = os.path.join(op_dir, 'dvs_' + "{:05d}".format(index) + '.png')
            plt.imsave(png_filename, image, cmap="bwr")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip_video_path', type=str, help='input video path')
    parser.add_argument('--frames_filename', type=str, help='frame times file path')
    parser.add_argument('--op_dir', type=str, help='output directory path')

    args = parser.parse_args()

    write_frames(args.ip_video_path, args.frames_filename, args.op_dir)