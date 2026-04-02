using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace UseUpdate
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private DataSet G_st = new DataSet();//声明表字段

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            G_st.Tables.Add(new DataTable());
            GetMessage();//填充表
            dgv_Message.DataSource = G_st.Tables[0];//设置数据源
            dgv_Message.Columns[0].Visible = false;//隐藏主键列

            /*
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
        }

        private void btn_Submit_Click(object sender, EventArgs e)
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            SqlDataAdapter P_SqlDataAdapter = new SqlDataAdapter();//创建数据适配器

            //创建命令对象
            SqlCommand P_cmd = new SqlCommand(
                @"UPDATE tb_Student_Copy SET 学生姓名=@name,学生年龄=@age,性别=@sex,家庭住址=@address
WHERE id=@id",
                new SqlConnection(cnstr));
            P_cmd.Parameters.Add("@id", SqlDbType.Int, 10, "id");//设置参数
            P_cmd.Parameters.Add("@name", SqlDbType.VarChar, 10, "学生姓名");//设置参数
            P_cmd.Parameters.Add("@age", SqlDbType.Int, 10, "学生年龄");//设置参数
            P_cmd.Parameters.Add("@sex", SqlDbType.NChar, 2, "性别");//设置参数
            P_cmd.Parameters.Add("address", SqlDbType.VarChar, 50, "家庭住址");//设置参数
            P_SqlDataAdapter.UpdateCommand = P_cmd;//设置UpdateCommand属性
            P_SqlDataAdapter.Update(G_st.Tables[0]);//更新数据库中数据
            G_st.AcceptChanges();//提交修改
            MessageBox.Show("更改成功！", "提示！");//弹出消息对话框
            GetMessage();//填充表
            dgv_Message.DataSource = G_st.Tables[0];//设置数据源
            dgv_Message.Columns[0].Visible = false;//隐藏主键列
        }

        /// <summary>
        /// 查询数据库信息
        /// </summary>v
        /// <returns>方法返回DataTable对象</returns>
        private void GetMessage()
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            // 連接字串
            string P_Str_ConnectionStr = cnstr;
            // 查詢字串
            string P_Str_SqlStr = string.Format("SELECT * FROM tb_Student_Copy");
            //创建数据适配器
            SqlDataAdapter P_SqlDataAdapter = new SqlDataAdapter(P_Str_SqlStr, P_Str_ConnectionStr);
            P_SqlDataAdapter.Fill(G_st.Tables[0]);//填充数据表
        }

        private void dgv_Message_CellEndEdit(object sender, DataGridViewCellEventArgs e)
        {
            //同步DataGridView控件中的数据
            G_st.Tables[0].Rows[e.RowIndex][e.ColumnIndex] = dgv_Message.Rows[e.RowIndex].Cells[e.ColumnIndex].Value;
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
