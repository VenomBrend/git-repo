from PIL import Image
import os

INPUT_FOLDER = "input files"
OUTPUT_FOLDER = "output files"
# size of new picture
WIDTH = 800
HEIGHT = 600


def main():
    if not os.path.isdir(INPUT_FOLDER):
        os.mkdir(INPUT_FOLDER)
    if not os.path.isdir(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)

    for input_file in os.listdir(INPUT_FOLDER):
        if os.path.isfile(INPUT_FOLDER + os.sep + input_file):
            try:
                new_img = Image.open(INPUT_FOLDER + os.sep + input_file).\
                    resize((WIDTH, HEIGHT))
                new_img.save(OUTPUT_FOLDER + os.sep + input_file)
            except Exception:
                pass


if __name__ == '__main__':
    main()
