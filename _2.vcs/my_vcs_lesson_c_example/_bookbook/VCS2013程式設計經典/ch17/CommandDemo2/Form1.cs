﻿using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data;
using System.Data.SqlClient;

namespace CommandDemo2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 建立cnstr連接字串用來連接ch17DB.mdf資料庫
        string cnstr = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch17DB.mdf;" +
                    "Integrated Security=True";

        void ShowData()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工 ORDER BY 編號 DESC", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
            }
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            ShowData();
        }
        // 按下 [新增] 鈕執行
        private void btnAdd_Click(object sender, EventArgs e)
        {
            try  //使用try...catch...敘述來補捉異動資料可能發生的例外 
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr ;
                    cn.Open();
                    string sqlStr = "INSERT INTO 員工(姓名, 職稱, 電話, 薪資) VALUES('" + txtName.Text.Replace("'", "''") + "','" + txtPosition.Text.Replace("'", "''") + "','" + txtTel.Text.Replace("'", "''") + "'," + int.Parse(txtSalary.Text) + ")";
                    SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                    Cmd.ExecuteNonQuery();
                }
                ShowData();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + ", 新增資料發生錯誤");
            }
        }
        // 按下 [更新] 鈕執行 
        private void btnUpdate_Click(object sender, EventArgs e)
        {
            try	//使用try...catch...敘述來補捉異動資料可能發生的例外
            {
                using (SqlConnection cn = new SqlConnection())
                {
                    cn.ConnectionString = cnstr ;
                    cn.Open();
                    string sqlStr = "UPDATE 員工 SET 職稱 = '" + txtPosition.Text.Replace("'", "''") + "',電話 = '" + txtTel.Text.Replace("'", "''") + "', 薪資 = " + int.Parse(txtSalary.Text) + " WHERE 姓名 = '" + txtName.Text.Replace("'", "''") + "'";
                    SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                    Cmd.ExecuteNonQuery();
                }
                ShowData();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message + ", 修改資料發生錯誤");
            }
        }
        // 按下 [刪除] 鈕 
        private void btnDel_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnstr;
                cn.Open();
                string sqlStr = "DELETE FROM 員工 WHERE 姓名 = '" + txtName.Text.Replace("'", "''") + "'";
                SqlCommand Cmd = new SqlCommand(sqlStr, cn);
                Cmd.ExecuteNonQuery();
            }
            ShowData();
        }
    }
}
