from PIL import Image, ImageFont, ImageDraw
import argparse
import yaml
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--config')
    args = parser.parse_args()
    if args.config == None:
        print("required argument --config <config>")
    else:
        with open(args.config, 'r') as confhandle:
            conf_info = yaml.safe_load(confhandle)
        font1 = ImageFont.truetype(conf_info["font"]["name"], conf_info["font"]["size"])
        baseImg = Image.open(conf_info["orig_file"])
        for i in range(1, conf_info["end_range"] + 1):
            img = baseImg.copy()
            imgDraw = ImageDraw.Draw(img)
            color = (conf_info["font"]["color"]["r"], conf_info["font"]["color"]["g"], conf_info["font"]["color"]["b"])
            if len(str(i)) <= 2:
                imgDraw.text((conf_info["coords"]["x2"], conf_info["coords"]["y"]), str(i).rjust(2, '0'), color, font1)
            elif len(str(i)) == 3:
                imgDraw.text((conf_info["coords"]["x3"], conf_info["coords"]["y"]), str(i), color, font1)

            img.save(f"{conf_info['output_dir']}/thumbnail{i}.png")


