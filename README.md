# Face Detection Using Computer Vision: A Human-Centric Research Perspective

## Tools and Tech Used
- Python
- OpenCV
- TensorFlow Lite
- MobileNetV2 SSD
- Raspberry Pi 4 (compatible)
- WIDER FACE + Indian dataset

## Project Overview
This project implements a robust face detection system using MobileNetV2 SSD (TensorFlow Lite) and OpenCV. It includes preprocessing steps (CLAHE, adaptive YCbCr, histogram matching) to improve accuracy in challenging conditions (low light, skin tone confusion, side profiles). The code is compatible with Raspberry Pi 4 and can be run on any PC.

## Results (Expected)
- Improved accuracy (90-95%) even in dim lighting
- Detection time < 1.5 seconds per frame
- Reduced false positives from skin-like backgrounds

## Challenges and Solutions
| Challenge            | Solution                        |
|---------------------|---------------------------------|
| Low-light detection | CLAHE + preprocessing           |
| Side profile faces  | MobileNet SSD                   |
| Skin tone confusion | Adaptive YCbCr + histogram matching |
| Hardware limits     | TensorFlow Lite deployment       |

## Future Work
- Integrate emotion detection
- Mask detection
- Real-time Android app
- Privacy-first design

## References
1. Inseong Kim et al., "Face Detection," EE368 Stanford Project Report, 2003
2. Prof. Anup Bhange et al., "Face Detection System with Face Recognition," IJRASET, 2022
3. https://www.pyimagesearch.com/
4. https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b
5. https://github.com/opencv/opencv

## How to Run
1. Install dependencies:
   ```bash
   pip install opencv-python numpy tensorflow tensorflow-lite
   ```
2. Download the MobileNetV2 SSD TensorFlow Lite model and label file.
3. Place your test images or video in the `data/` folder.
4. Run the main script:
   ```bash
   python detect_faces.py --image data/test.jpg
   ```
   or for video:
   ```bash
   python detect_faces.py --video data/test.mp4
   ```

## Folder Structure
- `detect_faces.py`: Main detection script
- `preprocessing.py`: Preprocessing functions (CLAHE, YCbCr, histogram matching)
- `models/`: Place TensorFlow Lite model and label file here
- `data/`: Test images/videos
- `README.md`: Project documentation
