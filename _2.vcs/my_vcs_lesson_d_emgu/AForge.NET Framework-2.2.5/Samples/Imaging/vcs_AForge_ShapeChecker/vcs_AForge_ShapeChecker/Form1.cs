using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for BitmapData
using System.IO;                //for Path

using AForge;
using AForge.Imaging;
using AForge.Imaging.Filters;
using AForge.Math.Geometry;

namespace vcs_AForge_ShapeChecker
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = Path.Combine(Application.StartupPath, "..\\..\\img\\demo2.png");
            LoadDemo(filename);
        }

        // Load one of the embedded demo image
        private void LoadDemo(string filename)
        {
            Bitmap image = new Bitmap(filename);
            ProcessImage(image);
        }

        // Process image
        private void ProcessImage(Bitmap bitmap)
        {
            // lock image
            BitmapData bitmapData = bitmap.LockBits(new Rectangle(0, 0, bitmap.Width, bitmap.Height), ImageLockMode.ReadWrite, bitmap.PixelFormat);

            // step 1 - turn background to black
            ColorFiltering colorFilter = new ColorFiltering();

            colorFilter.Red = new IntRange(0, 64);
            colorFilter.Green = new IntRange(0, 64);
            colorFilter.Blue = new IntRange(0, 64);
            colorFilter.FillOutsideRange = false;

            colorFilter.ApplyInPlace(bitmapData);

            // step 2 - locating objects
            BlobCounter blobCounter = new BlobCounter();

            blobCounter.FilterBlobs = true;
            blobCounter.MinHeight = 5;
            blobCounter.MinWidth = 5;

            blobCounter.ProcessImage(bitmapData);
            Blob[] blobs = blobCounter.GetObjectsInformation();
            bitmap.UnlockBits(bitmapData);

            // step 3 - check objects' type and highlight
            SimpleShapeChecker shapeChecker = new SimpleShapeChecker();

            Graphics g = Graphics.FromImage(bitmap);
            Pen yellowPen = new Pen(Color.Yellow, 2); // circles
            Pen redPen = new Pen(Color.Red, 2);       // quadrilateral
            Pen brownPen = new Pen(Color.Brown, 2);   // quadrilateral with known sub-type
            Pen greenPen = new Pen(Color.Green, 2);   // known triangle
            Pen bluePen = new Pen(Color.Blue, 2);     // triangle

            for (int i = 0, n = blobs.Length; i < n; i++)
            {
                List<IntPoint> edgePoints = blobCounter.GetBlobsEdgePoints(blobs[i]);

                AForge.Point center;
                float radius;

                // is circle ?
                if (shapeChecker.IsCircle(edgePoints, out center, out radius))
                {
                    g.DrawEllipse(yellowPen,
                        (float)(center.X - radius), (float)(center.Y - radius),
                        (float)(radius * 2), (float)(radius * 2));
                }
                else
                {
                    List<IntPoint> corners;

                    // is triangle or quadrilateral
                    if (shapeChecker.IsConvexPolygon(edgePoints, out corners))
                    {
                        // get sub-type
                        PolygonSubType subType = shapeChecker.CheckPolygonSubType(corners);

                        Pen pen;

                        if (subType == PolygonSubType.Unknown)
                        {
                            pen = (corners.Count == 4) ? redPen : bluePen;
                        }
                        else
                        {
                            pen = (corners.Count == 4) ? brownPen : greenPen;
                        }

                        g.DrawPolygon(pen, ToPointsArray(corners));
                    }
                }
            }

            yellowPen.Dispose();
            redPen.Dispose();
            greenPen.Dispose();
            bluePen.Dispose();
            brownPen.Dispose();
            g.Dispose();

            // put new image to clipboard
            Clipboard.SetDataObject(bitmap);
            // and to picture box
            pictureBox1.Image = bitmap;
        }

        // Conver list of AForge.NET's points to array of .NET points
        private System.Drawing.Point[] ToPointsArray(List<IntPoint> points)
        {
            System.Drawing.Point[] array = new System.Drawing.Point[points.Count];

            for (int i = 0, n = points.Count; i < n; i++)
            {
                array[i] = new System.Drawing.Point(points[i].X, points[i].Y);
            }
            return array;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Path.Combine(Application.StartupPath, "..\\..\\img\\coins.jpg");
            LoadDemo(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = Path.Combine(Application.StartupPath, "..\\..\\img\\demo.png");
            LoadDemo(filename);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = Path.Combine(Application.StartupPath, "..\\..\\img\\demo1.png");
            LoadDemo(filename);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = Path.Combine(Application.StartupPath, "..\\..\\img\\demo2.png");
            LoadDemo(filename);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1\";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    //ProcessImage((Bitmap)Bitmap.FromFile(openFileDialog1.FileName));
                    LoadDemo(openFileDialog1.FileName);
                }
                catch
                {
                    MessageBox.Show("Failed loading selected image file.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }
    }
}


