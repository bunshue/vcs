using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.IO;

namespace CollectionEnginery
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "CollectionEnginery_Data.MDF";
            // 查詢字串
            string sqlstr = "select * from tb_Collection";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            /*
            dataGridView1.Columns[0].HeaderText = "编号";
            dataGridView1.Columns[0].Width = 40;
            dataGridView1.Columns[1].HeaderText = "书名";
            dataGridView1.Columns[1].Width = 140;
            dataGridView1.Columns[2].HeaderText = "条形码";
            dataGridView1.Columns[2].Width = 80;
            dataGridView1.Columns[3].HeaderText = "累加值";
            dataGridView1.Columns[3].Width = 80;
            dataGridView1.Columns[4].HeaderText = "总计";
            dataGridView1.Columns[4].Width = 40;
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string tem_str = "";//记录当前行
            string tem_code = "";//条形码号
            string tem_mark = "";//个数
            string tem_s = " ";
            StreamReader sr = new StreamReader("../../AddData.dat");//实例化StreamReader，并打开指定的文件
            while (true)//读取dat文件中的所有行
            {
                tem_str = sr.ReadLine();//记录dat文件指定行的数据
                tem_code = tem_str.Substring(0, tem_str.IndexOf(Convert.ToChar(tem_s))).Trim();//获取当前行的条形码
                tem_mark = tem_str.Substring(tem_str.IndexOf(Convert.ToChar(tem_s)), tem_str.Length - tem_str.IndexOf(Convert.ToChar(tem_s)) - 1).Trim();//获取当前条形码的个数
                for (int i = 0; i < dataGridView1.RowCount - 1; i++)//在dataGridView1控件中查找相应的条形码
                {
                    if (dataGridView1.Rows[i].Cells[2].Value.ToString().Trim() == tem_code)//如查找到
                    {
                        dataGridView1.Rows[i].Cells[3].Value = tem_mark.ToString();//显示当前要添加的个数
                        dataGridView1.Rows[i].Cells[4].Value = Convert.ToInt32(dataGridView1.Rows[i].Cells[4].Value) + Convert.ToInt32(tem_mark);//计算当前条形码的总数
                    }
                }
                if (sr.EndOfStream)//如果查询到文件尾
                {
                    break;//退出循环
                }
            }
            sr.Close();//释放所有资源
        }

        // 以下為debug ----------------------------------------------------------------------------------------------------  # 100個

        void sql_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            //讀取資料庫至DGV
            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                    DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                    da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                    //da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
                    dgv.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
                    //dgv.DataSource = ds.Tables[0];  // DGV設置數據源, same

                    /*
                    //也可改成用 DataTable
                    DataTable dt = new DataTable();//创建数据表
                    da.Fill(dt);//填充数据表
                    dgv.DataSource = dt;
                    */
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        // 以下為debug ----------------------------------------------------------------------------------------------------  # 100個

        private void button2_Click(object sender, EventArgs e)
        {
            //ok
        }
    }
}
