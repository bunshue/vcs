using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace UseInsertSelect
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Student_Copy";
            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void btn_Insert_Click(object sender, EventArgs e)
        {
            InsertData();//插入多条数据记录

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Student_Copy";
            sql_read_database(db_filename, sqlstr, dataGridView2);
        }

        /// <summary>
        /// 查询数据库信息
        /// </summary>
        /// <returns>方法返回DataTable对象</returns>
        private void InsertData()
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            string P_Str_ConnectionStr = cnstr;
            // 查詢字串
            //string sqlstr = "SELECT * FROM tb_Student_Copy";
            string sqlstr = string.Format(
                @"INSERT INTO tb_Student_Copy(学生姓名,学生年龄,性别,家庭住址)
SELECT 学生姓名,年龄,性别,家庭住址 FROM tb_Student");
            //创建SQL连接对象
            SqlConnection P_con = new SqlConnection(P_Str_ConnectionStr);
            try
            {
                P_con.Open();//打开数据库连接
                //创建命令对象
                SqlCommand P_cmd = new SqlCommand(sqlstr, P_con);
                if (P_cmd.ExecuteNonQuery() != 0)//写入数据并判断是否成功
                {
                    MessageBox.Show("成功写入数据", "提示！");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "提示！");
            }
            finally
            {
                P_con.Close();//关闭数据库连接
            }
        }

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
    }
}
