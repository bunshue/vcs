using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox3_Resizable
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
            this.Text = "Resizable & Movable PictureBox Demo";
            this.Size = new Size(800, 600);

            pictureBox = new PictureBox();
            pictureBox.BackColor = Color.LightBlue;
            pictureBox.Location = new Point(100, 100);
            pictureBox.Size = new Size(200, 150);

            // 加入事件
            pictureBox.MouseDown += PictureBox_MouseDown;
            pictureBox.MouseMove += PictureBox_MouseMove;
            pictureBox.MouseUp += PictureBox_MouseUp;

            this.Controls.Add(pictureBox);
        }

        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                // 判斷是否在右下角 (調整大小區域)
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
                if (e.X >= pictureBox.Width - 10 && e.Y >= pictureBox.Height - 10)
                    pictureBox.Cursor = Cursors.SizeNWSE;  // 斜向箭頭
                else
                    pictureBox.Cursor = Cursors.Default;
            }
        }

        private void PictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            resizing = false;
            moving = false;
            pictureBox.Cursor = Cursors.Default;
        }
    }
}

