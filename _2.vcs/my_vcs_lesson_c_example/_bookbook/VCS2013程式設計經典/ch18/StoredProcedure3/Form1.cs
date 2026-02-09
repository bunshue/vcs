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

        private void ShowData(string cnstr)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;
                SqlDataAdapter daEmployee = new SqlDataAdapter("GetEmployee", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        // 按下 [新增] 鈕時執行
        private void btnAdd_Click(object sender, EventArgs e)
        {
            //讀取

            // 宣告cnStr用來存放連接ch17DB.mdf的連接字串
            string cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;" +
                @"AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch18DB.mdf;" +
                "Integrated Security=True";

            ShowData(cnStr);

            //新增
            try
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnStr;
                    cn.Open();
                    /* same
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
                    */
                    SqlCommand cmd = new SqlCommand("InsertEmployeeReturnEmpId", cn);
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.Parameters.Add(new SqlParameter("@name", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@position", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@tel", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@salary", SqlDbType.Int));
                    cmd.Parameters.Add(new SqlParameter("@RETURN_VALUE", SqlDbType.Int));
                    cmd.Parameters["@RETURN_VALUE"].Direction = ParameterDirection.ReturnValue;
                    cmd.Parameters["@name"].Value = txtName.Text;
                    cmd.Parameters["@position"].Value = txtPosition.Text;
                    cmd.Parameters["@tel"].Value = txtTel.Text;
                    cmd.Parameters["@salary"].Value = int.Parse(txtSalary.Text);
                    cmd.ExecuteNonQuery();
                    int EmpId = int.Parse(cmd.Parameters["@RETURN_VALUE"].Value.ToString());
                    MessageBox.Show(txtName.Text + "的員工編號是 " + EmpId.ToString(), "員工編號");
                }
                ShowData(cnStr);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            //修改

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
                ShowData(cnStr);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            //刪除

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
                ShowData(cnStr);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // 按下 [修改] 鈕時執行
        private void btnUpdate_Click(object sender, EventArgs e)
        {
        }

        // 按下 [刪除] 鈕執行 
        private void btnDel_Click(object sender, EventArgs e)
        {
        }
    }
}
