using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Text.RegularExpressions;
namespace CorporationEmployeeICCard
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
        private void Form2_Load(object sender, EventArgs e)
        {
            cbFolk.SelectedIndex = 0;//民族选项默认第一项被选中
            cbSex.SelectedIndex = 0;//性别选项默认第一项被选中
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtDept.Text == "" || txtICCard.Text == "" || txtJob.Text == "" || txtName.Text == "")
            {
                MessageBox.Show("请将信息输入完整！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                string icID = txtICCard.Text.Trim();//要写入IC卡的数据
                string name = txtName.Text.Trim();//员工姓名
                string sex = cbSex.Text.Trim();//员工性别
                string job = txtJob.Text.Trim();//员工职位
                string folk= cbFolk.Text.Trim();//员工民族
                string dept = txtDept.Text.Trim();//员工部门
                if (baseClass.CheckID(icID))//CheckID方法检查编号是否存在
                {
                    MessageBox.Show("IC卡编号已经存在！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    if (baseClass.WriteIC(icID) == 0)//WriteIC方法将编号写入IC卡，如果成功则返回0
                    {
                        //声明一条语句，用于将员工其他信息插入到数据表中
                        string strSQL = "insert into Employee(CardID,E_Name,E_Sex,E_Job,E_Folk,E_Dept,E_Time) values('" + icID + "','" + name + "','" + sex + "','" + job + "','" + folk + "','" + dept + "','"+DateTime.Now.ToShortDateString()+"')";
                        if (baseClass.ExecuteSQL(strSQL))//ExecuteSQL方法执行这条语句
                        {
                            MessageBox.Show("IC卡注册完毕！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        }
                    }
                }
            }
        }

        private void txtICCard_TextChanged(object sender, EventArgs e)
        {
            if (Regex.IsMatch(txtICCard.Text.Trim(), "[\u4e00-\u9fa5]"))
            {
                MessageBox.Show("禁止输入汉字！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }
}
