using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using vcs_MySmoothProgressBar;   //使用MySmoothProgressBar範例

//運用Visual C#繪制一個平滑地進度條
//建立一個簡單的、自定義的用戶控件——一個平滑的進度條。

/*
工具箱/選擇項目/瀏覽/選取vcs_MySmoothProgressBar.dll

工具箱出現SmoothProgressBar控件
*/

namespace vcs_MySmoothProgressBarDemo
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
