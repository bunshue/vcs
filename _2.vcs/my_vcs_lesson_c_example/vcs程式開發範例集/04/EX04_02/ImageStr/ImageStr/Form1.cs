using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

namespace ImageStr
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string str;
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                Image myImage = System.Drawing.Image.FromFile(str);
                Bitmap map = new Bitmap(myImage);
                myImage.Dispose();
                Graphics graphics = Graphics.FromImage(map);
                graphics.InterpolationMode = InterpolationMode.HighQualityBilinear;
                SolidBrush brush = new SolidBrush(Color.Red);
                PointF P = new PointF(100, 100);
                Font font = new Font(this.Font.Name, 40);
                graphics.DrawString(textBox1.Text, font, brush, P);
                map.Save(str.Substring(0, str.LastIndexOf("\\") + 1) + "new" + str.Substring(str.LastIndexOf("\\") + 1, str.LastIndexOf(".") - str.LastIndexOf("\\") - 1) + str.Substring(str.LastIndexOf("."), str.Length - str.LastIndexOf(".")), ImageFormat.Jpeg);
                MessageBox.Show("寫入成功");
                font.Dispose();
                graphics.Dispose();
            }
            catch { }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                openFileDialog1.Filter = "JPG文件(*.jpg)|*.jpg";
                openFileDialog1.ShowDialog();
                str = openFileDialog1.FileName;
                Image myImage = System.Drawing.Image.FromFile(str);
                this.pictureBox1.Image = myImage;
            }
            catch { }
        }
    }
}