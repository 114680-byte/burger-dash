scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    current_level += 1
    level_control(3)
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -150
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`hazardLava1`, function (sprite4, location4) {
    info.changeLifeBy(-1)
    game.splash("ow")
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -150
})
function level_control (level_number: number) {
    if (level_number == 1) {
        tiles.setCurrentTilemap(tilemap`level1`)
    }
    if (level_number == 2) {
        tiles.setCurrentTilemap(tilemap`level2`)
    }
    if (level_number == 3) {
        tiles.setCurrentTilemap(tilemap`level3`)
    }
    tiles.placeOnRandomTile(mySprite, assets.tile`myTile2`)
    scene.setBackgroundColor(8)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -150
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -150
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -150
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite2, location2) {
    game.gameOver(true)
    game.setGameOverMessage(true, "GAME OVER!")
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite3, location3) {
    current_level += 1
    level_control(2)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -150
})
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
scene.cameraFollowSprite(mySprite)
let current_level = 1
level_control(1)
mySprite.ay = 350
info.setLife(3)
