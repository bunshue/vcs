using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading.Tasks;

namespace vcs_Tank
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
         // 宣告 locX, locY用來存放坦克車開始的座標
        int locX, locY;

        // 表單載入時執行

        private void Form1_Load(object sender, EventArgs e)
        {
            // 取得picTank的X, Y座標並指定給locX, locY
            locX = picTank.Location.X;
            locY = picTank.Location.Y;
            lblX.Text = "X座標：" + picTank.Location.X;
            lblY.Text = "Y座標：" + picTank.Location.Y;
            lblMsg.Text = "請按上下左右鍵控制坦克！";
            picTank.SizeMode = PictureBoxSizeMode.AutoSize;
            picTank.Image = picTankU.Image;
            picTankU.Visible = false;  // 坦克往上圖隱藏
            picTankD.Visible = false;  // 坦克往下圖隱藏
            picTankL.Visible = false;  // 坦克往左圖隱藏
            picTankR.Visible = false;  // 坦克往右圖隱藏
        }
        // ===  在表單按下鍵盤不放時執行
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Up:       // 判斷是否按鍵盤上鍵
                    picTank.Image = picTankU.Image;
                    if ((picTank.Top + picTank.Height) <= 0)
                    {
                        picTank.Top = this.Height;
                    }
                    else
                    {
                        picTank.Top -= 10;
                    }
                    break;
                case Keys.Down:      // 判斷是否按鍵盤下鍵
                    picTank.Image = picTankD.Image;
                    if (picTank.Top >= this.Height)
                    {
                        picTank.Top = 0 - picTank.Height;
                    }
                    else
                    {
                        picTank.Top += 10;
                    }
                    break;
                case Keys.Left:    // 判斷是否按鍵盤左鍵
                    picTank.Image = picTankL.Image;
                    if (picTank.Width + picTank.Left <= 0)
                    {
                        picTank.Left = this.Width;
                    }
                    else
                    {
                        picTank.Left -= 10;
                    }
                    break;
                case Keys.Right:   // 判斷是否按鍵盤右鍵
                    picTank.Image = picTankR.Image;
                    if (picTank.Left >= this.Width)
                    {
                        picTank.Left = 0 - picTank.Width;
                    }
                    else
                    {
                        picTank.Left += 10;
                    }
                    break;
            }
            lblX.Text = "X座標：" + picTank.Location.X;
            lblY.Text = "Y座標：" + picTank.Location.Y;
            lblMsg.Text = "現在按下" + e.KeyCode.ToString() + "鍵, 鍵值為 : "
				          + e.KeyValue.ToString() + "!!";
        }
        // === 在表單放開鍵盤的按鍵時執行
        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            lblX.Text = "X座標：" + picTank.Location.X;
            lblY.Text = "Y座標：" + picTank.Location.Y;
            lblMsg.Text = "請按上下左右鍵控制坦克！";
        }
    }
}
