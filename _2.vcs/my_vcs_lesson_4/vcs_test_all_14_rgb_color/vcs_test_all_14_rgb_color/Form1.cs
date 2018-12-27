using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_14_rgb_color
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            panel1.BackColor = Color.FromArgb(hScrollBar1.Value, hScrollBar2.Value, hScrollBar3.Value);
            panel2.BackColor = Color.FromArgb(hScrollBar1.Value, 0, 0);
            panel3.BackColor = Color.FromArgb(0, hScrollBar2.Value, 0);
            panel4.BackColor = Color.FromArgb(0, 0, hScrollBar3.Value);
            SetupRandonColor();
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            //用水平滾動條調整背景色的實例
            //调用了方法，另外把hScrollBar2的scrooll时间设置成hScrollBar1的scroll事件就行了
            panel1.BackColor = Color.FromArgb(hScrollBar1.Value, hScrollBar2.Value, hScrollBar3.Value);
            textBox1.Text = hScrollBar1.Value.ToString();
            textBox2.Text = hScrollBar2.Value.ToString();
            textBox3.Text = hScrollBar3.Value.ToString();
            panel2.BackColor = Color.FromArgb(hScrollBar1.Value, 0, 0);
            panel3.BackColor = Color.FromArgb(0, hScrollBar2.Value, 0);
            panel4.BackColor = Color.FromArgb(0, 0, hScrollBar3.Value);
        }

        private void SetupRandonColor()
        {
            Random r = new Random();

            int color_r = r.Next(10);
            int color_g = r.Next(10);
            int color_b = r.Next(10);

            panel5.BackColor = Color.FromArgb(color_r * 255 / 10, color_g * 255 / 10, color_b * 255 / 10);
            label4.Text = (color_r * 255 / 10).ToString() + " " + (color_g * 255 / 10).ToString() + " " + (color_b * 255 / 10).ToString();

        }

        private void panel5_Click(object sender, EventArgs e)
        {
            SetupRandonColor();
        }
    }
}
