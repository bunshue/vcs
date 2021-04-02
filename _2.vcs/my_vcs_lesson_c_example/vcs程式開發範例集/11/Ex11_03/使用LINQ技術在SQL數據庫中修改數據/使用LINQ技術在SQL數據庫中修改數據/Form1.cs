using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 使用LINQ技術在SQL數據庫中修改數據
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string strCon = "Data Source=(local);database=db_11;uid=sa;pwd=;";
        linqtosqlDataContext linq;
        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
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
            binginfo();
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            txtName.Focus();
        }

        private void dataGridView1_Click(object sender, EventArgs e)
        {

        }
        int Pid;
        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (dataGridView1.SelectedRows.Count != 0)
            {
                linq = new linqtosqlDataContext(strCon);
                int id = Convert.ToInt32(dataGridView1.SelectedRows[0].Cells[0].Value);
                Pid = id;
                var result = from info in linq.tb_User
                             where info.ID == id
                             select new
                             {
                                 Name = info.User_Name,
                                 Sex = info.User_Sex,
                                 Age = info.User_Age,
                                 Mary = info.User_Marriage,
                                 Duty = info.User_Duty,
                                 Phone = info.User_Phone,
                                 Address = info.User_Address
                             };
                foreach (var item in result)
                {
                    txtName.Text = item.Name.Trim();
                    cbbSex.Text = item.Sex.Trim();
                    txtage.Text = item.Age.Trim();
                    cbbmary.Text = item.Mary.Trim();
                    cbbduty.Text = item.Duty.Trim();
                    txtphone.Text = item.Phone.Trim();
                    txtaddress.Text = item.Address.Trim();
                }
            }
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
                    var resultChange = from info in linq.tb_User
                                       where info.ID == Pid
                                       select info;
                    foreach (tb_User users in resultChange)
                    {
                        users.User_Name = txtName.Text;
                        users.User_Sex = cbbSex.Text;
                        users.User_Age = txtage.Text;
                        users.User_Marriage = cbbmary.Text;
                        users.User_Duty = cbbduty.Text;
                        users.User_Phone = txtphone.Text;
                        users.User_Address = txtaddress.Text;
                        linq.SubmitChanges();
                    }
                    MessageBox.Show("修改成功");
                    binginfo();
                }
            }
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
            if (txtage.Text.StartsWith("0"))
            {
                MessageBox.Show("年齡不能以0開頭");
                txtage.Text = "";
            }
        }
    }
}
