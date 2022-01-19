using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//滾動提示窗口

//加入/Windows Form

namespace vcs_Form7_ScrollShow
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

        private void button1_Click(object sender, EventArgs e)
        {
            Form2 form = new Form2();

            form.HeightMax = 120;//窗體滾動的高度
            form.WidthMax = 148;//窗體滾動的寬度
            form.ScrollShow();

        }
    }
}
