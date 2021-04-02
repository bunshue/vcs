using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace EncryptProcedure
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            SqlDataAdapter dap = new SqlDataAdapter("exec sp_helptext insert_加密學生訊息表", con);
            dap.SelectCommand.CommandType = CommandType.Text;
            DataSet ds = new DataSet();
            dap.Fill(ds);
            try
            {
                textBox1.Text = ds.Tables[0].Rows[0][0].ToString();
            }
            catch
            {
                textBox1.Text = "該預儲程序已加密，無法檢視！";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            con.Open();
            SqlCommand cmd = new SqlCommand("ALTER  PROCEDURE [insert_加密學生訊息表](@姓名_2 [varchar](50),@性別_3	[varchar](50),@年齡_4 [int],@籍貫_5 [varchar](50),@課程編號_6 [varchar](50)) with encryption AS INSERT INTO [db_10].[dbo].[學生訊息表] ([姓名],[性別],[年齡], [籍貫],[課程編號]) VALUES (@姓名_2, @性別_3, @年齡_4, @籍貫_5, @課程編號_6)", con);
            cmd.CommandType = CommandType.Text;
            cmd.ExecuteNonQuery();
            con.Close();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("Server=(local);database=db_10;Uid=sa;Pwd=");
            con.Open();
            SqlCommand cmd = new SqlCommand("ALTER  PROCEDURE [insert_加密學生訊息表](@姓名_2 [varchar](50),@性別_3	[varchar](50),@年齡_4 [int],@籍貫_5 [varchar](50),@課程編號_6 [varchar](50)) AS INSERT INTO [db_10].[dbo].[學生訊息表] ([姓名],[性別],[年齡], [籍貫],[課程編號]) VALUES (@姓名_2, @性別_3, @年齡_4, @籍貫_5, @課程編號_6)", con);
            cmd.CommandType = CommandType.Text;
            cmd.ExecuteNonQuery();
            con.Close();
        }
    }
}