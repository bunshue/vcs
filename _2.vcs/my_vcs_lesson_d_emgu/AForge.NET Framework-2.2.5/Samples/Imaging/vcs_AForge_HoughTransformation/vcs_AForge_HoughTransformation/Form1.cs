﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.IO;

using AForge;
using AForge.Imaging;
using AForge.Imaging.Filters;

namespace vcs_AForge_HoughTransformation
{
    public partial class Form1 : Form
    {
        string filename = Path.Combine(Application.StartupPath, "..\\..\\sample.bmp");

        // binarization filtering sequence
        private FiltersSequence filter = new FiltersSequence(
            Grayscale.CommonAlgorithms.BT709,
            new Threshold(64)
        );

        HoughLineTransformation lineTransform = new HoughLineTransformation();
        HoughCircleTransformation circleTransform = new HoughCircleTransformation(35);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            lineTransform.MinLineIntensity = 10;
            circleTransform.MinCircleIntensity = 20;

            label1.Text = "原圖                                                            Hough Line                                                 HoughCircle";
            open_image_file();
        }

        void open_image_file()
        {
            try
            {
                // load image
                Bitmap tempImage = (Bitmap)Bitmap.FromFile(filename);
                Bitmap image = AForge.Imaging.Image.Clone(tempImage, PixelFormat.Format24bppRgb);
                tempImage.Dispose();
                // format image
                AForge.Imaging.Image.FormatImage(ref image);
                // lock the source image
                BitmapData sourceData = image.LockBits(
                    new Rectangle(0, 0, image.Width, image.Height),
                    ImageLockMode.ReadOnly, image.PixelFormat);
                // binarize the image
                UnmanagedImage binarySource = filter.Apply(new UnmanagedImage(sourceData));

                // apply Hough line transofrm
                lineTransform.ProcessImage(binarySource);
                // get lines using relative intensity
                HoughLine[] lines = lineTransform.GetLinesByRelativeIntensity(0.2);

                foreach (HoughLine line in lines)
                {
                    string s = string.Format("Theta = {0}, R = {1}, I = {2} ({3})", line.Theta, line.Radius, line.Intensity, line.RelativeIntensity);
                    System.Diagnostics.Debug.WriteLine(s);

                    // uncomment to highlight detected lines
                    /*
                    // get line's radius and theta values
                    int    r = line.Radius;
                    double t = line.Theta;

                    // check if line is in lower part of the image
                    if ( r < 0 )
                    {
                        t += 180;
                        r = -r;
                    }

                    // convert degrees to radians
                    t = ( t / 180 ) * Math.PI;

                    // get image centers (all coordinate are measured relative
                    // to center)
                    int w2 = image.Width /2;
                    int h2 = image.Height / 2;

                    double x0 = 0, x1 = 0, y0 = 0, y1 = 0;

                    if ( line.Theta != 0 )
                    {
                        // none vertical line
                        x0 = -w2; // most left point
                        x1 = w2;  // most right point

                        // calculate corresponding y values
                        y0 = ( -Math.Cos( t ) * x0 + r ) / Math.Sin( t );
                        y1 = ( -Math.Cos( t ) * x1 + r ) / Math.Sin( t );
                    }
                    else
                    {
                        // vertical line
                        x0 = line.Radius;
                        x1 = line.Radius;

                        y0 = h2;
                        y1 = -h2;
                    }

                    // draw line on the image
                    Drawing.Line( sourceData,
                        new IntPoint( (int) x0 + w2, h2 - (int) y0 ),
                        new IntPoint( (int) x1 + w2, h2 - (int) y1 ),
                        Color.Red ); */
                }

                System.Diagnostics.Debug.WriteLine("Found lines: " + lineTransform.LinesCount);
                System.Diagnostics.Debug.WriteLine("Max intensity: " + lineTransform.MaxIntensity);

                // apply Hough circle transform
                circleTransform.ProcessImage(binarySource);
                // get circles using relative intensity
                HoughCircle[] circles = circleTransform.GetCirclesByRelativeIntensity(0.5);

                foreach (HoughCircle circle in circles)
                {
                    string s = string.Format("X = {0}, Y = {1}, I = {2} ({3})", circle.X, circle.Y, circle.Intensity, circle.RelativeIntensity);
                    System.Diagnostics.Debug.WriteLine(s);
                }

                System.Diagnostics.Debug.WriteLine("Found circles: " + circleTransform.CirclesCount);
                System.Diagnostics.Debug.WriteLine("Max intensity: " + circleTransform.MaxIntensity);

                // unlock source image
                image.UnlockBits(sourceData);
                // dispose temporary binary source image
                binarySource.Dispose();

                // show images
                pictureBox1.Image = image;
                pictureBox2.Image = lineTransform.ToBitmap();
                pictureBox3.Image = circleTransform.ToBitmap();
            }
            catch
            {
                MessageBox.Show("Failed loading the image", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
