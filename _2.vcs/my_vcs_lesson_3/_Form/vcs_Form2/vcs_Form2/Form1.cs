using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_Form2
{
    public partial class Form1 : Form
    {
        private bool showing = true;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            groupBox1.Location = new Point(10, 10);
            groupBox1.Width = this.ClientSize.Width - 20;
            groupBox1.Height = this.ClientSize.Height - 20;

            pictureBox1.Location = new Point(10, 10);
            pictureBox1.Width = this.groupBox1.ClientSize.Width - 20;
            pictureBox1.Height = this.groupBox1.ClientSize.Height - 20;

            int W = this.groupBox1.ClientSize.Width;
            int H = this.groupBox1.ClientSize.Height;
            lb_position.Location = new Point((W - 200) / 2, H * 2 / 3);

            //------------------------------------------------------------  # 60個

            //窗體顯示特效
            //要先將Form1的屬性的Opacity設為0
            //Opacity = 0.0; //窗體透明度為0

            timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            double d = 0.08;
            if (showing)
            {
                if (Opacity + d >= 1.0)
                {
                    Opacity = 1.0;
                    timer1.Enabled = false;
                    label1.Text += ", 啟動完成";
                }
                else
                {
                    Opacity += d;
                }
            }
            else
            {
                if (Opacity - d <= 0.0)
                {
                    Opacity = 0.0;
                    timer1.Stop();
                }
                else
                {
                    Opacity -= d;
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //製作閃動的窗體
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

        //------------------------------------------------------------  # 60個

        private void Form1_Resize(object sender, EventArgs e)
        {
            groupBox1.Location = new Point(10, 10);
            groupBox1.Width = this.ClientSize.Width - 20;
            groupBox1.Height = this.ClientSize.Height - 20;

            pictureBox1.Location = new Point(10, 10);
            pictureBox1.Width = this.groupBox1.ClientSize.Width - 20;
            pictureBox1.Height = this.groupBox1.ClientSize.Height - 20;

            int W = this.groupBox1.ClientSize.Width;
            int H = this.groupBox1.ClientSize.Height;
            lb_position.Location = new Point((W - 200) / 2, H * 2 / 3);
        }

        //------------------------------------------------------------  # 60個

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/




