using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace RelationsDemo1
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
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;" +
                    @"AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\Northwind.mdf;" +
                    "Integrated Security=True";
                DataSet ds = new DataSet();
                SqlDataAdapter daCategory = new SqlDataAdapter("SELECT * FROM 產品類別", cn);
                daCategory.Fill(ds, "產品類別");
                SqlDataAdapter daProduct = new SqlDataAdapter("SELECT * FROM 產品資料", cn);
                daProduct.Fill(ds, "產品資料");
                ds.Relations.Add("FK_產品資料_產品類別", ds.Tables["產品類別"].Columns["類別編號"], ds.Tables["產品資料"].Columns["類別編號"]);
                dgvCategory.DataSource = ds;
                dgvCategory.DataMember = "產品類別";
                dgvCategory.Dock = DockStyle.Top;  // dgvCategory停駐在表單上方
                dgvProduct.DataSource = ds;
                dgvProduct.DataMember = "產品類別.FK_產品資料_產品類別";
                dgvProduct.Dock = DockStyle.Fill;    // dgvProduct填滿整個表單
            }
        }
    }
}
