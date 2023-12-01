import os
import numpy as np

current_dir = os.getcwd()
# print('current direc: ', current_dir)
Configuration = {
    'sizePlat': (416,200),
    'weightPlatDir': os.path.join(current_dir, "weights\licence_plat.pt"),
    'weightCharDir': os.path.join(current_dir, "weights\licence_character.pt"),
    'imageSample': os.path.join(current_dir, "samples\mobil_2.jpg"),
    'outputFile': os.path.join(current_dir, "runs\detect"),
    'classListCharacter': np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M',
                            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                            '0','1','2','3','4','5','6','7','8','9'])
}
