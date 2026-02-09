using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace Linq_to_DataSet1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //建立DataSet物件ds，ds建立於所有事件處理函式之外以便所有事件一起共用
        DataSet ds = new DataSet();
        // 表單載入時執行此事件處理函式
        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;" +
                   "AttachDbFilename=|DataDirectory|ch20DB.mdf;" +
                   "Integrated Security=True";
                SqlDataAdapter daEmployee = new SqlDataAdapter
                ("SELECT * FROM 員工 ORDER BY 編號 DESC", cn);
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }

        // 按 [確定] 鈕執行此事件處理函式 
        private void btnOk_Click(object sender, EventArgs e)
        {
            try
            {
                DataTable dtEmp = ds.Tables["員工"];
                var emp = from p in dtEmp.AsEnumerable()
                          where p.Field<int>("薪資") >= int.Parse(txtInput.Text)
                          orderby p.Field<int>("薪資") descending
                          select new
                          {
                              員工編號 = p.Field<int>("編號"),
                              員工姓名 = p.Field<string>("姓名"),
                              員工電話 = p.Field<string>("電話"),
                              員工職稱 = p.Field<string>("職稱"),
                              員工薪資 = p.Field<int>("薪資")
                          };
                dataGridView1.DataSource = emp.ToList();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}

