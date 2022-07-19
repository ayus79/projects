from tkinter import *
from func import select_file, image_to_pdf, images_to_pdf

root = Tk()

root.geometry("400x350")
root.title("Image to Pdf Converter")
root.resizable(0,0)
root.configure(background='#f2f2f2')
Label(root,text= "Image Conversation", font="Helvetica 20 bold", fg="maroon").pack(pady=30)

Button(root, text= "Select Images", command= select_file, font= 14,bg="black", fg="white").pack(pady=10)

frame = Frame()
frame.pack(pady=20)

Button(frame, text= "Image to PDF", command= image_to_pdf , relief="solid",
bg='darkgreen',fg="white" ,font=15).pack(side=LEFT, padx=10)
 
Button(frame, text= "Images to PDF", command= images_to_pdf,  relief="solid",
bg='darkgreen',fg="white", font=15).pack()


root.mainloop()

