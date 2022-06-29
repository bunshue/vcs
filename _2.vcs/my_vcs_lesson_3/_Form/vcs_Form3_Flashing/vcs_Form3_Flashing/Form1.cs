using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_Form3_Flashing
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        //製作閃動的窗體
        private void button1_Click(object sender, EventArgs e)
        {
            while (Visible) // 關閉窗體時，停止循環
            {
                for (int c = 0; c < 254 && Visible; c++)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c); // 此方法指定三個數字：red/green/blue.
                    Application.DoEvents(); // 此語句使操作系統能夠在程序之外執行其他操作。否則
                    // 程序將占用所有CPU周期
                    Thread.Sleep(3); // 此語句在循環中插入3毫秒的延遲。
                }
                for (int c = 254; c >= 0 && Visible; c--)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c);
                    Application.DoEvents();
                    Thread.Sleep(3);
                }
            }
        }
    }
}
