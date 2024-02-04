import os
import pickle
import re

predefined_colors = {
    "kWhite" : 0,
    "kBlack" : 1,
    "kGray" : 920,
    "kRed" : 632,
    "kGreen" : 416,
    "kBlue" : 600,
    "kYellow" : 400,
    "kMagenta" : 616,
    "kCyan" : 432,
    "kOrange" : 800,
    "kSpring" : 820,
    "kTeal" : 840,
    "kAzure" : 860,
    "kViolet" : 880,
    "kPink" : 900,
}

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