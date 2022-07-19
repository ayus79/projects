from tkinter.filedialog import askopenfilenames
import img2pdf


def select_file():
        global file_names
        file_names = askopenfilenames(initialdir="/", title="Select files",)

def image_to_pdf():
        for index, file_name in enumerate(file_names):
            with open(f'file {index}.pdf', 'wb') as f:
                f.write(img2pdf.convert(file_name))

def images_to_pdf():
        with open('file.pdf', 'wb') as f:
            f.write(img2pdf.convert(file_names))
             
