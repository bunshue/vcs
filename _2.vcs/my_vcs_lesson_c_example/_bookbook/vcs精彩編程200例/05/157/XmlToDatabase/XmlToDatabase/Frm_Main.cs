using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;
using System.Xml.Linq;
using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter

namespace XmlToDatabase
{
    public partial class Frm_Main : Form
    {
        // 將 XML 的資料 儲存到 db_tomeTwo.mdf 的 tb_XML 表單

        static string strPath = "../../Employee.xml";  // 记录XML文件路径

        // 連接字串
        string strCon = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

        linqtosqlDataContext linq;  // 创建Linq连接对象

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            getXmlInfo();
        }

        // 将XML文件内容绑定到DataGridView控件
        private void getXmlInfo()
        {
            DataSet myds = new DataSet();//创建DataSet数据集对象
            myds.ReadXml(strPath);//读取XML结构
            dataGridView1.DataSource = myds.Tables[0];//在DataGridView中显示XML文件中的信息
        }

        //将数据更新到数据库
        private void btn_Edit_Click(object sender, EventArgs e)
        {
            int R = dataGridView1.Rows.Count;
            richTextBox1.Text += "R = " + R.ToString() + "\n";
            for (int i = 0; i < R - 1; i++)//遍历所有行
            {
                richTextBox1.Text += "ID : " + dataGridView1.Rows[i].Cells[3].Value.ToString() + "\n";
                richTextBox1.Text += "Name : " + dataGridView1.Rows[i].Cells[0].Value.ToString() + "\n";
                richTextBox1.Text += "Sex : " + dataGridView1.Rows[i].Cells[1].Value.ToString() + "\n";
                richTextBox1.Text += "Salary : " + Convert.ToInt32(dataGridView1.Rows[i].Cells[2].Value) + "\n";

                linq = new linqtosqlDataContext(strCon);//创建linq连接对象
                tb_XML xml = new tb_XML();//创建tb_XML对象
                xml.ID = dataGridView1.Rows[i].Cells[3].Value.ToString();//为ID赋值
                xml.Name = dataGridView1.Rows[i].Cells[0].Value.ToString();//为Name赋值
                xml.Sex = dataGridView1.Rows[i].Cells[1].Value.ToString();//为Sex赋值
                xml.Salary = Convert.ToInt32(dataGridView1.Rows[i].Cells[2].Value);//为Salary赋值
                linq.tb_XML.InsertOnSubmit(xml);//提交数据
                linq.SubmitChanges();//执行对数据库的修改
                linq.Dispose();//释放linq对象
            }
            MessageBox.Show("成功将XML中的数据更新到了数据库中！");//弹出提示
        }

        //--------------------------------------------------------------------------------------------------------------

        private void button1_Click(object sender, EventArgs e)
        {
            //getXmlInfo();

            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_XML";

            sql_read_database(db_filename, sqlstr, dataGridView2);
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
