using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace StoredProcedure2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 按下 [查詢] 鈕執行此事件
        private void btnOk_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                try
                {
                    cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch18DB.mdf;" +
                    "Integrated Security=True";
                    SqlCommand cmd = new SqlCommand();
                    cmd.Connection = cn;
                    cmd.CommandText = "GetStockByQty";
                    cmd.CommandType = CommandType.StoredProcedure;
                    cmd.Parameters.Add(new SqlParameter("@QMin", SqlDbType.NVarChar));
                    cmd.Parameters.Add(new SqlParameter("@QMax", SqlDbType.NVarChar));
                    cmd.Parameters["@QMin"].Value = int.Parse(txtMin.Text);
                    cmd.Parameters["@QMax"].Value = int.Parse(txtMax.Text);
                    SqlDataAdapter daStock = new SqlDataAdapter();
                    daStock.SelectCommand = cmd;
                    DataSet ds = new DataSet();
                    daStock.Fill(ds, "股票行情表");
                    dataGridView1.DataSource = ds.Tables["股票行情表"];
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }
    }
}
