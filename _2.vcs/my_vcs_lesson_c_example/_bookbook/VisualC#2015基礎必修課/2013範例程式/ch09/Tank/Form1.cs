using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tank
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            picTank.Image = Image.FromFile("tank1.gif");  //載入tank1.gif
            picTank.Left = 100; picTank.Top = 90;  //預設picTank的位置
            picFire.Image = Image.FromFile("fire.gif");  //載入fire.gif
            picFire.Visible = false;  //預設picFire不可見
        }
        //當按下按鍵時
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode) //根據e.KeyCode分別執行
            {
                case Keys.W:  //若按W鍵
                    picTank.Top -= 2;  //上移2點
                    break;
                case Keys.S:  //若按S鍵
                    picTank.Top += 2;  //上移2點
                    break;
                case Keys.A:  //若按A鍵
                    picTank.Left -= 2;  //左移2點
                    break;
                case Keys.D:  //若按D鍵
                    picTank.Left += 2;  //右移2點
                    break;
                case Keys.Up:  //若按向上鍵
                    picTank.Image = Image.FromFile("tank1.gif");  //載入tank1.gif
                    picFire.Left = picTank.Left + 5;  //根據picTank設picFire的位置
                    picFire.Top = picTank.Top - 50;
                    picFire.Visible = true;  //設picFire可視
                    break;
                case Keys.Right:  //若按向右鍵
                    picTank.Image = Image.FromFile("tank2.gif");
                    picFire.Left = picTank.Left + 60;
                    picFire.Top = picTank.Top + 5;
                    picFire.Visible = true;
                    break;
                case Keys.Down:  //若按向下鍵
                    picTank.Image = Image.FromFile("tank3.gif");
                    picFire.Left = picTank.Left + 5;
                    picFire.Top = picTank.Top + 60;
                    picFire.Visible = true;
                    break;
                case Keys.Left:  //若按向左鍵
                    picTank.Image = Image.FromFile("tank4.gif");
                    picFire.Left = picTank.Left - 50;
                    picFire.Top = picTank.Top + 5;
                    picFire.Visible = true;
                    break;
            }
        }
        //當放開按鍵時
        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            picFire.Visible = false;  //設picFire不可見
        }
    }
}
