using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
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
            openFileDialog1.Filter = "Images (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" + "All files (*.*)|*.*";

            // Allow the user to select multiple images.
            openFileDialog1.Multiselect = true;
            openFileDialog1.Title = "My Image Browser";

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "取得 " + openFileDialog1.FileNames.Length.ToString() + " 個檔案\n";
                richTextBox1.Text += "檔案：\n";
                foreach (string filename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "檔案: " + filename + "\n";
                    listBox1.Items.Add(filename);

                }
                richTextBox1.Text += "\n";
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

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += listBox1.SelectedItem + "\n";
            Image loadedImage = Image.FromFile(listBox1.SelectedItem.ToString());
            pictureBox1.Image = loadedImage;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    richTextBox1.Text += "Normal\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Normal; break;
                case 1:
                    richTextBox1.Text += "StretchImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; break;
                case 2:
                    richTextBox1.Text += "AutoSize\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize; break;
                case 3:
                    richTextBox1.Text += "CenterImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage; break;
                case 4:
                    richTextBox1.Text += "Zoom\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;
                default:
                    richTextBox1.Text += "Unknown\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;
            }

        }

        private void button10_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
                return;

            //顯示圖片
            richTextBox1.Text += "圖片大小：\tW=" + pictureBox1.Image.Width.ToString()+ "\t";
            richTextBox1.Text += "H=" + pictureBox1.Image.Height.ToString() + "\n";

            #region 影像縮放(縮小一半)
            richTextBox1.Text += "縮小一半\n";
            //建立新的影像，長寬為原始影像的1/2
            Image zoomImage = new Bitmap(pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2) as Image;
            //準備繪製新的影像
            Graphics graphics0 = Graphics.FromImage(zoomImage);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的1/2
            graphics0.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2);
            graphics0.Dispose();
            //儲存新的影像
            zoomImage.Save("zoom.jpg");
            richTextBox1.Text += "縮小一半，存檔完成，檔名： zoom.jpg\n";
            #endregion
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
                return;

            //顯示圖片
            richTextBox1.Text += "圖片大小：\tW=" + pictureBox1.Image.Width.ToString() + "\t";
            richTextBox1.Text += "H=" + pictureBox1.Image.Height.ToString() + "\n";

            #region 影像放大(放大一倍)
            richTextBox1.Text += "放大一倍\n";
            //建立新的影像，長寬為原始影像的2倍
            Image zoomImageb = new Bitmap(pictureBox1.Image.Width * 2, pictureBox1.Image.Height * 2) as Image;
            //準備繪製新的影像
            Graphics graphics0a = Graphics.FromImage(zoomImageb);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的2倍
            graphics0a.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width * 2, pictureBox1.Image.Height * 2);
            graphics0a.Dispose();
            //儲存新的影像
            zoomImageb.Save("big.jpg");
            richTextBox1.Text += "放大一倍，存檔完成，檔名： big.jpg\n";
            #endregion

        }

        private void button12_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
                return;

            #region 影像旋轉(以中心順時針轉10度)
            //建立新的影像
            Image rotateImage = new Bitmap(pictureBox1.Image.Width, pictureBox1.Image.Height) as Image;
            //準備繪製新的影像
            Graphics graphics1 = Graphics.FromImage(rotateImage);
            //設定中心點
            graphics1.TranslateTransform((float)pictureBox1.Image.Width / 2, (float)pictureBox1.Image.Height / 2);
            //順時針轉10度
            graphics1.RotateTransform(10);
            //還原中心點
            graphics1.TranslateTransform(-(float)pictureBox1.Image.Width / 2, -(float)pictureBox1.Image.Height / 2);
            //於座標(0,0)開始繪製來源影像
            graphics1.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width, pictureBox1.Image.Height);
            graphics1.Dispose();
            //儲存新的影像
            //rotateImage.Save("rotate.jpg");

            pictureBox1.Image = rotateImage;

            #endregion


        }
    }
}
