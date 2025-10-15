using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SQLite;

namespace vcs_SQLite2
{
    public partial class Form1 : Form
    {
        //path of data base
        string path = "data_table.db";
        string cs = @"URI=file:" + Application.StartupPath + "\\data_table.db"; //database creat debug folder

        SQLiteConnection con;
        SQLiteCommand cmd;
        SQLiteDataReader dr;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "path : " + path + "\n";
            richTextBox1.Text += "cs : " + cs + "\n";

            Create_db();
            data_show();
        }

        //show data in table
        private void data_show()
        {
            richTextBox1.Text += "讀取資料庫的資料\n";
            var con = new SQLiteConnection(cs);
            con.Open();

            string stm = "SELECT * FROM table01";
            var cmd = new SQLiteCommand(stm, con);
            dr = cmd.ExecuteReader();

            while (dr.Read())
            {
                richTextBox1.Text += "取得資料\t" + dr.GetString(0) + "\t" + dr.GetString(1) + "\n";
                //dataGridView1.Rows.Insert(0, dr.GetString(0), dr.GetString(1));
            }
        }

        //create database and table
        private void Create_db()
        {
            if (!System.IO.File.Exists(path))
            {
                richTextBox1.Text += "資料庫不存在, 建立之\n";
                SQLiteConnection.CreateFile(path);
                using (var sqlite = new SQLiteConnection(@"Data Source=" + path))
                {
                    sqlite.Open();
                    string sql = "CREATE TABLE table01(name varchar(20),id varchar(12))";
                    SQLiteCommand command = new SQLiteCommand(sql, sqlite);
                    command.ExecuteNonQuery();
                }
            }
            else
            {
                richTextBox1.Text += "資料庫已存在\n";
                return;
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            data_show();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "加入資料\n";
            var con = new SQLiteConnection(cs);
            con.Open();
            var cmd = new SQLiteCommand(con);

            try
            {
                cmd.CommandText = "INSERT INTO table01(name,id) VALUES(@name,@id)";

                string NAME = "david";
                string ID = "123";

                cmd.Parameters.AddWithValue("@name", NAME);
                cmd.Parameters.AddWithValue("@id", ID);

                //dataGridView1.ColumnCount = 2;
                //dataGridView1.Columns[0].Name = "Name";
                //dataGridView1.Columns[1].Name = "Id";
                //string[] row = new string[] { NAME, ID };
                //dataGridView1.Rows.Add(row);

                cmd.ExecuteNonQuery();
            }
            catch (Exception)
            {
                richTextBox1.Text += "無法新增資料\n";
                return;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "更新資料\n";
            var con = new SQLiteConnection(cs);
            con.Open();

            var cmd = new SQLiteCommand(con);

            try
            {
                cmd.CommandText = "UPDATE table01 Set id=@Id where name =@Name";
                cmd.Prepare();
                cmd.Parameters.AddWithValue("@Name", "john");
                cmd.Parameters.AddWithValue("@Id", "456");

                cmd.ExecuteNonQuery();
                //dataGridView1.Rows.Clear();
                data_show();
            }
            catch (Exception)
            {
                richTextBox1.Text += "無法更新資料\n";
                return;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "刪除資料\n";
            var con = new SQLiteConnection(cs);
            con.Open();

            var cmd = new SQLiteCommand(con);

            try
            {
                cmd.CommandText = "DELETE FROM table01 where name =@Name";
                cmd.Prepare();
                cmd.Parameters.AddWithValue("@Name", "david");

                cmd.ExecuteNonQuery();
                //dataGridView1.Rows.Clear();
                data_show();
            }
            catch (Exception)
            {
                richTextBox1.Text += "無法刪除資料\n";
                return;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }
    }
}

