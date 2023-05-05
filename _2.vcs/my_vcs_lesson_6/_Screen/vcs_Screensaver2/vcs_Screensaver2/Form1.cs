using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
    表單Form1的屬性/ 

    BackColor 改 White
    FormBorderStyle 改 None
    TransparencyKey = 改 White
    
    選一張圖，白色部分就會變成透明
    BackgroundImage
    BackgroundImageLayout 改 Center

    // Set the form's TransparencyKey and BackColor
    // to the image's transparent color.
*/

namespace vcs_Screensaver2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.CenterToScreen();       //將表單置中顯示

            //讀取圖檔
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            this.BackgroundImage = Image.FromFile(filename);
            //this.ClientSize = this.BackgroundImage.Size;
            this.ClientSize = new Size(this.BackgroundImage.Size.Width * 1 / 1, this.BackgroundImage.Size.Height * 1 / 1);  //調整圖片大小

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.TopMost = true;
        }

        int index_pic = 1;
        int cnt = 0;
        bool flag_move_right = true;
        bool flag_move_down = true;
        bool flag_enlarge = true;
        int ratio = 100;
        private void timer1_Tick(object sender, EventArgs e)
        {
            //richTextBox1.AppendText("螢幕解析度 : " + Screen.PrimaryScreen.Bounds.Width.ToString() + "*" + Screen.PrimaryScreen.Bounds.Height.ToString() + "\n");

            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            int x_st = this.Location.X;
            int y_st = this.Location.Y;

            int dx = 10;
            int dy = 5;

            int w = this.Width;
            int h = this.Height;

            if (flag_move_right == true) //move right
            {
                if ((x_st + w + dx) < W)
                {
                    x_st += dx;
                }
                else
                {
                    flag_move_right = false;
                    x_st -= dx;
                }
            }
            else   //move to left
            {
                if ((x_st - dx) > 0)
                {
                    x_st -= dx;
                }
                else
                {
                    flag_move_right = true;
                    x_st += dx;
                }
            }

            if (flag_move_down == true) //move down
            {
                if ((y_st + h + dy) < H)
                {
                    y_st += dy;
                }
                else
                {
                    flag_move_down = false;
                    y_st -= dy;
                }
            }
            else   //move to left
            {
                if ((y_st - dy) > 0)
                {
                    y_st -= dy;
                }
                else
                {
                    flag_move_down = true;
                    y_st += dy;
                }
            }
            this.Location = new Point(x_st, y_st);

            cnt++;
            if ((cnt % 10) == 0)
            {
                index_pic++;
                if (index_pic > 21)
                    index_pic = 1;

                /*
                //讀取圖檔
                string filename = @"C:\pic1018c\b\" + index_pic.ToString() + ".jpg";
                this.BackgroundImage = Image.FromFile(filename);
                //this.ClientSize = this.BackgroundImage.Size;
                this.ClientSize = new Size(this.BackgroundImage.Size.Width * 1 / 4, this.BackgroundImage.Size.Height * 1 / 4);
                */

                if (flag_enlarge == true)
                {
                    ratio += 10;
                    if (ratio > 150)
                    {
                        flag_enlarge = false;
                    }
                }
                else
                {
                    ratio -= 10;
                    if (ratio < 80)
                    {
                        flag_enlarge = true;
                    }
                }
                this.ClientSize = new Size(this.BackgroundImage.Size.Width * 1 / 4 * ratio / 100, this.BackgroundImage.Size.Height * 1 / 4 * ratio / 100);


            }
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            //按鍵後反相的寫法
            timer1.Enabled = !timer1.Enabled;
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************
        #region 移動無邊框表單
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
        #endregion
    }
}
