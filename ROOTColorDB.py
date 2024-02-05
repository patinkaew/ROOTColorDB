import os
import json
import pickle
import re

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ROOTPredefinedColor.json"), "r") as file:
    predefined_colors = json.load(file)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ROOTColorDB.p"), "rb") as file:
    color_hex_dict = pickle.load(file)

def get_ROOT_color_as_hex(ROOT_color_idx):
    def convert_to_color_idx_int(color_idx):    
        try:
            color_idx = int(color_idx)
        except:
            if color_idx in predefined_colors:
                color_idx = predefined_colors[color_idx]
        return color_idx
    
    if isinstance(ROOT_color_idx, str):
        if ROOT_color_idx in predefined_colors:
            ROOT_color_idx = predefined_colors[ROOT_color_idx]
        else: 
            ROOT_color_idx = eval("".join([str(convert_to_color_idx_int(token)) if token != "+" or token != "-" else token 
                                           for token in re.split(r"(\+|-)", ROOT_color_idx)]))
    
    return color_hex_dict[ROOT_color_idx]