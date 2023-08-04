import tkinter

from tkinter import filedialog 

def openFile():
    pdf_filename = filedialog.askopenfilename(title="Open PDF file", 
                                                  initialdir='C:/dddddddddd/____download',
                                                  filetypes=[('PDF files', '*.pdf')])
    print(pdf_filename)
    
    filename_label.configure(text=pdf_filename)    
    outputfile_text.delete("1.0", tkinter.END)
    
    current_text = 'aaaaaaaa'
    outputfile_text.insert(tkinter.END, current_text)


root = tkinter.Tk()
root.title("PDF Text Extractor")


filename_label = tkinter.Label(root, text="No File Selected")
outputfile_text = tkinter.Text(root)
openfile_button = tkinter.Button(root, text="Open PDF File", command=openFile)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()
