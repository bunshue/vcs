using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//預設是不能用滑鼠直接拉動大小的，需要自己加上「滑鼠事件」來模擬「可調整大小」的行為

namespace vcs_PictureBox3_Resizable2
{
    public partial class Form1 : Form
    {
        private PictureBox pictureBox;
        private bool resizing = false;
        private bool moving = false;
        private Point lastMousePos;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            pictureBox1.ImageLocation = filename;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            pictureBox1.Size = new Size(840, 560);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            button0.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 1);
            richTextBox1.Size = new Size(300, 690 - 140);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);


            this.Size = new Size(1273, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                // 判斷是否在右下角 (調整大小區域), 判斷滑鼠是否在右下角 10px 範圍內
                if (e.X >= pictureBox.Width - 10 && e.Y >= pictureBox.Height - 10)
                {
                    resizing = true;
                    lastMousePos = e.Location;
                    pictureBox.Cursor = Cursors.SizeNWSE;  // 斜向箭頭
                }
                else
                {
                    // 其他區域則進入拖曳模式
                    moving = true;
                    lastMousePos = e.Location;
                    pictureBox.Cursor = Cursors.SizeAll;
                }
            }
        }

        private void PictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (resizing)
            {
                int dx = e.X - lastMousePos.X;
                int dy = e.Y - lastMousePos.Y;

                pictureBox.Width += dx;
                pictureBox.Height += dy;

                lastMousePos = e.Location;
            }
            else if (moving)
            {
                int dx = e.X - lastMousePos.X;
                int dy = e.Y - lastMousePos.Y;

                pictureBox.Left += dx;
                pictureBox.Top += dy;
            }
            else
            {
                // 游標提示：右下角顯示縮放游標
                // 判斷是否在右下角 (調整大小區域), 判斷滑鼠是否在右下角 10px 範圍內
                if (e.X >= pictureBox.Width - 10 && e.Y >= pictureBox.Height - 10)
                {
                    pictureBox.Cursor = Cursors.SizeNWSE;  // 斜向箭頭
                }
                else
                {
                    pictureBox.Cursor = Cursors.Default;
                }
            }
        }

        private void PictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            resizing = false;
            moving = false;
            pictureBox.Cursor = Cursors.Default;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //選取

            pictureBox = new PictureBox();
            pictureBox.BackColor = Color.Transparent;
            pictureBox.Location = new Point(100, 100);
            pictureBox.Size = new Size(200, 150);

            // 加入事件
            pictureBox.MouseDown += PictureBox_MouseDown;
            pictureBox.MouseMove += PictureBox_MouseMove;
            pictureBox.MouseUp += PictureBox_MouseUp;

            this.Controls.Add(pictureBox);
            pictureBox.BringToFront();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //確定

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

