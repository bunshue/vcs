using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace TakeWhile
{
    public partial class Frm_Main : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo_log.ldf";   another

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            string conStr = "Data Source=MR-PC\\YL;Database=db_TomeTwo;UID=sa;Pwd=;";//取连接字符串
            string sql = "select * from EmployeeInfo";//构造sql语句
            DataSet ds = new DataSet();//创建数据集
            using (SqlConnection con = new SqlConnection(conStr))//创建数据连接
            {
                SqlCommand cmd = new SqlCommand(sql, con);//创建Command对象
                SqlDataAdapter sda = new SqlDataAdapter(cmd);//创建DataAdapter对象
                sda.Fill(ds, "EmployeeInfo");//填充数据集
            }
            //从头开始提取生日小于2009-7-1之前的员工信息
            IEnumerable<DataRow> query = ds.Tables["EmployeeInfo"].AsEnumerable().TakeWhile(itm => itm.Field<DateTime>("Birthday") < Convert.ToDateTime("2009-7-1"));
            dataGridView1.DataSource = query.CopyToDataTable();//设置dataGridView1数据源
        }
    }
}
