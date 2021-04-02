using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Linq;
using System.Data.SqlClient;

namespace SparePartSQLServer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using(SqlConnection con=new SqlConnection("server=.;pwd=;uid=sa;database=master"))
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
                        con.ConnectionString = "server=.;uid=sa;pwd=;database='"+this.comboBox1.Text+"'";
                        con.Open();
                        SqlCommand com = new SqlCommand();
                        this.textBox1.Text = sd.FileName.ToString();
                        com.CommandText = "BACKUP DATABASE " + this.comboBox1.Text + " TO DISK = '" + sd.FileName.ToString() + "'";
                        com.Connection = con;							//連接
                        com.ExecuteNonQuery();						    //執行
                        con.Close();
                        con.Dispose();
                        MessageBox.Show("數據備份成功！");
                    }
                    else
                    {
                        MessageBox.Show("請重新命名！");
                    }
                }
            }
            catch (Exception k)
            {
                MessageBox.Show(k.Message);
                return;
            }
        }
    }
}