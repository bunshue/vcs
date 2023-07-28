import contextlib
import io
import os
import sys
import importlib.util
import time
import struct
import zipfile
import unittest


from tempfile import TemporaryFile
from random import randint, random

from test.support import (TESTFN, findfile, unlink, rmtree,
                          requires_zlib, requires_bz2, requires_lzma,
                          captured_stdout, check_warnings)

TESTFN2 = TESTFN + "2"
TESTFNDIR = TESTFN + "d"
FIXEDTEST_SIZE = 1000
DATAFILES_DIR = 'zipfile_datafiles'

def get_files(test):
    yield TESTFN2
    with TemporaryFile() as f:
        yield f
        test.assertFalse(f.closed)
    with io.BytesIO() as f:
        yield f
        test.assertFalse(f.closed)

    def test_write_to_readonly(self):
        """Check that trying to call write() on a readonly ZipFile object
        raises a RuntimeError."""
        with zipfile.ZipFile(TESTFN2, mode="w") as zipfp:
            zipfp.writestr("somefile.txt", "bogus")

        with zipfile.ZipFile(TESTFN2, mode="r") as zipfp:
            self.assertRaises(RuntimeError, zipfp.write, TESTFN)

    def test_add_file_before_1980(self):
        # Set atime and mtime to 1970-01-01
        os.utime(TESTFN, (0, 0))
        with zipfile.ZipFile(TESTFN2, "w") as zipfp:
            self.assertRaises(ValueError, zipfp.write, TESTFN)



    def setUp(self):
        self._limit = zipfile.ZIP64_LIMIT
        self._filecount_limit = zipfile.ZIP_FILECOUNT_LIMIT
        zipfile.ZIP64_LIMIT = 1000
        zipfile.ZIP_FILECOUNT_LIMIT = 9

        # Make a source file with some lines
        with open(TESTFN, "wb") as fp:
            fp.write(self.data)



================================================================================================================

        with zipfile.ZipFile(TESTFN2, "r") as zipfp:
            infos = zipfp.infolist()
            data = b""
            for info in infos:
                with zipfp.open(info) as zipopen:
                    data += zipopen.read()
            self.assertIn(data, {b"foobar", b"barfoo"})
            data = b""
            for info in infos:
                data += zipfp.read(info)
            self.assertIn(data, {b"foobar", b"barfoo"})

    def test_universal_deprecation(self):
        f = io.BytesIO()
        with zipfile.ZipFile(f, "w") as zipfp:
            zipfp.writestr('spam.txt', b'ababagalamaga')

        with zipfile.ZipFile(f, "r") as zipfp:
            for mode in 'U', 'rU':
                with self.assertWarns(DeprecationWarning):
                    zipopen = zipfp.open('spam.txt', mode)
                zipopen.close()

    def test_writestr_extended_local_header_issue1202(self):
        with zipfile.ZipFile(TESTFN2, 'w') as orig_zip:
            for data in 'abcdefghijklmnop':
                zinfo = zipfile.ZipInfo(data)
                zinfo.flag_bits |= 0x08  # Include an extended local header.
                orig_zip.writestr(zinfo, data)

    def test_close_on_exception(self):
        """Check that the zipfile is closed if an exception is raised in the
        'with' block."""
        with zipfile.ZipFile(TESTFN2, "w") as zipfp:
            for fpath, fdata in SMALL_TEST_DATA:
                zipfp.writestr(fpath, fdata)

        try:
            with zipfile.ZipFile(TESTFN2, "r") as zipfp2:
                raise zipfile.BadZipFile()
        except zipfile.BadZipFile:
            self.assertIsNone(zipfp2.fp, 'zipfp is not closed')

    def test_write_unicode_filenames(self):
        with zipfile.ZipFile(TESTFN, "w") as zf:
            zf.writestr("foo.txt", "Test for unicode filename")
            zf.writestr("\xf6.txt", "Test for unicode filename")
            self.assertIsInstance(zf.infolist()[0].filename, str)

        with zipfile.ZipFile(TESTFN, "r") as zf:
            self.assertEqual(zf.filelist[0].filename, "foo.txt")
            self.assertEqual(zf.filelist[1].filename, "\xf6.txt")

    def test_close_erroneous_file(self):
        # This test checks that the ZipFile constructor closes the file object
        # it opens if there's an error in the file.  If it doesn't, the
        # traceback holds a reference to the ZipFile object and, indirectly,
        # the file object.
        # On Windows, this causes the os.unlink() call to fail because the
        # underlying file is still open.  This is SF bug #412214.
        #
        with open(TESTFN, "w") as fp:
            fp.write("this is not a legal zip file\n")
        try:
            zf = zipfile.ZipFile(TESTFN)
        except zipfile.BadZipFile:
            pass

    def test_is_zip_erroneous_file(self):
        """Check that is_zipfile() correctly identifies non-zip files."""
        # - passing a filename
        with open(TESTFN, "w") as fp:
            fp.write("this is not a legal zip file\n")
        self.assertFalse(zipfile.is_zipfile(TESTFN))
        # - passing a file object
        with open(TESTFN, "rb") as fp:
            self.assertFalse(zipfile.is_zipfile(fp))
        # - passing a file-like object
        fp = io.BytesIO()
        fp.write(b"this is not a legal zip file\n")
        self.assertFalse(zipfile.is_zipfile(fp))
        fp.seek(0, 0)
        self.assertFalse(zipfile.is_zipfile(fp))

    def test_damaged_zipfile(self):
        """Check that zipfiles with missing bytes at the end raise BadZipFile."""
        # - Create a valid zip file
        fp = io.BytesIO()
        with zipfile.ZipFile(fp, mode="w") as zipf:
            zipf.writestr("foo.txt", b"O, for a Muse of Fire!")
        zipfiledata = fp.getvalue()

        # - Now create copies of it missing the last N bytes and make sure
        #   a BadZipFile exception is raised when we try to open it
        for N in range(len(zipfiledata)):
            fp = io.BytesIO(zipfiledata[:N])
            self.assertRaises(zipfile.BadZipFile, zipfile.ZipFile, fp)

    def test_is_zip_valid_file(self):
        """Check that is_zipfile() correctly identifies zip files."""
        # - passing a filename
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            zipf.writestr("foo.txt", b"O, for a Muse of Fire!")

        self.assertTrue(zipfile.is_zipfile(TESTFN))
        # - passing a file object
        with open(TESTFN, "rb") as fp:
            self.assertTrue(zipfile.is_zipfile(fp))
            fp.seek(0, 0)
            zip_contents = fp.read()
        # - passing a file-like object
        fp = io.BytesIO()
        fp.write(zip_contents)
        self.assertTrue(zipfile.is_zipfile(fp))
        fp.seek(0, 0)
        self.assertTrue(zipfile.is_zipfile(fp))

    def test_empty_file_raises_BadZipFile(self):
        f = open(TESTFN, 'w')
        f.close()
        self.assertRaises(zipfile.BadZipFile, zipfile.ZipFile, TESTFN)

        with open(TESTFN, 'w') as fp:
            fp.write("short file")
        self.assertRaises(zipfile.BadZipFile, zipfile.ZipFile, TESTFN)

    def test_closed_zip_raises_RuntimeError(self):
        """Verify that testzip() doesn't swallow inappropriate exceptions."""
        data = io.BytesIO()
        with zipfile.ZipFile(data, mode="w") as zipf:
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")

        # This is correct; calling .read on a closed ZipFile should raise
        # a RuntimeError, and so should calling .testzip.  An earlier
        # version of .testzip would swallow this exception (and any other)
        # and report that the first file in the archive was corrupt.
        self.assertRaises(RuntimeError, zipf.read, "foo.txt")
        self.assertRaises(RuntimeError, zipf.open, "foo.txt")
        self.assertRaises(RuntimeError, zipf.testzip)
        self.assertRaises(RuntimeError, zipf.writestr, "bogus.txt", "bogus")
        with open(TESTFN, 'w') as f:
            f.write('zipfile test data')
        self.assertRaises(RuntimeError, zipf.write, TESTFN)

    def test_bad_constructor_mode(self):
        """Check that bad modes passed to ZipFile constructor are caught."""
        self.assertRaises(RuntimeError, zipfile.ZipFile, TESTFN, "q")

    def test_bad_open_mode(self):
        """Check that bad modes passed to ZipFile.open are caught."""
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")

        with zipfile.ZipFile(TESTFN, mode="r") as zipf:
        # read the data to make sure the file is there
            zipf.read("foo.txt")
            self.assertRaises(RuntimeError, zipf.open, "foo.txt", "q")

    def test_read0(self):
        """Check that calling read(0) on a ZipExtFile object returns an empty
        string and doesn't advance file pointer."""
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")
            # read the data to make sure the file is there
            with zipf.open("foo.txt") as f:
                for i in range(FIXEDTEST_SIZE):
                    self.assertEqual(f.read(0), b'')

                self.assertEqual(f.read(), b"O, for a Muse of Fire!")

    def test_open_non_existent_item(self):
        """Check that attempting to call open() for an item that doesn't
        exist in the archive raises a RuntimeError."""
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            self.assertRaises(KeyError, zipf.open, "foo.txt", "r")

    def test_bad_compression_mode(self):
        """Check that bad compression methods passed to ZipFile.open are
        caught."""
        self.assertRaises(RuntimeError, zipfile.ZipFile, TESTFN, "w", -1)

    def test_struct_sizes(self):
        """Check that ZIP internal structure sizes are calculated correctly."""
        self.assertEqual(zipfile.sizeEndCentDir, 22)
        self.assertEqual(zipfile.sizeCentralDir, 46)
        self.assertEqual(zipfile.sizeEndCentDir64, 56)
        self.assertEqual(zipfile.sizeEndCentDir64Locator, 20)

    def test_comments(self):
        """Check that comments on the archive are handled properly."""

        # check default comment is empty
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            self.assertEqual(zipf.comment, b'')
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")

        with zipfile.ZipFile(TESTFN, mode="r") as zipfr:
            self.assertEqual(zipfr.comment, b'')

        # check a simple short comment
        comment = b'Bravely taking to his feet, he beat a very brave retreat.'
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            zipf.comment = comment
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")
        with zipfile.ZipFile(TESTFN, mode="r") as zipfr:
            self.assertEqual(zipf.comment, comment)

        # check a comment of max length
        comment2 = ''.join(['%d' % (i**3 % 10) for i in range((1 << 16)-1)])
        comment2 = comment2.encode("ascii")
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            zipf.comment = comment2
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")

        with zipfile.ZipFile(TESTFN, mode="r") as zipfr:
            self.assertEqual(zipfr.comment, comment2)

        # check a comment that is too long is truncated
        with zipfile.ZipFile(TESTFN, mode="w") as zipf:
            with self.assertWarns(UserWarning):
                zipf.comment = comment2 + b'oops'
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")
        with zipfile.ZipFile(TESTFN, mode="r") as zipfr:
            self.assertEqual(zipfr.comment, comment2)

        # check that comments are correctly modified in append mode
        with zipfile.ZipFile(TESTFN,mode="w") as zipf:
            zipf.comment = b"original comment"
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")
        with zipfile.ZipFile(TESTFN,mode="a") as zipf:
            zipf.comment = b"an updated comment"
        with zipfile.ZipFile(TESTFN,mode="r") as zipf:
            self.assertEqual(zipf.comment, b"an updated comment")

        # check that comments are correctly shortened in append mode
        with zipfile.ZipFile(TESTFN,mode="w") as zipf:
            zipf.comment = b"original comment that's longer"
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")
        with zipfile.ZipFile(TESTFN,mode="a") as zipf:
            zipf.comment = b"shorter comment"
        with zipfile.ZipFile(TESTFN,mode="r") as zipf:
            self.assertEqual(zipf.comment, b"shorter comment")

    def test_unicode_comment(self):
        with zipfile.ZipFile(TESTFN, "w", zipfile.ZIP_STORED) as zipf:
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")
            with self.assertRaises(TypeError):
                zipf.comment = "this is an error"

    def test_change_comment_in_empty_archive(self):
        with zipfile.ZipFile(TESTFN, "a", zipfile.ZIP_STORED) as zipf:
            self.assertFalse(zipf.filelist)
            zipf.comment = b"this is a comment"
        with zipfile.ZipFile(TESTFN, "r") as zipf:
            self.assertEqual(zipf.comment, b"this is a comment")

    def test_change_comment_in_nonempty_archive(self):
        with zipfile.ZipFile(TESTFN, "w", zipfile.ZIP_STORED) as zipf:
            zipf.writestr("foo.txt", "O, for a Muse of Fire!")
        with zipfile.ZipFile(TESTFN, "a", zipfile.ZIP_STORED) as zipf:
            self.assertTrue(zipf.filelist)
            zipf.comment = b"this is a comment"
        with zipfile.ZipFile(TESTFN, "r") as zipf:
            self.assertEqual(zipf.comment, b"this is a comment")

    def test_empty_zipfile(self):
        # Check that creating a file in 'w' or 'a' mode and closing without
        # adding any files to the archives creates a valid empty ZIP file
        zipf = zipfile.ZipFile(TESTFN, mode="w")
        zipf.close()
        try:
            zipf = zipfile.ZipFile(TESTFN, mode="r")
        except zipfile.BadZipFile:
            self.fail("Unable to create empty ZIP file in 'w' mode")

        zipf = zipfile.ZipFile(TESTFN, mode="a")
        zipf.close()
        try:
            zipf = zipfile.ZipFile(TESTFN, mode="r")
        except:
            self.fail("Unable to create empty ZIP file in 'a' mode")

       
class AbstractBadCrcTests:
    def test_testzip_with_bad_crc(self):
        """Tests that files with bad CRCs return their name from testzip."""
        zipdata = self.zip_with_bad_crc

        with zipfile.ZipFile(io.BytesIO(zipdata), mode="r") as zipf:
            # testzip returns the name of the first corrupt file, or None
            self.assertEqual('afile', zipf.testzip())

    def test_read_with_bad_crc(self):
        """Tests that files with bad CRCs raise a BadZipFile exception when read."""
        zipdata = self.zip_with_bad_crc

        # Using ZipFile.read()
        with zipfile.ZipFile(io.BytesIO(zipdata), mode="r") as zipf:
            self.assertRaises(zipfile.BadZipFile, zipf.read, 'afile')

        with zipfile.ZipFile(f, "w", compression) as zipfp:
            zipfp.write(TESTFN, "another.name")
            zipfp.write(TESTFN, TESTFN)

        with zipfile.ZipFile(f, "r", compression) as zipfp:
            testdata = zipfp.read(TESTFN)

        with zipfile.ZipFile(f, "r", compression) as zipfp:
            zipdata1 = []
            with zipfp.open(TESTFN) as zipopen1:
                while True:
                    read_data = zipopen1.read(256)
                    if not read_data:
                        break
                    zipdata1.append(read_data)

            zipdata2 = []
            with zipfp.open("another.name") as zipopen2:
                while True:
                    read_data = zipopen2.read(256)
                    if not read_data:
                        break
                    zipdata2.append(read_data)

            testdata1 = b''.join(zipdata1)
            self.assertEqual(len(testdata1), len(self.data))
            self.assertEqual(testdata1, self.data)

            testdata2 = b''.join(zipdata2)
            self.assertEqual(len(testdata2), len(self.data))
            self.assertEqual(testdata2, self.data)

        # Read the ZIP archive
        with zipfile.ZipFile(f, "r", compression) as zipfp:
            zipdata1 = []
            with zipfp.open(TESTFN) as zipopen1:
                while True:
                    read_data = zipopen1.read(randint(1, 1024))
                    if not read_data:
                        break
                    zipdata1.append(read_data)

            testdata = b''.join(zipdata1)
            self.assertEqual(len(testdata), len(self.data))
            self.assertEqual(testdata, self.data)

    def test_random_open(self):
        for f in get_files(self):
            self.zip_random_open_test(f, self.compression)

    def test_same_file(self):
        # Verify that (when the ZipFile is in control of creating file objects)
        # multiple open() calls can be made without interfering with each other.
        self.make_test_archive(TESTFN2)
        with zipfile.ZipFile(TESTFN2, mode="r") as zipf:
            with zipf.open('ones') as zopen1, zipf.open('ones') as zopen2:
                data1 = zopen1.read(500)
                data2 = zopen2.read(500)
                data1 += zopen1.read()
                data2 += zopen2.read()
            self.assertEqual(data1, data2)
            self.assertEqual(data1, self.data1)

    def test_different_file(self):
        # Verify that (when the ZipFile is in control of creating file objects)
        # multiple open() calls can be made without interfering with each other.
        self.make_test_archive(TESTFN2)
        with zipfile.ZipFile(TESTFN2, mode="r") as zipf:
            with zipf.open('ones') as zopen1, zipf.open('twos') as zopen2:
                data1 = zopen1.read(500)
                data2 = zopen2.read(500)
                data1 += zopen1.read()
                data2 += zopen2.read()
            self.assertEqual(data1, self.data1)
            self.assertEqual(data2, self.data2)


class TestWithDirectory(unittest.TestCase):
    def setUp(self):
        os.mkdir(TESTFN2)

    def test_extract_dir(self):
        with zipfile.ZipFile(findfile("zipdir.zip")) as zipf:
            zipf.extractall(TESTFN2)
        self.assertTrue(os.path.isdir(os.path.join(TESTFN2, "a")))
        self.assertTrue(os.path.isdir(os.path.join(TESTFN2, "a", "b")))
        self.assertTrue(os.path.exists(os.path.join(TESTFN2, "a", "b", "c")))

    def test_bug_6050(self):
        # Extraction should succeed if directories already exist
        os.mkdir(os.path.join(TESTFN2, "a"))
        self.test_extract_dir()

    def test_write_dir(self):
        dirpath = os.path.join(TESTFN2, "x")
        os.mkdir(dirpath)
        mode = os.stat(dirpath).st_mode & 0xFFFF
        with zipfile.ZipFile(TESTFN, "w") as zipf:
            zipf.write(dirpath)
            zinfo = zipf.filelist[0]
            self.assertTrue(zinfo.filename.endswith("/x/"))
            self.assertEqual(zinfo.external_attr, (mode << 16) | 0x10)
            zipf.write(dirpath, "y")
            zinfo = zipf.filelist[1]
            self.assertTrue(zinfo.filename, "y/")
            self.assertEqual(zinfo.external_attr, (mode << 16) | 0x10)
        with zipfile.ZipFile(TESTFN, "r") as zipf:
            zinfo = zipf.filelist[0]
            self.assertTrue(zinfo.filename.endswith("/x/"))
            self.assertEqual(zinfo.external_attr, (mode << 16) | 0x10)
            zinfo = zipf.filelist[1]
            self.assertTrue(zinfo.filename, "y/")
            self.assertEqual(zinfo.external_attr, (mode << 16) | 0x10)
            target = os.path.join(TESTFN2, "target")
            os.mkdir(target)
            zipf.extractall(target)
            self.assertTrue(os.path.isdir(os.path.join(target, "y")))
            self.assertEqual(len(os.listdir(target)), 2)

    def test_writestr_dir(self):
        os.mkdir(os.path.join(TESTFN2, "x"))
        with zipfile.ZipFile(TESTFN, "w") as zipf:
            zipf.writestr("x/", b'')
            zinfo = zipf.filelist[0]
            self.assertEqual(zinfo.filename, "x/")
            self.assertEqual(zinfo.external_attr, (0o40775 << 16) | 0x10)
        with zipfile.ZipFile(TESTFN, "r") as zipf:
            zinfo = zipf.filelist[0]
            self.assertTrue(zinfo.filename.endswith("x/"))
            self.assertEqual(zinfo.external_attr, (0o40775 << 16) | 0x10)
            target = os.path.join(TESTFN2, "target")
            os.mkdir(target)
            zipf.extractall(target)
            self.assertTrue(os.path.isdir(os.path.join(target, "x")))
            self.assertEqual(os.listdir(target), ["x"])


==============================================================================================================
==============================================================================================================
==============================================================================================================
==============================================================================================================
    
                zipfp.writestr(fpath, fdata)




zipfile.ZIP_FILECOUNT_LIMIT






    def zip_test(self, f, compression):
        with zipfile.ZipFile(f, "w", compression, allowZip64=True) as zipfp:
            zipfp.write(TESTFN, "another.name")
            zipfp.write(TESTFN, TESTFN)
            zipfp.writestr("strfile", self.data)

        # Read the ZIP archive
        with zipfile.ZipFile(f, "r", compression) as zipfp:
            self.assertEqual(zipfp.read(TESTFN), self.data)
            self.assertEqual(zipfp.read("another.name"), self.data)
            self.assertEqual(zipfp.read("strfile"), self.data)

            # Print the ZIP directory
            fp = io.StringIO()
            zipfp.printdir(fp)

            directory = fp.getvalue()
            lines = directory.splitlines()
            self.assertEqual(len(lines), 4) # Number of files + header

            self.assertIn('File Name', lines[0])
            self.assertIn('Modified', lines[0])
            self.assertIn('Size', lines[0])

            # Check the namelist
            names = zipfp.namelist()
            self.assertEqual(len(names), 3)
            self.assertIn(TESTFN, names)
            self.assertIn("another.name", names)
            self.assertIn("strfile", names)

            # Check infolist
            infos = zipfp.infolist()
            names = [i.filename for i in infos]
            self.assertEqual(len(names), 3)
            self.assertIn(TESTFN, names)
            self.assertIn("another.name", names)
            self.assertIn("strfile", names)
            for i in infos:
                self.assertEqual(i.file_size, len(self.data))




