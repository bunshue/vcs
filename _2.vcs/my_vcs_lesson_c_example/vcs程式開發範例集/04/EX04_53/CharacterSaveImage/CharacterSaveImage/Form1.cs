using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Drawing.Imaging;

namespace CharacterSaveImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics myGraphics = this.CreateGraphics();
            saveFileDialog1.Filter = "圖片(*.bmp)|*.bmp";
            Bitmap myBitmap = new Bitmap(textBox1.Width, textBox1.Height);
            myGraphics = Graphics.FromImage(myBitmap);
            myGraphics.FillRectangle(new SolidBrush(Color.White), 0, 0, textBox1.Width, textBox1.Height);
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                myGraphics.DrawString(textBox1.Text, new Font("細明體", 9), new SolidBrush(Color.Black), new Point(0, 2));
                myBitmap.Save(saveFileDialog1.FileName, ImageFormat.Bmp);
                myGraphics.Dispose();
                myBitmap.Dispose();
            }
        }
    }
}