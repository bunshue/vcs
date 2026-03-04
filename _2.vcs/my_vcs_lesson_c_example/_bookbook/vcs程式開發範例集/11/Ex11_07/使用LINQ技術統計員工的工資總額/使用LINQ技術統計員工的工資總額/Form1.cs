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
        string strCon = "Data Source=(local);database=db_11;uid=sa;pwd=;";
        SqlConnection sqlcon;
        SqlDataAdapter sqlda;
        DataSet myds;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bindinfo();
        }

        private void bindinfo()
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
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
            button3.Text = "工資總額：" + intSum.ToString() + "元";
        }
    }
}


