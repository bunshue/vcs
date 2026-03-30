using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace UseINRange
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Frm_Main_Load(object sender, EventArgs e)
        {

        }

        private void btn_Select_Click(object sender, EventArgs e)
        {
            //设置数据源
            dgv_Message.DataSource = GetStudent(txt_Begin.Text, txt_End.Text);
            dgv_Message.Columns[2].Width = 200;//设置列宽度
        }

        /// <summary>
        /// 查询学生信息
        /// </summary>
        /// <returns>方法返回DataTable对象</returns>
        private DataTable GetStudent(string Begin, string end)
        {
            // 連接字串
            String P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 查詢字串
            string P_Str_SqlStr = string.Format(@"SELECT 学生姓名,性别,年龄 FROM tb_Student WHERE 学生编号 IN (SELECT 学生编号 FROM tb_Grade WHERE 总分>{0} AND 总分<{1})", Begin, end);
            //创建数据适配器
            SqlDataAdapter P_SqlDataAdapter = new SqlDataAdapter(P_Str_SqlStr, P_Str_ConnectionStr);
            DataTable P_dt = new DataTable();//创建数据表
            P_SqlDataAdapter.Fill(P_dt);//填充数据表
            return P_dt;//返回数据表
        }
    }
}
