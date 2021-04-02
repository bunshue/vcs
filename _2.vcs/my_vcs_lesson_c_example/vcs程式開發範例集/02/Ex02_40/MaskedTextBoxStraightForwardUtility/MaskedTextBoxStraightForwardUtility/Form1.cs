using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace MaskedTextBoxStraightForwardUtility
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            maskedTextBox1.Mask = "00";//只能輸入數字
            maskedTextBox2.ValidatingType = typeof(System.DateTime);//只能輸入日期
        }
        //格式不正確
        private void maskedTextBox1_MaskInputRejected(object sender, MaskInputRejectedEventArgs e)
        {
            toolTip1.ToolTipTitle = "年齡錄入";
            toolTip1.Show("年齡只能錄入數字", maskedTextBox1, maskedTextBox1.Location, 5000);
            maskedTextBox1.SelectAll();
            maskedTextBox1.SelectionStart = 0;
            maskedTextBox1.Focus();
        }
        //數據類型不正確
        private void maskedTextBox2_TypeValidationCompleted(object sender, TypeValidationEventArgs e)
        {
            if (!e.IsValidInput)
            {
                toolTip1.ToolTipTitle = "日期錄入";
                toolTip1.Show("錄入日期格式不正確 ", maskedTextBox1, 5000);
                e.Cancel = true;
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
                MessageBox.Show("保存成功！！");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();

        }
    }
}