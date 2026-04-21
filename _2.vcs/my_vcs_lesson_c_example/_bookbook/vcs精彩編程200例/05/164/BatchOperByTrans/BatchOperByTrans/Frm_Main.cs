using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace BatchOperByTrans
{
    public partial class Frm_Main : Form
    {
        private SqlConnection m_Conn = null;//声明数据库连接对象
        private SqlCommand m_Cmd = null;//声明执行SQL命令对象

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //实例化数据库连接对象
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            m_Conn = new SqlConnection(cnstr);
            m_Cmd = new SqlCommand();//实例化执行SQL命令对象
            BindDataGridView("");//对DataGridView控件进行数据绑定
        }

        private void toolDelete_Click(object sender, EventArgs e)
        {
            string strPRProduceCode = null; //生产单号
            string strSql = null;//要执行的单条SQL语句
            List<string> strSqls = new List<string>();//SQL语句集合
            if (this.dgvPRProduceInfo.RowCount <= 0)//判断数据表格中是否有行
            {
                return;
            }
            strPRProduceCode = this.dgvPRProduceInfo["PRProduceCode", this.dgvPRProduceInfo.CurrentCell.RowIndex].Value.ToString();//获取选中的生产单号
            //删除生产单子表
            strSql = "DELETE FROM PRProduceItem WHERE PRProduceCode = '" + strPRProduceCode + "'";
            strSqls.Add(strSql);//将要执行的SQL语句添加到List泛型集合中
            //删除生产单主表
            strSql = "DELETE FROM PRProduce WHERE PRProduceCode = '" + strPRProduceCode + "'";
            strSqls.Add(strSql);//将要执行的SQL语句添加到List泛型集合中
            if (MessageBox.Show("确定要删除吗？", "软件提示", MessageBoxButtons.YesNo, MessageBoxIcon.Exclamation) == DialogResult.Yes)//弹出删除确认对话框
            {
                try
                {
                    if (ExecDataBySqls(strSqls))//调用自定义方法批量删除数据
                    {
                        MessageBox.Show("删除成功！", "软件提示");
                    }
                    else
                    {
                        MessageBox.Show("删除失败！", "软件提示");
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "软件提示");
                }
                BindDataGridView("");//重新对DataGridView控件进行数据绑定
            }
        }

        /// <summary>
        /// 通过Transact-SQL语句得到DataSet数据集
        /// </summary>
        /// <param name="strSql">Transact-SQL语句</param>
        /// <param name="strTable">相关的数据表</param>
        /// <returns>DataSet数据集</returns>
        public DataSet GetDataSet(string strSql, string strTable)
        {
            DataSet ds = null;//声明数据集对象
            try
            {
                SqlDataAdapter sda = new SqlDataAdapter(strSql, m_Conn);//实例化数据桥接器对象
                ds = new DataSet();//实例化数据集对象
                sda.Fill(ds, strTable);//填充DataSet数据集
            }
            catch (Exception e)
            {
                throw e;
            }
            return ds;//返回得到的DataSet数据集
        }

        /// <summary>
        /// DataGridView控件绑定数据源
        /// </summary>
        /// <param name="strWhere">Where条件子句</param>
        private void BindDataGridView(string strWhere)
        {
            string strSql = null;//定义个字符串变量，用来存储SQL查询语句
            strSql = "SELECT * FROM PRProduce " + strWhere;//组合SQL查询语句
            try
            {
                //设置DataGridView控件的数据源
                dgvPRProduceInfo.DataSource = GetDataSet(strSql, "PRProduce").Tables["PRProduce"];
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "软件提示");
            }
        }

        /// <summary>
        /// 多条Transact-SQL语句提交数据
        /// </summary>
        /// <param name="strSqls">使用List泛型封装多条SQL语句</param>
        /// <returns>bool值(提交是否成功)</returns>
        public bool ExecDataBySqls(List<string> strSqls)
        {
            bool booIsSucceed;//标识是否成功
            if (m_Conn.State == ConnectionState.Closed)//判断数据库连接状态是否关闭
            {
                m_Conn.Open();//打开数据库连接
            }
            SqlTransaction sqlTran = m_Conn.BeginTransaction();//实例化事务对象
            try
            {
                m_Cmd.Connection = m_Conn;//指定SqlCommand对象的连接对象
                m_Cmd.Transaction = sqlTran;//指定SqlCommand对象的事务对象
                foreach (string item in strSqls)//遍历List泛型集合中的所有SQL命令
                {
                    m_Cmd.CommandType = CommandType.Text;//指定SqlCommand对象的执行命令方式
                    m_Cmd.CommandText = item;//指定SqlCommand对象要执行的SQL命令
                    m_Cmd.ExecuteNonQuery();//执行SQL命令
                }
                sqlTran.Commit();//提交数据库
                booIsSucceed = true;//表示提交数据库成功
            }
            catch
            {
                sqlTran.Rollback();//事务回滚
                booIsSucceed = false;//表示提交数据库失败
            }
            finally
            {
                m_Conn.Close();//关闭数据库连接
                strSqls.Clear();//清空List泛型集合
            }
            return booIsSucceed;//返回结果，判断是否执行成功
        }

        private void toolExit_Click(object sender, EventArgs e)
        {
            this.Close();//关闭当前窗体
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

        private void button4_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";

            // 查詢字串
            string sqlstr = "SELECT * FROM PRProduce";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
