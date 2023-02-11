Image Generation Script
=======================

This script takes an image file as input and generates a series of modified images based on a provided configuration file. The modifications include writing a number to the image and resizing it. The output images are saved as PNG files.

Requirements
------------

-   Python 3.x
-   PIL (Pillow)
-   PyYAML

Usage
-----

To run the script, you need to provide the path to a configuration file via the `--config` argument. The configuration file should be in YAML format and contain the following information:

-   `orig_file`: the path to the original image file
-   `output_dir`: the directory where the output images will be saved
-   `font`: information about the font to be used for writing the number on the image
    -   `name`: the path to the font file
    -   `size`: the size of the font in pixels
    -   `color`: the RGB color of the font
-   `coords`: the coordinates on the image where the number will be written
    -   `x2`: the x-coordinate for numbers with 2 digits
    -   `x3`: the x-coordinate for numbers with 3 digits
    -   `y`: the y-coordinate
-   `start_range` (optional): the starting number in the range of numbers to be written on the image. Default is 0.
-   `end_range` (optional): the ending number in the range of numbers to be written on the image. Default is 1000.

Here is an example configuration file:


```
orig_file: original.jpg
output_dir: output
font:
  name: font.ttf
  size: 24
  color:
    r: 0
    g: 0
    b: 0
coords:
  x2: 100
  x3: 90
  y: 50
start_range: 0
end_range: 10
```

To run the script, execute the following command:

`python thumbnailgenerator.py --config <config_file_path>`

The script will generate a series of images with numbers written on them and save them in the specified output directory. The names of the output images will be in the format `thumbnail<number>.png`.