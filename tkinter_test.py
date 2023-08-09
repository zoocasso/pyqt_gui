import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import filedialog

x=np.arange(1, 10, 1)
y=2*x**2
fig = Figure(figsize=(10, 7), dpi=100)  #그리프 그릴 창 생성
fig.add_subplot(1,1,1).plot(x, y)#창에 그래프 하나 추가

window = tk.Tk()  #Tk 객체 생성. 기본 윈도우 객체
window.title("타이틀")
window.geometry("640x400")
window.resizable(False, False)

def calc_dataframe(csv_df):
    print(csv_df)
    print(csv_df['num1']+csv_df['num2']*csv_df['num3']/csv_df['num4'])

def file_upload():
    file = filedialog.askopenfilename(title="csv파일을 선택하세요")
    csv_df = pd.read_csv(file)
    calc_dataframe(csv_df)
    

button = tk.Button(window, text="file_upload", width=15, command=file_upload)
button.pack()

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

window.mainloop()