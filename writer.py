import os

positive_image_dir = "training_images/positive/"

negative_image_dir = "training_images/negative/"

def write_image_paths(img_dir, txt_file):
    image_paths = []
    for filename in os.listdir(img_dir):
        if filename.endswith(".png"):
            image_paths.append(os.path.join(img_dir, filename))

    print(image_paths)
    with open(txt_file, "w+") as f:
        for path in image_paths:
            f.write(path + "\n")

write_image_paths(positive_image_dir, "positives.txt")
write_image_paths(negative_image_dir, "negatives.txt")
