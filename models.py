from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from settings import *
from perlin_noise import PerlinNoise
from numpy import floor
from ursina.shaders import basic_lighting_shader, lit_with_shadows_shader

class Tree(Button):
    def __init__(self, pos, **kwargs):
        super().__init__(parent=scene,
                        color= color.color(0,0,random.uniform(0.9, 1)),
                        highlight_color=color.gray,
                        model = 'minecraft_tree\scene.gltf',
                        position= pos,
                        scale=5,
                        collider='box',
                        origin_y=-.5,
                        shader =basic_lighting_shader,
                        **kwargs)
class Flower(Button):
    def __init__(self, pos, **kwargs):
        super().__init__(parent=scene,
                        color= color.color(0,0,random.uniform(0.9, 1)),
                        highlight_color=color.gray,
                        model = 'minecraft_poppy_flower\scene.gltf',
                        position= pos,
                        scale=1,
                        collider='box',
                        origin_y=-.5,
                        shader =basic_lighting_shader,
                        **kwargs)    

class Block(Button):
    cur_block = 1
    def __init__(self, pos, texture_id = 1, **kwargs):
        super().__init__(parent=scene,
                        color= color.color(0,0,random.uniform(0.9, 1)),
                        highlight_color=color.gray,
                        model = 'cube',
                        texture=block_textures[texture_id],
                        position= pos,
                        scale=1,
                        collider='box',
                        origin_y=-.5,
                        shader =basic_lighting_shader,
                        **kwargs)

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.armblock = Entity(model = 'cube',
                        texture=block_textures[Block.cur_block],
                        parent = camera.ui,
                        position = (0.6, -0.4),
                        rotation = Vec3(10,-30,10),
                        shader =basic_lighting_shader,
                        scale = 0.2
                        
                        )

    def input(self, key):
        super().input(key)
        if key=='left mouse down' and mouse.hovered_entity:
            destroy(mouse.hovered_entity)
        if key=='right mouse down' and mouse.hovered_entity:
            hitinfo = raycast(camera.world_position, camera.forward, distance=15)
            if hitinfo.hit and isinstance(hitinfo.entity, Block):
                Block(hitinfo.entity.position + hitinfo.normal, Block.cur_block)
        
        if key=="scroll up":
            Block.cur_block += 1
            if Block.cur_block >= len(block_textures):
                Block.cur_block = 0
            self.armblock.texture = block_textures[Block.cur_block]
        if key=='scroll down':
            Block.cur_block -= 1
            if Block.cur_block < 0:
                Block.cur_block = len(block_textures) - 1
            self.armblock.texture = block_textures[Block.cur_block]
            




class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=None, collider=None, **kwargs)
        self.blocks = {}
        self.noise = PerlinNoise(octaves=2, seed=3505)
    def generate(self):
        for x in range(MAP_SIZE):
            for z in range(MAP_SIZE):
                y = floor(self.noise([x/24, z/24])*6)
                cube = Block((x,y, z), 1)

                rand_num = random.randint(1, TREE_DENSITY)
                if rand_num == 40:
                    Tree((x,y-3.65,z))
                rand_num1 = random.randint(1, FLOWER_DENSITY)
                if rand_num1 == 20:
                    Flower((x,y+0.5,z))


