import argparse
from PIL import Image
import numpy as np


def filter(image_path_in, image_path_out):
    image = Image.open(image_path_in).convert('L')
    image.save(image_path_out + "gray.jpg")
    data = np.array(image)
    
    # make borders
    data_bordered = data

    # append first and last row to the begin and to the end of data array
    data_bordered = np.append([data[0]], data_bordered, axis=0)
    data_bordered = np.append(data_bordered, [data[-1]], axis=0)
    # append left and right column
    left_column = []

    for i in range(data_bordered.shape[0]):
        left_column.append([data_bordered[i][0]])

    np_left = np.array(left_column)

    right_column = []

    for i in range(data_bordered.shape[0]):
        right_column.append([data_bordered[i][-1]])

    np_right = np.array(right_column)

    
    data_bordered = np.append(np_left, data_bordered, axis=1)
    data_bordered = np.append(data_bordered, np_right, axis=1)
    
    width = data_bordered.shape[1] 
    height = data_bordered.shape[0]
    
    data_filtered = np.zeros(data.shape, dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            if x > 0 and y > 0 and x < width - 1 and y < height - 1:
                z1 = data_bordered[y - 1][x - 1]
                z2 = data_bordered[y - 1][x]
                z3 = data_bordered[y - 1][x + 1]

                z4 = data_bordered[y][x - 1]
                z5 = data_bordered[y][x]
                z6 = data_bordered[y][x + 1]

                z7 = data_bordered[y + 1][x - 1]
                z8 = data_bordered[y + 1][x]
                z9 = data_bordered[y + 1][x + 1]

                Gx = z7 + 2*z8 + z9 - (z1 + 2*z2 + z3)
                Gy = z3 + 2*z6 + z9 - (z1 + 2*z4 + z7)
                # Multiply by 255 to better show borders
                data_filtered[y - 1][x - 1] = np.sqrt(np.power(Gx, 2) + np.power(Gy, 2))           
    
    new_image = Image.fromarray(data_filtered)
    new_image.save(image_path_out + "filtered.jpg")
    print("SOBOL FILTERING IS DONE!")
    print("CHECK THE RESULT!")


def main():
    parser = argparse.ArgumentParser(description='Median filter')
    parser.add_argument('--input', type=str, help='Full path to unfiltered image')
    parser.add_argument('--output', type=str, help='Full path to save filtered image')

    args = parser.parse_args()
    filter(args.input, args.output)

main()
