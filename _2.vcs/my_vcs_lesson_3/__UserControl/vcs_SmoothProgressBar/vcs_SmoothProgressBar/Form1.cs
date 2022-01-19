using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//建立自定義的ProgressBar

//專案/右鍵/加入/使用者控制項, 名稱為SmoothProgressBar.cs, 修改此檔, 編譯後, 工具箱出現SmoothProgressBar控件


namespace vcs_SmoothProgressBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.smoothProgressBar1.Value = 100;
            this.smoothProgressBar2.Value = 0;

            this.timer1.Interval = 1;
            this.timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (this.smoothProgressBar1.Value > 0)
            {
                this.smoothProgressBar1.Value--;
                this.smoothProgressBar2.Value++;
            }
            else
            {
                this.timer1.Enabled = false;

                this.smoothProgressBar1.Value = 100;
                this.smoothProgressBar2.Value = 0;

                this.timer1.Interval = 1;
                this.timer1.Enabled = true;
            }
        }
    }
}
