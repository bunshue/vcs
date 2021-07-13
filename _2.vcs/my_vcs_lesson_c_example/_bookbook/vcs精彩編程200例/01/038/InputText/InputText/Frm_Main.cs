using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.DirectoryServices;
using System.Data.SqlClient;

namespace InputText
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        string strA = null;//定义字符串字段
        string strB = null;//定义字符串字段

        private void txtPasword_Validating(object sender, CancelEventArgs e)
        {
            if (txtPasword.Text != "mouse")//判断密码是否正确
            {
                //显示密码错误信息
                errPassword.SetError(txtPasword, "密码确误");
            }
            else
            {
                //显示密码错误信息
                errPassword.SetError(txtPasword, "");
                strA = txtPasword.Text;//得到密码字符串
            }
        }

        private void txtUser_Validating(object sender, CancelEventArgs e)
        {
            if (txtUser.Text != "lion")//判断用户名是否正确
            {
                //显示用户名错误信息
                errUser.SetError(txtUser, "登录名错误");
            }
            else
            {
                //显示用户名错误信息
                errUser.SetError(txtUser, "");
                strB = txtUser.Text;//得到用户名字符串
            }
        }

        private void btnOK_Click(object sender, EventArgs e)
        {
            if (strB != null && strA != null)//验证用户名和密码是否正确
            {
                MessageBox.Show("登录成功");
            }
            else
            {
                MessageBox.Show("输入用户名和密码");
            }
        }
    }
}

