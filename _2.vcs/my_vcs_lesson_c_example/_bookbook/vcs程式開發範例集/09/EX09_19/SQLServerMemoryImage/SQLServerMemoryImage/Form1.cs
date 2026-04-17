using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;
using System.IO;

namespace SQLServerMemoryImage
{
    public partial class Form1 : Form
    {
        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

        byte[] imgBytesIn;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工訊息";
            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫入影像資料\n";

            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(pic_filename);

            FileStream fs = new FileStream(pic_filename, FileMode.Open, FileAccess.Read);
            BinaryReader br = new BinaryReader(fs);
            imgBytesIn = br.ReadBytes((int)fs.Length);

            string new_num_id = "A12aaa";  // 員工編號
            string new_name = "david wang";  // 姓名
            string new_sex = "男";  // 性別
            string new_birthday = "2006/03/11";  // 出生日期
            string new_city = "hsinchu";  // 籍貫
            string new_work_year = "5";  // 工齡
            string new_telephone = "0912345678";  // 電話
            string new_department = "RD";  // 部門名稱

            ////string new_picture_filename = "";  // 照片路徑

            NumID = new_num_id;
            name = new_name;
            pic = imgBytesIn;
            sex = new_sex;
            birthday = new_birthday;
            city = new_city;
            years = Convert.ToInt16(new_work_year);
            phone = new_telephone;
            part = new_department;

            richTextBox1.Text += "增加資料\n";

            SqlConnection con = new SqlConnection(cnstr);

            try
            {
                con.Open();

                // 查詢字串
                string sqlstr = "INSERT INTO 員工訊息 values(@員工編號,@姓名,@照片,@性別,@出生日期,@籍貫,@工齡,@電話,@部門名稱)";

                SqlCommand cmd = new SqlCommand(sqlstr, con);

                cmd.Parameters.Add("@員工編號", SqlDbType.Text).Value = NumID;
                cmd.Parameters.Add("@姓名", SqlDbType.Text).Value = name;
                cmd.Parameters.Add("@照片", SqlDbType.Binary).Value = pic;
                cmd.Parameters.Add("@性別", SqlDbType.Text).Value = sex;
                cmd.Parameters.Add("@出生日期", SqlDbType.Text).Value = birthday;
                cmd.Parameters.Add("@籍貫", SqlDbType.Text).Value = city;
                cmd.Parameters.Add("@工齡", SqlDbType.Int).Value = years;
                cmd.Parameters.Add("@電話", SqlDbType.Text).Value = phone;
                cmd.Parameters.Add("@部門名稱", SqlDbType.Text).Value = part;
                cmd.ExecuteNonQuery();
                con.Close();

                richTextBox1.Text += "加入資料 OK\n";
            }
            catch (Exception ey)
            {
                richTextBox1.Text += "加入資料 NG, 原因\n";
                richTextBox1.Text += ey.Message.ToString() + "\n";
            }

            //string sqlstr = "SELECT 員工編號,姓名,性別,籍貫,電話,部門名稱 FROM 員工訊息";
            //this.dataGridView1.DataSource = DataBinding(sqlstr).DefaultView;
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
        }

        //#region//存取器
        private string 員工編號;
        private string 姓名;
        private byte[] 照片;
        private string 性別;
        private string 出生日期;
        private string 籍貫;
        private int 工齡;
        private string 電話;
        private string 部門名稱;
        private string NumID
        {
            get { return 員工編號; }
            set { 員工編號 = value; }
        }
        private string name
        {
            get { return 姓名; }
            set { 姓名 = value; }
        }
        private byte[] pic
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
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工訊息";
            sql_read_database(db_filename, sqlstr, dataGridView2);
        }
    }
}
