using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.OleDb;    //讀取Access需使用OLEDB

namespace vcs_OleDb2
{
    public partial class Form1 : Form
    {
        //string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";
        OleDbConnection cn;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "顯示 科系代碼資料表, 由系碼排序\n";
            Show_Record1();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "顯示 課程管理表, 由課號排序\n";
            Show_Record2();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "顯示 學生管理表, 由學號排序\n";
            Show_Record3();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "顯示 學生資料表\n";
            Show_Record4();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "取得 科系代碼資料表\n";
            Show_Dept_No();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "取得 課程資料表\n";
            Show_Subject();
            richTextBox1.Text += "------------------------------\n";  // 30個
            richTextBox1.Text += "取得 學生資料表\n";
            Display_Student();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            int dd = 26;
            dataGridView1.Size = new Size(510, 380);
            dataGridView2.Size = new Size(510, 380);
            dataGridView3.Size = new Size(420, 380);
            dataGridView4.Size = new Size(420, 380);

            lb_dgv1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            lb_dgv3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            dataGridView3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + dd);
            lb_dgv4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6);
            dataGridView4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6 + dd);
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";

            richTextBox1.Size = new Size(300, 820);
            richTextBox1.Location = new Point(x_st + dx * 7 + 110, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1920, 890);
            this.Text = "vcs_OleDb2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            dataGridView1.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView3.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView4.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            lb_dgv3.Text = "";
            lb_dgv4.Text = "";
        }

        OleDbConnectionStringBuilder get_builder(string db_filename)
        {
            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";
            return builder;
        }

        //讀取資料庫至DGV
        void oledb_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
            {
                OleDbCommand cmd = new OleDbCommand(builder.ConnectionString);
                cn.Open();  // 打開資料庫連線

                // 建構DataSet及其組成分子
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                OleDbDataAdapter da = new OleDbDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                // da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                //dgv.DataSource = ds.Tables["table"];  // DGV設置數據源, same
                dgv.DataSource = ds.Tables[0];  // DGV設置數據源
            }

            if (dgv == dataGridView1)
            {
                lb_dgv1.Text = "";
                lb_dgv2.Text = "";
                lb_dgv3.Text = "";
                lb_dgv4.Text = "";
            }
            else if (dgv == dataGridView2)
                lb_dgv2.Text = "";
            else if (dgv == dataGridView3)
                lb_dgv3.Text = "";
            else if (dgv == dataGridView4)
                lb_dgv4.Text = "";
        }

        // 執行SQL命令
        void oledb_write_database(string db_filename, string sqlstr)
        {
            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            //對資料庫操作 增茶改山
            try
            {
                using (OleDbConnection cn = new OleDbConnection(builder.ConnectionString))  // 建立資料庫連接對象cn
                {
                    cn.Open();  // 打開資料庫連線

                    OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
                    cmd.ExecuteNonQuery();
                    cn.Close();
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        void Show_Record1()
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            // 查詢字串, 顯示 科系代碼表, 由系碼排序
            string sqlstr = "SELECT * FROM 科系代碼資料表 ORDER BY 系碼 ASC";
            oledb_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "科系代碼資料表, 由系碼排序";
        }

        void Show_Record2()
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            // 查詢字串, 顯示 課程管理表, 由課號排序
            string sqlstr = "SELECT * FROM 課程資料表 ORDER BY 課號 ASC";
            oledb_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "課程管理表, 由課號排序";
        }

        void Show_Record3()
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            // 查詢字串, 顯示 學生管理表, 由學號排序
            string sqlstr = "SELECT 學號,姓名,系名 FROM 學生資料表,科系代碼資料表 WHERE 學生資料表.系碼=科系代碼資料表.系碼 ORDER BY 學號";
            oledb_read_database(db_filename, sqlstr, dataGridView3);
            lb_dgv3.Text = "學生管理表, 由學號排序";
        }

        void Show_Record4()
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            // 查詢字串, 顯示 學生資料表
            string sqlstr = "SELECT * FROM 學生資料表";
            oledb_read_database(db_filename, sqlstr, dataGridView4);
            lb_dgv4.Text = "學生資料表";
        }

        void Show_Dept_No()
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            // 查詢字串, 全部資料 科系代碼資料表
            string sqlstr = "SELECT Distinct * FROM 科系代碼資料表";

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                richTextBox1.Text += dr["系碼"] + "/" + dr["系名"] + "/" + dr["系主任"] + "\n";
            }
            cn.Close();
        }

        void Show_Subject()
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            // 查詢字串
            string sqlstr = "SELECT * FROM 課程資料表";

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                richTextBox1.Text += dr["課號"] + "/" + dr["課名"] + "/" + dr["學分數"] + "/" + dr["必選修"] + "\n";
            }
            cn.Close();
        }

        void Display_Student()
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            // 查詢字串
            string sqlstr = "SELECT * FROM 學生資料表";

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                richTextBox1.Text += dr["學號"] + "/" + dr["姓名"] + "/" + dr["系碼"] + "\n";
            }
            cn.Close();
        }

        //一、設定系碼[查詢功能]
        private void button1_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string ID = "D002";
            // 查詢字串
            string sqlstr = "SELECT * FROM 科系代碼資料表 WHERE 系碼='" + ID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                richTextBox1.Text += "系碼 : " + dr["系碼"].ToString() + "\n";
                richTextBox1.Text += "系名 : " + dr["系名"].ToString() + "\n";
                richTextBox1.Text += "系主任 : " + dr["系主任"].ToString() + "\n";
            }
            cn.Close();
        }

        //一、設定系碼[新增功能]
        private void button2_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string ID = "D007";  // 系碼
            string DNAME = "化學系";  // 系名
            string DTEACHER = "Peter";  // 系主任
            // 查詢字串
            string sqlstr = "INSERT INTO 科系代碼資料表(系碼,系名,系主任) Values('" + ID + "','" + DNAME + "','" + DTEACHER + "')";

            oledb_write_database(db_filename, sqlstr);

            richTextBox1.Text += "顯示 科系代碼資料表, 由系碼排序\n";
            Show_Record1();
        }

        //一、設定系碼[修改功能]
        private void button3_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string ID = "D007";
            string DNAME = "物理系";  // 系名
            string DTEACHER = "David";  // 系主任
            // 查詢字串
            string sqlstr = "UPDATE 科系代碼資料表 SET 系碼='" + ID + "',系名='" + DNAME + "' ,系主任='" + DTEACHER + "' WHERE 系碼='" + ID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "修改成功！\n";

            richTextBox1.Text += "顯示 科系代碼資料表, 由系碼排序\n";
            Show_Record1();
        }

        //一、設定系碼[刪除功能]
        private void button4_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string ID = "D007";
            // 查詢字串
            string sqlstr = "Delete From 科系代碼資料表 WHERE 系碼='" + ID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "刪除成功！\n";

            richTextBox1.Text += "顯示 科系代碼資料表, 由系碼排序\n";
            Show_Record1();
        }

        //二、課程管理[查詢功能]
        private void button5_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string CourseID = "C005";  // 課號
            // 查詢字串
            string sqlstr = "SELECT * FROM 課程資料表 WHERE 課號='" + CourseID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                richTextBox1.Text += "課號 : " + dr["課號"].ToString() + "\n";
                richTextBox1.Text += "課名 : " + dr["課名"].ToString() + "\n";
                richTextBox1.Text += "學分數 : " + dr["學分數"].ToString() + "\n";
                richTextBox1.Text += "必選修 : " + dr["必選修"].ToString() + "\n";
            }
            cn.Close();
        }

        //二、課程管理[新增功能]    
        private void button6_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string CourseID = "C006";  // 課號
            string CourseName = "離散數學";  // 課名
            string CourseCredit = "3";  // 學分數
            string sp = "選";  // 必選修
            // 查詢字串
            string sqlstr = "INSERT INTO 課程資料表(課號,課名,學分數,必選修) Values('" + CourseID + "','" + CourseName + "','" + CourseCredit + "','" + sp + "')";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "新增成功！\n";

            richTextBox1.Text += "顯示 課程管理表, 由課號排序\n";
            Show_Record2();
        }

        //二、課程管理[修改功能]
        private void button7_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string CourseID = "C006";  // 課號
            string CourseName = "機率";  // 課名
            string CourseCredit = "4";  // 學分數
            string sp = "必";  // 必選修
            // 查詢字串
            string sqlstr = "UPDATE 課程資料表 SET 課號='" + CourseID + "',課名='" + CourseName + "' ,學分數='" + CourseCredit + "', 必選修='" + sp + "' WHERE 課號='" + CourseID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "新增成功！\n";

            richTextBox1.Text += "顯示 課程管理表, 由課號排序\n";
            Show_Record2();
        }

        //二、課程管理[刪除功能]
        private void button8_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string CourseID = "C006";  // 課號
            // 查詢字串
            string sqlstr = "Delete From 課程資料表 WHERE 課號='" + CourseID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "刪除成功！\n";

            richTextBox1.Text += "顯示 課程管理表, 由課號排序\n";
            Show_Record2();
        }

        //三、學生管理[查詢功能]
        private void button9_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string ID = "96003";  // 學號
            // 查詢字串
            string sqlstr = "SELECT * FROM 學生資料表 WHERE 學號='" + ID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                richTextBox1.Text += "學號 : " + dr["學號"].ToString() + "\n";
                richTextBox1.Text += "姓名 : " + dr["姓名"].ToString() + "\n";
                richTextBox1.Text += "系碼 : " + dr["系碼"].ToString() + "\n";
            }
            cn.Close();

            //3030

            // 資料庫檔案
            db_filename = "DBMS1.mdb";

            ID = "96003";  // 學號
            // 查詢字串
            sqlstr = "SELECT 科系代碼資料表.系碼,系名 FROM 科系代碼資料表,學生資料表 WHERE 科系代碼資料表.系碼=學生資料表.系碼 AND 學號='" + ID + "'";

            builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            cmd = new OleDbCommand(sqlstr, cn);
            dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                richTextBox1.Text += dr["系碼"] + "/" + dr["系名"] + "\n";
            }
            cn.Close();
        }

        //三、學生管理[新增功能]
        private void button10_Click(object sender, EventArgs e)
        {
            Show_Record4();

            //科系代碼資料表

            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string ID = "96006";  // 學號
            string NAME = "劉備";  // 姓名
            string DID = "D008";  // 系碼
            // 查詢字串
            string sqlstr = "INSERT INTO 學生資料表(學號,姓名,系碼) Values('" + ID + "','" + NAME + "','" + DID + "')";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "新增成功！\n";

            richTextBox1.Text += "顯示 學生管理表, 由學號排序\n";
            Show_Record3();
        }

        //三、學生管理[修改功能]
        private void button11_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string ID = "96005";  // 學號
            string NAME = "李白";  // 姓名
            string DID = "D008";  // 系碼
            // 查詢字串
            string sqlstr = "UPDATE 學生資料表 SET 學號='" + ID + "',姓名='" + NAME + "' ,系碼='" + DID + "' WHERE 學號='" + ID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "修改成功！\n";

            richTextBox1.Text += "顯示 學生管理表, 由學號排序\n";
            Show_Record3();
        }

        //三、學生管理[刪除功能]
        private void button12_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            string ID = "96005";  // 學號
            // 查詢字串
            string sqlstr = "Delete From 學生資料表 WHERE 學號='" + ID + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "刪除成功！\n";

            richTextBox1.Text += "顯示 學生管理表, 由學號排序\n";
            Show_Record4();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            string CourseCredit = "3";  // 學分數
            // 查詢字串
            string sqlstr = "SELECT 學生資料表.學號,姓名,課名,學分數 FROM 科系代碼資料表,學生資料表,選課資料表,課程資料表 WHERE 學生資料表.系碼=科系代碼資料表.系碼 AND 學生資料表.學號=選課資料表.學號 AND 選課資料表.課號=課程資料表.課號 AND 選課資料表.學號='" + CourseCredit + "'";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            OleDbDataAdapter da;
            DataSet ds;
            da = new OleDbDataAdapter(sqlstr, cn);
            ds = new DataSet();
            //讀取資料表
            da.Fill(ds, "學生資料表");
            dataGridView4.DataSource = ds.Tables["學生資料表"];
            //dataGridView4.DataBind();
            cn.Close();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";
            string Str1 = "aaaa";  // 學號
            string Str2 = "bbbb";  // 課號
            // 查詢字串
            string sqlstr = "INSERT INTO 選課資料表(學號,課號) Values('" + Str1 + "','" + Str2 + "')";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);

            OleDbConnection cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線
            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            cmd.ExecuteNonQuery();
            cn.Close();

            richTextBox1.Text += "加選成功！\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "DBMS1.mdb";

            string Stu_ID = "96001";
            // 查詢字串
            string sqlstr = "SELECT * FROM 學生資料表 WHERE 學號='" + Stu_ID + "' ";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);
            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn
            cn.Open();  // 打開資料庫連線

            // =====顯示學生之學號與姓名清單==========


            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            //顯示資料表欄位的所有資料
            if (dr.Read())
            {
                richTextBox1.Text += "學號 : " + dr["學號"] + "\t姓名 : " + dr["姓名"] + "\n";
            }
            else
            {
                richTextBox1.Text += "您不是學員！\n";
            }
            cn.Close();
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //OleDB 20

            // 資料庫檔案
            string db_filename = "Northwind.mdb";

            // 查詢字串
            string sqlstr = "SELECT * FROM 員工";
            oledb_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            db_filename = "Northwind.mdb";

            OleDbConnectionStringBuilder builder = new OleDbConnectionStringBuilder();
            builder["Provider"] = "Microsoft.Jet.OLEDB.4.0";
            builder["Data Source"] = "D:\\" + db_filename;
            builder["User Id"] = "Admin";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //OleDB 21

            // 資料庫檔案
            string db_filename = "DBMS.mdb";
            // 查詢字串
            string sqlstr = "SELECT * FROM 學生資料表";

            oledb_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //string dbpath = "C:\\Inetpub\\wwwroot\\CS\\ch08\\App_Data\\DBMS.mdb";

            // 資料庫檔案
            db_filename = "DBMS.mdb";
            // 查詢字串
            sqlstr = "SELECT * FROM 學生資料表";

            OleDbConnectionStringBuilder builder = get_builder(db_filename);

            OleDbConnection cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn

            cn.Open();  // 打開資料庫連線

            OleDbCommand cmd = new OleDbCommand(sqlstr, cn);
            OleDbDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器

            //顯示資料表欄位名稱
            for (int i = 0; i <= dr.FieldCount - 1; i++)
            {
                richTextBox1.Text += dr.GetName(i) + "\n";
            }

            //顯示資料表欄位的所有資料
            while (dr.Read())
            {
                for (int i = 0; i <= dr.FieldCount - 1; i++)
                {
                    richTextBox1.Text += dr.GetValue(i) + "\n";
                }
            }
            cn.Close();

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 資料庫檔案
            db_filename = "DBMS.mdb";
            builder = get_builder(db_filename);

            //string dbpath = "C:\\Inetpub\\wwwroot\\ASPNET\\ch14\\App_Data\\DBMS.mdb";

            cn = new OleDbConnection(builder.ConnectionString);  // 建立資料庫連接對象cn

            cn.Open();  // 打開資料庫連線

            // 查詢字串
            sqlstr = "SELECT * FROM 學生資料表";

            OleDbDataAdapter da;
            DataSet ds;
            da = new OleDbDataAdapter(sqlstr, cn);
            ds = new DataSet();
            //讀取資料表
            da.Fill(ds, "Table");
            dataGridView2.DataSource = ds.Tables["Table"];
            cn.Close();
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */

