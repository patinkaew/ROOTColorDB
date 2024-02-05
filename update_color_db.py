import sys
import ROOT
import json
import pickle

ROOT.gInterpreter.Declare("""
                          int numberOfColors(){
                              TObjArray *colors = (TObjArray *)(gROOT -> GetListOfColors());
                              return colors->GetSize();}
                          """)

ROOT.gInterpreter.Declare("""
                          std::string colorIndex2Hex(int ci){
                              TObjArray *colors = (TObjArray *)(gROOT -> GetListOfColors());
                              TColor *col = (TColor *)(colors -> At(ci));
                              if(col){return std::string(col -> AsHexString());}else{return "";} }
                          """)

if __name__ == "__main__":
    num_colors = ROOT.numberOfColors()
    
    with open("ROOTPredefinedColor.json", "r") as file:
        predefined_colors = json.load(file)
        
    color_hex_dict = dict()
    
    for color_name, color_idx in predefined_colors.items():
        color_hex_dict[color_name] = ROOT.colorIndex2Hex(color_idx)
    
    for color_idx in range(num_colors):
        hex_code = ROOT.colorIndex2Hex(color_idx)
        if hex_code != "":
            color_hex_dict[color_idx] = hex_code
    
    if len(sys.argv) > 1 and sys.argv[1] == "json":
        with open('ROOTColorDB.json', 'w') as file:
            json.dump(color_hex_dict, file, indent=4)
    elif len(sys.argv) > 1 and sys.argv[1] == "pickle":
        with open("ROOTColorDB.p", "wb") as file:
            pickle.dump(color_hex_dict, file, protocol=pickle.HIGHEST_PROTOCOL)
    else:
        with open('ROOTColorDB.json', 'w') as file:
            json.dump(color_hex_dict, file, indent=4)
        with open("ROOTColorDB.p", "wb") as file:
            pickle.dump(color_hex_dict, file, protocol=pickle.HIGHEST_PROTOCOL)