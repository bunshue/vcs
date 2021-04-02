using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.DirectoryServices;
using System.Data.SqlClient;

namespace AuthenticateTextBoxInput
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnConcel_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        string strA = null;
        string strB = null;
        private void txtPasword_Validating(object sender, CancelEventArgs e)
        {
            if (txtPasword.Text != "mrsoft")//判斷輸入是否正確
            {
                errPassword.SetError(txtPasword, "密碼確誤");
            }
            else
            {
                errPassword.SetError(txtPasword, "");
                strA = txtPasword.Text;
            }
        }

        private void txtUser_Validating(object sender, CancelEventArgs e)
        {
            if (txtUser.Text != "mr")
            {
                errUser.SetError(txtUser, "登錄名錯誤");
            }
            else
            {
                errUser.SetError(txtUser, "");
                strB = txtUser.Text;
            }
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            if (strB != null && strA != null)
            { MessageBox.Show("登錄成功"); }
            else { MessageBox.Show("輸入用戶名和密碼"); }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }//

    }
}