using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

using System.Runtime.InteropServices;

namespace draw_test1
{
    public partial class Form1 : Form
    {
        public Point pt_st = new Point(0, 0);  //鼠標第一點 
        public Point pt_sp = new Point(0, 0);  //鼠標第二點 
        public bool flag_mouse_down = false;   //是否開始畫矩形 

        /// <summary>
        /// 在 picturebox1 上畫矩形
        /// </summary>
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = this.pictureBox1.CreateGraphics();
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0+50);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //this.Hide();//隱藏當前窗體
            Thread.Sleep(50);//讓線程睡眠一段時間，窗體消失需要一點時間
            Catch CatchForm = new Catch();
            Bitmap CatchBmp = new Bitmap(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height);//新建一個和屏幕大小相同的圖片
            Graphics g = Graphics.FromImage(CatchBmp);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height));//保存全屏圖片
            CatchForm.BackgroundImage = CatchBmp;//將Catch窗體的背景設為全屏時的圖片
            if (CatchForm.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "CatchForm OK\n";
                //如果Catch窗體結束,就將剪貼板中的圖片放到信息發送框中
                IDataObject iData = Clipboard.GetDataObject();
                DataFormats.Format myFormat = DataFormats.GetFormat(DataFormats.Bitmap);
                if (iData.GetDataPresent(DataFormats.Bitmap))
                {
                    richTextBox1.Paste(myFormat);
                    Clipboard.Clear();//清除剪貼板中的對象
                }

                //this.Show();//重新顯示窗體
            }
            else
            {
                richTextBox1.Text += "CatchForm Cancel\n";
            }
        }

        /// <summary>
        /// 在 pictureBox1 上按下鼠標事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            pt_st = new Point(e.X, e.Y);
        }

        /// <summary>
        /// 在 pictureBox1 上鼠標移動開始繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                //清除 pictureBox1 繪圖面,相當於刷新了一次窗體界面然後重新繪制
                g.Clear(this.BackColor);
                //獲取新的右下角坐標 
                pt_sp = new Point(e.X, e.Y);
                //獲取兩個數中的大者或小者
                int minX = Math.Min(pt_st.X, pt_sp.X);
                int minY = Math.Min(pt_st.Y, pt_sp.Y);
                int maxX = Math.Max(pt_st.X, pt_sp.X);
                int maxY = Math.Max(pt_st.Y, pt_sp.Y);

                //畫矩形
                g.DrawRectangle(new Pen(Color.Red), minX, minY, maxX - minX, maxY - minY);
                //ControlPaint.DrawReversibleFrame(new Rectangle(minX, minY, maxX - minX, maxY - minY),this.BackColor,FrameStyle.Dashed);
            }
        }

        /// <summary>
        /// 鼠標放開停止繪圖
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
        }
    }
}

