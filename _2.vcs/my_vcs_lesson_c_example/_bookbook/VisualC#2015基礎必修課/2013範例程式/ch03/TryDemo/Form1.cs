using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TryDemo
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
        {
            try
            {   //可能發生錯誤的程式碼放在try區塊中
                int degree = Convert.ToInt32(txtDegree.Text);
                txtTotal.Text = Convert.ToString(degree * 2.1) + "元";
            }
            catch   //發生錯誤時執行catch區塊
            {
                txtTotal.Text = "度數請輸入數值！"; //顯示提示訊息
                txtDegree.Clear();      //清空錯誤資料
            }
            txtDegree.Focus();    //將停駐焦點移到txtDegree
        }
    }
}
