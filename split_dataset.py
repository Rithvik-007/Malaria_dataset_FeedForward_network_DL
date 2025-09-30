# split_dataset.py
import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split

def make_split(src_root, dst_root, seed=42):
    src = Path(src_root)  # should contain Parasitized/ and Uninfected/
    dst = Path(dst_root)
    assert (src / "Parasitized").exists() and (src / "Uninfected").exists(), \
        f"Expected {src}/Parasitized and {src}/Uninfected"

    for split in ["train","valid","test"]:
        for cls in ["Parasitized","Uninfected"]:
            (dst / split / cls).mkdir(parents=True, exist_ok=True)

    # Collect files and labels
    files, labels = [], []
    for cls in ["Parasitized","Uninfected"]:
        for p in (src / cls).glob("*.*"):
            files.append(p)
            labels.append(cls)

    # 70/30 first, then split that 30 into 15/15
    X_train, X_tmp, y_train, y_tmp = train_test_split(
        files, labels, test_size=0.30, random_state=seed, stratify=labels
    )
    X_valid, X_test, y_valid, y_test = train_test_split(
        X_tmp, y_tmp, test_size=0.50, random_state=seed, stratify=y_tmp
    )

    def copy_to(items, labels, split):
        for p, lab in zip(items, labels):
            dest = dst / split / lab / p.name
            shutil.copy2(p, dest)

    copy_to(X_train, y_train, "train")
    copy_to(X_valid, y_valid, "valid")
    copy_to(X_test,  y_test,  "test")

if __name__ == "__main__":
    # EDIT these for your machine:
    RAW = r"D:\GMU Courses\Sem-3\DL\Assignments\Malaria_dataset\archive\cell_images\cell_images"
    OUT = r"D:\GMU Courses\Sem-3\DL\Assignments\Malaria_dataset\malaria_splits"
    make_split(RAW, OUT, seed=42)
    print("✔ Stratified splits created at:", OUT)
