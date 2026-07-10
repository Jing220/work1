import numpy as np
import cv2
import torch

print(f"NumPy 版本: {np.__version__}")
print(f"OpenCV 版本: {cv2.__version__}")
print(f"PyTorch 版本: {torch.__version__}")
print(f"CUDA 可用: {torch.cuda.is_available()}")