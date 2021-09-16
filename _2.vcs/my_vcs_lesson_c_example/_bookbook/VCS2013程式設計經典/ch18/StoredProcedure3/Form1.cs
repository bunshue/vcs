using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace StoredProcedure3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 宣告cnStr用來存放連接ch17DB.mdf的連接字串
        string cnStr = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch18DB.mdf;" +
                    "Integrated Security=True";

        // 定義ShowData()方法
        // 此方法用來將員工資料表的所有記錄顯示於dataGridView1上
        private void ShowData()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;
                SqlDataAdapter daEmployee = new SqlDataAdapter("GetEmployee", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            ShowData();
        }
        // 按下 [新增] 鈕時執行
        private void btnAdd_Click(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection cn = new SqlConnection())
                {

                    cn.ConnectionString = cnStr;
                    cn.Open();
                    SqlCommand cmd = new SqlCommand("InsertEmployee", cn);
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@position", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@tel", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@salary", SqlDbType.Int));
                    cmd.Parameters["@name"].Value = txtName.Text;
                    cmd.Parameters["@position"].Value = txtPosition.Text;
                    cmd.Parameters["@tel"].Value = txtTel.Text;
                    cmd.Parameters["@salary"].Value = int.Parse(txtSalary.Text);
                    cmd.ExecuteNonQuery();
                }
                ShowData();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        // 按下 [修改] 鈕時執行
        private void btnUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnStr;
                    cn.Open();
                    SqlCommand cmd = new SqlCommand("UpdateEmployee", cn);
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@position", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@tel", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@salary", SqlDbType.Int));
                    cmd.Parameters["@name"].Value = txtName.Text;
                    cmd.Parameters["@position"].Value = txtPosition.Text;
                    cmd.Parameters["@tel"].Value = txtTel.Text;
                    cmd.Parameters["@salary"].Value = int.Parse(txtSalary.Text);
                    cmd.ExecuteNonQuery();
                }
                ShowData();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        // 按下 [刪除] 鈕執行 
        private void btnDel_Click(object sender, EventArgs e)
        {
            try
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnStr;
                    cn.Open();
                    SqlCommand cmd = new SqlCommand("DeleteEmployee", cn);
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters["@name"].Value = txtName.Text;
                    cmd.ExecuteNonQuery();
                }
                ShowData();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
