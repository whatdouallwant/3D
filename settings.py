import os
from ursina import load_texture

block_textures = []
TREE_DENSITY = 80
BASE_DIR = os.getcwd()
MAP_SIZE = 40
FLOWER_DENSITY = 20
BLOCKS_DIR = os.path.join(BASE_DIR, 'blockss/minecraft')
file_list = os.listdir(BLOCKS_DIR)

for image in file_list:
    texture = load_texture('blockss/minecraft' + os.sep + image)
    block_textures.append(texture)