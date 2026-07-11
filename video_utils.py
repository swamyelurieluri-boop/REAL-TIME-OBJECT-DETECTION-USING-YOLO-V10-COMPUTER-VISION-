import os
import cv2
import tempfile


def get_video_info(video_path):
    """
    Returns FPS, width, height and total frames.
    """

    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()

    return fps, width, height, total_frames


def create_output_video(fps, width, height):

    if not os.path.exists("outputs/videos"):
        os.makedirs("outputs/videos")

    output_path = tempfile.mktemp(
        suffix=".mp4",
        dir="outputs/videos"
    )

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    return writer, output_path


def save_image(image, filename="detected_image.jpg"):

    if not os.path.exists("outputs/photos"):
        os.makedirs("outputs/photos")

    output_path = os.path.join(
        "outputs/photos",
        filename
    )

    cv2.imwrite(output_path, image)

    return output_path


def release_resources(cap, writer):

    if cap is not None:
        cap.release()

    if writer is not None:
        writer.release()

    cv2.destroyAllWindows()