import pickle

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

with open("ROOTColorDB.p", "rb") as file:
    color_hex_dict = pickle.load(file)

def get_hex_color(ROOT_color_idx):
    return color_hex_dict[ROOT_color_idx]