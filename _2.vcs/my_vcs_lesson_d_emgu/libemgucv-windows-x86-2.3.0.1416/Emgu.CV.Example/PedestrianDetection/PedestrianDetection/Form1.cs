using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Runtime.InteropServices;

using Emgu.CV;
using Emgu.CV.GPU;
using Emgu.CV.Structure;
using Emgu.CV.UI;


namespace PedestrianDetection
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\_emgu\pedestrian.png";

            Image<Bgr, Byte> image = new Image<Bgr, byte>(filename);

            Stopwatch watch;
            Rectangle[] regions;

            //check if there is a compatible GPU to run pedestrian detection
            if (GpuInvoke.HasCuda)
            {  //this is the GPU version
                using (GpuHOGDescriptor des = new GpuHOGDescriptor())
                {
                    des.SetSVMDetector(GpuHOGDescriptor.GetDefaultPeopleDetector());

                    watch = Stopwatch.StartNew();
                    using (GpuImage<Bgr, Byte> gpuImg = new GpuImage<Bgr, byte>(image))
                    using (GpuImage<Bgra, Byte> gpuBgra = gpuImg.Convert<Bgra, Byte>())
                    {
                        regions = des.DetectMultiScale(gpuBgra);
                    }
                }
            }
            else
            {  //this is the CPU version
                using (HOGDescriptor des = new HOGDescriptor())
                {
                    des.SetSVMDetector(HOGDescriptor.GetDefaultPeopleDetector());

                    watch = Stopwatch.StartNew();
                    regions = des.DetectMultiScale(image);
                }
            }
            watch.Stop();

            foreach (Rectangle pedestrain in regions)
            {
                image.Draw(pedestrain, new Bgr(Color.Red), 1);
            }

            /*
            ImageViewer.Show(
               image,
               String.Format("Pedestrain detection using {0} in {1} milliseconds.",GpuInvoke.HasCuda ? "GPU" : "CPU",watch.ElapsedMilliseconds)
            */


            //display the image 
            pictureBox1.Image = image.ToBitmap();

            string str = String.Format("Pedestrain detection using {0} in {1} milliseconds.", GpuInvoke.HasCuda ? "GPU" : "CPU", watch.ElapsedMilliseconds);
            richTextBox1.Text += str + "\n";




        }
    }
}
