using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter

namespace vcs_SqlConnection1
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        //建立MyDBClass類別物件db，來管理Database1.mdf資料庫
        MyDBClass db = new MyDBClass();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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
            dataGridView1.Size = new Size(500, 380);
            dataGridView2.Size = new Size(500, 380);
            dataGridView3.Size = new Size(300, 380);
            dataGridView4.Size = new Size(300, 380);

            lb_dgv1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            lb_dgv3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            dataGridView3.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0 + dd);
            lb_dgv4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6);
            dataGridView4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6 + dd);
            lb_dgv1.Text = "dataGridView1";
            lb_dgv2.Text = "dataGridView2";
            lb_dgv3.Text = "dataGridView3";
            lb_dgv4.Text = "dataGridView4";
            dataGridView1.DataSource = null;//設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;//設定DGV的資料來源為無, 即清除
            dataGridView3.DataSource = null;//設定DGV的資料來源為無, 即清除
            dataGridView4.DataSource = null;//設定DGV的資料來源為無, 即清除

            richTextBox1.Size = new Size(400, 820);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1910, 910);
            this.Text = "vcs_SqlConnection1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // 固定查詢
        private void ShowData3(string cnstr)
        {
            // DB => DS => dataGridView1
            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                // 連接資料庫
                cn.ConnectionString = cnstr;

                string sqlstr = "SELECT * FROM 銀行帳戶";  // 宣告查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds, "銀行帳戶");  // 將DataAdapter查詢之後的結果填充至DataSet

                dataGridView1.DataSource = ds.Tables["銀行帳戶"];
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //測試登錄功能

            string id_name = "david";
            string password = "123456";

            string db_filename = "db_TomeTwo.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串

            //SqlConnection cn = new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30");//创建数据库连接对象
            SqlConnection cn = new SqlConnection(cnstr);  // 建立資料庫連接對象cn

            // 建立資料庫適配器對象da
            SqlDataAdapter sqlda = new SqlDataAdapter("SELECT Name,Pwd from tb_Login where Name=@name and Pwd=@pwd", cn);//创建数据库桥接器对象

            //为SQL语句中的参数赋值
            sqlda.SelectCommand.Parameters.Add("@name", SqlDbType.NChar, 10).Value = id_name;
            sqlda.SelectCommand.Parameters.Add("@pwd", SqlDbType.NChar, 10).Value = password;
            DataSet myds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            sqlda.Fill(myds);  // da將查詢的結果填充至數據集ds, 不指定TableName
            if (myds.Tables[0].Rows.Count > 0)//判断数据集中的表中是否有行
            {
                MessageBox.Show("用户登录成功！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("用户登录失败，原因为：用户名或密码错误！", "错误", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 查询销售量占前50%的图书信息
            // 查询数据库信息

            //创建数据库连接字符串
            //string P_Str_ConnectionStr = string.Format(@"server=MR-PC\YL;database=db_TomeTwo;uid=sa;pwd=");
            //String P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            String P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            //创建SQL查询字符串
            string sqlstr = string.Format("SELECT * FROM tb_Book");

            //创建数据适配器
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, P_Str_ConnectionStr);  // 建立資料庫適配器對象da
            //SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);//compare    // 建立資料庫適配器對象da

            //创建数据表
            DataTable dt = new DataTable();

            da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName

            dataGridView1.DataSource = dt;//设置数据源

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 查询销售量占前50%的图书信息
            // 查询数据库信息

            //创建数据库连接字符串
            //string P_Str_ConnectionStr = string.Format(@"server=USER-20170504OU;database=db_TomeTwo;uid=sa;pwd=");
            //String P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";
            P_Str_ConnectionStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            //创建SQL查询字符串
            sqlstr = string.Format(@"SELECT TOP 50 PERCENT 书号,书名,sum(销售数量)as 合计销售数量 FROM tb_Book group by 书号,书名,作者 order by 3 desc");

            //创建数据适配器
            da = new SqlDataAdapter(sqlstr, P_Str_ConnectionStr);  // 建立資料庫適配器對象da
            //SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);//compare    // 建立資料庫適配器對象da

            //创建数据表
            dt = new DataTable();

            da.Fill(dt);  // da將查詢的結果填充至數據集ds, 不指定TableName

            dataGridView1.DataSource = dt;//设置数据源
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //跳过满足指定条件的记录
            //跳过生日小于2009-7-1的员工:

            //string cnstr = "Data Source=USER-20170504OU;Database=db_TomeTwo;UID=sa;Pwd=;";//取连接字符串
            string db_filename = "db_TomeTwo.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                string sql = "SELECT * from EmployeeInfo";//构造sql语句
                SqlCommand cmd = new SqlCommand(sql, cn);//创建Command对象

                SqlDataAdapter da = new SqlDataAdapter(cmd);  // 建立資料庫適配器對象da

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                da.Fill(ds, "EmployeeInfo");//填充数据集

                //跳过生日小于2009-7-1的员工信息
                IEnumerable<DataRow> query = ds.Tables["EmployeeInfo"].AsEnumerable().SkipWhile(itm => itm.Field<DateTime>("Birthday") < Convert.ToDateTime("2009-7-1"));
                dataGridView1.DataSource = query.CopyToDataTable();//设置dataGridView1数据源
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //RelationsDemo
            string db_filename = "Northwind.mdf";
            string cnstr = string.Format(db_cnstr, db_filename);  // 連接字串

            using (SqlConnection cn = new SqlConnection())  // 建立資料庫連接對象cn
            {
                cn.ConnectionString = cnstr;

                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)

                string sqlstr1 = "SELECT * FROM 產品類別";  // 宣告查詢字串
                SqlDataAdapter da1 = new SqlDataAdapter(sqlstr1, cn);  // 建立資料庫適配器對象da
                da1.Fill(ds, "產品類別");

                string sqlstr2 = "SELECT * FROM 產品資料";  // 宣告查詢字串
                SqlDataAdapter da2 = new SqlDataAdapter(sqlstr2, cn);  // 建立資料庫適配器對象da
                da2.Fill(ds, "產品資料");

                ds.Relations.Add("FK_產品資料_產品類別", ds.Tables["產品類別"].Columns["類別編號"], ds.Tables["產品資料"].Columns["類別編號"]);

                dataGridView1.DataSource = ds;
                dataGridView1.DataMember = "產品類別";

                dataGridView2.DataSource = ds;
                dataGridView2.DataMember = "產品類別.FK_產品資料_產品類別";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //兩個表單
            //兩個表單

            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

            //產品類別 => dataGridView1
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT * From 產品類別";  // 查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "產品類別";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品資料 => dataGridView2
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT * From 產品資料";  // 查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView2.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv2.Text = "產品資料";
            }

        }

        void show_product_data(DataGridView dgv, string mesg)
        {
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

            //取得產品類別, 並顯示dataGridView1上
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT * From 產品類別";  // 查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dgv.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = mesg;
            }
        }



        private void button11_Click(object sender, EventArgs e)
        {
            //產品類別管理 產品資料管理 產品關聯查詢

            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";


            //產品類別管理

            show_product_data(dataGridView1, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品資料管理

            //將產品類別顯示在清單中   
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT * From 產品類別";  // 查詢字串
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView2.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv2.Text = "產品類別";
            }

            //查詢 類別編號 = 1 的資料
            int CategoryId1 = 1;
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1;  // 查詢字串
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView3.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv3.Text = "產品資料管理";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //產品關聯查詢

            show_product_data(dataGridView1, "產品類別");

            //查詢 類別編號 = 1 的資料
            //int CategoryId1 = 1;

            //取得目前產品類別dataGridView4所選取記錄的第一欄資料，即類別編號
            //並指定給CategoryId整數變數
            int CategoryId2 = 1;
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            //傳入類別編號CategoryId來取得該類別相對應的產品資料
            //接著將產品資料顯示在dataGridView4上
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2;  // 查詢字串
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView4.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv4.Text = "產品關聯查詢";
            }

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //新增 修改 刪除
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

            richTextBox1.Text += "新增類別名稱\n";

            string new_item = "麥當勞";

            //呼叫Edit()方法並傳入INSERT陳述式新增產品類別記錄
            db.Edit("INSERT INTO 產品類別(類別名稱)VALUES(N'" + new_item + "')");

            show_product_data(dataGridView1, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "修改, 修改 類別編號4 的 產品類別\n";

            int old_id = 4;

            string new_item2 = "肯德雞";

            //呼叫Edit()方法並傳入UPDATE陳述式修改產品類別記錄
            //取得DataGridView目前選取第一欄的資料，也就是類別編號欄位
            db.Edit("UPDATE 產品類別 SET 類別名稱=N'" + new_item2 + "' WHERE 類別編號=" + old_id.ToString());

            show_product_data(dataGridView2, "產品類別");

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "刪除\n";

            int delete_id = 5;

            //呼叫Edit()方法並傳入DELETE陳述式刪除指定的產品類別記錄
            db.Edit("DELETE FROM 產品類別 WHERE 類別編號=" + delete_id.ToString());

            delete_id = 6;
            //刪除與產品類別相關聯的產品資料
            db.Edit("DELETE FROM 產品資料 WHERE 類別編號=" + delete_id.ToString());

            show_product_data(dataGridView3, "產品類別");

        }

        private void button13_Click(object sender, EventArgs e)
        {
            //新增 修改 刪除
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

            richTextBox1.Text += "新增\n";

            string new_item = "必勝客";
            int price = 12345;//單價
            string mesg = "電話訂購";//說明

            db.Edit("INSERT INTO 產品資料(類別編號,品名,單價,說明)VALUES(" +
                "1" + ",N'" +
                new_item + "'," +
                price.ToString() + ",N'" +
                mesg + "')");

            int CategoryId1 = 1;//類別編號
            richTextBox1.Text += "CategoryId1 = " + CategoryId1.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId1;  // 查詢字串
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "新增 產品資料";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "修改\n";

            new_item = "達美樂";
            price = 123;//單價
            mesg = "網路訂購";//說明

            db.Edit("UPDATE 產品資料 SET 品名=N'" +
                new_item + "', 單價=" +
                price.ToString() + ", 說明=N'" +
                mesg + "' WHERE 產品編號=" +
                dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId2 = 1;//類別編號
            richTextBox1.Text += "CategoryId2 = " + CategoryId2.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId2;  // 查詢字串
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "修改 產品資料";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "刪除\n";

            db.Edit("DELETE FROM 產品資料 WHERE 產品編號=" + dataGridView1.CurrentRow.Cells[0].Value.ToString());

            int CategoryId3 = 1;//類別編號
            richTextBox1.Text += "CategoryId3 = " + CategoryId3.ToString() + "\n";
            using (SqlConnection cn = new SqlConnection(db_cnstr))  // 建立資料庫連接對象cn
            {
                string sqlstr = "SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId3;  // 查詢字串
                //依傳入的類別編號來傳回指定的產品資料的DataTable
                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
                DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
                lb_dgv1.Text = "刪除 產品資料";
            }

        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
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
        }

        private void button21_Click(object sender, EventArgs e)
        {
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

    class MyDBClass
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\Database1.mdf;Integrated Security=True;Connect Timeout=30";

        //Edit()方法可依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除
        public void Edit(string SqlCmd)
        {
            try
            {
                SqlConnection cn = new SqlConnection(db_cnstr);  // 建立資料庫連接對象cn
                cn.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = SqlCmd;
                cmd.Connection = cn;
                cmd.ExecuteNonQuery();
                cn.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
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

// 連接字串
//string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";
//cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|\ch17DB.mdf;Integrated Security=True";
//string cnstr1 = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
//cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

/*
有v11.0的, 就不可以, 要改用MSSQLLocalDB
AttachDbFilename=|DataDirectory|ch17DB.mdf  是 mdf 在 |DataDirectory|之下
AttachDbFilename=D:\ch17DB.mdf 是 指定 mdf 的位置
固定的寫法 :
Integrated Security=True";
其他參數 :
Connect Timeout=30

cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;       AttachDbFilename=|DataDirectory|ch17DB.mdf;                                   ;
cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;       AttachDbFilename=D:\ch17DB.mdf;      ;
cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\ch17DB.mdf; ;
*/

        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        //string cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";
        // 連接字串
//                    String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\VisualC#2015基礎必修課\2015範例程式\data\MyDB.mdf;Integrated Security=True;Connect Timeout=30";


//string cnstr =  "Data Source=MR-PC\\YL;Database=db_TomeTwo;UID=sa;Pwd=;";//取连接字符串
//string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";







//combobox 類別編號
//cboCategoryId.DisplayMember = "類別名稱";//指定Text屬性繫結的是類別名稱
//cboCategoryId.ValueMember = "類別編號";  //指定Value屬性繫結的是類別編號
//int CategoryId1 = int.Parse(cboCategoryId.SelectedValue.ToString());
//int CategoryId2 = int.Parse(cboCategoryId.SelectedValue.ToString());
//int CategoryId3 = int.Parse(cboCategoryId.SelectedValue.ToString());

//dataGridView1.CurrentRow.Cells[0].Value
//dataGridView1.CurrentRow.Cells[0].Value


/*
                Bitmap bitM = new Bitmap(this.pictureBox1.Width, this.pictureBox1.Height);  // 创建画布
                Graphics g = Graphics.FromImage(bitM);  // 创建Graphics对象
                Pen p = new Pen(new SolidBrush(Color.SlateGray), 1.0f);  // 创建Pen对象
                p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;  // 设置虚线
                g.Clear(Color.White);  // 设置画布颜色

                        int x, y, w, h;  // 声明变量存储坐标和大小
                        g.DrawString(dr[0].ToString(), new Font("宋体", 9, FontStyle.Regular), new SolidBrush(Color.Black), 76 + 40 * j, this.pictureBox1.Height - 16);  // 绘制商品名称
                        x = 78 + 40 * j;  // X坐标

                        //richTextBox1.Text += "bbbb : " + Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100))) + "\n";
                        y = this.pictureBox1.Height - 20 - Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100)));  // Y坐标

                        w = 24;  // 宽度

                        richTextBox1.Text += "cccc : " + dr[1].ToString() + "\n";
                        //richTextBox1.Text += "cccc : " + Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100) + "\n";
                        h = Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100);  // 高度

                        g.FillRectangle(new SolidBrush(Color.SlateGray), x, y, w, h);  // 绘制柱形图
                        g.DrawString((h * 100 / 20).ToString(), new Font("宋体", 8, FontStyle.Bold), new SolidBrush(Color.Tomato), new Point(x + 4, y - 10));  // 在柱形图指定的位置绘制文字
                this.pictureBox1.BackgroundImage = bitM;  // 显示绘制的图形

*/





