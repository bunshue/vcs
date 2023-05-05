using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace SelectComplex
{
    public partial class Frm_Main : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo_log.ldf";   another

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            dgv_Message.DataSource = GetMessage();//设置数据源
        }

        private void btn_Select_Click(object sender, EventArgs e)
        {
            try
            {
                dgv_Message.DataSource =//设置数据源
                    GetStudent(txt_Name.Text, int.Parse(txt_Age.Text),
                    txt_Address.Text);
            }
            catch (Exception ex)//捕获异常
            {
                MessageBox.Show(ex.Message, "提示！");//弹出消息对话框
            }
        }

        /// <summary>
        /// 查询数据库信息
        /// </summary>
        /// <returns>方法返回DataTable对象</returns>
        private DataTable GetStudent(string Name, int Age, string Address)
        {
            string P_Str_ConnectionStr = string.Format(//创建数据库连接字符串
                @"server=mr-pc\yl;database=db_TomeTwo;uid=sa;pwd=");
            string P_Str_SqlStr = string.Format(//创建SQL查询字符串
                @"SELECT 学生姓名,年龄,性别,家庭住址 FROM tb_Student
            WHERE 学生姓名 LIKE '{0}%' and 年龄 LIKE '{1}%' and 家庭住址 LIKE '{2}%'",
                Name, Age, Address);
            SqlDataAdapter P_SqlDataAdapter = new SqlDataAdapter(//创建数据适配器
                P_Str_SqlStr, P_Str_ConnectionStr);
            DataTable P_dt = new DataTable();//创建数据表
            P_SqlDataAdapter.Fill(P_dt);//填充数据表
            return P_dt;//返回数据表
        }

        /// <summary>
        /// 查询数据库信息
        /// </summary>
        /// <returns>方法返回DataTable对象</returns>
        private DataTable GetMessage()
        {
            string P_Str_ConnectionStr = string.Format(//创建数据库连接字符串
                @"server=USER-20170504OU;database=db_TomeTwo;uid=sa;pwd=");
            string P_Str_SqlStr = string.Format(//创建SQL查询字符串
                "SELECT  学生姓名,年龄,性别,家庭住址 FROM tb_Student");
            SqlDataAdapter P_SqlDataAdapter = new SqlDataAdapter(//创建数据适配器
                P_Str_SqlStr, P_Str_ConnectionStr);
            DataTable P_dt = new DataTable();//创建数据表
            P_SqlDataAdapter.Fill(P_dt);//填充数据表
            return P_dt;//返回数据表
        }
    }
}
