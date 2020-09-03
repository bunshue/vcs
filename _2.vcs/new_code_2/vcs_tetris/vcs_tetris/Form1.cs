using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_tetris
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 宣告 locX, locY用來存放坦克車開始的座標
        int locX, locY;

        private void Form1_Load(object sender, EventArgs e)
        {
            // 取得picTank的X, Y座標並指定給locX, locY
            locX = pb_tetris.Location.X;
            locY = pb_tetris.Location.Y;
            pb_tetris.SizeMode = PictureBoxSizeMode.AutoSize;

            this.BackColor = Color.Black;
            pb_tetris.Image = vcs_tetris.Properties.Resources.tetris;


        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Up:       // 判斷是否按鍵盤上鍵
                    if ((pb_tetris.Top + pb_tetris.Height) <= 0)
                    {
                        pb_tetris.Top = this.Height;
                    }
                    else
                    {
                        pb_tetris.Top -= 10;
                    }
                    break;
                case Keys.Down:      // 判斷是否按鍵盤下鍵
                    if (pb_tetris.Top >= this.Height)
                    {
                        pb_tetris.Top = 0 - pb_tetris.Height;
                    }
                    else
                    {
                        pb_tetris.Top += 10;
                    }
                    break;
                case Keys.Left:    // 判斷是否按鍵盤左鍵
                    if (pb_tetris.Width + pb_tetris.Left <= 0)
                    {
                        pb_tetris.Left = this.Width;
                        pb_tetris.Left = this.Width;
                    }
                    else
                    {
                        pb_tetris.Left -= 10;
                        pb_tetris.Left -= 10;
                    }
                    break;
                case Keys.Right:   // 判斷是否按鍵盤右鍵
                    if (pb_tetris.Left >= this.Width)
                    {
                        pb_tetris.Left = 0 - pb_tetris.Width;
                    }
                    else
                    {
                        pb_tetris.Left += 10;
                    }
                    break;
            }

            label1.Text = "(" + pb_tetris.Location.X.ToString() + ", " + pb_tetris.Location.Y.ToString() + ")";
        }
    }
}
