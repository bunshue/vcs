using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh3_2_1_11
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
            Form2 newMDIChild = new Form2();

            // 設定newMDIChild的MDI(Multiple Documnet Interface)父表單
            newMDIChild.MdiParent = this;
            newMDIChild.Show();
        }
    }
}

