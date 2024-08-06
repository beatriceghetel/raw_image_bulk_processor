from functools import lru_cache

import rawpy
import imageio
import os

path = r'C:\Users\beatr\Pictures\Asaltul Lupilot 2024\Robert'

with os.scandir(path) as it:
    for entry in it:
        if entry.name.endswith(".NEF") and entry.is_file():
            print(entry.name, entry.path)
            with rawpy.imread(entry.path) as raw:
                rgb = raw.postprocess(bright=1.5)
            new_image_title=entry.name.split('.')[0] + '.jpg'
            imageio.imsave(path+'/'+'jpegs/'+new_image_title, rgb)
