using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1207
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void txtName_KeyPress(object sender,
              KeyPressEventArgs e)
        {
            int word;
            word = (int)(e.KeyChar);
            if (word < 65 || word > 90) //判斷是否輸入字元為A~Z
            {
                MessageBox.Show("必須輸入A~Z的字元");
                e.Handled = true; ;//不能忽略使用者輸入的字元
                txtName.Clear(); //清除文字方塊內容            
            }
        }

        private void txtPhone_KeyPress(object sender, KeyPressEventArgs e)
        {
            int wd;
            wd = (int)(e.KeyChar);
            if (wd < 48 || wd > 57) //判斷是否輸入字元為A~Z
            {
                MessageBox.Show("必須輸入0~9的數字");
                e.Handled = true; ;//不能忽略使用者輸入的字元
            }
        }
    }
}
