using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace StoredProcedure1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 按下 [查詢] 鈕執行
        private void btnOk_Click(object sender, EventArgs e)
        {
            if (txtName.Text == "")
            {
                txtResult.Text = "請輸入欲查詢的員工姓名";
                return;
            }
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch18DB.mdf;" +
                    "Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.Connection = cn;
                cmd.CommandText = "GetEmployeeByName";
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.Add(new SqlParameter("@EmpName", SqlDbType.NVarChar));
                cmd.Parameters["@EmpName"].Value = txtName.Text;
                txtResult.Text = "";
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.Read())
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        txtResult.Text += dr.GetName(i) + "：" + dr[i].ToString () + Environment.NewLine;
                    }
                }
                else
                {
                    txtResult.Text = "找不到" + txtName.Text + "這個員工";
                }
            }
        }
    }
}
