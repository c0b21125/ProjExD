import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん") # 練習１
    scrn_sfc = pg.display.set_mode((1600, 900))

    bg_sfc = pg.image.load("fig/pg_bg.jpg") # surface
    bg_rct = bg_sfc.get_rect() # Rect

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect() # Rect
    tori_rct.center = 900, 400 # 横：900, 縦：400の座標

    clock = pg.time.Clock() # 練習１

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習２

        for event in pg.event.get(): # イベントを繰り返しで処理
            if event.type == pg.QUIT: # ウィンドウの×ボタンをクリックしたら閉じる
                return

        scrn_sfc.blit(tori_sfc, tori_rct) # 練習３

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

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # モジュールを初期化する
    main()
    pg.quit() # モジュールの初期化を解除する
    sys.exit()