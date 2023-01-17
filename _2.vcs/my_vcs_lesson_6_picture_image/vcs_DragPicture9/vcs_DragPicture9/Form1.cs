using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


using System.IO;    //for Directory
using System.Collections;   //for ArrayList

//應改成 vcs_DynamicAddRemoveControls8_MergeMap
//切割一圖 並做成拼圖


namespace vcs_DragPicture9
{
    public partial class Form1 : Form
    {
        private const int COLUMNS = 2;
        private const int ROWS = 2;
        //private const int PICTURE_WIDTH = 1920 / COLUMNS * 9 / 10;
        //private const int PICTURE_HEIGHT = 1080 / ROWS * 9 / 10;

        int PICTURE_WIDTH = 500;
        int PICTURE_HEIGHT = 500;

        ArrayList picture_files = new ArrayList();

        List<string> filenames = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            filenames.Clear();
            filenames.Add(@"C:\______test_files\__pic\_書畫字圖\_peony1\p1.jpg");
            filenames.Add(@"C:\______test_files\__pic\_書畫字圖\_peony1\p2.jpg");
            filenames.Add(@"C:\______test_files\__pic\_書畫字圖\_peony1\p3.jpg");
            filenames.Add(@"C:\______test_files\__pic\_書畫字圖\_peony1\p4.jpg");

            showPictures();
        }

        void showPictures()
        {
            // 設定位置及圖片方塊寬高值
            int LEFT_ANCHOR = 0;
            int TOP_ANCHOR = 0;

            int i;
            int j;
            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    // 實例化圖片方塊
                    PictureBox pbx = new PictureBox();
                    // 設定圖片方塊參數
                    pbx.Left = LEFT_ANCHOR + PICTURE_WIDTH * i;
                    pbx.Top = TOP_ANCHOR + PICTURE_HEIGHT * j;
                    pbx.Width = PICTURE_WIDTH;
                    pbx.Height = PICTURE_HEIGHT;
                    //pbx.BackColor = Color.Pink;
                    //pbx.Text = i.ToString() + ", " + j.ToString();
                    pbx.Tag = "dynamic" + (COLUMNS * j + i).ToString("D2");
                    pbx.Name = "pbx" + (COLUMNS * j + i).ToString("D2");
                    pbx.SizeMode = PictureBoxSizeMode.Normal;
                    pbx.MouseDown += PictureBox_MouseDown;
                    pbx.MouseMove += PictureBox_MouseMove;
                    pbx.MouseUp += PictureBox_MouseUp;

                    pbx.Image = Image.FromFile(filenames[j * 2 + i]);

                    // 將圖片方塊加入表單
                    this.Controls.Add(pbx);
                }
            }
        }

        bool flag_pictureBox_mouse_down = false;
        int pictureBox_position_x_old = 0;
        int pictureBox_position_y_old = 0;

        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_pictureBox_mouse_down = true;
                //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                pictureBox_position_x_old = e.X;
                pictureBox_position_y_old = e.Y;
                ((PictureBox)sender).BringToFront();    //選中的那一片拉到最上層顯示
            }
        }

        private void PictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox_position_x_old;
                int dy = e.Y - pictureBox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);
            }
        }

        private void PictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_pictureBox_mouse_down = false;
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox_position_x_old;
                int dy = e.Y - pictureBox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);
            }
        }
    }
}
