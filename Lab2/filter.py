import argparse
from PIL import Image
import numpy as np


def get_median(window):
    r_sum = 0
    g_sum = 0
    b_sum = 0
    for i in range(len(window)):
        r_sum += window[i][0]
        g_sum += window[i][1]
        b_sum += window[i][2]
    return [r_sum / 9, g_sum / 9, b_sum / 9]


def filter(image_path_in, image_path_out):
    image = Image.open(image_path_out).convert('RGB')
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

    width = data_bordered.shape[0] 
    height = data_bordered.shape[1]

    data_filtered = np.zeros(data.shape, dtype=np.uint8)

    for i in range(width):
        for j in range(height):
            window = [ None for _ in range(9) ]
            if i > 0 and j > 0 and i < width - 1 and j < height - 1:
                window[0] = data_bordered[i - 1][j - 1]
                window[1] = data_bordered[i - 1][j]
                window[2] = data_bordered[i -1][j + 1]

                window[3] = data_bordered[i][j - 1]
                window[4] = data_bordered[i][j]
                window[5] = data_bordered[i][j + 1]

                window[6] = data_bordered[i + 1][j - 1]
                window[7] = data_bordered[i + 1][j]
                window[8] = data_bordered[i + 1][j + 1]

                data_filtered[i - 1][j - 1] = get_median(window)            
    
    new_image = Image.fromarray(data_filtered)
    new_image.save(image_path_out)
    print("MEDIAN FILTERING IS DONE!")
    print("CHECK THE RESULT!")


def main():
    parser = argparse.ArgumentParser(description='Median filter')
    parser.add_argument('--input', type=str, help='Full path to unfiltered image')
    parser.add_argument('--output', type=str, help='Full path to save filtered image')

    args = parser.parse_args()
    filter(args.input, args.ouptut)

main()
