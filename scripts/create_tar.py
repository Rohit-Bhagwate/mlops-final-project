import tarfile
import os

model_path = "model/model.pkl"
tar_path = "model.tar.gz"

with tarfile.open(tar_path, "w:gz") as tar:
    tar.add(model_path, arcname="model.pkl")
    tar.add("inference.py", arcname="inference.py")

print("✅ model.tar.gz created")