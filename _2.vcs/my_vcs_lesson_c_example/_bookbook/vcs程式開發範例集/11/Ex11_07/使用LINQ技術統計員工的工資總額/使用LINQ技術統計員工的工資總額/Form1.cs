using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace 使用LINQ技術統計員工的工資總額
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        linqtosqlDataContext linq;
        string strCon = "Data Source=(local);database=db_11;uid=sa;pwd=;";
        SqlConnection sqlcon;
        SqlDataAdapter sqlda;
        DataSet myds;
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
                             月薪=info.User_Pay,
                             聯繫電話 = info.User_Phone.Trim(),
                             聯繫地址 = info.User_Address.Trim()
                         };
            dataGridView1.DataSource = result;//對DataGridView控制元件進行數據綁定
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bindinfo();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            sqlcon = new SqlConnection(strCon);
            sqlda = new SqlDataAdapter("select * from tb_User", sqlcon);
            myds = new DataSet();
            sqlda.Fill(myds, "tb_User");
            var query = from salary in myds.Tables["tb_User"].AsEnumerable()
                        where salary.Field<int>("User_Pay") > 0
                        select salary;
            int intSum = query.Sum(salary => salary.Field<int>("User_Pay"));
            button3.Text = "工資總額："+intSum.ToString()+"元"; 
        }
    }
}
