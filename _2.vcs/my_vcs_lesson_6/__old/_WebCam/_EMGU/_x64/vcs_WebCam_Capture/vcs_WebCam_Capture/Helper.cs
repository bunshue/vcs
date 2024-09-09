using System;
using System.IO;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace vcs_WebCam_Capture
{
    //Design by Pongsakorn Poosankam
    class Helper
    {
        public static void SaveImageCapture(string filename, System.Drawing.Image image)
        {
            FileStream fstream = new FileStream(filename, FileMode.Create);
            image.Save(fstream, System.Drawing.Imaging.ImageFormat.Jpeg);
            fstream.Close();
        }
    }
}
