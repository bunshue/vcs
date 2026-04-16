using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.SqlClient;  // for SqlConnection, SqlCommand, SqlDataAdapter
using System.Collections;  // for Hashtable
using System.Drawing.Drawing2D;  // for LinearGradientBrush
//using System.Drawing.Imaging;

namespace vcs_SqlConnection4
{
    public partial class Form1 : Form
    {
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

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
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            int dd = 26;
            dataGridView1.Size = new Size(510, 380);
            dataGridView2.Size = new Size(510, 380);
            panel1.Size = new Size(420, 380);
            pictureBox1.Size = new Size(420, 380);

            lb_dgv1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + dd);
            lb_dgv2.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            dataGridView2.Location = new Point(x_st + dx * 3, y_st + dy * 6 + dd);
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
            panel1.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 6);

            richTextBox1.Size = new Size(300, 820);
            richTextBox1.Location = new Point(x_st + dx * 7 + 110, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1920, 890);
            this.Text = "vcs_SqlConnection4";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            dataGridView1.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            dataGridView2.DataSource = null;  // 設定DGV的資料來源為無, 即清除
            lb_dgv1.Text = "";
            lb_dgv2.Text = "";
        }

        void sql_read_database_dr(string db_filename, string sqlstr)
        {
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            //讀取資料庫
            using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
            {
                //cn.ConnectionString = cnstr;  // 連接字串, 可有可無
                cn.Open();  // 打開資料庫連線

                SqlCommand cmd = new SqlCommand(sqlstr, cn);
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                /*
                //讀出所有欄位資訊
                DataTable schema = dr.GetSchemaTable();  // 建立DT
                foreach (DataRow schema_row in schema.Rows)
                {
                    richTextBox1.Text += "欄位名稱 : " + schema_row.Field<string>("ColumnName") + "\t";
                    richTextBox1.Text += "資料型態 : " + schema_row.Field<Type>("DataType").ToString() + "\n";
                }
                */
                richTextBox1.Text += "欄數 dr.FieldCount = " + dr.FieldCount.ToString() + "\t欄位名稱 :\n";
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    richTextBox1.Text += dr.GetName(i) + "\t";
                }
                richTextBox1.Text += "\n";

                //印出全部資料
                //richTextBox1.Text += "內容\n";
                while (dr.Read())  // 讀取一筆資料到dr
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        richTextBox1.Text += dr[i].ToString();
                        //richTextBox1.Text += dr.GetValue(i).ToString();  // same
                        if (i == (dr.FieldCount - 1))
                        {
                            richTextBox1.Text += "\n";
                        }
                        else
                        {
                            richTextBox1.Text += "\t";
                        }
                    }
                    //richTextBox1.Text += dr[0].ToString() + "\t" + Convert.ToDouble(dr[1].ToString()) + "\n";
                    //直接印出 richTextBox1.Text += dr[0].ToString() + "\t" + dr[1].ToString() + "\t" + dr[2].ToString() + "\n";
                }
                dr.Close();
            }
        }

        void sql_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
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
            if (dgv == dataGridView1)
            {
                lb_dgv1.Text = "";
                lb_dgv2.Text = "";
            }
            else if (dgv == dataGridView2)
            {
                lb_dgv2.Text = "";
            }
        }

        void sql_write_database(string db_filename, string sqlstr)
        {
            //依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除 應該都只是操作 並不能取出資料

            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

            //對資料庫操作 增茶改山
            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    cn.Open();  // 打開資料庫連線
                    SqlCommand cmd = new SqlCommand();
                    cmd.CommandText = sqlstr;
                    cmd.Connection = cn;
                    cmd.ExecuteNonQuery();  // 執行SQL命令
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
        }


        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //利用控制元件完成柱形圖分析

            //水果出售情況統計表

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                DataSet ds = new DataSet();
                SqlCommand cmd = new SqlCommand("SELECT * FROM tb_Rectangle SELECT SUM(t_Num) FROM tb_Rectangle", con);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = cmd;
                da.Fill(ds);

                int Values = Convert.ToInt32(ds.Tables[1].Rows[0][0].ToString());
                richTextBox1.Text += "總數 : " + Values.ToString() + "\n";

                richTextBox1.Text += "資料筆數 : " + ds.Tables[0].Rows.Count.ToString() + "\n";

                for (int i = 0; i < ds.Tables[0].Rows.Count; i++)
                {
                    ds.Tables[0].Rows[i][0].ToString();

                    richTextBox1.Text += ds.Tables[0].Rows[i][0].ToString() + "\t";
                    richTextBox1.Text += ds.Tables[0].Rows[i][1].ToString() + "\n";
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            //在柱形圖的指定位置顯示說明文字

            //商品分析

            SqlConnection con;
            SqlCommand cmd;

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            con = new SqlConnection(cnstr);
            con.Open();

            using (cmd = new SqlCommand("SELECT TOP 3 * FROM tb_Rectangle ORDER BY t_Num DESC", con))//降冪
            {
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器

                for (int j = 0; j < 4; j++)
                {
                    if (dr.Read())
                    {
                        richTextBox1.Text += dr[0].ToString() + "\t" + Convert.ToDouble(dr[1].ToString()) + "\n";
                    }
                }
            }
        }
        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //利用圖表分析產品銷售走勢
            //D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\vcs程式開發範例集\13\Ex13_11\利用圖表分析產品銷售走勢\利用圖表分析產品銷售走勢
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //利用圖表分析彩票中獎情況

            //t_year 在 2005/4/1 ~ 2006/10/1 有資料
            string time_st = "2005/8/15";
            string time_sp = "2006/4/15";

            string sqlstr = "SELECT * FROM tb_lottery WHERE t_year BETWEEN '" + time_st + "' AND '" + time_sp + "' ORDER BY t_year";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();

            SqlCommand cmd = new SqlCommand(sqlstr, con);
            SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
            int i = 0;
            string str = null;
            float f = 0.0f;
            while (dr.Read())
            {
                i++;

                richTextBox1.Text += dr[0].ToString() + "\t" + Convert.ToDouble(dr[1].ToString()) + "\n";
                richTextBox1.Text += dr[0].ToString().Substring(0, 7) + "月---" + "\n";

                richTextBox1.Text += dr[1].ToString() + "\n";

                str += dr[1].ToString() + "#";
                f += Convert.ToSingle(dr[1].ToString());
            }
            dr.Close();

            richTextBox1.Text += "str = " + str + "\n";
            richTextBox1.Text += "總數 : " + f + "\n";

            string[] strCount = str.Split('#');
            int[] ICount = new int[strCount.Length];
            for (int l = 0; l < strCount.Length - 1; l++)
            {
                ICount[l] = Convert.ToInt32(strCount[l]);
                richTextBox1.Text += "strCount[l] = " + strCount[l] + "\tICount[l] = " + ICount[l] + "\n";
            }

            Point[] P = new Point[ICount.Length - 1];
            for (int j = 0; j < ICount.Length - 1; j++)
            {
                P[j].X = 35 + 28 * j;
                P[j].Y = this.panel1.Height - 20 - Convert.ToInt32(ICount[j] / f * (this.panel1.Height + 20));
            }
            f = 0.0f;
            str = null;
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            //多曲線數據分析

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            //有資料的年份
            //1999, 2000, 2001, 2004, 2005, 2006, 2007
            int query_year = 1999;

            int height = 440;
            int width = 600;
            Bitmap image = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(image);

            //清空圖片背景色
            g.Clear(Color.White);

            Font font = new Font("Arial", 9, FontStyle.Regular);
            Font font1 = new Font("細明體", 12, FontStyle.Regular);
            Font font2 = new Font("Arial", 8, FontStyle.Regular);

            LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, image.Width, image.Height), Color.Blue, Color.Blue, 1.2f, true);
            g.FillRectangle(Brushes.AliceBlue, 0, 0, width, height);
            Brush brush1 = new SolidBrush(Color.Blue);
            Brush brush2 = new SolidBrush(Color.SaddleBrown);

            string sqlstr = "SELECT * FROM tb_curve WHERE Years=" + query_year + "";

            using (SqlConnection Con = new SqlConnection(cnstr))
            {
                Con.Open();
                SqlCommand Com = new SqlCommand(sqlstr, Con);
                SqlDataReader dr = Com.ExecuteReader();  // 建立數據讀取器
                dr.Read();
                if (dr.HasRows)
                {
                    g.DrawString("" + query_year + "年公司內部人員統計表", font1, brush1, new PointF(160, 30));
                }
                dr.Close();
                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Blue), 0, 0, image.Width - 1, image.Height - 1);

                Pen mypen = new Pen(brush, 1);
                Pen mypen2 = new Pen(Color.Red, 2);
                //繪製線條
                //繪製縱向線條
                int x = 60;
                for (int i = 0; i < 12; i++)
                {
                    g.DrawLine(mypen, x, 80, x, 340);
                    x = x + 40;
                }
                Pen mypen1 = new Pen(Color.Blue, 2);
                g.DrawLine(mypen1, x - 480, 80, x - 480, 340);

                //繪製橫向線條
                int y = 106;
                for (int i = 0; i < 9; i++)
                {
                    g.DrawLine(mypen, 60, y, 540, y);
                    y = y + 26;
                }
                g.DrawLine(mypen1, 60, y, 540, y);

                //x軸
                String[] n = { "  一月", "  二月", "  三月", "  四月", "  五月", "  六月", "  七月", "  八月", "  九月", "  十月", "十一月", "十二月" };
                x = 35;
                for (int i = 0; i < 12; i++)
                {
                    g.DrawString(n[i].ToString(), font, Brushes.Red, x, 348); //設定文字內容及輸出位置
                    x = x + 40;
                }

                //y軸
                String[] m = { "900人", " 800人", " 700人", "600人", " 500人", " 400人", " 300人", " 200人", " 100人" };
                y = 100;
                for (int i = 0; i < 9; i++)
                {
                    g.DrawString(m[i].ToString(), font, Brushes.Red, 10, y); //設定文字內容及輸出位置
                    y = y + 26;
                }

                int[] Count1 = new int[12];
                int[] Count2 = new int[12];
                string[] NumChr = new string[12];
                string cmdtxt2 = "SELECT * FROM tb_curve WHERE Years=" + query_year + "";
                SqlCommand Com1 = new SqlCommand(cmdtxt2, Con);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = Com1;
                DataSet ds = new DataSet();
                da.Fill(ds);
                int j = 0;
                for (int i = 0; i < 12; i++)
                {
                    NumChr[i] = ds.Tables[0].Rows[0][i + 1].ToString();
                }
                for (j = 0; j < 12; j++)
                {
                    Count1[j] = Convert.ToInt32(NumChr[j].Split('|')[0].ToString()) * 26 / 100;
                }
                for (int k = 0; k < 12; k++)
                {
                    Count2[k] = Convert.ToInt32(NumChr[k].Split('|')[1].ToString()) * 26 / 100;
                }

                //顯示折線效果
                SolidBrush mybrush = new SolidBrush(Color.Red);
                Point[] points1 = new Point[12];
                points1[0].X = 60; points1[0].Y = 340 - Count1[0];
                points1[1].X = 100; points1[1].Y = 340 - Count1[1];
                points1[2].X = 140; points1[2].Y = 340 - Count1[2];
                points1[3].X = 180; points1[3].Y = 340 - Count1[3];
                points1[4].X = 220; points1[4].Y = 340 - Count1[4];
                points1[5].X = 260; points1[5].Y = 340 - Count1[5];
                points1[6].X = 300; points1[6].Y = 340 - Count1[6];
                points1[7].X = 340; points1[7].Y = 340 - Count1[7];
                points1[8].X = 380; points1[8].Y = 340 - Count1[8];
                points1[9].X = 420; points1[9].Y = 340 - Count1[9];
                points1[10].X = 460; points1[10].Y = 340 - Count1[10];
                points1[11].X = 500; points1[11].Y = 340 - Count1[11];
                g.DrawLines(mypen2, points1);  //繪製折線

                Pen mypen3 = new Pen(Color.Black, 2);
                Point[] points2 = new Point[12];
                points2[0].X = 60; points2[0].Y = 340 - Count2[0];
                points2[1].X = 100; points2[1].Y = 340 - Count2[1];
                points2[2].X = 140; points2[2].Y = 340 - Count2[2];
                points2[3].X = 180; points2[3].Y = 340 - Count2[3];
                points2[4].X = 220; points2[4].Y = 340 - Count2[4];
                points2[5].X = 260; points2[5].Y = 340 - Count2[5];
                points2[6].X = 300; points2[6].Y = 340 - Count2[6];
                points2[7].X = 340; points2[7].Y = 340 - Count2[7];
                points2[8].X = 380; points2[8].Y = 340 - Count2[8];
                points2[9].X = 420; points2[9].Y = 340 - Count2[9];
                points2[10].X = 460; points2[10].Y = 340 - Count2[10];
                points2[11].X = 500; points2[11].Y = 340 - Count2[11];
                g.DrawLines(mypen3, points2);  //繪製折線

                //繪製標識
                g.DrawRectangle(new Pen(Brushes.Red), 150, 370, 250, 50);  //繪製範圍框
                g.FillRectangle(Brushes.Red, 250, 380, 20, 10);  //繪製小矩形
                g.DrawString("試用員工人數", font2, Brushes.Red, 270, 380);
                g.FillRectangle(Brushes.Black, 250, 400, 20, 10);
                g.DrawString("正式員工人數", font2, Brushes.Black, 270, 400);

                this.panel1.BackgroundImage = image;
            }
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            //網站人氣指數曲線分析

            // 資料庫連線參數, 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            //清空圖片背景色
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.WhiteSmoke);
            //繪製畫筆
            Pen p = new Pen(Color.Blue);
            //可能要用到的字體
            Font fontO = new Font("Arial", 9, FontStyle.Regular);
            Font fontT = new Font("華文新魏", 16, FontStyle.Regular);
            //給制邊框與顯示字體
            Point pointStart = new Point(0, 0);
            Size sizeWindows = new Size(this.Width - 8, this.Height - 34);
            Rectangle rect = new Rectangle(pointStart, sizeWindows);
            g.DrawRectangle(p, rect);
            Brush brus = new SolidBrush(Color.Red);
            g.DrawString("網站人氣指數曲線分析", fontT, brus, this.Width / 2.00f - 150, 10.00f);
            //繪製網格線
            int x = this.Width / 10;
            int y = this.Height / 14;
            int z = this.Width / 10;
            int k = y * 12;
            //Y
            for (int i = 0; i < 12; i++)
            {
                g.DrawLine(p, x, y * 3 - 10, x, y * 12);
                x = x + (this.Width - 34) / 14;
            }
            //Y軸
            String[] n = { " 1月", " 2月", " 3月", " 4月", " 5月", " 6月", " 7月", " 8月", " 9月", "10月", "11月", "12月" };
            x = this.Width / 10 - 16;
            for (int i = 0; i < 12; i++)
            {
                g.DrawString(n[i].ToString(), fontO, Brushes.Red, x, y * 12); //設定文字內容及輸出位置
                x = x + (this.Width - 34) / 14;
            }
            //X
            for (int i = 0; i < 12; i++)
            {
                g.DrawLine(p, z, k, x + 10, k);
                k = k - (y * 12) / 16;
            }
            //X軸
            int h = k;
            String[] m = { "5500", "5000", "4500", "4000", "3500", "3000", "2500", "2000", "1500", "1000", "  500" };
            k = y * 12;
            for (int i = 0; i < 11; i++)
            {
                g.DrawString(m[10 - i].ToString(), fontO, Brushes.Red, z - 35, k - y);//設定文字內容及輸出位置
                k = k - (y * 12) / 16;
            }
            //繪製曲線圖
            //顯示折線效果
            int[] Count = new int[12];
            Pen mypen = new Pen(Color.Red, 2);
            Point[] points = new Point[12];
            x = this.Width / 10;//X的
            k = y * 12;
            SqlConnection Con = new SqlConnection(cnstr);
            string cmdtxt2 = "SELECT * FROM tb_reticulation";
            SqlCommand Com1 = new SqlCommand(cmdtxt2, Con);
            SqlDataAdapter da = new SqlDataAdapter();
            da.SelectCommand = Com1;
            DataSet ds = new DataSet();
            da.Fill(ds);
            int j = 0;
            for (j = 0; j < 12; j++)
            {
                //與Y軸數產生有關(y * 12) / 16  因為起始為500
                Count[j] = Convert.ToInt32(ds.Tables[0].Rows[0][j + 2].ToString()) * (y * 12) / 16 / 500;
            }
            points[0].X = x;
            points[0].Y = k - Count[0];
            x = x + (this.Width - 34) / 14;
            points[1].X = x;
            points[1].Y = k - Count[1];
            x = x + (this.Width - 34) / 14;
            points[2].X = x;
            points[2].Y = k - Count[2];
            x = x + (this.Width - 34) / 14;
            points[3].X = x;
            points[3].Y = k - Count[3];
            x = x + (this.Width - 34) / 14;
            points[4].X = x;
            points[4].Y = k - Count[4];
            x = x + (this.Width - 34) / 14;
            points[5].X = x;
            points[5].Y = k - Count[5];
            x = x + (this.Width - 34) / 14;
            points[6].X = x;
            points[6].Y = k - Count[6];
            x = x + (this.Width - 34) / 14;
            points[7].X = x;
            points[7].Y = k - Count[7];
            x = x + (this.Width - 34) / 14;
            points[8].X = x;
            points[8].Y = k - Count[8];
            x = x + (this.Width - 34) / 14;
            points[9].X = x;
            points[9].Y = k - Count[9];
            x = x + (this.Width - 34) / 14;
            points[10].X = x;
            points[10].Y = k - Count[10];
            x = x + (this.Width - 34) / 14;
            points[11].X = x;
            points[11].Y = k - Count[11];
            g.DrawLines(mypen, points);  //繪製折線      
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        static int SumNum;
        static float TimeNum;
        SqlConnection con;
        SqlCommand cmd;
        Hashtable ht = new Hashtable();

        private void button9_Click(object sender, EventArgs e)
        {
            //利用餅型圖分析產品市場佔有率

            // debug ST
            string db_filename = "db_13.mdf";
            string sqlstr = "SELECT * FROM tb_product";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            // debug SP

            ht.Clear();

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection con = new SqlConnection(cnstr);
            con.Open();

            using (SqlCommand cmd = new SqlCommand("SELECT SUM(t_Num) FROM tb_product", con))
            {
                SumNum = Convert.ToInt32(cmd.ExecuteScalar());
            }

            Random rnd = new Random();

            using (cmd = new SqlCommand("SELECT t_Name, SUM(t_Num) AS Num FROM tb_product GROUP BY t_Name", con))
            {
                Graphics g2 = this.pictureBox1.CreateGraphics();
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                while (dr.Read())
                {
                    ht.Add(dr[0], Convert.ToInt32(dr[1]));
                }
                float[] flo = new float[ht.Count];
                int T = 0;
                foreach (DictionaryEntry de in ht)
                {
                    flo[T] = Convert.ToSingle((Convert.ToDouble(de.Value) / SumNum).ToString().Substring(0, 6));
                    Brush Bru = new SolidBrush(Color.FromArgb(rnd.Next(255), rnd.Next(255), rnd.Next(255)));
                    g2.DrawString(de.Key + "        " + flo[T] * 100 + "%", new Font("Arial", 8, FontStyle.Regular), Bru, 7, 5 + T * 18);

                    float f = flo[T];

                    Graphics g = this.panel1.CreateGraphics();
                    if (TimeNum == 0.0f)
                    {
                        g.FillPie(Bru, 0, 0, this.panel1.Width, this.panel1.Height, 0, f * 360);
                    }
                    else
                    {
                        g.FillPie(Bru, 0, 0, this.panel1.Width, this.panel1.Height, TimeNum, f * 360);
                    }
                    TimeNum += f * 360;

                    T++;
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void draw_sub_picture(Graphics g, float f, string str)
        {
            richTextBox1.Text += "ConutNum = " + ConutNum.ToString() + "\t" + f.ToString() + "\t" + str + "\n";
            if (ConutNum == 0)
            {
                g.FillPie(new SolidBrush(Color.Black), 0, 0, (this.panel1.Width) / 2, (this.panel1.Height - 10) / 2, 0, 360 * f);
                g.DrawString(str, new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Black), (this.panel1.Width) / 2 - 70, 10);
                g.DrawString(Convert.ToString(f * 100).Substring(0, 5) + "%", new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Black), (this.panel1.Width) / 2 - 70, 25);
                floatNum = 360 * f;
                ConutNum += 1;
            }
            else if (ConutNum == 1)
            {
                g.FillPie(new SolidBrush(Color.DarkOrange), (this.panel1.Width) / 2, 0, (this.panel1.Width) / 2, (this.panel1.Height - 10) / 2, floatNum, 360 * f);
                g.DrawString(str, new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.DarkOrange), (this.panel1.Width) / 2 + 10, 10);
                g.DrawString(Convert.ToString(f * 100).Substring(0, 5) + "%", new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.DarkOrange), (this.panel1.Width) / 2 + 10, 25);
                floatNum += 360 * f;
                ConutNum += 1;
            }
            else if (ConutNum == 2)
            {
                g.FillPie(new SolidBrush(Color.Red), 0, (this.panel1.Height - 10) / 2 + 10, (this.panel1.Width) / 2, (this.panel1.Height - 10) / 2, floatNum, 360 * f);
                g.DrawString(str, new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Red), 10, (this.panel1.Height - 10) / 2 + 20);
                g.DrawString(Convert.ToString(f * 100).Substring(0, 5) + "%", new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Red), 10, (this.panel1.Height - 10) / 2 + 35);
                floatNum += 360 * f;
                ConutNum += 1;
            }
            else if (ConutNum == 3)
            {
                g.FillPie(new SolidBrush(Color.Blue), (this.panel1.Width) / 2 - 10, (this.panel1.Height - 10) / 2 + 10, (this.panel1.Width) / 2, (this.panel1.Height - 10) / 2, floatNum, 360 * f);
                g.DrawString(str, new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Blue), (this.panel1.Width) / 2 + 10, (this.panel1.Height - 10) / 2 + 20);
                g.DrawString(Convert.ToString(f * 100).Substring(0, 5) + "%", new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Blue), (this.panel1.Width) / 2 + 10, (this.panel1.Height - 10) / 2 + 35);
            }
        }

        // 連接字串
        string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

        static int ConutNum = 0;
        static float floatNum = 0.0f;

        private void button10_Click(object sender, EventArgs e)
        {
            //利用多餅型圖分析企業人力資源情況

            // debug ST
            string db_filename = "db_13.mdf";
            string sqlstr = "SELECT * FROM tb_manpower";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            // debug SP

            SqlConnection con = new SqlConnection(cnstr);

            int Sum = 100;
            using (SqlCommand cmd = new SqlCommand("SELECT SUM(t_Num) FROM tb_manpower ", con))
            {
                con.Open();
                Sum = Convert.ToInt32(cmd.ExecuteScalar());
                richTextBox1.Text += "Sum = " + Sum.ToString() + "\n";
                con.Close();
            }

            richTextBox1.Text += "Sum = " + Sum.ToString() + "\n";

            using (SqlCommand cmd = new SqlCommand("SELECT t_Point, SUM(t_Num) FROM tb_manpower GROUP BY t_Point ORDER BY SUM(t_Num) DESC", con))//降冪
            {
                Bitmap bmp = new Bitmap(this.panel1.Width, this.panel1.Height);
                Graphics g = Graphics.FromImage(bmp);
                cmd.Connection.Open();
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                while (dr.Read())
                {
                    richTextBox1.Text += dr[0].ToString() + "\t" + Convert.ToDouble(dr[1].ToString()) + "\n";
                    float f = Convert.ToSingle(dr[1]) / Sum;
                    string str = dr[0].ToString();
                    draw_sub_picture(g, f, str);
                }
                g.DrawLine(new Pen(Color.Black), 0, this.panel1.Height / 2, this.panel1.Width, this.panel1.Height / 2);
                g.DrawLine(new Pen(Color.Black), this.panel1.Width / 2, 0, this.panel1.Width / 2, this.panel1.Height);
                this.panel1.BackgroundImage = bmp;
                dr.Close();
                con.Close();
            }
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            //製作一個可以旋轉的餅型圖
            //D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\vcs程式開發範例集\13\Ex13_18\製作一個可以旋轉的餅型圖\製作一個可以旋轉的餅型圖
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 12\n";

            // 分析公司男女比率
            string db_filename = "db_13.mdf";
            string sqlstr = "SELECT * FROM tb_sex";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            sqlstr = "SELECT sex, COUNT(sex) num FROM tb_sex GROUP BY sex";
            sql_read_database(db_filename, sqlstr, dataGridView2);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 13 員工表\n";

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表";
            sql_read_database(db_filename, sqlstr, dataGridView1);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);

            con.Open();

            using (SqlCommand cmd = new SqlCommand("SELECT Max(員工編號) FROM 員工表", con))
            {
                //找到目前最大的員工編號 再加1，做為新增資料的員工編號
                if (Convert.ToString(cmd.ExecuteScalar()) != "")
                {
                    richTextBox1.Text += "aaaaaaaaaaaaaaaaa\n";
                    string strID = Convert.ToString(cmd.ExecuteScalar());
                    richTextBox1.Text += "取出員工表中最大的員工編號 : " + strID + "\n";
                }
                else
                {
                    richTextBox1.Text += "bbbbbbbbbbbbbbbbbb\n";
                }
            }
            con.Close();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增

            string id = "P1007";  // 員工編號
            string name = "mary";  // 員工姓名
            string money = "12345";  // 基本工資
            string description = "well done";  // 工作評價

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            con = new SqlConnection(cnstr);

            con.Open();

            // 查詢字串
            sqlstr = "INSERT INTO 員工表 " + "VALUES (@員工編號, @員工姓名,@基本工資,@工作評價)";

            using (SqlCommand command = new SqlCommand(sqlstr, con))
            {
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工編號", SqlDbType.VarChar, 50, "員工編號").Value = id;
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 50, "員工姓名").Value = name;
                command.Parameters.Add("@基本工資", SqlDbType.Float, 8, "基本工資").Value = Convert.ToString(money);
                command.Parameters.Add("@工作評價", SqlDbType.VarChar, 50, "工作評價").Value = description;
                command.ExecuteNonQuery();
                richTextBox1.Text += "OK\n";
            }

            con.Close();

            sqlstr = "SELECT * FROM 員工表";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //新增資料
            id = "P1008";  // 員工編號
            name = "mary";  // 員工姓名
            money = "12345";  // 基本工資
            description = "well done";  // 工作評價

            // 查詢字串
            sqlstr = "INSERT INTO 員工表(員工編號, 員工姓名,基本工資,工作評價) values('" + id + "','" + name + "','" + Convert.ToSingle(money) + "','" + description + "')";

            // 連接字串
            cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            con = new SqlConnection(cnstr);

            using (SqlCommand cmd = new SqlCommand(sqlstr, con))
            {
                con.Open();
                cmd.ExecuteNonQuery();
                richTextBox1.Text += "OK\n";
                con.Close();
            }

            sqlstr = "SELECT * FROM 員工表";
            sql_read_database(db_filename, sqlstr, dataGridView2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            string strid = "P1008";  // 員工編號
            richTextBox1.Text += "員工編號 : " + strid + "\n";
            //SqlCommand cmd = new SqlCommand("SELECT * FROM 員工表 WHERE 員工編號='" + strid + "'", con))

            richTextBox1.Text += "------------------------------\n";  // 30個
            /*
            richTextBox1.Text += "測試 UPDATE\n";
            richTextBox1.Text += "員工編號 : " + textBox1.Text + "\n";
            richTextBox1.Text += "員工姓名 : " + textBox2.Text + "\n";
            richTextBox1.Text += "基本工資 : " + textBox4.Text + "\n";
            richTextBox1.Text += "工作評價 : " + textBox5.Text + "\n";

            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    cmd.CommandText = "UPDATE 員工表 SET 員工姓名='" + this.textBox2.Text + "',基本工資='" + this.textBox4.Text + "',工作評價='" + this.textBox5.Text + "' WHERE 員工編號='" + this.textBox1.Text + "'";
                    con.Open();
                    cmd.Connection = con;
                    cmd.ExecuteNonQuery();
                    con.Close();
                }
                catch
                {

                }
            }
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //刪除資料
            /*
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                con.Open();
                SqlCommand cmd = new SqlCommand("DELETE FROM 員工表 WHERE 員工編號='" + str + "'", con);
                cmd.Connection = con;
                cmd.ExecuteNonQuery();
                con.Close();
                richTextBox1.Text += "刪除成功\n";
            }
            */
        }

        private void button14_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 14\n";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection con = new SqlConnection(cnstr);

            //新增

            string get_new_id = ID();//自定義方法，自動產生編號

            //保存

            //利用預儲程序登入數據

            string id = "P1006";  // 員工編號1
            string name = "mary";  // 員工姓名2
            string money = "12345";  // 基本工資4
            string description = "well done";  // 工作評價5

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
                    prams[0].Value = id;//設定參數值
                    prams[1].Value = name;
                    prams[2].Value = money;
                    prams[3].Value = description;
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
                    richTextBox1.Text += "訊息有誤！！！\n";
                    con.Close();
                    return;
                }
                int i = Convert.ToInt16(cmd.Parameters["@Return"].Value.ToString());//傳回影響的行數
                if (i == 1)
                {
                    richTextBox1.Text += "新增過程成功\n";
                }
                else if (i == -1)
                {
                    richTextBox1.Text += "新增過程失敗\n";
                }
            }
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
                richTextBox1.Text += "新增編號 : " + cmd.Parameters["@Id"].Value.ToString() + "\n";
                return cmd.Parameters["@Id"].Value.ToString();//傳回編號的值
            }
            catch (Exception ey)
            {
                richTextBox1.Text += ey.Message + "\n";
                return null;
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 15\n";


            string db_filename = "db_09_Data.mdf";
            /*
            textBox1.Text = "david";  // 員工姓名
            textBox2.Text = "12345";  // 基本工資
            textBox3.Text = "2000";  // 獎金
            textBox4.Text = "1000";  // 扣款
            textBox5.Text = "1500";  // 午餐
            textBox6.Text = "22222";  // 實際工資
            */
            //textBox1 員工姓名
            //textBox2 基本工資
            //textBox3 獎金
            //textBox4 扣款
            //textBox5 午餐
            //textBox6 實際工資

            //解析回資料庫
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                SqlCommand command = new SqlCommand("INSERT INTO 帳單 " + "VALUES (@員工姓名, @基本工資,@獎金,@扣款,@午餐,@實際工資)", con);
                // Add the parameters for the InsertCommand.
                command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 10, "員工姓名");
                command.Parameters.Add("@基本工資", SqlDbType.VarChar, 10, "基本工資");
                command.Parameters.Add("@獎金", SqlDbType.VarChar, 10, "獎金");
                command.Parameters.Add("@扣款", SqlDbType.VarChar, 10, "扣款");
                command.Parameters.Add("@午餐", SqlDbType.VarChar, 10, "午餐");
                command.Parameters.Add("@實際工資", SqlDbType.VarChar, 10, "實際工資");
                da.InsertCommand = command;
                richTextBox1.Text += "已成功能將訊息解析回資料庫\n";
            }

            // 看一下結果

            // 資料庫檔案
            db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 帳單";

            sql_read_database(db_filename, sqlstr, dataGridView1);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 16\n";

            //D:\db_09_Data.mdf

            //新增資料
            string pic_filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string file_no = "A123456";  // 檔案編號
            string work_no = "1234";  // 工號
            string name = "david";  // 姓名
            string birthday = "2006/03/11";  // 出生日期
            string city = "Taiwan";  // 籍貫
            string work_year = "5";  // 工齡
            string department = "研發部";  // 部門名稱
            string telephone = "0912345678";  // 電話
            string sex = "男";  // 性別
            string position = "員工";  // 技術職稱
            string marriage = "已婚";  // 婚姻狀態
            string health = "良好";  // 健康狀態

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);

            try
            {
                con.Open();

                // 查詢字串
                string sqlstr = "INSERT INTO 檔案訊息 values(@檔案編號,@工號,@姓名,@照片,@性別,@出生日期,@籍貫,@工齡,@電話,@部門名稱,@技術職稱,@婚姻狀態,@健康狀態)";

                SqlCommand cmd = new SqlCommand(sqlstr, con);
                cmd.Parameters.Add("@檔案編號", SqlDbType.Text).Value = file_no;
                cmd.Parameters.Add("@工號", SqlDbType.Text).Value = work_no;
                cmd.Parameters.Add("@姓名", SqlDbType.Text).Value = name;
                cmd.Parameters.Add("@照片", SqlDbType.Text).Value = pic_filename;
                cmd.Parameters.Add("@性別", SqlDbType.Text).Value = sex;
                cmd.Parameters.Add("@出生日期", SqlDbType.Text).Value = birthday;
                cmd.Parameters.Add("@籍貫", SqlDbType.Text).Value = city;
                cmd.Parameters.Add("@工齡", SqlDbType.Int).Value = Convert.ToInt16(work_year);
                cmd.Parameters.Add("@電話", SqlDbType.Text).Value = telephone;
                cmd.Parameters.Add("@部門名稱", SqlDbType.Text).Value = department;
                cmd.Parameters.Add("@技術職稱", SqlDbType.Text).Value = position;
                cmd.Parameters.Add("@婚姻狀態", SqlDbType.Text).Value = marriage;
                cmd.Parameters.Add("@健康狀態", SqlDbType.Text).Value = health;
                cmd.ExecuteNonQuery();
                con.Close();
                richTextBox1.Text += "新增成功\n";
            }
            catch (Exception ey)
            {
                richTextBox1.Text += "新增失敗\n";
            }

            /*
            //讀取全部

            // 資料庫檔案
            string db_filename = "db_09_Data.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM 檔案訊息";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            */
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 17\n";

            //更新資料範例
            //SqlDataAdapter da = new SqlDataAdapter("SELECT name FROM tb_power", con);

            string strValue = null;
            strValue += "1,";
            strValue += "1,";
            strValue += "1,";
            strValue += "1,";
            strValue += "1,";
            strValue += "1,";
            strValue += "1,";
            strValue += "1";

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";
            /*
            using (SqlConnection con = new SqlConnection(cnstr))
            {
                SqlCommand cmd = new SqlCommand("UPDATE tb_Power SET power='" + strValue + "' WHERE name='" + this.listBox1.Text + "' ", con);
                cmd.Connection = con;
                cmd.Connection.Open();
                cmd.ExecuteNonQuery();
                richTextBox1.Text += "授權成功！！！\n";
            }
            */
            richTextBox1.Text += "------------------------------\n";  // 30個

            //查詢範例

            string str = null;

            // 連接字串
            //string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";
            //richTextBox1.Text += "aaaaa : " + this.listBox1.Text + "\n";
            /*
            using (SqlConnection con = new SqlConnection(cnstr))//連接資料庫
            {
                SqlCommand cmd = new SqlCommand("SELECT power FROM tb_power WHERE name='" + this.listBox1.Text + "'", con);//連接SQL語句與數擾庫的連接
                cmd.Connection = con;
                cmd.Connection.Open();//打開資料庫的連接
                SqlDataReader dr = cmd.ExecuteReader();  // 建立數據讀取器
                if (dr.HasRows)//如果有記錄
                {
                    dr.Read();//讀取下一行
                    str = dr[0].ToString();//取得權限值
                    richTextBox1.Text += "取得權限值 = " + str + "\n";
                }
                dr.Close();//關閉
                con.Close();//關閉連接
                con.Dispose();
            }
            */
        }

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 18\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "SQL 19\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //show db

            //只是看一下db
            // 資料庫檔案
            string db_filename = "db_13.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_Rectangle";

            /*
            //sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "";

            sqlstr = "SELECT SUM(t_Num) FROM tb_Rectangle";
            sql_read_database(db_filename, sqlstr, dataGridView2);
            lb_dgv2.Text = "";

            sqlstr = "SELECT * FROM tb_Rectangle SELECT SUM(t_Num) FROM tb_Rectangle";
            sql_read_database(db_filename, sqlstr, dataGridView1);
            //lb_dgv3.Text = "";

            string sort_type = "ASC";  // 升冪
            sort_type = "DESC";  // 降冪
            //string sqlstr = "SELECT TOP 3 * FROM tb_Rectangle ORDER BY t_Num " + sort_type;
            */


            db_filename = "db_13.mdf";
            //sqlstr = "SELECT * FROM tb_lottery";
            sqlstr = "SELECT * FROM tb_curve";
            sql_read_database(db_filename, sqlstr, dataGridView1);


            sqlstr = "SELECT Years FROM tb_curve";
            sql_read_database(db_filename, sqlstr, dataGridView2);


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
//richTextBox1.Text += "---------------\n";  // 15個
//---------------  # 15個


/*  可搬出

 */

/*

//------------------------------------------------------------  # 60個

            // 資料庫檔案
            db_filename = "db_09_Data.MDF";
            // 查詢字串
            sqlstr = "SELECT name FROM sysdatabases ";  // 系統查詢資料庫名稱
            //sqlstr = "SELECT filename FROM sysdatabases ";  // 系統查詢資料庫檔案

            sql_read_database(db_filename, sqlstr, dataGridView1);

//------------------------------------------------------------  # 60個

//查看表格結構
            // 查詢字串
            //"SELECT name FROM sysobjects WHERE type = 'U' and name<>'dtproperties' "

            string strTableName = "table_name";
 
            string sqlstr = "SELECT name 字段名, xusertype 類型編號, length 長度 into hy_Linshibiao FROM syscolumns WHERE id=object_id('" + strTableName + "') ";
            sqlstr += "SELECT name 類型, xusertype 類型編號 into angel_Linshibiao FROM systypes WHERE xusertype in (SELECT xusertype FROM syscolumns WHERE id=object_id('" + strTableName + "'))";

            SqlDataAdapter da = new SqlDataAdapter("SELECT 字段名, 類型, 長度 FROM hy_Linshibiao t,angel_Linshibiao b WHERE t.類型編號=b.類型編號", con);
            DataTable dt = new DataTable();
            da.Fill(dt);
            this.dataGridView1.DataSource = dt.DefaultView;

            SqlCommand cmdnew = new SqlCommand("drop table hy_Linshibiao,angel_Linshibiao", con);
            con.Open();
            cmdnew.ExecuteNonQuery();
            con.Close();

//------------------------------------------------------------  # 60個
//------------------------------------------------------------  # 60個

            // 斷開服務

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_09_Data.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                try
                {
                    string strShutdown = "SHUTDOWN WITH NOWAIT";
                    SqlCommand cmd = new SqlCommand();
                    cmd.Connection = con;
                    cmd.Connection.Open();
                    cmd.CommandText = strShutdown;
                    cmd.ExecuteNonQuery();
                    richTextBox1.Text += "已成功斷開服務\n";
                }
                catch (Exception euy)
                {
                    richTextBox1.Text += euy.Message + "\n" ;
                }
            }

//------------------------------------------------------------  # 60個

            //枚举本地网络中的SQL Server所有可用实例
            SqlDataSourceEnumerator instance = SqlDataSourceEnumerator.Instance;
            DataTable table = instance.GetDataSources();//获取所有数据源，并存储到DataTable中
            richTextBox1.Text += table + "\n";
            foreach (DataRow row in table.Rows)//遍历获取到的数据源
            {
                richTextBox1.Text += row + "\n";
                richTextBox1.Text += row["ServerName"] + "\n";
            }

//------------------------------------------------------------  # 60個

            // 資料庫檔案
            string db_filename = "db_TomeTwo.MDF";
            // 查詢字串
            string sqlstr =
    @"SELECT 学生姓名,性别,家庭住址 FROM tb_Student
union
SELECT 学生姓名,convert(varchar,年龄),家庭住址 FROM tb_Student
union
SELECT 学生姓名,convert(varchar,出生年月),家庭住址 FROM tb_Student
union
SELECT 学生姓名,所在学院,家庭住址 FROM tb_Student";

            sql_read_database(db_filename, sqlstr, dataGridView1);

//------------------------------------------------------------  # 60個

*/

