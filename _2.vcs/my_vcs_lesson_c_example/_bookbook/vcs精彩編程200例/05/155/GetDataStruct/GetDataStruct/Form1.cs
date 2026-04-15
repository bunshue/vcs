using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;
using System.Data.Sql;

namespace GetDataStruct
{
    public partial class Form1 : Form
    {
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_09_Data.MDF";
        //string filename = @"D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_09_Log.LDF";   another

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.Text = "master";
            comboBox2.SelectedIndex = 0;
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            try
            {
                string strTableName = listBox1.SelectedValue.ToString();
                string strCon = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.MDF;DataBase=" + comboBox1.Text + ";Integrated Security=True;Connect Timeout=30";

                using (SqlConnection con = new SqlConnection(strCon))
                {
                    string strSql = "select  name 字段名, xusertype 类型编号, length 长度 into hy_Linshibiao from  syscolumns  where id=object_id('" + listBox1.Text + "') ";
                    strSql += "select name 类型,xusertype 类型编号 into angel_Linshibiao from systypes where xusertype in (select xusertype from syscolumns where id=object_id('" + listBox1.Text + "'))";
                    con.Open();
                    SqlCommand cmd = new SqlCommand(strSql, con);
                    cmd.ExecuteNonQuery();
                    SqlDataAdapter da = new SqlDataAdapter("select 字段名,类型,长度 from hy_Linshibiao t,angel_Linshibiao b where t.类型编号=b.类型编号", con);
                    DataTable dt = new DataTable();
                    da.Fill(dt);
                    dataGridView1.DataSource = dt.DefaultView;
                    SqlCommand cmdnew = new SqlCommand("drop table hy_Linshibiao,angel_Linshibiao", con);
                    cmdnew.ExecuteNonQuery();
                    con.Close();
                }
            }
            catch { }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndices.Count > 0)
            {
                frmDataExport dataexport = new frmDataExport();
                dataexport.OutData = comboBox1.Text;
                dataexport.OutTable = listBox1.Text;
                //dataexport.strserver = toolStripTextBox1.Text;
                //dataexport.struser = toolStripTextBox2.Text;
                //dataexport.strpwd = toolStripTextBox3.Text;
                dataexport.ShowDialog();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndices.Count > 0)
            {
                frmOutData outdata = new frmOutData();
                outdata.OutData = comboBox1.Text;
                outdata.OutTable = listBox1.Text;
                //outdata.strserver = toolStripTextBox1.Text;
                //outdata.struser = toolStripTextBox2.Text;
                //outdata.strpwd = toolStripTextBox3.Text;
                outdata.ShowDialog();
            }
        }

        private DataTable getTable(string strCon, string strSql, string strTable)
        {
            richTextBox1.Text += "strCon : " + strCon + "\n";
            richTextBox1.Text += "strSql : " + strSql + "\n";
            richTextBox1.Text += "strTable : " + strTable + "\n";

            try
            {
                SqlConnection sqlcon = new SqlConnection(strCon);
                SqlDataAdapter da = new SqlDataAdapter(strSql, sqlcon);
                DataTable dt = new DataTable(strTable);
                da.Fill(dt);
                richTextBox1.Text += "OK dt\n";

                dataGridView2.DataSource = dt;
                dataGridView2.Columns[0].Width = 350;

                return dt;
            }
            catch
            {
                richTextBox1.Text += "NG dt\n";
                return null;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //test

            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";
            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            richTextBox1.Text += "cnstr  : " + cnstr + "\n";

            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_09_Data.MDF;Integrated Security=True;Connect Timeout=30";
            richTextBox1.Text += "cnstr  : " + cnstr + "\n";

            string db = "master";
            string strCon = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.MDF;DataBase=" + db + ";Integrated Security=True;Connect Timeout=30";
            richTextBox1.Text += "strCon : " + strCon + "\n";

            comboBox1.DataSource = getTable(cnstr, "select name from sysdatabases", "sysdatabases");
            comboBox1.DisplayMember = "name";
            comboBox1.ValueMember = "name";

            comboBox1.Enabled = true;
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

        private void button3_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Employee";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

    }
}

/*
    //測試 getTable

    string strCon = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_09_Data.MDF;DataBase=" + comboBox1.Text + ";Integrated Security=True;Connect Timeout=30";

    DataTable dt = null;
    //数据表
    dt = getTable(strCon, "SELECT name FROM sysobjects WHERE type = 'U' and name<>'dtproperties'", "sysobjects");
    //"视图"
    dt = getTable(strCon, "select name from sysobjects where xtype='v'", "sysobjects");
    //"存储过程"
    dt = getTable(strCon, "SELECT name FROM sysobjects WHERE xtype='p'", "sysobjects");
*/

//comboBox1.DataSource = getTable(str, "select name from sysdatabases", "sysdatabases");

