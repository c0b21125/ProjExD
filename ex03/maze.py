from http.client import TOO_MANY_REQUESTS
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm # 練習８

def count_up():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    root.after(1000, count_up)


# 練習５
def key_down(event):
    global key
    key = event.keysym

# 練習６
def key_up(event):
    global key
    key = ""

# 練習7,11,12
def main_proc():
    global mx, my
    global cx, cy
    # 床0,壁1
    # 移動
    if key == "Up" and maze_lst[my-1][mx] == 0:
        my -= 1
    if key == "Down" and maze_lst[my+1][mx] == 0:
        my += 1
    if key == "Left" and maze_lst[my][mx-1] == 0:
        mx -= 1
    if key == "Right" and maze_lst[my][mx+1] == 0:
        mx += 1

    cx, cy = mx*100+50, my*100+50 # 1マス100x100
    canvas.coords("tori", cx, cy)

    # ゴール確認
    if maze_lst[my][mx] == 0 and cx==1350 and cy==550:
        canvas.update()
        tkm.showinfo("おめでとう", "ゴールしました")
    
    else:
        root.after(100, main_proc) # そうでなければこの関数を実行
    
    #cx, cy = mx*100+50, my*100+50 # 1マス100x100

    # 通った道に色付け
    #if maze_lst[my][mx] == 0:
    #    maze_lst[my][mx] = 2
    #    canvas.create_rectangle(cx, cy, fill="pink", width=0)
    #canvas.delete("tori")
    #canvas.create_image(cx, cy, image=tori, tag="tori")

    #cx, cy = mx*100+50, my*100+50 # 1マス100x100
    #canvas.coords("tori", cx, cy)
    #root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk() # 練習１
    root.title("迷えるこうかとん")
    label = tk.Label(root,font=("", 30))
    label.pack()

    tmr = 0
    root.after(1000, count_up)

    # キャンバスのサイズ設定
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack() # 練習２

    # 練習９，１０
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)
    canvas.create_rectangle(100, 100, 200, 200, 
                                    fill="blue") # start
    canvas.create_text(150, 150, text="start", font=("", 25), fill="white")
    canvas.create_rectangle(1300, 500, 1400, 600, 
                                    fill="red") # goal
    canvas.create_text(1350, 550, text="goal", font=("", 25), fill="white")

    # 練習３ こうかとん表示
    tori = tk.PhotoImage(file="fig/0.png")
    #tori_lst = glob.glob("C:/Users/admin/Documents/ProjExD2022/fig/*.png") # ランダムにこうかとんの画像抽出
    #tori_data = random.choice(tori_lst)
    #tori_file = os.path.split(tori_data)[1]
    #tori = tk.PhotoImage(file = tori_file)
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    # 練習４
    key = "" # 現在押されているキーを表す変数

    # 練習５
    root.bind("<KeyPress>", key_down)
    # 練習６
    root.bind("<KeyRelease>", key_up)

    # 練習７
    main_proc()

    root.mainloop()