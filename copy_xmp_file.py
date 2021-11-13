from os import listdir
import shutil
import re

source_dir = "C:\\Users\\yungp_000\\OneDrive\\Pictures\\astrophotography\\20211104_aurora_home\\"
dest_dir = "C:\\Users\\yungp_000\\OneDrive\\Pictures\\astrophotography\\20211104_aurora_home\\"

files = [f for f in listdir(source_dir)]

pattern = r"^(.*)\.(.*)"
source_xmp = ""

for item in files:
    match = re.search(pattern, item)
    if match:
        if match.group(2) == "xmp":
            print("I found source xmp file {}".format(match.group(0)))
            source_xmp = match.group(0)
        if source_xmp != "" and match.group(1)+".xmp" != source_xmp:
            print("source_xmp has been found, I can start copying {} to {}.xmp".format(source_xmp, match.group(1)))
            shutil.copyfile(source_dir+"\\"+source_xmp, dest_dir+str(match.group(1)+".xmp"))


