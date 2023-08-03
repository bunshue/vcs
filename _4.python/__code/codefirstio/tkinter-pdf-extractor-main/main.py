import tkinter, PyPDF2
from tkinter import filedialog 


def openFile():
    filename = filedialog.askopenfilename(title="Open PDF file", 
                                                  initialdir='D:\codefirst.io\Tkinter Extract PDF Text',
                                                  filetypes=[('PDF files', '*.pdf')])
    print(filename)
    
    filename_label.configure(text=filename)    
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range (reader.numPages):
        current_text = reader.getPage(i).extractText()
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
