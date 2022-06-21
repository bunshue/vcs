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

namespace vcs_Form6_NotRectangle7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // On mouse down, start moving the form.
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            const int WM_NCLBUTTONDOWN = 0xA1;
            const int HT_CAPTION = 0x2;
            this.Capture = false;
            Message msg = Message.Create(this.Handle,
                WM_NCLBUTTONDOWN, (IntPtr)HT_CAPTION, IntPtr.Zero);
            WndProc(ref msg);
        }

        //使用鍵盤方向鍵控制窗體移動
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            Point point = this.Location;//定义一个标识窗体的变量
            switch (e.KeyData)//判断按键类型
            {
                case Keys.Up://当按键为上方向键时
                    point.Y -= 2;
                    break;
                case Keys.Down://当按键为下方向键时
                    point.Y += 2;
                    break;
                case Keys.Right://当按键为右方向键时
                    point.X += 2;
                    break;
                case Keys.Left://当按键为左方向键时
                    point.X -= 2;
                    break;
                case Keys.Escape://当按键为Esc键时
                    this.Close();//关闭本窗体
                    break;
                case Keys.X://当按键为X键时
                    this.Close();//关闭本窗体
                    break;
                default: break;
            }
            this.Location = point;

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Form1 form1 = new Form1();//创建窗体对象
            form1.KeyPreview = true;//设置窗体接收按键事件
        }
    }
}
