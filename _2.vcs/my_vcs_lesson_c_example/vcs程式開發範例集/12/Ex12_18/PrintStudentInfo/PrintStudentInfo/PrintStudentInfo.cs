using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace PrintStudentInfo
{
    public partial class PrintStudentInfo : Form
    {
        public PrintStudentInfo()
        {
            InitializeComponent();
        }
        SqlConnection sqlcon = new SqlConnection("Data Source=.;Database=db_12;integrated security=sspi");
        SqlDataAdapter myda;
        DataSet myds;

        private void Form1_Load(object sender, EventArgs e)
        {
            myda = new SqlDataAdapter("select * from tb_18", sqlcon);
            myds = new DataSet();
            sqlcon.Open();
            myda.Fill(myds);
            sqlcon.Close();
            dataGridView1.DataSource = myds.Tables[0];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ExportDataGridview(dataGridView1, true);
        }

        public bool ExportDataGridview(DataGridView dgv, bool isShowExcle)
        {
            if (dgv.Rows.Count == 0)
                return false;
            //建立Excel對像
            Excel.Application excel = new Excel.Application();
            excel.Application.Workbooks.Add(true);
            excel.Visible = isShowExcle;
            //產生字段名稱
            for (int i = 0; i < dgv.ColumnCount; i++)
            {
                excel.Cells[1, i + 1] = dgv.Columns[i].HeaderText;
            }
            //填充數據
            for (int i = 0; i < dgv.RowCount - 1; i++)
            {
                for (int j = 0; j < dgv.ColumnCount; j++)
                {
                    if (dgv[j, i].ValueType == typeof(string))
                    {
                        excel.Cells[i + 2, j + 1] = "'" + dgv[j, i].Value.ToString();
                    }
                    else
                    {
                        excel.Cells[i + 2, j + 1] = dgv[j, i].Value.ToString();
                    }
                }
            }
            return true;
        }
    }
}
