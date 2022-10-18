import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk() # 練習１
    root.title("迷えるこうかとん")

    # キャンバスのサイズ設定
    canvas = tk.Canvas(root, width = 1500, height = 900, bg = "black")
    canvas.pack() # 練習２

    root.mainloop()