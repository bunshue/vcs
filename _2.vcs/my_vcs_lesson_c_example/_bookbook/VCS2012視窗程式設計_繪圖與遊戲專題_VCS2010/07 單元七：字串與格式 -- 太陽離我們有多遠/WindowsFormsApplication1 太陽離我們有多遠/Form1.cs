using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            //label2.Text = "聲音的速度為 340 公尺/每秒";
            //label3.Text = "光的速度為 299,792,458 公尺/每秒";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double dis = 150000000000.0 / 340.0 / 60.0 / 60.0 / 24.0;
            label4.Text = dis.ToString("#,###,###,###.##") + " 天";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            double dis = 150000000000.0 / 299792458.0;
            //label5.Text = dis.ToString() + " 秒";
            label5.Text = dis.ToString("#,###,###,###.##") + " 秒";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            string Today;
            Today = DateTime.Now.ToString();     // 日期時間模式 2009/8/24 下午 08:09:42
            //Today = DateTime.Now.ToString("Y"); // 年月模式  2009年8月
            //Today = DateTime.Now.ToString("M"); // 月日模式  8月24日
            //Today = DateTime.Now.ToString("D"); // 完整日期模式  2009年8月24日
            //Today = DateTime.Now.ToString("d"); // 簡短日期模式  2009/8/24
            //Today = DateTime.Now.ToString("T"); // 完整時間模式   下午 08:09:42
            //Today = DateTime.Now.ToString("t"); // 簡短時間模式   下午 08:09
            //Today = DateTime.Now.ToString("F"); // 完整日期時間模式  2009年8月24日 下午 08:09:42
            //Today = DateTime.Now.ToString("f"); // 簡短日期時間模式  2009年8月24日 下午 08:09

            label1.Text = String.Format("名字：{0}， 日期：{1}", "太空人", Today);  // 複合格式
        }
    }
}
