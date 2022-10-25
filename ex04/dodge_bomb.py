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
    global scrn_sfc
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

    # 爆弾の追加
    bomb2_sfc = pg.Surface((20, 20)) # 空のsurface
    bomb2_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透明にする
    # 爆弾の色をランダムにする
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    pg.draw.circle(bomb2_sfc, (red, green, blue), (10, 10), 10) # 円を描画
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = randint(0, scrn_rct.width)
    bomb2_rct.centery = randint(0, scrn_rct.height)

    # 焼き鳥
    yakitori_sfc = pg.image.load("fig/food_yakitori01_01.png")
    yakitori_sfc = pg.transform.rotozoom(yakitori_sfc, 0, 0.2)
    yakitori_rct = yakitori_sfc.get_rect()
    yakitori_rct.center = tori_rct.centerx, tori_rct.centery


    # 練習６
    vx, vy = +1, +1
    vx2, vy2 = +2, +2
    flag = 0 # こうかとんと爆弾の当たり判定

    clock = pg.time.Clock() # 練習１

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習２

        for event in pg.event.get(): # イベントを繰り返しで処理
            if event.type == pg.QUIT: # ウィンドウの×ボタンをクリックしたら閉じる
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1: # F1キーが押されたらフルスクリーンモードに
                    scrn_sfc = pg.display.set_mode((1600, 900), pg.FULLSCREEN)
                if event.key == pg.K_F2: # F2キーが押されたら元のサイズに戻す
                    scrn_sfc = pg.display.set_mode(1600, 900)
                if event.key == pg.K_ESCAPE: # Escキーが押されたら閉じる
                    return
                if event.key == pg.K_SPACE: # スペースキーが押されたら爆弾を止める
                    vx, vy = 0, 0
                    vx2, vy2 = 0, 0
                if event.key == pg.K_s:
                    vx *= 1.1
                    vy *= 1.1

                    vx2 *= 1.1
                    vy2 *= 1.1

        if flag == 0:
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

        # 爆弾１
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) # 練習６
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習５

        # 爆弾２
        yoko, tate = check_bound(bomb2_rct, scrn_rct)
        vx2 *= yoko
        vy2 *= tate
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)

        # 練習８
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            flag += 1
            tori_rct = yakitori_rct
        
        if tori_rct.colliderect(bomb2_rct):
            flag += 1
            tori_rct = yakitori_rct

        if flag == 1: # flag=1（一回当たった）の時こうかとんが焼き鳥になる
            scrn_sfc.blit(yakitori_sfc, yakitori_rct)

        if flag == 2: # 2回当たったら終了
            bg_sfc = pg.image.load("fig/gameover.png") # gameoverの画像
            bg_rct = bg_sfc.get_rect()
            bg_rct.center = 900, 400


        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # モジュールを初期化する
    main()
    pg.quit() # モジュールの初期化を解除する
    sys.exit()