using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace PROCEDUREWrite
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showinfo();
        }
        //自定義方法，顯示數據
        private void showinfo()
        {
            using (SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con))//建立SQL語旬與數據庫的連接
            {
                DataTable dt = new DataTable();//實例化DataTable類
                da.Fill(dt);//新增SQL語句並執行
                DataView dv = new DataView(dt);//實例化DataView
                this.dataGridView1.DataSource = dv;//顯示數據
            }
        }
        //新增
        private void button1_Click(object sender, EventArgs e)
        {
            this.textBox1.Text = ID();//自定義方法，自動產生編號
            this.textBox1.Enabled = false;//按鈕不可用
        }
        //自定義方法
        private string ID()
        {
            try
            {
                SqlCommand cmd = new SqlCommand();//實例化SqlCommand類
                cmd.Connection = con;//設定資料庫的連接
                con.Open();//打開資料庫的連接
                cmd.CommandType = CommandType.StoredProcedure;//設定類型為預儲程序
                cmd.CommandText = "proc_Id";//預儲程序的名稱
                SqlParameter sqlOutput = new SqlParameter("@Id", SqlDbType.VarChar, 8);//取得最後一個記錄的編號
                sqlOutput.Direction = ParameterDirection.Output;//參數輸出
                cmd.Parameters.Add(sqlOutput);//新增編號
                cmd.ExecuteNonQuery();//執行SQL語句
                con.Close();//關閉連接
                return cmd.Parameters["@Id"].Value.ToString();//傳回編號的值
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return null;
            }
        }
        //保存
        private void button2_Click(object sender, EventArgs e)
        {
            using (SqlCommand cmd = new SqlCommand())//實例化SqlCommand類
            {
                try
                {
                    cmd.Connection = con;//建立資料庫的連接
                    con.Open();//打開資料庫的連接
                    cmd.CommandType = CommandType.StoredProcedure;//設定類型為預儲程序
                    cmd.CommandText = "proc_insert";//預儲程序我
                    SqlParameter[] prams =
                        {
						        new SqlParameter("@id", SqlDbType.VarChar, 8),
                                new SqlParameter("@name", SqlDbType.VarChar, 50),
                                new SqlParameter("@money", SqlDbType.Float),
                                new SqlParameter("@talk", SqlDbType.VarChar, 50)
				        };//新增預儲程序的參數名
                    prams[0].Value = this.textBox1.Text;//設定參數值
                    prams[1].Value = this.textBox2.Text;
                    prams[2].Value = this.textBox4.Text;
                    prams[3].Value = this.textBox5.Text;
                    //新增參數
                    foreach (SqlParameter parameter in prams)
                        cmd.Parameters.Add(parameter);
                    SqlParameter sqlpar = cmd.Parameters.Add("@Return", SqlDbType.Int);
                    sqlpar.Direction = ParameterDirection.ReturnValue;//取得傳回值
                    cmd.ExecuteNonQuery();//執行SQL語句
                    con.Close();//關閉資料庫的連接
                }
                catch (Exception eu)
                {
                    MessageBox.Show("訊息有誤！！！");
                    con.Close();
                    return;
                }
                int i = Convert.ToInt16(cmd.Parameters["@Return"].Value.ToString());//傳回影響的行數
                if (i == 1)
                {
                    MessageBox.Show("新增過程成功");
                }
                else if (i == -1)
                {
                    MessageBox.Show("新增過程失敗");
                }
                showinfo();//顯示新增後的結果
            }
        }
    }
}