using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 使用LINQ技術在SQL數據庫中刪除數據
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        linqtosqlDataContext linq;
        string strCon = "Data Source=(local);database=db_11;uid=sa;pwd=;";
        private void bindinfo()
        {
            linq = new linqtosqlDataContext(strCon);//實例化Linq連接對像
            //取得所有員工訊息
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
            dataGridView1.DataSource = result;//對DataGridView控制元件進行數據綁定
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            bindinfo();
        }
        int id;
        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (dataGridView1.SelectedRows.Count != 0)
            {
                id =Convert.ToInt32( dataGridView1.SelectedRows[0].Cells[0].Value);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count != 0)
            {
                linq = new linqtosqlDataContext(strCon);
                var result = from info in linq.tb_User
                             where info.ID == id
                             select info;
                linq.tb_User.DeleteAllOnSubmit(result);
                linq.SubmitChanges();
                MessageBox.Show("刪除成功");
                bindinfo();
            }
            else
            {
                MessageBox.Show("請選擇刪除項");
            }
        }
    }
}
