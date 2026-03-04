using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;//聲明與數據庫操作有關的命名空間

namespace ListWaferFacility
{
    public partial class ListWaferFacility : Form
    {
        public DataSet WaferSet = null;//定義一個數據集對像

        public ListWaferFacility()
        {
            InitializeComponent();
        }

        private void ListWaferFacility_Load(object sender, EventArgs e)
        {
            /*
            if (IsExistDataBase() == false)//當不存在數據庫連接時
            {
                Application.Exit();//退出應用程序
            }
            */
        }


        private bool IsExistDataBase()
        {
            SqlConnection con = new SqlConnection("Data Source=.;DataBase=master;integrated security=sspi");//初始化一個數據庫連接對像
            con.Open();//打開數據庫連接

            SqlCommand cmd = new SqlCommand("select count(*) from master.dbo.sysdatabases where name='db_02'", con);//執行一條SQL查詢語句
            if (Convert.ToInt32(cmd.ExecuteScalar()) == 0)//當無查詢結果時
            {
                MessageBox.Show("沒有建立數據庫，請用Data文件夾下的SQL語句建立數據庫！", "消息提示", MessageBoxButtons.OK, MessageBoxIcon.Warning);//彈出消息提示
                return false;//返回false
            }
            else //當存在查詢結果時
            {
                con.Close();//關閉數據庫連接
                return true;//返回true
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);//初始化一個數據庫連接對像
            con.Open();//打開數據庫連接

            SqlCommand cmd = new SqlCommand("select count(*) from master.dbo.sysdatabases where name='db_02'", con);//執行一條SQL查詢語句
            if (Convert.ToInt32(cmd.ExecuteScalar()) == 0)//當無查詢結果時
            {
                //MessageBox.Show("沒有建立數據庫，請用Data文件夾下的SQL語句建立數據庫！", "消息提示", MessageBoxButtons.OK, MessageBoxIcon.Warning);//彈出消息提示
                //return false;//返回false
                richTextBox1.Text += "111111 NG\n";
            }
            else //當存在查詢結果時
            {
                con.Close();//關閉數據庫連接
                //return true;//返回true
                richTextBox1.Text += "2222222 OK\n";
            }

            /*
            using (SqlConnection con = new SqlConnection(cnstr))
            {
                //SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases ", con);
                SqlDataAdapter da = new SqlDataAdapter("select count(*) from master.dbo.sysdatabases where name='db_02'", con);
                DataTable dt = new DataTable("sysdatabases");
                da.Fill(dt);

                richTextBox1.Text += dt.ToString() + "\n";
            }
            */

            //SqlCommand cmd = new SqlCommand("select count(*) from master.dbo.sysdatabases where name='db_02'", con);//執行一條SQL查詢語句


            /*

            try
            {
                SqlConnection con = new SqlConnection(cnstr);//"server=.;database=db_02;integrated security=sspi");//初始化一個數據庫連接對像
            }
            catch (Exception error)//捕獲異常信息
            {
                throw new Exception(error.Message);//顯示異常信息
            }
            */

            richTextBox1.Text += "done\n";
        }
    }
}

//string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";
