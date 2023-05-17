import os
import sys
import string
from PIL import Image
from PIL import ImageDraw, ImageFont
from pdf2image import convert_from_path
#import cairosvg
from datetime import datetime
import argparse
from html import escape

def find_images(folder_path):
    images = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.pdf', '.png', '.jpg', '.svg')):
                images.append(os.path.join(root, file))
    return images

def convert_image(image_path, whole_width):
    if image_path.endswith('.pdf'):
        images = convert_from_path(image_path)
    else:
        image = Image.open(image_path)
        images = [image]

    processed_images = []
    for image in images:
        target_width = int(whole_width // 2.4)
        target_height = int(image.height * target_width // image.width)
        new_size = (target_width, target_height)
        image = image.resize(new_size)
        processed_images.append(image)

    return processed_images

def add_watermark(image, image_name, date):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text1 = 'wanglab'
    text2 = image_name
    text3 = date.strftime('%Y-%m-%d')
    text_width1, text_height1 = draw.textbbox((0, 0), text1, font)[2:]
    text_width2, text_height2 = draw.textbbox((0, 0), text2, font)[2:]
    text_width3, text_height3 = draw.textbbox((0, 0), text3, font)[2:]
    max_text_width = max(text_width1, text_width2, text_width3)
    x1 = (image.width - max_text_width) // 2
    y1 = (image.height - text_height1 * 3) // 2
    x2 = (image.width - max_text_width) // 2
    y2 = y1 + text_height1
    x3 = (image.width - max_text_width) // 2
    y3 = y2 + text_height2
    #draw.rectangle([x1 - 10, y1 - 10, x1 + max_text_width + 10, y3 + text_height3 + 10], fill=(211, 211, 211))
    draw.text((x1, y1), text1, fill=(211, 211, 211, 37), font=font)
    draw.text((x2, y2), text2, fill=(211, 211, 211, 37), font=font)
    draw.text((x3, y3), text3, fill=(211, 211, 21, 37), font=font)
    return image

def images_to_div(processed_images,output_folder,image_names):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_path = os.path.join(output_folder,"px_images")
    os.makedirs(image_path)
    div = "<div class='pictures'><div class='row'><div id='left' class='left'></div><div id='right' class='right'></div></div></div>"
    left_column = ""
    right_column = ""
    left_height = 0
    right_height = 0
    index = 1
    left_index = 1
    right_index = 1
    for i, image in enumerate(processed_images[:260]):
        image_name = image_names[i]
        new_image_name = "image_" + str(i) + ".png"
        new_image_path = os.path.join(image_path, new_image_name)
        image.save(new_image_path)
        label1 = string.ascii_uppercase[(index - 1) // 10]
        if left_height <= right_height:
            label2 = "L"
            label3 = left_index
            left_index += 1
            left_column += f"<img src='{os.path.join('.', 'px_images', new_image_name)}'/><p>{label1}_{label2}_{label3}: {image_name}</p>"
            left_height += image.height
        else:
            label2 = "R"
            label3 = right_index
            right_index += 1
            right_column += f"<img src='{os.path.join('.', 'px_images', new_image_name)}'/><p>{label1}_{label2}_{label3}: {image_name}</p>"
            right_height += image.height
        index += 1

    if len(processed_images) > 260:
        warning = "<p style='color:red'>Warning: Too many pictures to read! Just represent top 260 pictures.</p>"
        left_column += warning
        right_column += warning

    div = div.replace("<div id='left' class='left'></div>", f"<div id='left' class='left'>{left_column}</div>")
    div = div.replace("<div id='right' class='right'></div>", f"<div id='right' class='right'>{right_column}</div>")
    return div




def process_images(processed_images, output_folder, image_names):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    image_path = os.path.join(output_folder,"px_images")
    os.makedirs(image_path)
    html = "<html><head><style>.left {float: left;width: 45%;padding: 5px;} .right {float: right;width: 45%;padding: 5px;} p {word-wrap: break-word;}</style></head><body><div class='row'><div id='left' class='left'></div><div id='right' class='right'></div></div></body></html>"
    left_column = ""
    right_column = ""
    left_height = 0
    right_height = 0
    index = 1
    left_index = 1
    right_index = 1
    for i, image in enumerate(processed_images[:260]):
        image_name = image_names[i]
        new_image_name = "image_" + str(i) + ".png"
        new_image_path = os.path.join(image_path, new_image_name)
        image.save(new_image_path)
        label1 = string.ascii_uppercase[(index - 1) // 10]
        if left_height <= right_height:
            label2 = "L"
            label3 = left_index
            left_index += 1
            left_column += f"<img src='{new_image_path}'/><p>{label1}_{label2}_{label3}: {image_name}</p>"
            left_height += image.height
        else:
            label2 = "R"
            label3 = right_index
            right_index += 1
            right_column += f"<img src='{new_image_path}'/><p>{label1}_{label2}_{label3}: {image_name}</p>"
            right_height += image.height
        index += 1

    if len(processed_images) > 260:
        warning = "<p style='color:red'>Warning: Too many pictures to read! Just represent top 260 pictures.</p >"
        left_column += warning
        right_column += warning

    html = html.replace("<div id='left' class='left'></div>", f"<div id='left' class='left'>{left_column}</div>")
    html = html.replace("<div id='right' class='right'></div>", f"<div id='right' class='right'>{right_column}</div>")
    with open(os.path.join(output_folder, "px_pictures.html"), "w") as f:
        f.write(html)

def main():
    parser = argparse.ArgumentParser(description='Get script info')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing scripts')
    parser.add_argument('output', type=str, help='Dir to the output HTML file')
    args = parser.parse_args()
    image_paths = find_images(args.folder_path)
    whole_width = 800
    processed_images = []
    image_name_list = []
    for image_path in image_paths:
        images = convert_image(image_path, whole_width)
        for image in images:
            image_name = os.path.basename(image_path)
            image_name_list.append(image_name)
            date = datetime.now().date()
            image = add_watermark(image, image_name, date)
            processed_images.append(image)

    output_folder = args.output
    process_images(processed_images, output_folder, image_name_list)

if __name__ == '__main__':
    main()