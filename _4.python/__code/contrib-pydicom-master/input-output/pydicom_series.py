import gc
import os
import pydicom
from pydicom.sequence import Sequence

import numpy as np

def _listFiles(files, path):
    """List all files in the directory, recursively. """

    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isdir(item):
            _listFiles(files, item)
        else:
            files.append(item)

def _splitSerieIfRequired(serie, series):

    # Sort the original list and get local name
    serie._sort()
    L = serie._datasets

    # Init previous slice
    ds1 = L[0]

    # Check whether we can do this
    if "ImagePositionPatient" not in ds1:
        return

    # Initialize a list of new lists
    L2 = [[ds1]]

    # Init slice distance estimate
    distance = 0

    for index in range(1, len(L)):

        # Get current slice
        ds2 = L[index]

        # Get positions
        pos1 = float(ds1.ImagePositionPatient[2])
        pos2 = float(ds2.ImagePositionPatient[2])

        # Get distances
        newDist = abs(pos1 - pos2)
        # deltaDist = abs(firstPos-pos2)

        # If the distance deviates more than 2x from what we've seen,
        # we can agree it's a new dataset.
        if distance and newDist > 2.1 * distance:
            L2.append([])
            distance = 0
        else:
            # Test missing file
            if distance and newDist > 1.5 * distance:
                print(f'Warning: missing file after "{ds1.filename}"')
            distance = newDist

        # Add to last list
        L2[-1].append(ds2)

        # Store previous
        ds1 = ds2

    # Split if we should
    if len(L2) > 1:

        # At what position are we now?
        i = series.index(serie)

        # Create new series
        series2insert = []
        for L in L2:
            newSerie = DicomSeries(serie.suid)
            newSerie._datasets = Sequence(L)
            series2insert.append(newSerie)

        # Insert series and remove self
        for newSerie in reversed(series2insert):
            series.insert(i, newSerie)
        series.remove(serie)


def _getPixelDataFromDataset(ds):
    """ Get the pixel data from the given dataset. If the data
    was deferred, make it deferred again, so that memory is
    preserved. Also applies RescaleSlope and RescaleIntercept
    if available. """

    # Get original element
    el = ds['PixelData']

    # Get data
    data = ds.pixel_array

    # Remove data (mark as deferred)
    ds['PixelData'] = el
    del ds._pixel_array

    # Obtain slope and offset
    slope = 1
    offset = 0
    needFloats = False
    needApplySlopeOffset = False
    if 'RescaleSlope' in ds:
        needApplySlopeOffset = True
        slope = ds.RescaleSlope
    if 'RescaleIntercept' in ds:
        needApplySlopeOffset = True
        offset = ds.RescaleIntercept
    if int(slope) != slope or int(offset) != offset:
        needFloats = True
    if not needFloats:
        slope, offset = int(slope), int(offset)

    # Apply slope and offset
    if needApplySlopeOffset:

        # Maybe we need to change the datatype?
        if data.dtype in [np.float32, np.float64]:
            pass
        elif needFloats:
            data = data.astype(np.float32)
        else:
            # Determine required range
            minReq, maxReq = data.min(), data.max()
            minReq = min(
                [minReq, minReq * slope + offset, maxReq * slope + offset])
            maxReq = max(
                [maxReq, minReq * slope + offset, maxReq * slope + offset])

            # Determine required datatype from that
            dtype = None
            if minReq < 0:
                # Signed integer type
                maxReq = max([-minReq, maxReq])
                if maxReq < 2 ** 7:
                    dtype = np.int8
                elif maxReq < 2 ** 15:
                    dtype = np.int16
                elif maxReq < 2 ** 31:
                    dtype = np.int32
                else:
                    dtype = np.float32
            else:
                # Unsigned integer type
                if maxReq < 2 ** 8:
                    dtype = np.uint8
                elif maxReq < 2 ** 16:
                    dtype = np.uint16
                elif maxReq < 2 ** 32:
                    dtype = np.uint32
                else:
                    dtype = np.float32

            # Change datatype
            if dtype != data.dtype:
                data = data.astype(dtype)

        # Apply slope and offset
        data *= slope
        data += offset

    # Done
    return data


# The public functions and classes

def find_shape(dataset):
    """Find the expected shape of `dataset.pixel_array` without reading the pixel data.
    The returned shape is a tuple"""
    shape = dataset.Rows, dataset.Columns
    frames = dataset.get('NumberOfFrames', 1) or 1
    if frames > 1:
        shape = (frames,) + shape
    samples = dataset.SamplesPerPixel
    if samples > 1:
        conf = dataset.PlanarConfiguration
        if conf == 0:
            shape += (samples,)
        elif conf == 1:
            shape = (samples,) + shape
        else:
            raise ValueError(f"Invalid Planar Configuration: '{conf}'")
    return shape


def read_files(path, readPixelData=False, force=False):
    print(path)

    # Init list of files
    files = []

    # Obtain data from the given path
    if isinstance(path, str):
        # Make dir nice
        basedir = os.path.abspath(path)
        # Check whether it exists
        if not os.path.isdir(basedir):
            raise ValueError('The given path is not a valid directory.')
        # Find files recursively
        _listFiles(files, basedir)
        print('files a')

    elif isinstance(path, (tuple, list)):
        # Iterate over all elements, which can be files or directories
        for p in path:
            print(p)
            if os.path.isdir(p):
                _listFiles(files, os.path.abspath(p))
                print('files b')
            elif os.path.isfile(p):
                files.append(p)
                print('files c')
            else:
                print(f"Warning, the path '{p}' is not valid.")
    else:
        raise ValueError('The path argument must be a string or list.')

    # Set defer size
    deferSize = 16383  # 128**2-1
    if readPixelData:
        deferSize = None

    # Gather file data and put in DicomSeries
    series = {}
    count = 0
    print('111')
    for filename in files:
        print(filename)

        # Skip DICOMDIR files
        if filename.count("DICOMDIR"):
            print('skip 1')
            continue

        # Try loading dicom ...
        try:
            dcm = pydicom.dcmread(filename, deferSize, force=force)
        except pydicom.filereader.InvalidDicomError:
            print('skip 2')
            continue  # skip non-dicom file
        except Exception as why:
            print('skip 3')
            continue

        # Get SUID and register the file with an existing or new series object
        try:
            suid = dcm.SeriesInstanceUID
            print('suid = ', suid)
        except AttributeError:
            print('skip 4')
            continue  # some other kind of dicom file
        if suid not in series:
            series[suid] = DicomSeries(suid)
        series[suid]._append(dcm)

        count += 1

    print('222')

    # Make a list and sort, so that the order is deterministic
    series = list(series.values())
    series.sort(key=lambda x: x.suid)

    # Split series if necessary
    for serie in reversed([serie for serie in series]):
        _splitSerieIfRequired(serie, series)

    print('333')
    # Finish all series
    series_ = []
    for i in range(len(series)):
        print(i)
        print(series[i])
        try:
            #series[i]._finish()    ????
            series_.append(series[i])
            print('append ', series[i])
        except Exception:
            pass  # Skip serie (probably report-like file without pixels)

    return series_


class DicomSeries(object):
    def __init__(self, suid):
        # Init dataset list and the callback
        self._datasets = Sequence()

        # Init props
        self._suid = suid
        self._info = None
        self._shape = None
        self._spacing = None

    @property
    def suid(self):
        """ The Series Instance UID. """
        return self._suid

    @property
    def shape(self):
        """ The shape of the data (nz, ny, nx).
        If None, the series contains a single dicom file. """
        return self._shape

    @property
    def spacing(self):
        """ The spacing (voxel distances) of the data (dz, dy, dx).
        If None, the series contains a single dicom file. """
        return self._spacing

    @property
    def info(self):
        """ A DataSet instance containing the information as present in the
        first dicomfile of this series. """
        return self._info

    @property
    def description(self):
        """ A description of the dicom series. Used fields are
        PatientName, shape of the data, SeriesDescription,
        and ImageComments.
        """

        info = self.info

        # If no info available, return simple description
        if info is None:
            return "DicomSeries containing %i images" % len(self._datasets)

        fields = []

        # Give patient name
        if 'PatientName' in info:
            fields.append(f"{info.PatientName}")

        # Also add dimensions
        if self.shape:
            tmp = [str(d) for d in self.shape]
            fields.append('x'.join(tmp))

        # Try adding more fields
        if 'SeriesDescription' in info:
            fields.append("'" + info.SeriesDescription + "'")
        if 'ImageComments' in info:
            fields.append("'" + info.ImageComments + "'")

        # Combine
        return ' '.join(fields)

    def __repr__(self):
        adr = hex(id(self)).upper()
        data_len = len(self._datasets)
        return "<DicomSeries with %i images at %s>" % (data_len, adr)

    def get_pixel_array(self):
        """ get_pixel_array()

        Get (load) the data that this DicomSeries represents, and return
        it as a numpy array. If this serie contains multiple images, the
        resulting array is 3D, otherwise it's 2D.

        If RescaleSlope and RescaleIntercept are present in the dicom info,
        the data is rescaled using these parameters. The data type is chosen
        depending on the range of the (rescaled) data.

        """

        # It's easy if no file or if just a single file
        if len(self._datasets) == 0:
            raise ValueError('Serie does not contain any files.')
        elif len(self._datasets) == 1:
            ds = self._datasets[0]
            slice = _getPixelDataFromDataset(ds)
            return slice

        # Check info
        if self.info is None:
            raise RuntimeError("Cannot return volume if series not finished.")

        # Init data (using what the dicom packaged produces as a reference)
        ds = self._datasets[0]
        slice = _getPixelDataFromDataset(ds)
        vol = np.zeros(self.shape, dtype=slice.dtype)
        vol[0] = slice

        # Fill volume
        ll = self.shape[0]
        for z in range(1, ll):
            ds = self._datasets[z]
            vol[z] = _getPixelDataFromDataset(ds)

        # Finish

        # Done
        gc.collect()
        return vol

    def _append(self, dcm):
        """ _append(dcm)
        Append a dicomfile (as a pydicom.dataset.FileDataset) to the series.
        """
        self._datasets.append(dcm)

    def _sort(self):
        """ sort()
        Sort the datasets by instance number.
        """
        self._datasets.sort(key=lambda k: k.InstanceNumber)

    def _finish(self):
        """ _finish()

        Evaluate the series of dicom files. Together they should make up
        a volumetric dataset. This means the files should meet certain
        conditions. Also some additional information has to be calculated,
        such as the distance between the slices. This method sets the
        attributes for "shape", "spacing" and "info".

        This method checks:
          * that there are no missing files
          * that the dimensions of all images match
          * that the pixel spacing of all images match

        """

        # The datasets list should be sorted by instance number
        L = self._datasets
        if len(L) == 0:
            return
        elif len(L) < 2:
            # Set attributes
            ds = self._datasets[0]
            self._info = self._datasets[0]
            self._shape = find_shape(ds)
            self._spacing = ds.PixelSpacing
            return

        # Get previous
        ds1 = L[0]

        # Init measures to calculate average of
        distance_sum = 0.0

        # Init measures to check (these are in 2D)
        dimensions = find_shape(ds1)

        # row, column
        spacing = ds1.PixelSpacing

        for index in range(len(L)):
            # The first round ds1 and ds2 will be the same, for the
            # distance calculation this does not matter

            # Get current
            ds2 = L[index]

            # Get positions
            pos1 = float(ds1.ImagePositionPatient[2])
            pos2 = float(ds2.ImagePositionPatient[2])

            # Update distance_sum to calculate distance later
            # TODO: use ImageOrientationPatient's normal to calculate this distance
            distance_sum += abs(pos1 - pos2)

            # Test measures
            dimensions2 = find_shape(ds2)
            spacing2 = ds2.PixelSpacing
            if dimensions != dimensions2:
                # We cannot produce a volume if the dimensions match
                raise ValueError('Dimensions of slices does not match.')
            if spacing != spacing2:
                # We can still produce a volume, but we should notify the user
                msg = 'Warning: spacing does not match.'
                print(msg)
            # Store previous
            ds1 = ds2

        # Create new dataset by making a deep copy of the first
        info = pydicom.dataset.Dataset()
        firstDs = self._datasets[0]
        for key in firstDs.keys():
            if key != 'PixelData':
                el = firstDs[key]
                info.add_new(el.tag, el.VR, el.value)

        # Finish calculating average distance
        # (Note that there are len(L)-1 distances)
        distance_mean = distance_sum / (len(L) - 1)

        # Store information that is specific for the series
        self._shape = (len(L),) + dimensions
        spacing.insert(0, distance_mean)
        self._spacing = spacing

        # Store
        self._info = info


import sys
foldername = 'C:/_git/vcs/_1.data/______test_files1/__RW/_dicom'

adir = foldername
all_series = read_files(adir, False, False)

print("Summary of each series:")
for series in all_series:
    print(series.description)
    arr = series.get_pixel_array()
