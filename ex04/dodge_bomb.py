import pygame as pg
import sys
from random import randint

def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct、爆弾rct
    scr_rct：スクリーンrct
    領域内：-1/領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん") # 練習１
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("fig/pg_bg.jpg") # surface
    bg_rct = bg_sfc.get_rect() # Rect

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() # Rect
    tori_rct.center = 900, 400 # 横：900, 縦：400の座標

    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 空のsurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透明にする
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描画
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)

    # 練習６
    vx, vy = +1, +1

    clock = pg.time.Clock() # 練習１

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習２

        for event in pg.event.get(): # イベントを繰り返しで処理
            if event.type == pg.QUIT: # ウィンドウの×ボタンをクリックしたら閉じる
                return

        # 練習４
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]: # こうかとんの縦座標を-1
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]: # 縦座標を+1
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]: # 横座標を-1
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: # 横座標を+1
            tori_rct.centerx += 1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1

        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1

        scrn_sfc.blit(tori_sfc, tori_rct) # 練習３

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) # 練習６
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習５

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # モジュールを初期化する
    main()
    pg.quit() # モジュールの初期化を解除する
    sys.exit()