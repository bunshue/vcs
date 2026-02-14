using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;//引用與數據庫操作有關的命名空間

// 無資料庫 pubs

namespace IllegalAutoRank
{
    public partial class IllegalAutoRank : Form
    {
        public IllegalAutoRank()
        {
            InitializeComponent();
        }

        private void IllegalAutoRank_Load(object sender, EventArgs e)
        {
            string ConnectString = "server=.;database=pubs;integrated security=sspi";//初始化數據庫連接字串
            SqlConnection IllegalRankConn = new SqlConnection(ConnectString);//初始化數據庫連接對像
            string SelectString = "select au_id as 使用者編號,au_lname as 姓名,phone as 電話號碼 from authors";//初始化SQL查詢語句
            SqlDataAdapter IllegalRankAdapter = new SqlDataAdapter(SelectString, IllegalRankConn);//初始化一個數據讀取器
            DataSet IllegalRankSet = new DataSet();//初始化一個數據集
            IllegalRankAdapter.Fill(IllegalRankSet, "authors");//向數據集中填充內容
            dataGridView1.DataSource = IllegalRankSet.Tables["authors"].DefaultView;//為DataGridView控制元件填充數據源
            for (int i = 0; i < dataGridView1.Columns.Count; i++)//循環搜尋DataGridView控制元件中的每一列
            {
                dataGridView1.Columns[i].SortMode = DataGridViewColumnSortMode.NotSortable;//設定每一列的排序類型為不排序
            }
        }
    }
}

