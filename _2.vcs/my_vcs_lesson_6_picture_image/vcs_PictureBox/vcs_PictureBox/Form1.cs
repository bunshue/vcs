using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
            pictureBox2.Image = null;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            pictureBox2.Image = null;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // Set the file dialog to filter for graphics files.
            openFileDialog1.Filter = "Images (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" + "All files (*.*)|*.*";

            // Allow the user to select multiple images.
            openFileDialog1.Multiselect = true;
            openFileDialog1.Title = "My Image Browser";
            openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1\";

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

                //the same
                //pictureBox1.Image = Image.FromFile(openFileDialog1.FileName);

            }
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += listBox1.SelectedItem + "\n";
            Image loadedImage = Image.FromFile(listBox1.SelectedItem.ToString());
            pictureBox1.Image = loadedImage;
        }

        bool flag_mouse_down = false;
        int mouse_down_position_x = 0;
        int mouse_down_position_y = 0;
        int mouse_up_position_x = 0;
        int mouse_up_position_y = 0;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (pictureBox1.Image == null)
                return;

            flag_mouse_down = true;
            mouse_down_position_x = e.X;
            mouse_down_position_y = e.Y;

            richTextBox1.Text += "MouseDown   (" + e.X.ToString() + ", " + e.Y + ")\n";
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (pictureBox1.Image == null)
                return;

            if (flag_mouse_down == true)
            {
                //g.DrawRectangle(new Pen(Color.Black), new Rectangle(mouse_down_position_x, mouse_down_position_y, e.X - mouse_down_position_x, e.Y - mouse_down_position_y));
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (pictureBox1.Image == null)
                return;

            mouse_up_position_x = e.X;
            mouse_up_position_y = e.Y;

            if ((mouse_down_position_x < 0) || (mouse_down_position_y < 0) || (mouse_up_position_x < 0) || (mouse_up_position_y < 0))
                return;

            richTextBox1.Text += "MouseUp   (" + e.X.ToString() + ", " + e.Y + ") 畫矩形\n";
            //g.DrawRectangle(new Pen(Color.Black), new Rectangle(mouse_down_position_x, mouse_down_position_y, mouse_up_position_x - mouse_down_position_x, mouse_up_position_y - mouse_down_position_y));
            //pictureBox2.Image = pictureBox1.Image.Clone(

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            richTextBox1.Text += "圖片大小 W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int ww = 0;
            int hh = 0;
            Rectangle cropArea;

            bool flag_crop_area_valid = true;

            if (mouse_up_position_x > mouse_down_position_x)        //往右
            {
                ww = mouse_up_position_x - mouse_down_position_x;
                if (mouse_up_position_y > mouse_down_position_y)//往下
                {
                    hh = mouse_up_position_y - mouse_down_position_y;
                    cropArea = new Rectangle(mouse_down_position_x, mouse_down_position_y, ww, hh);
                    if ((mouse_down_position_x + ww) > W)
                        flag_crop_area_valid = false;
                    if ((mouse_down_position_y + hh) > H)
                        flag_crop_area_valid = false;
                }
                else//往上
                {
                    hh = mouse_down_position_y - mouse_up_position_y;
                    cropArea = new Rectangle(mouse_down_position_x, mouse_up_position_y, ww, hh);
                    if ((mouse_down_position_x + ww) > W)
                        flag_crop_area_valid = false;
                    if ((mouse_up_position_y + hh) > H)
                        flag_crop_area_valid = false;
                }
            }
            else//往左
            {
                ww = mouse_down_position_x - mouse_up_position_x;
                if (mouse_up_position_y > mouse_down_position_y)//往下
                {
                    hh = mouse_up_position_y - mouse_down_position_y;
                    cropArea = new Rectangle(mouse_up_position_x, mouse_down_position_y, ww, hh);
                    if ((mouse_up_position_x + ww) > W)
                        flag_crop_area_valid = false;
                    if ((mouse_down_position_y + hh) > H)
                        flag_crop_area_valid = false;
                }
                else//往上
                {
                    hh = mouse_down_position_y - mouse_up_position_y;
                    cropArea = new Rectangle(mouse_up_position_x, mouse_up_position_y, ww, hh);
                    if ((mouse_up_position_x + ww) > W)
                        flag_crop_area_valid = false;
                    if ((mouse_up_position_y + hh) > H)
                        flag_crop_area_valid = false;
                }
            }
            if (ww <= 0)
                return;
            if (hh <= 0)
                return;

            if (flag_crop_area_valid == true)
            {
                richTextBox1.Text += "x_st = " + cropArea.X.ToString() + " y_st = " + cropArea.Y.ToString() + " w = " + cropArea.Width.ToString() + " h = " + cropArea.Height.ToString() + "\n";

                Image zoomImage = new Bitmap(ww, hh) as Image;
                zoomImage = bitmap1.Clone(cropArea, zoomImage.PixelFormat);

                pictureBox2.Image = zoomImage;
            }




            //            Bitmap bmpImage = new Bitmap(img);
            //return bmpImage.Clone(cropArea, bmpImage.PixelFormat);

            //Bitmap bmpImage = pictureBox1.Image;

            //Graphics g = Graphics.FromImage(targetbitmap);

            //Image loadedImage = Image.FromFile(openFileDialog1.FileName);
            //pictureBox1.Image = loadedImage;
            /*
            Image zoomImage = new Bitmap(pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2) as Image;
            //準備繪製新的影像
            Graphics graphics0 = Graphics.FromImage(zoomImage);
            //於座標(0,0)開始繪製來源影像，長寬設置為來源影像的1/2
            graphics0.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width / 2, pictureBox1.Image.Height / 2);
            graphics0.Dispose();


            */





            flag_mouse_down = false;
        }

        private void rb_picturebox_sizemode(object sender, EventArgs e)
        {
            if (rb_0.Checked == true)
            {
                richTextBox1.Text += "Normal\n";
                pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            }
            else if (rb_1.Checked == true)
            {
                richTextBox1.Text += "StretchImage\n";
                pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            }
            else if (rb_2.Checked == true)
            {
                //richTextBox1.Text += pictureBox1.Size.ToString() + "\n";
                richTextBox1.Text += "AutoSize, 會改變pictureBox的大小\n";
                pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                //richTextBox1.Text += pictureBox1.Size.ToString() + "\n";
            }
            else if (rb_3.Checked == true)
            {
                richTextBox1.Text += "CenterImage\n";
                pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
            }
            else if (rb_4.Checked == true)
            {
                richTextBox1.Text += "Zoom\n";
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            }
            else
            {
                richTextBox1.Text += "XXXXXXX\n";
                pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            }
        }
    }
}
