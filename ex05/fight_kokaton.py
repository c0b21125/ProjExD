import pygame as pg
from pygame.locals import *
import sys
import random
import os

class Screen:
    def __init__(self, title, wh, bgimg):
        # 練習１
        pg.display.set_caption(title) # 練習１
        self.sfc = pg.display.set_mode(wh) # 1600, 900
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) # "fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # tori_sfc, 0, 2.0
        self.rct = sfc.get_rect()
        self.rct.center = xy #900, 400
        #self.enemy = enemy # 衝突判定用
        self.tori_x = 1 # こうかとんの向き（左右）

    def blit(self, scr:Screen): #scrがScreenクラスであることを明記
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        # キー入力取得
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items(): #key_deltaはクラス関数
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]

            if key_states[K_RIGHT]:
                self.tori_x = 1
            elif key_states[K_LEFT]:
                self.tori_x = 0
        
        # ミサイルの発射
        if key_states[K_SPACE]:
            Shot(self.rct.center, self.tori_x, self.enemy)
        
        self.blit(scr) # scr.sfc.blit(self.sfc, self.rct)


class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く (255, 0, 0),(10, 10),10
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # +1, +1

    def blit(self, scr:Screen): # scrがScreenクラスであることを明記
        scr.sfc.blit(self.sfc, self.rct) # selfは爆弾のsfc, rct

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy) # 練習6
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # scr.sfc.blit(self.sfc, self.rct)

# 敵キャラクラス
class Enemy(pg.sprite.Sprite):
    def __init__(self, img, zoom, vxy, scr:Screen):
        sfc = pg.image.load(img) # enemy_img
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom)
        self.rct = sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
        self.collision()

    def collision(self):
        # ミサイルとの衝突判定
        for shot in self.shots:
            collide = self.rct.colliderect(shot.rct)
            if collide: # 衝突するミサイルあり
                self.kill()


# こうかとんから発射されるビーム
class Shot(pg.sprite.Sprite):
    def __init__(self, img, pos, tori_x, enemy):
        #pg.sprite.Sprite.__init__(self, self.containers)
        self.sfc = pg.image.load(img)
        self.rct = self.sfc.get_rect()
        self.rct.center = pos # 中心座標をposに設定
        self.player_x = tori_x # こうかとんの左右の向きを判定
        self.enemy = enemy # 衝突判定用
        self.speed = 10 # ミサイルの移動速度

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen, enemy:Enemy):
        if self.tori_x == 1:
            self.rct.move_ip(self.speed, 0) # 右に発射
        elif self.tori_x == 0:
            self.rct.move_ip(-self.speed, 0) # 左に発射

        # 敵とミサイルの衝突判定
        for enemy in self.enemy:
            collide = self.rct.colliderect(enemy.rct)
            if collide: # 敵と衝突した
                self.kill()
        

def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    #flag = 0 # 当たり判定
    # 練習１
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習３ こうかとんの初期設定
    tori = Bird("fig/6.png", 2.0, (900, 400))
    #yakitori = Bird("fig/food_yakitori01_01.png", 0.2, (900, 400))

    # 練習5 爆弾の初期配置    
    bkd1 = Bomb((255, 0, 0), 10, (+1, +1), scr)
    # 爆弾の色をランダムにする
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    bkd2 = Bomb((r, g, b), 10, (+1.5, +1.5), scr)

    # Enemyの初期配置
    ene = Enemy("fig/alien1.png", 2.0, (+1, +1), scr)

    # Shot
    beam = Shot("fig/shot.gif", tori.rct, Bird.tori_x, ene)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1: # F1キーが押されたらフルスクリーンモードに
                    scrn_sfc = pg.display.set_mode((1600, 900), pg.FULLSCREEN)
                if event.key == pg.K_F2: # F2キーが押されたら元のサイズに戻す
                    scrn_sfc = pg.display.set_mode(1600, 900)
                if event.key == pg.K_ESCAPE: # Escキーが押されたら閉じる
                    return

        # 爆弾に一度も当たっていないときはこうかとんを表示
        #if flag == 0:
        tori.update(scr)

        # 練習7
        bkd1.update(scr)
        bkd2.update(scr)

        # Enemy
        ene.update(scr)

        # Shot
        beam.update(scr)

        # 練習8
        if tori.rct.colliderect(bkd1.rct): # こうかとんrctが爆弾rctと重なったら
            #flag += 1
            return
        if tori.rct.colliderect(bkd2.rct): # こうかとんrctが爆弾rctと重なったら
            #flag += 1
            return

        # 爆弾に一度当たったらこうかとん→焼き鳥に変更
        #if flag == 1:
            #yakitori.update(scr)

        #if flag == 2:
            #return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()