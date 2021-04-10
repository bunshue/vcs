using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Emgu.CV;
using Emgu.CV.Structure;
using Emgu.CV.UI;
using System.Diagnostics;
using System.Runtime.InteropServices;

namespace LatentSvmDetectorExample
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            if (!IsPlaformCompatable()) return;
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Run();
        }

        static void Run()
        {
            string filename_jpg = @"C:\______test_files\_emgu\cat.jpg";
            string filename_xml = @"C:\______test_files\_emgu\cat.xml";

            using (Image<Bgr, Byte> image = new Image<Bgr, byte>(filename_jpg))
            using (LatentSvmDetector detector = new LatentSvmDetector(filename_xml))
            {
                Stopwatch watch = Stopwatch.StartNew();
                MCvObjectDetection[] regions = detector.Detect(image, 0.5f);
                watch.Stop();

                foreach (MCvObjectDetection region in regions)
                {
                    if (region.score > -0.5)
                        image.Draw(region.Rect, new Bgr(Color.Red), 1);
                }

                ImageViewer.Show(image, String.Format("Object detected in {0} milliseconds", watch.ElapsedMilliseconds));
            }
        }

        /// <summary>
        /// Check if both the managed and unmanaged code are compiled for the same architecture
        /// </summary>
        /// <returns>Returns true if both the managed and unmanaged code are compiled for the same architecture</returns>
        static bool IsPlaformCompatable()
        {
            int clrBitness = Marshal.SizeOf(typeof(IntPtr)) * 8;
            if (clrBitness != CvInvoke.UnmanagedCodeBitness)
            {
                MessageBox.Show(String.Format("Platform mismatched: CLR is {0} bit, C++ code is {1} bit."
                   + " Please consider recompiling the executable with the same platform target as C++ code.",
                   clrBitness, CvInvoke.UnmanagedCodeBitness));
                return false;
            }
            return true;
        }
    }
}
