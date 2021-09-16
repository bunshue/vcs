using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace CommandDemo1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch17DB.mdf;" +
                    "Integrated Security=True";
                cn.Open();
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
                SqlCommand cmdCount, cmdSum, cmdAvg, cmdMax, cmdMin;
                //取員工資料筆數
                cmdCount = new SqlCommand("SELECT COUNT(*) FROM 員工", cn);
                lblCount.Text = "員工資料表共 " + cmdCount.ExecuteScalar().ToString () + " 筆記錄";
                //取薪資加總
                cmdSum = new SqlCommand("SELECT SUM(薪資) FROM 員工", cn);
                lblSum.Text = "員工資料表薪資加總共 " + cmdSum.ExecuteScalar().ToString ();
                //取薪資平均
                cmdAvg = new SqlCommand("SELECT AVG(薪資) FROM 員工", cn);
                lblAvg.Text = "員工資料表薪資平均為 " + cmdAvg.ExecuteScalar().ToString ();
                //取薪資最高薪
                cmdMax = new SqlCommand("SELECT Max(薪資) FROM 員工", cn);
                lblMax.Text = "最高薪為 " + cmdMax.ExecuteScalar().ToString ();
                //取薪資最低薪
                cmdMin = new SqlCommand("SELECT Min(薪資) FROM 員工", cn);
                lblMin.Text = "最低薪為 " + cmdMin.ExecuteScalar().ToString ();
            }
        }
    }
}
