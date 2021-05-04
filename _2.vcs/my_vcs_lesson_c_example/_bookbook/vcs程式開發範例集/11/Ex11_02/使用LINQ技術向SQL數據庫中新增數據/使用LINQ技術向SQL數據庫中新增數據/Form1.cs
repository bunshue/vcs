using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 使用LINQ技術向SQL數據庫中新增數據
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string strCon = "Data Source=(local);database=db_11;uid=sa;pwd=;";
        linqtosqlDataContext linq;
        private void Form1_Activated(object sender, EventArgs e)
        {
            txtName.Focus();
        }
        private void binginfo()
        {
            linq = new linqtosqlDataContext(strCon);
            var result = from info in linq.tb_User
                         select new 
                         {
                             編號 = info.ID,
                             姓名 = info.User_Name.Trim(),
                             性別 = info.User_Sex.Trim(),
                             年齡 = info.User_Age.Trim(),
                             婚姻狀況 = info.User_Marriage.Trim(),
                             職位 = info.User_Duty.Trim(),
                             聯繫電話 = info.User_Phone.Trim(),
                             聯繫地址 = info.User_Address.Trim()
                         };
            dataGridView1.DataSource = result;
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            cbbduty.SelectedIndex = 0;
            cbbmary.SelectedIndex = 0;
            cbbSex.SelectedIndex = 0;
            binginfo();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtaddress.Text != "" && txtage.Text != "" && txtName.Text != "" && txtphone.Text != "")
            {
                if (txtphone.Text.Length != 11)
                {
                    MessageBox.Show("電話號碼位數不正確");
                }
                else
                {
                    linq = new linqtosqlDataContext(strCon);
                    tb_User users = new tb_User();
                    users.User_Name = txtName.Text.Trim();
                    users.User_Sex = cbbSex.Text;
                    users.User_Age = txtage.Text;
                    users.User_Marriage = cbbmary.Text;
                    users.User_Duty = cbbduty.Text;
                    users.User_Phone = txtphone.Text;
                    users.User_Address = txtaddress.Text;
                    linq.tb_User.InsertOnSubmit(users);
                    linq.SubmitChanges();
                    binginfo();
                    MessageBox.Show("新增成功");
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void txtage_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!(e.KeyChar <= '9' && e.KeyChar >= '0') && e.KeyChar != '\r' && e.KeyChar != '\b')
            {
                e.Handled = true;
            }
        }

        private void txtphone_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!(e.KeyChar <= '9' && e.KeyChar >= '0') && e.KeyChar != '\r' && e.KeyChar != '\b')
            {
                e.Handled = true;
            }
        }

        private void txtage_KeyUp(object sender, KeyEventArgs e)
        {
            if(txtage.Text.StartsWith("0"))
            {
                MessageBox.Show("年齡不能以0開頭");
                txtage.Text = "";
            }
        }
    }
}
