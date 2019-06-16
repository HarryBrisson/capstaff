
import cv2
import pandas as pd
import numpy as np


def get_simplified_color_distribution(frame):
    
    simplified_color_distribution = {}
    
    for row in frame:
        
        for pixel in row:
            
            simplified_color = ""
            for color in pixel:
                simplified_color += str(color*8//256)
            
            if simplified_color in simplified_color_distribution.keys():
                simplified_color_distribution[simplified_color] += 1
            else:
                simplified_color_distribution[simplified_color] = 1
                
        return simplified_color_distribution
    

def get_color_dataframe_for_video(video_file):

    cap = cv2.VideoCapture(video_file)

    color_distribution_data = []

    while True:

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            color_distribution_data += [get_simplified_color_distribution(frame)]
        else:
            break

    df = pd.DataFrame(color_distribution_data)
    
    return df


def get_three_color_gradient_list():

    two_color_gradient_list = []

    for i1 in range(8):
        seq = list(range(8))
        if i1%2 == 1:
            seq.reverse()
        for i2 in seq:
            two_color_gradient_list += [f'{i1}{i2}']

    three_color_gradient_list = []

    for i1 in range(8):
        seq = two_color_gradient_list
        if i1%2 == 1:
            seq.reverse()
        for i2 in seq:
            three_color_gradient_list += [f'{i1}{i2}']

    return three_color_gradient_list


def create_color_palette_strip_for_color_distribution(color_distribution):
    gradient = get_three_color_gradient_list()

    color_strip = []

    for c in gradient:
        if c in color_distribution.keys() and not np.isnan(color_distribution[c]):
            pixel_values = ()
            for i in range(3):
                pixel_values += (int(c[i])*32,)
            color_strip += [pixel_values]*int(color_distribution[c])

    return color_strip


def get_palette_over_time_data_for_color_df(df):

    color_data = df.to_dict(orient='records')
    palette_over_time_data = []
    i = 0
    for color_distribution in color_data:
        color_strip = create_color_palette_strip_for_color_distribution(color_distribution)
        palette_over_time_data.append(color_strip)
        i += 1
        print(f'frame {i}')

    return palette_over_time_data


def create_image_from_palette_data(data,filename):

    image = np.array(data)
    image = np.rot90(image)
    cv2.imwrite(filename,image)


def create_palette_over_time_visual(video_input,image_filename):

    df = get_color_dataframe_for_video(video_input)
    if len(df) == 0:
        print('empty dataframe')
        return
    data = get_palette_over_time_data_for_color_df(df)
    create_image_from_palette_data(data, image_filename)


