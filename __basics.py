from PIL import Image, ImageFont, ImageDraw
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("orig_file", type=str, help="original file")
parser.add_argument("output_dir", type=str, help="output directory")
parser.add_argument("end_range", type=int, help="output directory")

args = parser.parse_args()


font1 = ImageFont.truetype("/usr/share/fonts/truetype/tlwg/Loma-Oblique.ttf", 300)
baseImg = Image.open(args.orig_file)
for i in range(1, args.end_range + 1):
    img = baseImg.copy()
    imgDraw = ImageDraw.Draw(img)
    if len(str(i)) <= 2:
        imgDraw.text((90,400), str(i).rjust(2, '0'), (180, 190, 40), font1)
    elif len(str(i)) == 3:
        imgDraw.text((15,400), str(i), (180, 190, 40), font1)

    img.save(f"{args.output_dir}/thumbnail{i}.png")


