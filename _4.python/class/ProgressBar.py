import gc
import os
import time


# Helper functions and classes
class ProgressBar(object):
    """To print progress to the screen."""

    def __init__(self, char="-", length=20):
        self.char = char
        self.length = length
        self.progress = 0.0
        self.nbits = 0
        self.what = ""

    def Start(self, what=""):
        """Start(what='')
        Start the progress bar, displaying the given text first.
        Make sure not to print anything untill after calling
        Finish(). Messages can be printed while displaying
        progess by using printMessage().
        """
        self.what = what
        self.progress = 0.0
        self.nbits = 0
        sys.stdout.write(what + " [")

    def Stop(self, message=""):
        """Stop the progress bar where it is now.
        Optionally print a message behind it."""
        delta = int(self.length - self.nbits)
        sys.stdout.write(" " * delta + "] " + message + "\n")

    def Finish(self, message=""):
        """Finish the progress bar, setting it to 100% if it
        was not already. Optionally print a message behind the bar.
        """
        delta = int(self.length - self.nbits)
        sys.stdout.write(self.char * delta + "] " + message + "\n")

    def Update(self, newProgress):
        """Update progress. Progress is given as a number
        between 0 and 1.
        """
        self.progress = newProgress
        required = self.length * (newProgress)
        delta = int(required - self.nbits)
        if delta > 0:
            sys.stdout.write(self.char * delta)
            self.nbits += delta

    def PrintMessage(self, message):
        """Print a message (for example a warning).
        The message is printed behind the progress bar,
        and a new bar is started.
        """
        self.Stop(message)
        self.Start(self.what)


_progressBar = ProgressBar()


def _progressCallback(progress):
    """The callback for displaying progress."""
    if isinstance(progress, str):
        _progressBar.Start(progress)
        _progressBar._t0 = time.time()
    elif progress is None:
        dt = time.time() - _progressBar._t0
        _progressBar.Finish(f"{dt:2.2f} seconds")
    else:
        _progressBar.Update(progress)


def _listFiles(files, path):
    """List all files in the directory, recursively."""

    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isdir(item):
            _listFiles(files, item)
        else:
            files.append(item)


def read_files(path):
    print(path)

    # Init list of files
    files = []

    # Make dir nice
    basedir = os.path.abspath(path)
    print("basedir", basedir)
    print("files", files)
    # Check whether it exists
    if not os.path.isdir(basedir):
        raise ValueError("The given path is not a valid directory.")
    # Find files recursively
    _listFiles(files, basedir)
    print(files)

    showProgress = _progressCallback

    count = 0
    print("111")
    showProgress("Loading series information:")
    for filename in files:
        print(filename)

        # doing something
        time.sleep(0.1)

        # Show progress (note that we always start with a 0.0)
        showProgress(float(count) / len(files))
        count += 1

    # Finish progress
    showProgress(None)

    print("333")
    showProgress("Analysing series")
    for i in range(100):
        # print(i)
        # print('append ', i)
        showProgress(float(i + 1) / 100)
    showProgress(None)

    # Fill volume
    showProgress("Loading data:")
    for z in range(1, 100):
        showProgress(float(z) / 100)

    # Finish
    showProgress(None)

    msg = "lion-mouse"
    _progressBar.PrintMessage(msg)


import sys

foldername = "C:/_git/vcs/_1.data/______test_files1/__RW/_dicom"
t0 = time.time()
read_files(foldername)
