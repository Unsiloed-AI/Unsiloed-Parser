import os

_current_dir = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(_current_dir, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "yolov11_5_x_best.pt")

_model = None


YOLO_CLASSES = {
    "caption",
    "footnote",
    "formula",
    "list-item",
    "page-footer",
    "page-header",
    "picture",
    "section-header",
    "table",
    "text",
    "title",
}

EASY_CLASSES = {
    "caption",
    "footnote",
    "list-item",
    "page-footer",
    "page-header",
    "section-header",
    "text",
    "title",
}