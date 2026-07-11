from ultralytics import YOLO
import cv2


class ObjectDetector:

    def __init__(self, model_name):

        self.model = YOLO(f"models/{model_name}.pt")


    # -------------------------
    # Detect Objects in Image
    # -------------------------
    def detect_image(self, image, image_size=640, confidence=0.25):

        results = self.model.predict(
            source=image,
            imgsz=image_size,
            conf=confidence,
            verbose=False
        )

        annotated_image = results[0].plot()

        return annotated_image


    # -------------------------
    # Detect Objects in Frame
    # -------------------------
    def detect_frame(self, frame, image_size=640, confidence=0.25):

        results = self.model.predict(
            source=frame,
            imgsz=image_size,
            conf=confidence,
            verbose=False
        )

        annotated_frame = results[0].plot()

        return annotated_frame


    # -------------------------
    # Detect Objects in Video
    # -------------------------
    def detect_video(
        self,
        input_video,
        output_video,
        image_size=640,
        confidence=0.25,
    ):

        cap = cv2.VideoCapture(input_video)

        fps = cap.get(cv2.CAP_PROP_FPS)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        writer = cv2.VideoWriter(
            output_video,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height),
        )

        while True:

            success, frame = cap.read()

            if not success:
                break

            annotated = self.detect_frame(
                frame,
                image_size,
                confidence,
            )

            writer.write(annotated)

        cap.release()

        writer.release()

        return output_video