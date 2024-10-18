import pydicom
import tkinter as tk
import PIL.Image
from PIL import Image, ImageTk
import numpy as np


def get_LUT_value(data, window, level):
    """Apply the RGB Look-Up Table for the given
    data and window/level value."""

    return np.piecewise(
        data,
        [
            data <= (level - 0.5 - (window - 1) / 2),
            data > (level - 0.5 + (window - 1) / 2),
        ],
        [
            0,
            255,
            lambda data: ((data - (level - 0.5)) / (window - 1) + 0.5) * (255 - 0),
        ],
    )


def get_PIL_image(dataset):
    """Get Image object from Python Imaging Library(PIL)"""

    if "PixelData" not in dataset:
        print("XXXXXXXXXXX")
        raise TypeError(
            "Cannot show image -- DICOM dataset does not have " "pixel data"
        )
    # can only apply LUT if these window info exists
    if ("WindowWidth" not in dataset) or ("WindowCenter" not in dataset):
        print('1111')
        bits = dataset.BitsAllocated
        samples = dataset.SamplesPerPixel
        if bits == 8 and samples == 1:
            print('L')
            mode = "L"
        elif bits == 8 and samples == 3:
            print('RGB')
            mode = "RGB"
        elif bits == 16:
            print('16')
            # not sure about this -- PIL source says is 'experimental'
            # and no documentation. Also, should bytes swap depending
            # on endian of file and system??
            mode = "I;16"
        else:
            print('XXXX')
            raise TypeError(
                "Don't know PIL mode for %d BitsAllocated "
                "and %d SamplesPerPixel" % (bits, samples)
            )

        # PIL size = (width, height)
        size = (dataset.Columns, dataset.Rows)
        print(size)

        im = PIL.Image.frombuffer(mode, size, dataset.PixelData, "raw", mode, 0, 1)
    else:
        print('2222')
        ew = dataset["WindowWidth"]
        ec = dataset["WindowCenter"]
        print(ew)
        print(ec)
        ww = int(ew.value[0] if ew.VM > 1 else ew.value)
        wc = int(ec.value[0] if ec.VM > 1 else ec.value)
        image = get_LUT_value(dataset.pixel_array, ww, wc)

        im = PIL.Image.fromarray(image).convert("L")  # 轉換成灰階圖像

    return im


def show_PIL(dataset):
    """Display an image using the Python Imaging Library (PIL)"""
    im = get_PIL_image(dataset)
    im.show()


def show_PIL_in_tk(dataset):
    """Display an image using the Python Imaging Library (PIL)"""
    im = get_PIL_image(dataset)
    im.show()


print("讀取dicom檔案內的圖片")

filename1 = "data/CT_small.dcm"
filename2 = "data/ims000525.dcm"
filename3 = "data/test.dcm"

ds = pydicom.dcmread(filename3)

block = True
master = None

frame = tk.Frame(master=master, background="#000")

if "SeriesDescription" in ds and "InstanceNumber" in ds:
    print("1111")
    title = ", ".join(
        ("Ser: " + ds.SeriesDescription, "Img: " + str(ds.InstanceNumber))
    )
else:
    print("2222")
    title = "pydicom image"

print(title)
frame.master.title(title)

photo_image = get_PIL_image(ds)
photo_image = ImageTk.PhotoImage(photo_image)
label = tk.Label(frame, image=photo_image, background="#000")

# keep a reference to avoid disappearance upon garbage collection
label.photo_reference = photo_image
label.grid()
frame.grid()

if block:
    frame.mainloop()
