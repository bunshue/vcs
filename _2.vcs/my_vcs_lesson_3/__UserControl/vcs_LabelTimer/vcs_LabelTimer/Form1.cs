using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//複合控制項(Composite Control)

//專案 / 右鍵 / 加入 / 使用者控制項(U)  將 UserControl1.cs 改成 LabelTimer.cs


namespace vcs_LabelTimer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            labelTimer1.Location = new System.Drawing.Point(30, 30);
            labelTimer1.Text = "現在時間 : ";
        }
    }
}
