using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//http://www.jysblog.com/coding/c-%e7%88%b6%e5%ad%90%e8%a6%96%e7%aa%97%e5%82%b3%e5%80%bc%e5%95%8f%e9%a1%8c/

/*
簡單的說，
就是利用class中get, set以及form owner來控制變數值的傳遞。
*/

namespace vcs_FormSendData
{
    public partial class Form1 : Form
    {
        private string form1_data;
        public string SetupForm1Data
        {
            set
            {
                form1_data = value;
            }
        }

        public void setForm1Value()
        {
            this.richTextBox1.Text += "父得到信息 : " + form1_data + "\n";
        }

        Form2 childForm = new Form2();
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            childForm.SetupForm2Data = "父告訴子一件事~~~~~~~";
            childForm.setForm2Value();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            childForm.StartPosition = FormStartPosition.Manual;
            childForm.Location = new Point(this.Location.X + 550, this.Location.Y);
            childForm.Owner = this;
            //childForm.ShowDialog();
            childForm.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
