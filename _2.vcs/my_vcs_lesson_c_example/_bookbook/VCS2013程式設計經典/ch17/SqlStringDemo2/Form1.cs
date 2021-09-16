using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace SqlStringDemo2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            // 使用using敘述建立SqlConnection物件cn
            using (SqlConnection cn = new SqlConnection())
            {
                // 連接字串指定連接ch16DB.mdf資料庫
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch17DB.mdf;" +
                    "Integrated Security=True";
                cn.Open();  // 連接資料庫
                // 將輸入的姓名指定給searchName字串變數
                string searchName = txtName.Text;
                // SELECT敘述的查詢條件為姓名等於searchName
                string selectCmd = "SELECT * FROM 成績單 WHERE 姓名 = '" + searchName.Replace("'", "''") + "'";
                // 建立SqlCommand物件cmd
                SqlCommand cmd = new SqlCommand(selectCmd, cn);
                // 傳回查詢結果的SqlDataRadedr物件dr
                SqlDataReader dr = cmd.ExecuteReader();
                if (dr.Read())   // 若有該筆記錄則執行下面敘述
                {
                    txtShow.Text = "學號：" + dr["學號"].ToString() + Environment.NewLine;
                    txtShow.Text += "姓名：" + dr["姓名"].ToString() + Environment.NewLine;
                    txtShow.Text += "國文：" + dr["國文"].ToString() + Environment.NewLine;
                    txtShow.Text += "英文：" + dr["英文"].ToString() + Environment.NewLine;
                    txtShow.Text += "數學：" + dr["數學"].ToString();
                }
                else   // 若沒有該筆記錄則執行else下面敘述
                {
                    txtShow.Text = "找不到這個學生的成績！";
                }
            }
        }
    }
}
