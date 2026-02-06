using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;  // 引用此命名空間

namespace ConnectionDemo1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        SqlConnection cn = new SqlConnection();  // SqlConnection物件cn

        // 定義ShowConnection方法用來在txtShow上顯示資料來源的相關資訊
        private void ShowConnection()
        {
            txtShow.Text = "連接字串：" + cn.ConnectionString + Environment.NewLine;
            txtShow.Text += "逾時秒數：" + cn.ConnectionTimeout + Environment.NewLine;
            txtShow.Text += "　資料庫：" + cn.Database + Environment.NewLine;
            txtShow.Text += "資料來源：" + cn.DataSource + Environment.NewLine;
        }
        // 表單載入時執行此事件
        private void Form1_Load(object sender, EventArgs e)
        {
            // 設定連接字串，用來連接Northwind.mdf資料庫
            cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|Northwind.mdf;Integrated Security=True";
            ShowConnection();  // 呼叫ShowConnection方法
        }
        // 按下開啟鈕執行此事件
        private void btnCnState_Click(object sender, EventArgs e)
        {
            // 判斷目前是否為資料庫關閉連接狀態
            if (cn.State == ConnectionState.Closed) 
            {
                cn.Open();
                btnCnState.Text = "關閉";
                txtShow.Text += "目前狀態：資料庫已連接" + Environment.NewLine;
            }
                // 判斷目前是否為資料庫開啟連接狀態
            else if (cn.State == ConnectionState.Open) 
            {
                cn.Close();
                btnCnState.Text = "開啟";
                txtShow.Text += "目前狀態：資料庫已關閉" + Environment.NewLine;
            }
            ShowConnection();
        }
    }
}
