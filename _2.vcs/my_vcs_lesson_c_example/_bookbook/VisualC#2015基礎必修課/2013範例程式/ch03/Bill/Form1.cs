using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bill
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtDegree.MaxLength = 3;    //設最多只能輸入3位數
            txtTotal.ReadOnly = true;   //設為唯讀不能輸入
            txtDegree.TabIndex = 0;     //設為第一個停駐焦點
        }

        private void btnHome_Click(object sender, EventArgs e)
        {   //將輸入的數字字串轉成整數，並指定給整數變數degree
            int degree = Convert.ToInt32(txtDegree.Text);
            txtTotal.Text = Convert.ToString(degree * 2.1) + "元";
            txtDegree.Focus();    //將停駐焦點移到txtDegree
        }
    }
}
