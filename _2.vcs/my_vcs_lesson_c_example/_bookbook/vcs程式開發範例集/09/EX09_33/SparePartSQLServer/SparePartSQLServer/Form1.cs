using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.IO;
using System.Data.SqlClient;

namespace SparePartSQLServer
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases", con);
                da.Fill(dt);
                this.comboBox1.DataSource = dt.DefaultView;
                this.comboBox1.DisplayMember = "name";
                this.comboBox1.ValueMember = "name";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            beifenInfo();
        }

        public void beifenInfo()
        {
            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串

            try
            {
                sd.InitialDirectory = Application.StartupPath + "\\";//預設路徑為D：//
                sd.FilterIndex = 1;								//預設值為第一個
                sd.RestoreDirectory = true;						//重新定位保存路徑
                sd.Filter = "備份文件 (*.bak)|*.bak|所有文件 (*.*)|*.*";//過濾器，定義文件類型
                if (sd.ShowDialog() == DialogResult.OK)
                {
                    if (!File.Exists(sd.FileName.ToString()))
                    {
                        SqlConnection con = new SqlConnection();		//利用程式碼完成連接資料庫
                        con.ConnectionString = "server=.;uid=sa;pwd=;database='" + this.comboBox1.Text + "'";
                        con.Open();
                        SqlCommand com = new SqlCommand();
                        this.textBox1.Text = sd.FileName.ToString();
                        com.CommandText = "BACKUP DATABASE " + this.comboBox1.Text + " TO DISK = '" + sd.FileName.ToString() + "'";
                        com.Connection = con;							//連接
                        com.ExecuteNonQuery();						    //執行
                        con.Close();
                        con.Dispose();
                        //MessageBox.Show("數據備份成功！");
                        richTextBox1.Text += "數據備份成功\n";
                    }
                    else
                    {
                        //MessageBox.Show("請重新命名！");
                        richTextBox1.Text += "請重新命名\n";
                    }
                }
            }
            catch (Exception k)
            {
                //MessageBox.Show(k.Message);
                richTextBox1.Text += "數據備份失敗, 原因 : \n";
                richTextBox1.Text += k.Message + "\n";

                return;
            }
        }
    }
}
