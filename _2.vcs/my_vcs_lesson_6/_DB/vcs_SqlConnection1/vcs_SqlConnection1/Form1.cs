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
        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        //String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\MyDB.mdf;Integrated Security=True;Connect Timeout=30";

        // 設定相關資料庫連線參數
        String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\VisualC#2015基礎必修課\2015範例程式\data\MyDB.mdf;Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

        }

        void show_item_location()
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

            dataGridView1.Size = new Size(640, 480);
            dataGridView1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            textBox1.Size = new Size(640, 360);
            textBox1.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            richTextBox1.Size = new Size(300, 498);
            richTextBox1.Location = new Point(x_st + dx * 7 + 40, y_st + dy * 4 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1860, 910);
            this.Text = "vcs_SqlConnection1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            SqlConnection cn = new SqlConnection(cnStr);
            SqlDataAdapter da = new SqlDataAdapter("SELECT * From 員工", cn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                //cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|\ch17DB.mdf;Integrated Security=True";
                cn.ConnectionString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\VisualC#2015基礎必修課\2015範例程式\data\ch17DB.mdf;Integrated Security=True;Connect Timeout=30";

                cn.Open();
                SqlDataAdapter daEmployee = new SqlDataAdapter("SELECT * FROM 員工", cn);
                DataSet ds = new DataSet();
                daEmployee.Fill(ds, "員工");
                dataGridView1.DataSource = ds.Tables["員工"];
                SqlCommand cmdCount, cmdSum, cmdAvg, cmdMax, cmdMin;
                //取員工資料筆數
                cmdCount = new SqlCommand("SELECT COUNT(*) FROM 員工", cn);
                richTextBox1.Text += "員工資料表共 " + cmdCount.ExecuteScalar().ToString() + " 筆記錄\n";
                //取薪資加總
                cmdSum = new SqlCommand("SELECT SUM(薪資) FROM 員工", cn);
                richTextBox1.Text += "員工資料表薪資加總共 " + cmdSum.ExecuteScalar().ToString() + "\n";
                //取薪資平均
                cmdAvg = new SqlCommand("SELECT AVG(薪資) FROM 員工", cn);
                richTextBox1.Text += "員工資料表薪資平均為 " + cmdAvg.ExecuteScalar().ToString() + "\n";
                //取薪資最高薪
                cmdMax = new SqlCommand("SELECT Max(薪資) FROM 員工", cn);
                richTextBox1.Text += "最高薪為 " + cmdMax.ExecuteScalar().ToString() + "\n";
                //取薪資最低薪
                cmdMin = new SqlCommand("SELECT Min(薪資) FROM 員工", cn);
                richTextBox1.Text += "最低薪為 " + cmdMin.ExecuteScalar().ToString() + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //test 2

            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|Northwind.mdf;Integrated Security=True";
                cn.Open();
                if (cn.State == ConnectionState.Open)
                {
                    MessageBox.Show("資料庫已連接", "目前狀態");
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|Northwind.mdf;Integrated Security=True

            /*
            using (SqlConnection cn = new SqlConnection(Properties.Settings.Default.connString))
            {
                cn.Open();
                MessageBox.Show("連接資料庫：" + cn.Database, "Form1狀態");
            }
            */
        }

        private void button4_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        textBox1.Text += dr[i].ToString() + "\t";
                    }
                    textBox1.Text += Environment.NewLine;
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    textBox1.Text += dr["學號"].ToString() + "\t";
                    textBox1.Text += dr["姓名"].ToString() + "\t";
                    textBox1.Text += dr["國文"].ToString() + "\t";
                    textBox1.Text += dr["英文"].ToString() + "\t";
                    textBox1.Text += dr["數學"].ToString() + "\t";
                    textBox1.Text += Environment.NewLine;
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        textBox1.Text += dr.GetValue(i).ToString() + "\t";
                    }
                    textBox1.Text += Environment.NewLine;
                }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    textBox1.Text += dr.GetString(0) + "\t";   //讀取學號
                    textBox1.Text += dr.GetString(1) + "\t";   //讀取姓名
                    textBox1.Text += dr.GetInt32(2).ToString() + "\t";   //讀取國文
                    textBox1.Text += dr.GetInt32(3).ToString() + "\t";   //讀取英文
                    textBox1.Text += dr.GetInt32(4).ToString() + "\t";   //讀取數學
                    textBox1.Text += Environment.NewLine;
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;AttachDbFilename=|DataDirectory|ch17DB.mdf;Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    textBox1.Text += dr.GetSqlString(0).ToString() + "\t";//讀取學號
                    textBox1.Text += dr.GetSqlString(1).ToString() + "\t";//讀取姓名
                    textBox1.Text += dr.GetSqlInt32(2).ToString() + "\t";//讀取國文
                    textBox1.Text += dr.GetSqlInt32(3).ToString() + "\t";//讀取英文
                    textBox1.Text += dr.GetSqlInt32(4).ToString() + "\t";//讀取數學
                    textBox1.Text += Environment.NewLine;
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
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

