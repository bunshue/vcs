using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class MyForm : Form
    {
        public MyForm()
        {
            InitializeComponent();
        }

        private void MyForm_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ModalForm mf = new ModalForm();

            mf.ShowDialog();  //顯示表單          
            if (mf.DialogResult == DialogResult.OK) { //判斷使用者的動作
            // if (mf.ShowDialog() == DialogResult.OK) {
                MessageBox.Show("你輸入了" + mf.mInput + "!");
                //MessageBox.Show("你輸入了" + mf.getInput() + "!");
                //MessageBox.Show("你輸入了" + mf.txtInput.Text + "!"); // public
            }
            else if (mf.DialogResult == DialogResult.Cancel)
            {
                MessageBox.Show("你按了取消鍵!");
            }
            else MessageBox.Show("未知選項!");

            mf.Dispose(); // 釋放表單資源
        }
    }
}
