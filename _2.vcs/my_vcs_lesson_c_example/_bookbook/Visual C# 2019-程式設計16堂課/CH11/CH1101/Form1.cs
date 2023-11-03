using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1101
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            string name = txtName.Text;
            string pwd = txtPwd.Text;
            DateTime login = DateTime.Now; //取得當前時間
            if (name == string.Empty)  //名稱空白
            {
                MessageBox.Show("請重新輸入");
            }
            //密碼長度小於5個或大於10個字元都不可以
            else if (pwd.Length < 5 || pwd.Length > 10)
            {
                MessageBox.Show("不符合設定");
            }
            else
            {
                //Environment.NewLine換行
                txtShow.Text = $"Hi! {name}," +
                   Environment.NewLine +
                   $"登入時間 {login.ToShortTimeString()}";
            }
        }
    }
}
