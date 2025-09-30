# resize_images.py
import os
import logging
from pathlib import Path
from PIL import Image

# Configure logging to print to console only
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def batch_resize(src_root, dst_root, size=64):
    src_root, dst_root = Path(src_root), Path(dst_root)
    logger.info(f"Starting batch resize from {src_root} to {dst_root} with size {size}x{size}")
    dst_root.mkdir(parents=True, exist_ok=True)

    total_processed = 0
    total_skipped = 0

    for split in ["train", "valid", "test"]:
        logger.info(f"Processing {split} split...")
        for cls in ["Parasitized", "Uninfected"]:
            outdir = dst_root / split / cls
            outdir.mkdir(parents=True, exist_ok=True)

            files = list((src_root / split / cls).glob("*.*"))
            logger.info(f"Found {len(files)} images in {split}/{cls}")
            
            for p in files:
                try:
                    im = Image.open(p).convert("RGB")
                    im = im.resize((size, size), resample=Image.BILINEAR)
                    im.save(outdir / p.name, quality=95, optimize=True)
                    total_processed += 1
                    if total_processed % 100 == 0:  # Log progress every 100 images
                        logger.info(f"Processed {total_processed} images so far...")
                except Exception as e:
                    logger.error(f"Skipping {p}: {e}")
                    total_skipped += 1
    
    logger.info(f"Batch resize completed! Processed: {total_processed}, Skipped: {total_skipped}")

if __name__ == "__main__":
    batch_resize("malaria_splits", "malaria_resized", size=64)