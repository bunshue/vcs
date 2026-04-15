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

namespace ByteImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(pic_filename);
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            //记录选择的用户名
            string user_name = dataGridView1.Rows[e.RowIndex].Cells[1].Value.ToString();

            if (user_name != "")
            {
                richTextBox1.Text += "你點選的用戶名 : " + user_name + "\n";

                // 連接字串
                string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

                SqlConnection cn = new SqlConnection(cnstr);     //实例化数据库连接对象

                // 查詢字串
                string sqlstr = "SELECT * FROM tb_Image WHERE name='" + user_name + "'";
                richTextBox1.Text += sqlstr + "\n";

                SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);

                DataSet ds = new DataSet();                   //实例化数据集对象
                da.Fill(ds);                       //填充数据集

                richTextBox1.Text += "取得用戶名稱 : " + ds.Tables[0].Rows[0][1].ToString() + "\n";

                //使用数据库中存储的二进制头像实例化内存数据流
                MemoryStream MStream = new MemoryStream((byte[])ds.Tables[0].Rows[0][2]); // 圖片
                pictureBox1.Image = Image.FromStream(MStream);  //显示用户头像

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "添加用戶訊息\n";

            //選擇的頭像名稱
            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            //string user_name = "david wang aaaccc";  // 用戶名稱
            string user_name = textBox1.Text;  // 用戶名稱

            //添加用户信息

            richTextBox1.Text += "用戶名稱 : " + user_name + "\n";
            richTextBox1.Text += "影像檔案 : " + pic_filename + "\n";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_TomeTwo.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection cn = new SqlConnection(cnstr);

            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Image WHERE name='" + user_name + "'";
            SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);
            DataSet ds = new DataSet();                   //实例化数据集对象
            da.Fill(ds);                       //填充数据集
            if (ds.Tables[0].Rows.Count <= 0)
            {
                FileStream FStream = new FileStream(pic_filename, FileMode.Open, FileAccess.Read);
                BinaryReader BReader = new BinaryReader(FStream);
                byte[] byteImage = BReader.ReadBytes((int)FStream.Length);
                SqlCommand sqlcmd = new SqlCommand("insert into tb_Image(name,photo) values(@name,@photo)", cn);
                sqlcmd.Parameters.Add("@name", SqlDbType.VarChar, 50).Value = user_name;
                sqlcmd.Parameters.Add("@photo", SqlDbType.Image).Value = byteImage;
                cn.Open();
                sqlcmd.ExecuteNonQuery();
                cn.Close();
                richTextBox1.Text += "加入用戶信息 OK\n";

            }
            else
            {
                richTextBox1.Text += "加入用戶信息 NG, 已經存在該用戶\n";
            }
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

        private void button1_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_TomeTwo.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Image";
            //da = new SqlDataAdapter("select name as 用户名称 from tb_Image", cn);

            sql_read_database(db_filename, sqlstr, dataGridView1);

        }
    }
}
