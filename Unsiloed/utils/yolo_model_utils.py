from ultralytics import YOLO
from Unsiloed.parse_config import MODEL_PATH, MODEL_DIR, _model
import logging
import os
import shutil
from typing import List, Dict, Any
from PIL import Image

logger = logging.getLogger(__name__)


def download_model():
    """Download YOLO model from HuggingFace if not present."""
    try:
        from huggingface_hub import hf_hub_download
        
        # Create models directory if it doesn't exist
        os.makedirs(MODEL_DIR, exist_ok=True)
        
        logger.info(f"📥 Downloading YOLO model from HuggingFace (109MB)...")
        logger.info(f"This is a one-time download. Future runs will use the cached model.")
        
        # Download using huggingface_hub (most reliable method)
        downloaded_path = hf_hub_download(
            repo_id="mubashiross/Unsiloed_YOLO_MODEL",
            filename="yolo11_5_x_best.pt",
            repo_type="model",
            cache_dir=None  # Use default HF cache
        )
        
        # Copy to our models directory
        shutil.copy(downloaded_path, MODEL_PATH)
        
        logger.info(f"✅ YOLO model downloaded and cached successfully")
        logger.info(f"Model path: {MODEL_PATH}")
            
    except ImportError:
        logger.error("huggingface_hub not installed. Installing dependencies...")
        raise RuntimeError(
            "Missing dependency 'huggingface_hub'. Please run: pip install huggingface-hub"
        )
    except Exception as e:
        logger.error(f"Failed to download YOLO model: {e}")
        raise RuntimeError(
            f"Could not download YOLO model. "
            "Please download it manually from https://huggingface.co/mubashiross/Unsiloed_YOLO_MODEL "
            f"and place it at {MODEL_PATH}"
        ) from e


def get_model() -> YOLO:
    """Returns a singleton YOLO model instance with auto-download if needed."""
    global _model
    if _model is None:
        try:
            # Auto-download model if it doesn't exist
            if not os.path.exists(MODEL_PATH):
                logger.warning(f"YOLO model not found at {MODEL_PATH}")
                download_model()
            
            _model = YOLO(MODEL_PATH)
            logger.info("✅ YOLO model loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading YOLO model from {MODEL_PATH}: {e}")
            raise RuntimeError("YOLO model could not be loaded.") from e
    return _model


def run_yolo_inference(image_list: List[Image.Image]) -> List[Dict[str, Any]]:
    """
    Run YOLO inference on a list of images.
    """
    model = get_model()
    yolo_results = model(image_list)
    return yolo_results
