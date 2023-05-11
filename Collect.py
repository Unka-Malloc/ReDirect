import os
import hashlib
import shutil

from PIL import Image

def is_pic_dir(dir_path):
    if os.path.isdir(dir_path) and os.listdir(dir_path):
        return all(fname.endswith(("jpg", "png", "webp", "json")) for fname in os.listdir(dir_path))

    return False

if __name__ == "__main__":
    sources = [
        "T:/Downloads",
        "V:/Design/Label"
    ] + [
        f"V:/FavSour/Shoes/{i}" for i in os.listdir(f"V:/FavSour/Shoes")
    ]

    destination = "T:/DesignStore"

    for src_path in sources:
        for sub_name in os.listdir(src_path):
            sub_dir = f"{src_path}/{sub_name}"
            if is_pic_dir(sub_dir):
                sub_hash = hashlib.sha256(sub_dir.encode("UTF-8")).hexdigest()

                for image_name in os.listdir(sub_dir):
                    if image_name.endswith('json'):
                        continue

                    image_path = f"{sub_dir}/{image_name}"

                    with open(image_path, "rb") as f:
                        image_hash = hashlib.sha256(f.read()).hexdigest()

                    if not os.path.exists(f"{destination}/{sub_hash}"):
                        os.makedirs(f"{destination}/{sub_hash}")

                    new_image_path = f"{destination}/{sub_hash}/{image_hash}.png"

                    if os.path.exists(new_image_path):
                        continue

                    if image_path.endswith(".png"):
                        shutil.copy(image_path, new_image_path)
                    else:
                        tmp_image = Image.open(image_path)
                        tmp_image.save(new_image_path, "PNG")
