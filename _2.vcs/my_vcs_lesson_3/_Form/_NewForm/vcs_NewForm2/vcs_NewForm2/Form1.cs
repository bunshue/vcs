using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NewForm2
{
    public partial class Form1 : Form
    {
        static int x = 200;
        static int y = 200;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            f2.Visible = true;

            // 每新增一個Form2表單，其出現的位置依序往右下角100個像素
            f2.SetDesktopLocation(x, y);
            x += 100;
            y += 100;

            // 讓Form1保持在Activate的狀態
            this.Activate();
        }
    }
}
