using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Linq;

using System.IO;

// Program to view simple DICOM images.
// Written by Amarnath S, Mahesh Reddy S, Bangalore, India, April 2009.
// Updated along with Harsha T, April 2010 to include Window/Level
// Updated by Amarnath S, July 2010, to include Ultrasound images of 8-bit depth, 3 samples per pixel (RGB).
// Updated July 2012 to incorporate Zoom 1:1 and Zoom To Fit.
// Updated Aug 2013 to accommodate earlier DICOM files.
// Updated Oct 2020 for a couple of bug fixes.

// Inspired by ImageJ

namespace vcs_ReadWrite_DICOM
{
    public enum ImageBitsPerPixel { Eight, Sixteen, TwentyFour };
    public enum ViewSettings { Zoom1_1, ZoomToFit };

    /// <summary>
    /// This program reads in a DICOM file and displays it on the screen. 
    /// The functionality for viewer is:
    /// o Open DICOM files created as per DICOM 3.0 standard
    /// o Open files with Explicit VR and Implicit VR Transfer Syntax
    /// o Read those files where image bit depth is 8 or 16 bits (Digital Radiography), 
    ///    or RGB images (from Ultrasound)
    /// o Read a DICOM file with just one image inside it
    /// o Read a DICONDE file also (a DICONDE file is a DICOM file with NDE - Non Destructive   
    ///    Evaluation - tags inside it)
    /// o Read older DICOM files. Earlier DICOM files don't have the preamble and prefix, and 
    ///    just contain the string 1.2.840.10008 somewhere in the beginning
    /// o Perform Window/Level operations on the image.
    /// 
    /// This viewer is not intended to:
    /// o Check whether all mandatory tags are present
    /// o Open files with VR other than Explicit and Implicit - in particular, not to open 
    ///    JPEG Lossy and Lossless files

    /// o Read a sequence of images. 
    /// </summary>
    public partial class MainForm : Form
    {
        DicomDecoder dd;
        List<byte> pixels8;
        List<ushort> pixels16;
        List<byte> pixels24; // 30 July 2010
        int imageWidth;
        int imageHeight;
        int bitDepth;
        int samplesPerPixel;  // Updated 30 July 2010
        bool imageOpened;
        double winCentre;
        double winWidth;
        bool signedImage;
        int maxPixelValue;    // Updated July 2012
        int minPixelValue;

        public MainForm()
        {
            InitializeComponent();
            dd = new DicomDecoder();
            pixels8 = new List<byte>();
            pixels16 = new List<ushort>();
            pixels24 = new List<byte>();
            imageOpened = false;
            signedImage = false;
            maxPixelValue = 0;
            minPixelValue = 65535;
        }

        private void bnOpen_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_dicom\test.dcm";
            //string filename = @"C:\______test_files\__RW\_dicom\ims000525.dcm";

            Cursor = Cursors.WaitCursor;
            ReadAndDisplayDicomFile(filename);
            imageOpened = true;
            Cursor = Cursors.Default;
        }

        private void ReadAndDisplayDicomFile(string fileName)
        {
            dd.DicomFileName = fileName;

            TypeOfDicomFile typeOfDicomFile = dd.typeofDicomFile;

            if (typeOfDicomFile == TypeOfDicomFile.Dicom3File || typeOfDicomFile == TypeOfDicomFile.DicomOldTypeFile)
            {
                imageWidth = dd.width;
                imageHeight = dd.height;
                bitDepth = dd.bitsAllocated;
                winCentre = dd.windowCentre;
                winWidth = dd.windowWidth;
                samplesPerPixel = dd.samplesPerPixel;
                signedImage = dd.signedImage;

                label1.Visible = true;
                label2.Visible = true;
                label3.Visible = true;
                label4.Visible = true;
                bnSave.Enabled = true;
                bnTags.Enabled = true;
                bnResetWL.Enabled = true;
                label2.Text = imageWidth.ToString() + " X " + imageHeight.ToString();
                if (samplesPerPixel == 1)
                {
                    label4.Text = bitDepth.ToString() + " bit";
                }
                else
                {
                    label4.Text = bitDepth.ToString() + " bit, " + samplesPerPixel + " samples per pixel";
                }

                imagePanelControl.NewImage = true;
                Text = "DICOM Image Viewer: " + fileName;

                if (samplesPerPixel == 1 && bitDepth == 8)
                {
                    pixels8.Clear();
                    pixels16.Clear();
                    pixels24.Clear();
                    dd.GetPixels8(ref pixels8);

                    // This is primarily for debugging purposes, 
                    //  to view the pixel values as ascii data.
                    //if (true)
                    //{
                    //    StreamWriter file = new StreamWriter(
                    //               "C:\\imageSigned.txt");

                    //    for (int ik = 0; ik < pixels8.Count; ++ik)
                    //        file.Write(pixels8[ik] + "  ");

                    //    file.Close();
                    //}

                    minPixelValue = pixels8.Min();
                    maxPixelValue = pixels8.Max();

                    // Bug fix dated 24 Aug 2013 - for proper window/level of signed images
                    // Thanks to Matias Montroull from Argentina for pointing this out.
                    if (dd.signedImage)
                    {
                        winCentre -= char.MinValue;
                    }

                    if (Math.Abs(winWidth) < 0.001)
                    {
                        winWidth = maxPixelValue - minPixelValue;
                    }

                    if ((winCentre == 0) || (minPixelValue > winCentre) || (maxPixelValue < winCentre))
                    {
                        winCentre = (maxPixelValue + minPixelValue) / 2;
                    }

                    imagePanelControl.SetParameters(ref pixels8, imageWidth, imageHeight, winWidth, winCentre, samplesPerPixel, true, this);
                }

                if (samplesPerPixel == 1 && bitDepth == 16)
                {
                    pixels16.Clear();
                    pixels8.Clear();
                    pixels24.Clear();
                    dd.GetPixels16(ref pixels16);

                    // This is primarily for debugging purposes, 
                    //  to view the pixel values as ascii data.
                    //if (true)
                    //{
                    //    StreamWriter file = new StreamWriter(
                    //               "C:\\imageSigned.txt");

                    //    for (int ik = 0; ik < pixels16.Count; ++ik)
                    //        file.Write(pixels16[ik] + "  ");

                    //    file.Close();
                    //}

                    minPixelValue = pixels16.Min();
                    maxPixelValue = pixels16.Max();

                    // Bug fix dated 24 Aug 2013 - for proper window/level of signed images
                    // Thanks to Matias Montroull from Argentina for pointing this out.
                    if (dd.signedImage)
                    {
                        winCentre -= short.MinValue;
                    }

                    if (Math.Abs(winWidth) < 0.001)
                    {
                        winWidth = maxPixelValue - minPixelValue;
                    }

                    if ((winCentre == 0) || (minPixelValue > winCentre) || (maxPixelValue < winCentre))
                    {
                        winCentre = (maxPixelValue + minPixelValue) / 2;
                    }

                    imagePanelControl.Signed16Image = dd.signedImage;

                    imagePanelControl.SetParameters(ref pixels16, imageWidth, imageHeight, winWidth, winCentre, true, this);
                }

                if (samplesPerPixel == 3 && bitDepth == 8)
                {
                    // This is an RGB colour image
                    pixels8.Clear();
                    pixels16.Clear();
                    pixels24.Clear();
                    dd.GetPixels24(ref pixels24);

                    // This code segment is primarily for debugging purposes, 
                    //    to view the pixel values as ascii data.
                    //if (true)
                    //{
                    //    StreamWriter file = new StreamWriter(
                    //                      "C:\\image24.txt");

                    //    for (int ik = 0; ik < pixels24.Count; ++ik)
                    //        file.Write(pixels24[ik] + "  ");

                    //    file.Close();
                    //}

                    imagePanelControl.SetParameters(ref pixels24, imageWidth, imageHeight, winWidth, winCentre, samplesPerPixel, true, this);
                }
            }
            else
            {
                if (typeOfDicomFile == TypeOfDicomFile.DicomUnknownTransferSyntax)
                {
                    MessageBox.Show("Sorry, I can't read a DICOM file with this Transfer Syntax.", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
                else
                {
                    MessageBox.Show("Sorry, I can't open this file. " + "This file does not appear to contain a DICOM image.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }

                Text = "DICOM Image Viewer: ";
                // Show a plain grayscale image instead
                pixels8.Clear();
                pixels16.Clear();
                pixels24.Clear();
                samplesPerPixel = 1;

                imageWidth = imagePanelControl.Width - 25;   // 25 is a magic number
                imageHeight = imagePanelControl.Height - 25; // Same magic number
                int iNoPix = imageWidth * imageHeight;

                for (int i = 0; i < iNoPix; ++i)
                {
                    pixels8.Add(240);// 240 is the grayvalue corresponding to the Control colour
                }
                winWidth = 256;
                winCentre = 127;
                imagePanelControl.SetParameters(ref pixels8, imageWidth, imageHeight, winWidth, winCentre, samplesPerPixel, true, this);
                imagePanelControl.Invalidate();
                label1.Visible = false;
                label2.Visible = false;
                label3.Visible = false;
                label4.Visible = false;
                bnSave.Enabled = false;
                bnTags.Enabled = false;
                bnResetWL.Enabled = false;
            }
        }

        private void bnTags_Click(object sender, EventArgs e)
        {
            if (imageOpened == true)
            {
                List<string> str = dd.dicomInfo;

                DicomTagsForm dtf = new DicomTagsForm();
                dtf.SetString(ref str);
                dtf.ShowDialog();

                imagePanelControl.Invalidate();
            }
            else
            {
                richTextBox1.Text += "尚未開啟DICOM圖片\n";
            }
        }

        private void bnSave_Click(object sender, EventArgs e)
        {
            if (imageOpened == true)
            {
                string filename = Application.StartupPath + "\\png_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
                imagePanelControl.SaveImage(filename);

                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            else
            {
                richTextBox1.Text += "尚未開啟DICOM圖片\n";
            }

            imagePanelControl.Invalidate();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            label1.Visible = false;
            label2.Visible = false;
            label3.Visible = false;
            label4.Visible = false;
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            pixels8.Clear();
            pixels16.Clear();
            if (imagePanelControl != null)
            {
                imagePanelControl.Dispose();
            }
        }

        private void bnResetWL_Click(object sender, EventArgs e)
        {
            if ((pixels8.Count > 0) || (pixels16.Count > 0) || (pixels24.Count > 0))
            {
                imagePanelControl.ResetValues();
                if (bitDepth == 8)
                {
                    if (samplesPerPixel == 1)
                    {
                        imagePanelControl.SetParameters(ref pixels8, imageWidth, imageHeight, winWidth, winCentre, samplesPerPixel, false, this);
                    }
                    else // samplesPerPixel == 3
                    {
                        imagePanelControl.SetParameters(ref pixels24, imageWidth, imageHeight, winWidth, winCentre, samplesPerPixel, false, this);
                    }
                }

                if (bitDepth == 16)
                {
                    imagePanelControl.SetParameters(ref pixels16, imageWidth, imageHeight, winWidth, winCentre, false, this);
                }
            }
            else
            {
                richTextBox1.Text += "尚未開啟DICOM圖片\n";
            }
        }

        public void UpdateWindowLevel(int winWidth, int winCentre, ImageBitsPerPixel bpp)
        {
            int winMin = Convert.ToInt32(winCentre - 0.5 * winWidth);
            int winMax = winMin + winWidth;
            this.windowLevelControl.SetWindowWidthCentre(winMin, winMax, winWidth, winCentre, bpp, signedImage);
        }

        private void viewSettingsCheckedChanged(object sender, EventArgs e)
        {
            if (rbZoom1_1.Checked)
            {
                imagePanelControl.viewSettings = ViewSettings.Zoom1_1;
            }
            else
            {
                imagePanelControl.viewSettings = ViewSettings.ZoomToFit;
            }

            imagePanelControl.viewSettingsChanged = true;
            imagePanelControl.Invalidate();
        }
    }
}

