def on_overlap_tile(sprite, location):
    global current_level
    current_level += 1
    level_control(3)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
        """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.game_over(True)
    game.set_game_over_message(True, "GAME OVER!")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
        """),
    on_overlap_tile2)

def on_up_pressed():
    mySprite.vy = -150
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    mySprite.vy = -150
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile3(sprite3, location3):
    global current_level
    current_level += 1
    level_control(2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
        """),
    on_overlap_tile3)

def level_control(level_number: number):
    if level_number == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
            """))
    if level_number == 2:
        tiles.set_current_tilemap(tilemap("""
            level2
            """))
    if level_number == 3:
        tiles.set_current_tilemap(tilemap("""
            level3
            """))
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile2
        """))
    scene.set_background_color(8)

def on_a_pressed():
    mySprite.vy = -150
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile4(sprite4, location4):
    info.change_life_by(-1)
    game.splash("ow")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        hazardLava1
        """),
    on_overlap_tile4)

def on_left_pressed():
    mySprite.vy = -150
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    mySprite.vy = -150
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    mySprite.vy = -150
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . c c c b b b b b . . . .
        . . c c b 4 4 4 4 4 4 b b b . .
        . c c 4 4 4 4 4 5 4 4 4 4 b c .
        . e 4 4 4 4 4 4 4 4 4 5 4 4 e .
        e b 4 5 4 4 5 4 4 4 4 4 4 4 b c
        e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e
        e b b 4 4 4 4 4 4 4 4 4 4 4 b e
        . e b 4 4 4 4 4 5 4 4 4 4 b e .
        8 7 e e b 4 4 4 4 4 4 b e e 6 8
        8 7 2 e e e e e e e e e e 2 7 8
        e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e
        e c 6 7 6 6 7 7 7 6 6 7 6 c c e
        e b e 8 8 c c 8 8 c c c 8 e b e
        e e b e c c e e e e e c e b e e
        . e e b b 4 4 4 4 4 4 4 4 e e .
        . . . c c c c c e e e e e . . .
        """),
    SpriteKind.player)
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)
current_level = 1
level_control(1)
mySprite.ay = 350
info.set_life(3)