using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考 http://www.jysblog.com/coding/c-%e5%ad%90%e8%a6%96%e7%aa%97%e6%8e%a7%e5%88%b6%e7%88%b6%e8%a6%96%e7%aa%97%e4%b9%8b%e6%8e%a7%e4%bb%b6/
/*
Form1之 button1的「Modifiers」屬性變更為“public”，以供Form2存取。
*/

namespace 子視窗控制父視窗之控件
{
    public partial class Form1 : Form
    {
        private Form2 frm2 = null;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //將Form1傳入Form2中
            frm2 = new Form2(this);
            frm2.ShowDialog();
        }
    }
}
