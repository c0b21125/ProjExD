import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm # 練習８

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
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk() # 練習１
    root.title("迷えるこうかとん")

    # キャンバスのサイズ設定
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack() # 練習２

    # 練習９，１０
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)

    # 練習３ こうかとん表示
    tori = tk.PhotoImage(file="fig/0.png")
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