using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.CV.UI;
using System.Diagnostics;

namespace TrafficSignRecognition
{
    public partial class Form1 : Form
    {
        private StopSignDetector _stopSignDetector;

        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            _stopSignDetector = new StopSignDetector();

            string filename = @"C:\______test_files\_emgu\stop-sign.jpg";

            ProcessImage(new Image<Bgr, byte>(filename));
        }

        private void ProcessImage(Image<Bgr, byte> image)
        {
            Stopwatch watch = Stopwatch.StartNew(); // time the detection process

            List<Image<Gray, Byte>> stopSignList = new List<Image<Gray, byte>>();
            List<Rectangle> stopSignBoxList = new List<Rectangle>();
            _stopSignDetector.DetectStopSign(image, stopSignList, stopSignBoxList);

            watch.Stop(); //stop the timer
            processTimeLabel.Text = String.Format("Stop Sign Detection time: {0} milli-seconds", watch.Elapsed.TotalMilliseconds);

            panel1.Controls.Clear();
            Point startPoint = new Point(10, 10);

            for (int i = 0; i < stopSignList.Count; i++)
            {
                Rectangle rect = stopSignBoxList[i];
                AddLabelAndImage(
                   ref startPoint,
                   String.Format("Stop Sign [{0},{1}]:", rect.Location.Y + rect.Width / 2, rect.Location.Y + rect.Height / 2),
                   stopSignList[i]);
                image.Draw(rect, new Bgr(Color.Aquamarine), 2);
            }

            imageBox1.Image = image;
        }

        private void AddLabelAndImage(ref Point startPoint, String labelText, IImage image)
        {
            Label label = new Label();
            panel1.Controls.Add(label);
            label.Text = labelText;
            label.Width = 100;
            label.Height = 30;
            label.Location = startPoint;
            startPoint.Y += label.Height;

            ImageBox box = new ImageBox();
            panel1.Controls.Add(box);
            box.ClientSize = image.Size;
            box.Image = image;
            box.Location = startPoint;
            startPoint.Y += box.Height + 10;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DialogResult result = openFileDialog1.ShowDialog();
            if (result == DialogResult.OK)
            {
                Image<Bgr, Byte> img;
                try
                {
                    img = new Image<Bgr, byte>(openFileDialog1.FileName);
                }
                catch
                {
                    MessageBox.Show("Invalide file format");
                    return;
                }

                ProcessImage(img);
            }
        }


    }
}
