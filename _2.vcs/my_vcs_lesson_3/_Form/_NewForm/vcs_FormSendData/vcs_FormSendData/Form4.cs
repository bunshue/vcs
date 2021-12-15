using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData
{
    public partial class Form4 : Form
    {
        int[] data;

        //public Form4() old, 改成可以接收參數
        public Form4(int[] histData)
        {
            InitializeComponent();

            data = histData;    //表單初始化 接收父表單傳送過來的資料
        }

        void Draw_Hist(int[] data)  //直方圖 只顯示正的數值 且 畫好畫滿
        {
            int W = panel1.ClientSize.Width;
            int H = panel1.ClientSize.Height;

            Graphics g = panel1.CreateGraphics();

            g.DrawRectangle(new Pen(Color.Red, 3), 0, 0, W - 3, H - 3);

            Pen pen = new Pen(Brushes.Black, 1);

            int N = data.Length;

            // get the max value
            int max = 0;
            for (int i = 0; i < N; i++)
            {
                max = Math.Max(max, data[i]);   //找出最大值 為了畫好畫滿
            }
            //richTextBox1.Text += "max = " + max.ToString() + "\n";
            
            // draw
            for (int i = 0; i < N; i += 2)
            {
                g.DrawLine(pen, i, H, i, H - H * data[i] / max);    //高度依最大值比例畫出來
            }
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            Draw_Hist(data);
        }
    }
}