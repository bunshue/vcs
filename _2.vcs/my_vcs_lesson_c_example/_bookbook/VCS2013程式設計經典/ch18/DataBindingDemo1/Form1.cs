using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data .SqlClient ;

// 使用 控制項資料繫結

namespace DataBindingDemo1
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
                    @"AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\ch18DB.mdf;" +
                    "Integrated Security=True";
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工 ORDER BY 編號 DESC", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                // ComboBox控制項資料繫結
                cboId.DataSource = ds;
                cboId.DisplayMember = "員工.編號";

                // TextBox控制項資料繫結
                txtName.DataBindings.Add("Text", ds, "員工.姓名");
                txtTel.DataBindings.Add("Text", ds, "員工.電話");
                txtPosition.DataBindings.Add("Text", ds, "員工.職稱");

                txtSalary.DataBindings.Add("Text", ds, "員工.薪資");

                // DataGridView控制項資料繫結
                dataGridView1.DataSource = ds;
                dataGridView1.DataMember = "員工";
            }
        }
    }
}
