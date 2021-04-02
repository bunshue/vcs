using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace 使用LINQ技術查詢前5名數據
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        #region 定義全局變數及對像
        string strCon = "Data Source=(local);Database=db_11;Uid=sa;Pwd=;";
        linqtosqlDataContext linq;
        #endregion

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

        private void button2_Click(object sender, EventArgs e)
        {
            binginfo();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            linq = new linqtosqlDataContext(strCon);
            var result = (from info in linq.tb_User orderby info.ID ascending select new 
            {
                編號 = info.ID,
                姓名 = info.User_Name.Trim(),
                性別 = info.User_Sex.Trim(),
                年齡 = info.User_Age.Trim(),
                婚姻狀況 = info.User_Marriage.Trim(),
                職位 = info.User_Duty.Trim(),
                聯繫電話 = info.User_Phone.Trim(),
                聯繫地址 = info.User_Address.Trim()
            }).Take(5);
            dataGridView1.DataSource = result;
        }
    }
}
