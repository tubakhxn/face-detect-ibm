import cv2
import argparse
from preprocessing import preprocess_image

def detect_faces(image):
    img = preprocess_image(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return faces, img

def draw_faces(img, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return img

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help='Path to image file')
    parser.add_argument('--video', type=str, help='Path to video file')
    parser.add_argument('--webcam', action='store_true', help='Use webcam for real-time detection')
    args = parser.parse_args()

    if args.image:
        image = cv2.imread(args.image)
        faces, img = detect_faces(image)
        img = draw_faces(img, faces)
        cv2.imshow('Face Detection', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif args.video:
        cap = cv2.VideoCapture(args.video)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            faces, img = detect_faces(frame)
            img = draw_faces(img, faces)
            cv2.imshow('Face Detection', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    elif args.webcam:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            faces, img = detect_faces(frame)
            img = draw_faces(img, faces)
            cv2.imshow('Face Detection - Webcam', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print('Please provide --image, --video, or --webcam argument.')

if __name__ == '__main__':
    main()
