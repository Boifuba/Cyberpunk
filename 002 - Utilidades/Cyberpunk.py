import json
import os
import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def convert(list, num):
    for i in list:
        print(i)
        if not("tech_level" in i):
            continue
        num += 1
        if not("value" in i):
            i["value"] = "0"
        if re.match(r'^5(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*1)
        elif re.match(r'^6(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*1)
        elif re.match(r'^7(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*1)
        elif re.match(r'^8(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*1)
        elif re.match(r'^9(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*10)
        elif re.match(r'^10(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*64)
        elif re.match(r'^11(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*128)
        elif re.match(r'^12(?!\d)',i["tech_level"]):
            i["value"] = str(float(i["value"])*256)
        if "children" in i:
            i["children"], num = convert(i["children"],num)
    return list, num


Tk().withdraw()
print("This script will convert a GCS .eqp file, editing the item costs in accordance with\nthe Equipment Cost Table in GURPS After The End 1: Wastelanders, p. 29.")
input("Press any key to select a file and continue:")
filename = askopenfilename()
f = open(filename,"r",encoding="utf-8")
j = json.load(f)
if j["type"] != "equipment_list" or j["version"] != 2:
    input("This is not a valid .eqp file. Exiting...")
else:
    print("Converting",filename)
    nj = j
    nj["rows"], num = convert(j["rows"], 0)
    new_filename = os.path.split(filename)
    name = os.path.splitext(new_filename[1])[0]+" - Converted.eqp"
    nfd = str(new_filename[0]+"/"+name)
    with open(nfd,"w",encoding="utf-8") as nf:
        json.dump(nj,nf)
    print("Converted "+str(num)+" item(s). Exported to \""+nfd+"\".")
    input("Press any key to exit...")
    