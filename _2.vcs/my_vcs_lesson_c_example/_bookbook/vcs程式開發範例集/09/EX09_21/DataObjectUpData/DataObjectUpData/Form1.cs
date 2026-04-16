using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;

using System.Data.SqlClient;

namespace DataObjectUpData
{
    public partial class Form1 : Form
    {
        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

        SqlConnection con;

        static int Num = 0;
        int Count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            con = new SqlConnection(cnstr);

            Resultinfo(Num);

            // 查詢字串
            string sqlstr = "select Count(*) from 員工表";

            using (SqlCommand cmd = new SqlCommand(sqlstr, con))
            {
                con.Open();
                Count = Convert.ToInt32(cmd.ExecuteScalar());
                con.Close();
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private DataSet DtReslut(int i)
        {
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                // 查詢字串
                string sqlstr = "SELECT * FROM 員工表";

                da.SelectCommand = new SqlCommand(sqlstr, con);
                DataSet ds = new DataSet();
                da.Fill(ds, i, i + 1, "員工表");
                return ds;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Num = 0;
            Resultinfo(Num);
        }

        private void Resultinfo(int j)
        {
            DataSet dsNew = DtReslut(j);
            this.textBox1.Text = dsNew.Tables[0].Rows[0][0].ToString();
            this.textBox2.Text = dsNew.Tables[0].Rows[0][1].ToString();
            this.textBox4.Text = dsNew.Tables[0].Rows[0][2].ToString();
            this.textBox5.Text = dsNew.Tables[0].Rows[0][3].ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Num -= 1;
            if (Num >= 0)
            {
                Resultinfo(Num);
            }
            else
            {
                MessageBox.Show("現已是首條記錄");
                Num = 0;
                return; ;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Num += 1;
            if (Num < Count)
            {
                Resultinfo(Num);
            }
            else
            {
                MessageBox.Show("現已是末條記錄");
                Num = Count - 1;
                return;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Num = Count;
            Resultinfo(Num - 1);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (update())
            {
                MessageBox.Show("成功修改");
            }
        }

        private bool update()
        {
            // 查詢字串
            string sqlstr = "update 員工表 set 員工姓名=@員工姓名,基本工資=@基本工資,工作評價=@工作評價 where 員工編號=@員工編號";

            using (SqlCommand command = new SqlCommand(sqlstr, con))
            {
                con.Open();
                try
                {
                    command.Parameters.Add("@員工編號", SqlDbType.VarChar, 50, "員工編號").Value = this.textBox1.Text;
                    command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 50, "員工姓名").Value = this.textBox2.Text;
                    command.Parameters.Add("@基本工資", SqlDbType.Float, 8, "基本工資").Value = Convert.ToString(this.textBox4.Text);
                    command.Parameters.Add("@工作評價", SqlDbType.VarChar, 50, "工作評價").Value = this.textBox5.Text;
                    command.ExecuteNonQuery();
                    con.Close();
                    return true;
                }
                catch
                {
                    return false;
                }
            }
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

        //以下為debug ----------------------------------------------------------------------------------------------------  # 100個

        private void button7_Click(object sender, EventArgs e)
        {
            //以下為debug
            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }
    }
}
