using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        string filename = "c:\\______test_files\\picture1.jpg";


        /// <summary>
        /// 背景圖
        /// </summary>
        private Bitmap bitmapBack;

        /// <summary>
        /// 用於浮水印圖
        /// </summary>
        private Bitmap bitmapWaterMark;



        public Form1()
        {
            InitializeComponent();

            bitmapBack = new Bitmap(filename);
            pictureBox1.Image = bitmapBack;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Rectangle rect = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap = new Bitmap(rect.Width, rect.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                    g.CopyFromScreen(Point.Empty, Point.Empty, rect.Size);

                bitmap.Save("test.jpg", ImageFormat.Jpeg);
            }

        }
       

        private void button2_Click(object sender, EventArgs e)
        {


        }


    }
}
