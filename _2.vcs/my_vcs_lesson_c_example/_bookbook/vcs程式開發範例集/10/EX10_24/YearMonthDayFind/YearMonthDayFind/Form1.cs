using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace YearMonthDayFind
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ShowDate("select 書號,書名,銷售數量,日期 from tb_xsb", dataGridView1);
        }

        public void ShowDate(string SQL, DataGridView DataGridV)
        {
            string db_filename = "db_10_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            SqlConnection cn = new SqlConnection(cnstr);//連接數據庫
            SqlDataAdapter dap = new SqlDataAdapter(SQL, cn);//SQL語句與數據庫建立連接
            DataSet ds = new DataSet();//實例化DataSet類
            dap.Fill(ds);//更新行
            DataGridV.DataSource = ds.Tables[0].DefaultView;//顯示結果
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string DataSQL = "select 書號,書名,銷售數量,日期 from tb_xsb";//設定SQL語句

            if (textBox1.Text.Length > 0)//如果年份有值
            {
                DataSQL = DataSQL + " where year(日期)='" + textBox1.Text + "'";//新增年的條件
            }

            if (textBox2.Text.Length > 0)//如果月份有值
            {
                DataSQL = DataSQL + " and month(日期)='" + textBox2.Text + "'";//新增月的條件
            }

            if (textBox3.Text.Length > 0)//如果日有值
            {
                DataSQL = DataSQL + " and day(日期)='" + textBox3.Text + "'";//新增日的條件
            }

            ShowDate(DataSQL, dataGridView1);//呼叫自定義方漢
        }
    }
}

