
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
    
