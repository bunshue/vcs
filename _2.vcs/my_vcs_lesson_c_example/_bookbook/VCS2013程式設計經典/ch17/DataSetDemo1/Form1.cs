using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;   // DataSet置於此命名空間下
using System.Data.SqlClient;

namespace DataSetDemo1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 建立ds為DataSet類別物件
        DataSet ds = new DataSet();
        // 表單載入時執行此事件
        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|Northwind.mdf;" +
                    "Integrated Security=True";
                // 建立三個DataAdapter物件，用來取得員工, 客戶, 產品類別資料表
                // 再將三個資料表放入ds(DataSet)物件中
                SqlDataAdapter daEmp = new SqlDataAdapter("SELECT * FROM 員工", cn);
                daEmp.Fill(ds, "員工");
                SqlDataAdapter daCust = new SqlDataAdapter("SELECT * FROM 客戶", cn);
                daCust.Fill(ds, "客戶");
                SqlDataAdapter daCategory = new SqlDataAdapter("SELECT * FROM 產品類別", cn);
                daCategory.Fill(ds, "產品類別");
                // 將ds物件內三個DataTable名稱放入cboTable下拉式清單內
                for (int i = 0; i < ds.Tables.Count; i++) 
                {
                    cboTable.Items.Add(ds.Tables[i].TableName);
                }
                // cboTable下拉式清單顯示 "員工"
                cboTable.Text = ds.Tables["員工"].TableName;
                // dataGridView1顯示員工資料表所有記錄
                dataGridView1.DataSource = ds.Tables["員工"]; 
            }
        }
        // 按下 [查詢] 鈕執行此事件 
        private void btnSelect_Click(object sender, EventArgs e)
        {
            dataGridView1.DataSource = ds.Tables[cboTable.Text];
        }
    }
}
