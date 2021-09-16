using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;    // DataSet置於此命名空間下
using System.Data.SqlClient;

namespace DataTableDemo1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 使用using敘述建立SqlConnection物件
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接ch16DB.mdf資料庫
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch17DB.mdf;" +
                    "Integrated Security=True";
                DataSet ds = new DataSet();  // 建立DataSet物件ds
                // 建立SqlDataAdapter物件daScore並取出成績單資料表
                SqlDataAdapter daScore = new SqlDataAdapter("SELECT * FROM 成績單", cn);
                // 將成績單資料表所有記錄填入ds物件
                daScore.Fill(ds, "成績單");
                // 宣告DataTable物件dt，該dt內存放ds中的成績單DataTable
                DataTable dt = ds.Tables["成績單"];
                // 在textBox1內顯示成績單的所有欄位名稱
                for (int i = 0; i < dt.Columns.Count; i++)
                {
                    textBox1.Text += dt.Columns[i].ColumnName + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                // 在textBox1內顯示成績單的所有記錄
                for (int i = 0; i < dt.Rows.Count; i++)
                {
                    for (int j = 0; j < dt.Columns.Count; j++)
                    {
                        textBox1.Text += dt.Rows[i][j].ToString() +"\t";
                    }
                    textBox1.Text += Environment.NewLine;
                }
            }
        }
    }
}
