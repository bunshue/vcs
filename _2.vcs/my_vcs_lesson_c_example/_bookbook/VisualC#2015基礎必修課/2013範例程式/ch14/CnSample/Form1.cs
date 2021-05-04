using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace CnSample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        String cnStr = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True";
        //表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection(cnStr);
            SqlDataAdapter da = new SqlDataAdapter("SELECT * From 員工", cn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0];
        }
        //按新增鈕執行
        private void btnAdd_Click(object sender, EventArgs e)
        {
            try
            {
                SqlConnection cn = new SqlConnection(cnStr);
                cn.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = "INSERT INTO 員工(員工編號,姓名,性別,薪資)VALUES(N'" +
                    txtId.Text.Replace("'", "''") + "',N'" +
                    txtName.Text.Replace("'", "''") + "',N'" +
                    cboSex.Text + "'," +
                    txtSalary.Text + ")";
                cmd.Connection = cn;
                cmd.ExecuteNonQuery();
                Form1_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        //按修改鈕執行
        private void btnUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                SqlConnection cn = new SqlConnection(cnStr);
                cn.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = "UPDATE 員工 SET 姓名=N'" +
                    txtName.Text.Replace("'", "''") + "', 性別=N'" +
                    cboSex.Text + "', 薪資=" +
                    txtSalary.Text + " WHERE 員工編號=N'" +
                    txtId.Text.Replace("'", "''") + "'";
                cmd.Connection = cn;
                cmd.ExecuteNonQuery();
                Form1_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        //按刪除鈕執行
        private void btnDel_Click(object sender, EventArgs e)
        {
            try
            {
                SqlConnection cn = new SqlConnection(cnStr);
                cn.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = "DELETE FROM 員工 WHERE 員工編號=N'" +
                    txtId.Text.Replace("'", "''") + "'";
                cmd.Connection = cn;
                cmd.ExecuteNonQuery();
                Form1_Load(sender, e);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}

