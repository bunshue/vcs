using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//建立自定義的ProgressBar

//專案/右鍵/加入/使用者控制項, 名稱為MyProgressBar.cs, 修改此檔, 編譯後, 工具箱出現MyProgressBar控件

namespace vcs_MyProgressBar
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

        int v = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            myProgressBar1.Value = v;
            v++;
            if (v > 100)
            {
                v = 0;
            }
        }
    }
}
