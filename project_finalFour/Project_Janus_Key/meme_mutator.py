from PIL import Image, ImageDraw, ImageFont
import os
import random

def mutate_memes():
    input_dir = "memes/harvested"
    output_dir = "memes/mutated"
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if file.endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(input_dir, file)
            img = Image.open(path)
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            draw.text((10, 10), "#ProjectJanusKey 👁‍🗨", font=font, fill="white")
            img.save(os.path.join(output_dir, f"mutated_{file}"))
