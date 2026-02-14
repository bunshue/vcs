using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;//聲明與數據庫操作有關的命名空間

namespace ListWaferFacility
{
    public partial class ListWaferFacility : Form
    {
        public DataSet WaferSet = null;//定義一個數據集對像
        private DataTable WaferTable = null;//定義一個數據表對像

        public ListWaferFacility()
        {
            InitializeComponent();
        }

        private void ListWaferFacility_Load(object sender, EventArgs e)
        {
            if (IsExistDataBase() == false)//當不存在數據庫連接時
            {
                Application.Exit();//退出應用程序
            }
            if (!System.IO.Directory.Exists(Application.StartupPath + "\\photo\\"))//當指定路徑下不存在圖片時
            {
                MessageBox.Show("不存在圖片，需要退出！");//彈出消息提示
                Application.Exit();//退出應用程序
            }
            PrintData();//顯示數據集中的數據
        }

        private void PrintData()
        {
            try
            {
                string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";

                SqlConnection con = new SqlConnection(cnstr);//"server=.;database=db_02;integrated security=sspi");//初始化一個數據庫連接對像
                SqlCommand WaferCommand = new SqlCommand("select 產品編號,產品名稱,產品說明,產品圖片 from tb_Photo", con);//執行SQL查詢語句
                SqlDataAdapter WaferAdapter = new SqlDataAdapter(WaferCommand);//初始化一個數據讀取器
                WaferSet = new DataSet();//初始化一個數據集
                WaferAdapter.Fill(WaferSet, "商品");//向數據集中填充數據
                WaferTable = WaferSet.Tables["商品"];//向數據表中填充數據
                DataColumn WaferColumn = new DataColumn("商品圖片", typeof(System.Drawing.Image));//初始化一個新列
                WaferTable.Columns.Add(WaferColumn);//向DataGridView控件中新添加一列
                foreach (DataRow dataRow in WaferTable.Rows)//循環遍歷DataGridView控件中的每一行
                {
                    dataRow["商品圖片"] = SnatchPhoto(dataRow["產品圖片"].ToString());//為每一條數據對應的圖片賦值
                }
                WaferTable.Columns.Remove("產品圖片");//移除數據集中原有的「產品圖片」列
                this.dataGridView1.DataSource = WaferSet.Tables["商品"].DefaultView;//為DataGridView控件綁定數據源
            }
            catch (Exception error)//捕獲異常信息
            {
                throw new Exception(error.Message);//顯示異常信息
            }
        }

        private bool IsExistDataBase()
        {
            SqlConnection con = new SqlConnection("Data Source=.;DataBase=master;integrated security=sspi");//初始化一個數據庫連接對像
            con.Open();//打開數據庫連接

            SqlCommand cmd = new SqlCommand("select count(*) from master.dbo.sysdatabases where name='db_02'", con);//執行一條SQL查詢語句
            if (Convert.ToInt32(cmd.ExecuteScalar()) == 0)//當無查詢結果時
            {
                MessageBox.Show("沒有建立數據庫，請用Data文件夾下的SQL語句建立數據庫！", "消息提示", MessageBoxButtons.OK, MessageBoxIcon.Warning);//彈出消息提示
                return false;//返回false
            }
            else //當存在查詢結果時
            {
                con.Close();//關閉數據庫連接
                return true;//返回true
            }
        }

        private Image SnatchPhoto(string path)
        {
            string[] strpath = path.Split('.');//定義一個字符串數組
            if (!strpath[strpath.Length - 1].Equals("bmp", StringComparison.OrdinalIgnoreCase))//當該路徑下存在圖片時
            {
                path = path + ".bmp";//還原該路徑
            }
            path = Application.StartupPath + "\\photo\\" + path;//指定圖片的相對路徑
            return System.Drawing.Image.FromFile(path);//從指定的相對路徑中獲取圖片
        }
    }
}

