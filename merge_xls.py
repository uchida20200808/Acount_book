import tkinter as tk
from tkinter import filedialog
import pandas as pd

#window
root = tk.Tk()

#window size
HEIGHT = 500
WIDTH = 800

class merge_file:
    def open_file_hiro(self):
        idir = '/home/uchida/ドキュメント/kakeibo'
        filetype = [("excel", "*.xls"), ("all", "*")]
        file_path_hiro = tk.filedialog.askopenfilename(filetypes=filetype, initialdir = idir)
        entry_hiro.insert(tk.END, file_path_hiro)
        hiro = pd.read_excel(file_path_hiro)
        hiro['payer'] = 'hiro'
        print(hiro.head())
        self.hiro = hiro
    
    def open_file_misa(self):
        idir = '/home/uchida/ドキュメント/kakeibo'
        filetype = [("excel", "*.xls"),("all", "*")]
        file_path_misa = tk.filedialog.askopenfilename(filetypes=filetype, initialdir = idir)
        entry_misa.insert(tk.END, file_path_misa)
        misa = pd.read_excel(file_path_misa)
        misa['payer'] = 'misa'
        print(misa.head())
        self.misa = misa

    def open_file_credit(self):
        idir = '/home/uchida/ドキュメント/kakeibo'
        filetype = [("excel", "*.xls"), ("all", "*")]
        file_path_credit = tk.filedialog.askopenfilename(filetypes=filetype, initialdir = idir)
        entry_credit.insert(tk.END, file_path_credit)
        credit = pd.read_excel(file_path_credit)
        print(credit.head())
        self.credit = credit

    def merge_file(self):
        try:
            df = pd.concat([self.hiro, self.misa, self.credit])
            df = df.dropna()
            df.to_excel('merge_data.xls', index=False)
            print(df.head())
            self.df = df
        except:
            print('処理できませんでした')
      

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#background image:Change image file name
background_image = tk.PhotoImage(file='chokinbako.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#Merge corner
label1 = tk.Label(root, text='1.Select account books saved as xls', font=40)
label1.place(x=0, y=0)


#Entry name & column
label_hiro = tk.Label(root, text = 'hiro', font=40)
label_hiro.place(x=0, y=25)
entry_hiro = tk.Entry(root, font=40)
entry_hiro.place(x=60, y=25)

label_misa = tk.Label(root, text='misa', font=40)
label_misa.place(x=0, y=50)
entry_misa = tk.Entry(root, font=40)
entry_misa.place(x=60, y=50)

label_credit = tk.Label(root, text='credit', font=40)
label_credit.place(x=0, y=75)
entry_credit = tk.Entry(root, font=40)
entry_credit.place(x=60, y=75)


#button to open file
book = merge_file()
hiro_button = tk.Button(root, text='Ref.', command=book.open_file_hiro)
hiro_button.place(x=250, y=25)

misa_button = tk.Button(root,text='Ref.', command=book.open_file_misa)
misa_button.place(x=250, y=50)

credit_button = tk.Button(root,text='Ref.', command=book.open_file_credit)
credit_button.place(x=250, y=75)

#button to merge files into a single file
merge_button = tk.Button(root, text='merge & save', command=book.merge_file)
merge_button.place(x=0, y=120)

root.mainloop()
