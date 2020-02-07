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

namespace 父子視窗傳值問題
{
    public partial class Form1 : Form
    {
        private string strValue;
        public string MsgFromChild
        {
            set { strValue = value; }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form2 childForm = new Form2();
            childForm.Msg = "父告訴子一件事~~~~~~~";
            childForm.setValue();
            childForm.ShowDialog();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 childForm = new Form2();
            // important!! Point the Form2's owner to Form1
            childForm.Owner = this;
            childForm.ShowDialog();
            MessageBox.Show(strValue);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //Form2 childForm = new Form2();
            //childForm.ShowDialog();
        }
    }
}
