using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace FileMemoryImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            this.pictureBox1.Image = Image.FromFile(pic_filename);

            textBox1.Text = "A123456";  // 檔案編號
            textBox2.Text = "1234";  // 工號
            textBox3.Text = "david";  // 姓名
            textBox4.Text = "2006/03/11";  // 出生日期
            textBox5.Text = "Taiwan";  // 籍貫
            textBox6.Text = "5";  // 工齡
            textBox7.Text = "研發部";  // 部門名稱
            textBox8.Text = "0912345678";  // 電話

            comboBox1.Text = "男";  // 性別
            comboBox2.Text = "員工";  // 技術職稱
            comboBox3.Text = "已婚";  // 婚姻狀態
            comboBox4.Text = "良好";  // 健康狀態

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);

            try
            {
                con.Open();
                StringBuilder strSql = new StringBuilder();
                strSql.Append("insert into 檔案訊息 values(@檔案編號,@工號,");
                strSql.Append("@姓名,@照片,@性別,@出生日期,@籍貫,@工齡,@電話,");
                strSql.Append("@部門名稱,@技術職稱,@婚姻狀態,@健康狀態)");

                richTextBox1.Text += "strSql : " + strSql + "\n";

                SqlCommand cmd = new SqlCommand(strSql.ToString(), con);
                cmd.Parameters.Add("@檔案編號", SqlDbType.Text).Value = this.textBox1.Text.Trim().ToString();
                cmd.Parameters.Add("@工號", SqlDbType.Text).Value = this.textBox2.Text.Trim().ToString();
                cmd.Parameters.Add("@姓名", SqlDbType.Text).Value = this.textBox3.Text.Trim().ToString();
                cmd.Parameters.Add("@照片", SqlDbType.Text).Value = pic_filename;
                cmd.Parameters.Add("@性別", SqlDbType.Text).Value = this.comboBox1.Text.Trim().ToString();
                cmd.Parameters.Add("@出生日期", SqlDbType.Text).Value = this.textBox4.Text.Trim().ToString();
                cmd.Parameters.Add("@籍貫", SqlDbType.Text).Value = this.textBox5.Text.Trim().ToString();
                cmd.Parameters.Add("@工齡", SqlDbType.Int).Value = Convert.ToInt16(this.textBox6.Text.Trim().ToString());
                cmd.Parameters.Add("@電話", SqlDbType.Text).Value = this.textBox6.Text.Trim().ToString();
                cmd.Parameters.Add("@部門名稱", SqlDbType.Text).Value = this.textBox7.Text.Trim().ToString();
                cmd.Parameters.Add("@技術職稱", SqlDbType.Text).Value = this.comboBox2.Text.Trim().ToString();
                cmd.Parameters.Add("@婚姻狀態", SqlDbType.Text).Value = this.comboBox3.Text.Trim().ToString();
                cmd.Parameters.Add("@健康狀態", SqlDbType.Text).Value = this.comboBox4.Text.Trim().ToString();
                cmd.ExecuteNonQuery();
                con.Close();
                MessageBox.Show("新增成功");
            }
            catch (Exception ey)
            {
                MessageBox.Show("新增失敗");
            }
        }

        //#region//存取器
        private string 檔案編號;
        private string 工號;
        private string 姓名;
        private string 照片;
        private string 性別;
        private string 出生日期;
        private string 籍貫;
        private int 工齡;
        private string 電話;
        private string 部門名稱;
        private string 技術職稱;
        private string 婚姻狀態;
        private string 健康狀態;

        private string ID
        {
            get { return 檔案編號; }
            set { 檔案編號 = value; }
        }
        private string NumID
        {
            get { return 工號; }
            set { 工號 = value; }
        }
        private string name
        {
            get { return 姓名; }
            set { 姓名 = value; }
        }
        private string pic
        {
            get { return 照片; }
            set { 照片 = value; }
        }
        private string sex
        {
            get { return 性別; }
            set { 性別 = value; }
        }
        private string birthday
        {
            get { return 出生日期; }
            set { 出生日期 = value; }
        }
        private string city
        {
            get { return 籍貫; }
            set { 籍貫 = value; }
        }
        private int years
        {
            get { return 工齡; }
            set { 工齡 = value; }
        }
        private string phone
        {
            get { return 電話; }
            set { 電話 = value; }
        }
        private string part
        {
            get { return 部門名稱; }
            set { 部門名稱 = value; }
        }
        private string state
        {
            get { return 技術職稱; }
            set { 技術職稱 = value; }
        }
        private string marriage
        {
            get { return 婚姻狀態; }
            set { 婚姻狀態 = value; }
        }
        private string health
        {
            get { return 健康狀態; }
            set { 健康狀態 = value; }
        }

        //#endregion


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

        private void button2_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 檔案訊息";

            sql_read_database(db_filename, sqlstr, dataGridView1);

        }
    }
}
