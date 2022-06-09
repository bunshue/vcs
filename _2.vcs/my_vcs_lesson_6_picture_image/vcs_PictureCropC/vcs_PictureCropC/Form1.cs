using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureCropC
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
