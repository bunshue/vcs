using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MDI1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //設定能使用MDI容器
            this.IsMdiContainer = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //開啟新表單
            Form2 f2 = new Form2();
            f2.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //開啟MDI子表單
            Form2 newMDIChild = new Form2();

            // 設定newMDIChild的MDI(Multiple Documnet Interface)父表單
            newMDIChild.MdiParent = this;
            newMDIChild.Show();
        }
    }
}
