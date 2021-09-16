using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace StoredProcedure5
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
                    "AttachDbFilename=|DataDirectory|ch18DB.mdf;" +
                    "Integrated Security=True";
                cn.Open();
                SqlDataAdapter daEmployee = new SqlDataAdapter("GetEmployee", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
                SqlCommand cmd = new SqlCommand();

                // 與資料庫連接
                cmd.Connection = cn;
                // 指定Command要執行的是預存程序
                cmd.CommandType = CommandType.StoredProcedure;
                // 執行GetEmployeeStatistics預存程序
                cmd.CommandText = "GetEmployeeStatistics";
                // 設定預存程序的參數
                cmd.Parameters.Add(new SqlParameter("@EmpCount", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@SalarySum", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@SalaryAvg", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@SalaryMax", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter("@SalaryMin", SqlDbType.Int));
                // 設定預存程序的參數為傳出型態
                cmd.Parameters["@EmpCount"].Direction = ParameterDirection.Output;
                cmd.Parameters["@SalarySum"].Direction = ParameterDirection.Output;
                cmd.Parameters["@SalaryAvg"].Direction = ParameterDirection.Output;
                cmd.Parameters["@SalaryMax"].Direction = ParameterDirection.Output;
                cmd.Parameters["@SalaryMin"].Direction = ParameterDirection.Output;
                // 執行預存程序
                cmd.ExecuteNonQuery();

                int intCount, intSum, intAvg, intMax, intMin;
                // 取得傳出的預存程序
                intCount = int.Parse(cmd.Parameters["@EmpCount"].Value.ToString());
                intSum = int.Parse(cmd.Parameters["@SalarySum"].Value.ToString());
                intAvg = int.Parse(cmd.Parameters["@SalaryAvg"].Value.ToString());
                intMax = int.Parse(cmd.Parameters["@SalaryMax"].Value.ToString());
                intMin = int.Parse(cmd.Parameters["@SalaryMin"].Value.ToString());

                // 取員工資料筆數
                lblCount.Text = "員工資料表共 " + intCount + " 筆記錄";
                // 取薪資加總
                lblSum.Text = "員工資料表薪資加總共 " + intSum;
                // 取薪資平均
                lblAvg.Text = "員工資料表薪資平均為 " + intAvg;
                // 取薪資最高薪
                lblMax.Text = "最高薪為 " + intMax;
                // 取薪資最低薪
                lblMin.Text = "最低薪為 " + intMin;
            }
        }
    }
}
