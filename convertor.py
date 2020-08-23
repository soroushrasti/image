import sys
import os
from PIL import Image
input_folder=sys.argv[1]
target_folder=sys.argv[2]
print(input_folder)
if not os.path.exists(target_folder):
    os.mkdir(target_folder)

for file in os.listdir(input_folder):
     img=Image.open('./{}/{}'.format(input_folder,file))
     img.save('./{}/{}'.format(target_folder,os.path.splitext(file)[0]+'.png'),'png')   
