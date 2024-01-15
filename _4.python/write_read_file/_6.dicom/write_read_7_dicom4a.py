import pydicom
import PIL.Image
import numpy as np

def get_LUT_value(data, window, level):
    """Apply the RGB Look-Up Table for the given
       data and window/level value."""

    win = window
    lvl = level

    e = [
        0, 255,
        lambda data: ((data - (lvl - 0.5)) / (win - 1) + 0.5) * (255 - 0)
    ]
    return np.piecewise(data, [
        data <= (lvl - 0.5 - (win - 1) / 2),
        data > (lvl - 0.5 + (win - 1) / 2)
    ], e)


# -----------------------------------------------------------
# ImFrame.loadPIL_LUT(dataset)
# Display an image using the Python Imaging Library (PIL)
# -----------------------------------------------------------
def loadPIL_LUT(dataset):
    if 'PixelData' not in dataset:
        print('XXXXXXXXXXX')
        raise TypeError("Cannot show image -- DICOM dataset does not have pixel data")

    # can only apply LUT if these values exist
    if ('WindowWidth' not in dataset) or ('WindowCenter' not in dataset):
        bits = dataset.BitsAllocated
        samples = dataset.SamplesPerPixel
        if bits == 8 and samples == 1:
            mode = "L"
        elif bits == 8 and samples == 3:
            mode = "RGB"
        # not sure about this -- PIL source says is
        # 'experimental' and no documentation.
        elif bits == 16:
            # Also, should bytes swap depending
            # on endian of file and system??
            mode = "I;16"
        else:
            msg = "Don't know PIL mode for %d BitsAllocated" % (bits)
            msg += " and %d SamplesPerPixel" % (samples)
            raise TypeError(msg)
        size = (dataset.Columns, dataset.Rows)

        # Recommended to specify all details by
        # http://www.pythonware.com/library/pil/handbook/image.htm
        im = PIL.Image.frombuffer(mode, size, dataset.PixelData, "raw", mode, 0, 1)
    else:
        ew = dataset['WindowWidth']
        ec = dataset['WindowCenter']
        ww = int(ew.value[0] if ew.VM > 1 else ew.value)
        wc = int(ec.value[0] if ec.VM > 1 else ec.value)
        image = get_LUT_value(dataset.pixel_array, ww, wc)

        # Convert mode to L since LUT has only 256 values:
        # http://www.pythonware.com/library/pil/handbook/image.htm
        im = PIL.Image.fromarray(image).convert('L')	#轉換成灰階圖像
    return im

def show_file(fullPath):
    ds = pydicom.dcmread(str(fullPath))
    # change strings to unicode
    ds.decode()
    if 'PixelData' in ds:
        print('aaaaaaa')
        dImage = loadPIL_LUT(ds)
        if dImage is not None:
            print('bbbbb')
            dImage.show()

print('讀取dicom檔案內的圖片')

filename1 = 'data/CT_small.dcm'
filename2 = 'data/ims000525.dcm'
filename3 = 'data/test.dcm'

show_file(filename3)
