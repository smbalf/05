import os
import xml.etree.ElementTree as ET


positive_image_dir = "training_images/positive/"
negative_image_dir = "training_images/negative/"
xml_dir = "xml/"

def write_image_paths(img_dir, txt_file):
    image_paths = []
    for filename in os.listdir(img_dir):
        if filename.endswith(".png"):
            image_paths.append(os.path.join(img_dir, filename))

    print(image_paths)
    with open(txt_file, "w+") as f:
        for path in image_paths:
            f.write(path + "\n")

# write_image_paths(negative_image_dir, "negatives.txt")

positive_image_paths = []


# THIS CAN BE CLEANED UP TO REMOVE [](),
def write_positives_bbox(img_dir, xml_dir, txt_file):
    for filename in os.listdir(xml_dir):
        if filename.endswith(".xml"):
            xml_path = os.path.join(xml_dir, filename)
            tree = ET.parse(xml_path)
            root = tree.getroot()
            bboxes = []

            for obj in root.iter("object"):
                xmlbox = obj.find('bndbox')
                xmin = int(xmlbox.find('xmin').text)
                ymin = int(xmlbox.find('ymin').text)
                xmax = int(xmlbox.find('xmax').text)
                ymax = int(xmlbox.find('ymax').text)
                bboxes.append((xmin, ymin, xmax-xmin, ymax-ymin))

            filename = root.find("filename").text
            line = f"{img_dir}{filename} {len(bboxes)} {bboxes}\n"

            with open(txt_file, "a") as f:
                f.write(line)

write_positives_bbox(positive_image_dir, xml_dir, "positives.txt")