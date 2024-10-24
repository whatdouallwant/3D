from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

from settings import *
from models import Block, Map, Player

sky = Sky(image='unreal_engine_4_sky\scene.gltf')
sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(1,-1,1))
ground = Entity(model='plane', collider='box', scale=150, texture='grass', texture_scale=(4,4))
map = Map()
map.generate()
ground.y = -5
player = Player()
window.fullscreen = True
app.run()
