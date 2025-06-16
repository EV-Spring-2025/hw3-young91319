import cv2
import numpy as np
import torch

def calculate_psnr(img1, img2):
    mse = np.mean((img1.astype(np.float32) - img2.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def compute_video_psnr(video_path_1, video_path_2):
    cap1 = cv2.VideoCapture(video_path_1)
    cap2 = cv2.VideoCapture(video_path_2)

    psnrs = []
    frame_idx = 0

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break

        if frame1.shape != frame2.shape:
            raise ValueError("Frame size mismatch")

        psnr = calculate_psnr(frame1, frame2)
        psnrs.append(psnr)
        frame_idx += 1

    cap1.release()
    cap2.release()

    print(f"Computed PSNR for {frame_idx} frames.")
    print(f"Average PSNR: {np.mean(psnrs):.2f} dB")
    return psnrs

# Example usage
video1 = "/tmp2/young91319/EV/hw3-young91319/PhysGaussian/output_jelly/output.mp4"
video2 = "/tmp2/young91319/EV/hw3-young91319/PhysGaussian/output_jelly_softening1.0/output.mp4"
compute_video_psnr(video1, video2)
