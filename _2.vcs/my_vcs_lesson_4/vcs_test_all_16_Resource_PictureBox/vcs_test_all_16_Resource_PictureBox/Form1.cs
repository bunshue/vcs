using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_16_Resource_PictureBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.MouseWheel += new MouseEventHandler(Form1_MouseWheel);
        }

        /*
         * [C#]pictureBox隨滑鼠滾輪滾動改變大小
         * pictureBox的Sizemode屬性設為Zoom
         * 再添加事件
         * this.MouseWheel += new MouseEventHandler(Form1_MouseWheel);
         */

        void Form1_MouseWheel(object sender, MouseEventArgs e)
        {
            var t = pictureBox1.Size;
            //t.Width += e.Delta;
            //t.Height += e.Delta;
            if (e.Delta > 0)
            {
                t.Width++;
                t.Height++;
            }
            else
            {
                t.Width--;
                t.Height--;
            }
            pictureBox1.Size = t;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;


            //1. 載入圖檔，由資源檔
            pictureBox1.Image = Resource1.bear;
            
            //2. picturebox載入一圖
            //pictureBox1.Image = Image.FromFile("c:\\______test_vcs\\picture1.jpg"); //載入圖檔，由檔案

            //3. picturebox顯示圖檔
            //Image img = Image.FromFile("c:\\______test_vcs\\picture1.jpg");
            //pictureBox1.Image = img;

            //pictureBox1.Height = 800; 設定圖片高度和寬度
            //pictureBox1.Width = 600;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.Height += 10;
            pictureBox1.Width += 10;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Height -= 10;
            pictureBox1.Width -= 10;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // Set the file dialog to filter for graphics files.
            openFileDialog1.Filter =
                "Images (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" +
                "All files (*.*)|*.*";

            // Allow the user to select multiple images.
            openFileDialog1.Multiselect = true;
            openFileDialog1.Title = "My Image Browser";

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Image loadedImage = Image.FromFile(openFileDialog1.FileName);
                pictureBox1.Image = loadedImage;
            }

        }

        private void button8_Click(object sender, EventArgs e)
        {
            pictureBox1.Location = new Point(pictureBox1.Location.X + 5, pictureBox1.Location.Y + 5);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            pictureBox1.Location = new Point(pictureBox1.Location.X - 5, pictureBox1.Location.Y - 5);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //把pictureBox移到(60, 100)位置
            int xx = 60;
            int yy = 100;
            pictureBox1.Location = new Point(xx, yy);
        }
    }
}
