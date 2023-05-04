using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace TimeFind
{
    public partial class Frm_Main : Form
    {
        string filename = @"C:\______test_files1\_vcs200_db\db_TomeTwo.mdf";
        //string filename = @"C:\______test_files1\_vcs200_db\db_TomeTwo_log.ldf";   another

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
            dgv_Message.DataSource = GetBook(//设置数据源
                dtPicker_Begin.Value, dtPicker_End.Value);
        }

        /// <summary>
        /// 查询数据库信息
        /// </summary>
        /// <returns>方法返回DataTable对象</returns>
        private DataTable GetBook(DateTime dt1, DateTime dt2)
        {
            string P_Str_ConnectionStr = string.Format(//创建数据库连接字符串
                @"server=USER-20170504OU;database=db_TomeTwo;uid=sa;pwd=");
            string P_Str_SqlStr = string.Format(//创建SQL查询字符串
                "SELECT * FROM tb_Book WHERE 日期 BETWEEN '{0}' AND '{1}'",
                dt1, dt2);
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
                @"server=MR-PC\YL;database=db_TomeTwo;uid=sa;pwd=");
            string P_Str_SqlStr = string.Format(//创建SQL查询字符串
                "SELECT * FROM tb_Book");
            SqlDataAdapter P_SqlDataAdapter = new SqlDataAdapter(//创建数据适配器
                P_Str_SqlStr, P_Str_ConnectionStr);
            DataTable P_dt = new DataTable();//创建数据表
            P_SqlDataAdapter.Fill(P_dt);//填充数据表
            return P_dt;//返回数据表
        }
    }
}
