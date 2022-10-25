import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん") # 練習１
    scrn_sfc = pg.display.set_mode((1600, 900))

    bg_sfc = pg.image.load("fig/pg_bg.jpg") # surface
    bg_rct = bg_sfc.get_rect() # Rect

    clock = pg.time.Clock() # 練習１

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習２
        pg.display.update() # 野原貼り付け

        for event in pg.event.get(): # イベントを繰り返しで処理
            if event.type == pg.QUIT: # ウィンドウの×ボタンをクリックしたら閉じる
                return

        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # モジュールを初期化する
    main()
    pg.quit() # モジュールの初期化を解除する
    sys.exit()