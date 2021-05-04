using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace ReadWriteXML_2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 宣告DataSet的ds物件在事件處理函式外以利所有事件共用
        DataSet ds = new DataSet();

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch19DB.mdf;" +
                    "Integrated Security=True";
                SqlDataAdapter daEmp = new SqlDataAdapter("SELECT * FROM 產品", cn);
                daEmp.Fill(ds, "產品");
                dataGridView1.DataSource = ds.Tables["產品"];
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            // 將ds物件的所有產品資料寫入product.xml檔
            ds.WriteXml("product.xml"); 
            MessageBox.Show("產品資料成功寫入product.xml檔內");
        }
    }
}
