using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;//引用與數據庫操作有關的命名空間

namespace CarryOutMultiFacility
{
    public partial class CarryOutMultiFacility : Form
    {
        static string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";
        SqlConnection cn = new SqlConnection(cnstr);//初始化一個數據庫連接對像
        SqlDataAdapter da;//宣告一個數據讀取器
        DataSet ds = new DataSet();//初始化一個數據集

        public CarryOutMultiFacility()
        {
            InitializeComponent();
        }

        private void CarryOutMultiFacility_Load(object sender, EventArgs e)
        {

        }

        private void print_Click(object sender, EventArgs e)
        {
            excision.Enabled = true;//設定「刪除」按鈕為可用狀態
            try
            {
                if (cn.State == ConnectionState.Closed)//當數據庫連接處於關閉狀態時
                {
                    cn.Open();//打開數據庫連接
                }
                ds.Clear();//清空數據集中原有內容
                string selectString = "select 產品編號,產品名稱,產品說明 from tb_WidgetApply";//定義SQL查詢語句
                da = new SqlDataAdapter(selectString, cn);//初始化數據讀取器
                da.Fill(ds, "WidgetApply");//向數據集中填充數據
                DataTable dt = ds.Tables["WidgetApply"];//初始化一個數據表
                dataGridView1.DataSource = dt.DefaultView;//設定DataGridView控制元件的數據源
            }
            catch (SqlException ex)//擷取異常
            {
                MessageBox.Show(ex.Message);//彈出異常訊息提示
            }
            finally
            {
                cn.Close();//關閉數據庫連接
            }
        }

        private void excision_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < dataGridView1.Rows.Count; i++)//循環搜尋DataGridView控制元件中的每一行
            {
                try
                {
                    if (dataGridView1.Rows[i].Cells[0].Value != null)//當目前單元格的內容不為空時
                    {
                        if (bool.Parse(dataGridView1.Rows[i].Cells[0].Value.ToString()) == true)//當該行處於選定狀態時
                        {
                            dataGridView1.Rows.RemoveAt(i);//刪除處於選定狀態的記錄
                            ExcisionData(i + 1);//執行刪除操作
                            i--;//不改變循環變數i的值
                        }
                    }
                }
                catch (Exception ex)//擷取異常
                {
                    MessageBox.Show(ex.Message);//彈出吟唱提示訊息
                }
            }
        }

        private void ExcisionData(int id)
        {
            cn.Open();//打開數據庫連接
            string DeleteString = "delete tb_WidgetApply where 產品編號=" + id.ToString();//初始化刪除數據的字段
            SqlCommand DeleteCommand = new SqlCommand(DeleteString, cn);//初始化執行SQL語句的對象
            DeleteCommand.ExecuteNonQuery();//執行SQL語句
            cn.Close();//關閉數據庫連接
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }


        //以下為debug ----------------------------------------------------------------------------------------------------  # 100個

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

        //以下為debug ----------------------------------------------------------------------------------------------------  # 100個

        private void button1_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM ddddd";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
