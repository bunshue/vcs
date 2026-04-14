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

        //對排序數據進行分析 ST

        SqlConnection con;
        SqlCommand cmd;

        private void Conn()
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            con = new SqlConnection(cnstr);
            con.Open();
        }

        private void ShowPic(string str)
        {
            Conn();
            using (cmd = new SqlCommand("SELECT TOP 3 * FROM tb_Rectangle order by t_Num " + str, con))
            {
                SqlDataReader dr = cmd.ExecuteReader();

                Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
                Graphics g = Graphics.FromImage(bitM);
                g.Clear(Color.White);
                for (int i = 0; i < 5; i++)
                {
                    g.DrawLine(new Pen(new SolidBrush(Color.Red), 2.0f), 50, this.panel1.Height - 20 - i * 20, this.panel1.Width - 40, this.panel1.Height - 20 - i * 20);
                    g.DrawString(Convert.ToString(i * 100), new Font("Times New Roman", 10, FontStyle.Regular), new SolidBrush(Color.Black), 20, this.panel1.Height - 27 - i * 20);
                }

                for (int j = 0; j < 4; j++)
                {
                    g.DrawLine(new Pen(new SolidBrush(Color.Red), 1.0f), 50 + 40 * j, this.panel1.Height - 20, 50 + 40 * j, 50);
                    if (dr.Read())
                    {
                        int x, y, w, h;
                        g.DrawString(dr[0].ToString(), new Font("宋本", 8, FontStyle.Regular), new SolidBrush(Color.Black), 76 + 40 * j, this.panel1.Height - 16);
                        x = 78 + 40 * j;
                        y = this.panel1.Height - 20 - Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100)));
                        w = 24;
                        h = Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100);
                        g.FillRectangle(new SolidBrush(Color.FromArgb(56, 129, 78)), x, y, w, h);
                    }

                }
                if (str == "desc")
                {
                    g.DrawString("熱賣前三名", new Font("細明體", 9), new SolidBrush(Color.Red), this.panel1.Width / 2 - 26, 20);
                }
                else if (str == "asc")
                {
                    g.DrawString("熱賣後三名", new Font("細明體", 9), new SolidBrush(Color.Red), this.panel1.Width / 2 - 26, 20);
                }
                this.panel1.BackgroundImage = bitM;
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //對排序數據進行分析 升冪
            ShowPic("asc");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //對排序數據進行分析 降冪
            ShowPic("desc");
        }

        //對排序數據進行分析 SP

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //利用控制元件完成柱形圖分析

            //水果出售情況統計表

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                int XValse = 20;
                DataSet ds = new DataSet();
                SqlCommand cmd = new SqlCommand("select * from tb_Rectangle select Sum(t_Num) from tb_Rectangle", con);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = cmd;
                da.Fill(ds);
                Panel[] p = new Panel[ds.Tables[0].Rows.Count];
                int Values = Convert.ToInt32(ds.Tables[1].Rows[0][0].ToString());
                for (int i = 0; i < ds.Tables[0].Rows.Count; i++)
                {
                    ds.Tables[0].Rows[i][0].ToString();
                    float f = Convert.ToInt32(ds.Tables[0].Rows[i][1].ToString());
                    Size s = new Size();
                    s.Width = 30;
                    s.Height = Convert.ToInt32(f / Values * 200);

                    Point pint = new Point();
                    pint.X = XValse;
                    pint.Y = this.Height - 50 - s.Height;
                    p[i] = new Panel();
                    p[i].Location = pint;
                    p[i].BackColor = Color.Red;
                    p[i].Size = s;
                    XValse += 40;
                    Label lbl = new Label();
                    lbl.Text = ds.Tables[0].Rows[i][0].ToString();
                    lbl.Font = new Font("細明體", 9, FontStyle.Regular);
                    lbl.ForeColor = Color.White;
                    p[i].Controls.Add(lbl);
                    this.Controls.Add(p[i]);
                }
            }
        }

        //------------------------------------------------------------  # 60個

        //SqlConnection con;
        //SqlCommand cmd;

        private void Conn2()
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            con = new SqlConnection(cnstr);
            con.Open();
        }

        private void ShowPic2()
        {
            Conn2();
            using (cmd = new SqlCommand("SELECT TOP 3 * FROM tb_Rectangle order by t_Num desc", con))
            {
                SqlDataReader dr = cmd.ExecuteReader();

                Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
                Graphics g = Graphics.FromImage(bitM);
                Pen p = new Pen(new SolidBrush(Color.SlateGray), 1.0f);
                p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
                g.Clear(Color.White);
                for (int i = 0; i < 5; i++)
                {
                    g.DrawLine(p, 50, this.panel1.Height - 20 - i * 20, this.panel1.Width - 40, this.panel1.Height - 20 - i * 20);
                    g.DrawString(Convert.ToString(i * 100), new Font("Times New Roman", 10, FontStyle.Regular), new SolidBrush(Color.Black), 20, this.panel1.Height - 27 - i * 20);
                }

                for (int j = 0; j < 4; j++)
                {
                    g.DrawLine(p, 50, this.panel1.Height - 20, 50, 20);
                    if (dr.Read())
                    {
                        int x, y, w, h;
                        g.DrawString(dr[0].ToString(), new Font("細明體", 9, FontStyle.Regular), new SolidBrush(Color.Black), 76 + 40 * j, this.panel1.Height - 16);
                        x = 78 + 40 * j;
                        y = this.panel1.Height - 20 - Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100)));
                        w = 24;
                        h = Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100);
                        g.FillRectangle(new SolidBrush(Color.SlateGray), x, y, w, h);
                        g.DrawString((h * 100 / 20).ToString(), new Font("細明體", 8, FontStyle.Bold), new SolidBrush(Color.Tomato), new Point(x + 4, y - 10));
                    }

                }
                this.panel1.BackgroundImage = bitM;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //在柱形圖的指定位置顯示說明文字
            //商品分析
            ShowPic2();
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

            SqlConnection con;
            SqlCommand cmd;
            SqlDataAdapter da;
            DataSet ds;

            //t_year 在 2005/4/1 ~ 2006/10/1 有資料

            string time_st = "2005/8/15";
            string time_sp = "2006/4/15";

            string sqlstr = "SELECT * FROM tb_lottery WHERE t_year BETWEEN '" + time_st + "' AND '" + time_sp + "' ORDER BY t_year";

            try
            {
                System.Drawing.Bitmap bmp = new Bitmap(this.panel1.Width, this.panel1.Height);
                Graphics g = Graphics.FromImage(bmp);
                g.Clear(Color.White);
                Brush bru = new SolidBrush(Color.Blue);
                Pen p = new Pen(bru);
                Font font = new Font("Arial", 9, FontStyle.Bold);

                // 連接字串
                string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
                con = new SqlConnection(cnstr);
                con.Open();

                cmd = new SqlCommand(sqlstr, con);
                SqlDataReader dr = cmd.ExecuteReader();
                int i = 0;
                Pen pLine = new Pen(Color.Orange, 4.0f);
                string str = null;
                float f = 0.0f;
                while (dr.Read())
                {
                    i++;
                    g.DrawString(dr[0].ToString().Substring(0, 7) + "月---", font, bru, 10, 15.0f * i);
                    g.DrawString(dr[1].ToString(), font, bru, this.panel1.Width - 50, 15.0f * i);
                    str += dr[1].ToString() + "#";
                    f += Convert.ToSingle(dr[1].ToString());
                }
                dr.Close();
                this.panel1.BackgroundImage = bmp;

                Bitmap bmpP = new Bitmap(this.panel1.Width, this.panel1.Height);

                Graphics gP = Graphics.FromImage(bmpP);
                gP.Clear(Color.White);
                Brush bruImg = new SolidBrush(Color.Orange);
                Pen Pg = new Pen(bruImg, 1.0f);
                string[] strCount = str.Split('#');
                int[] ICount = new int[strCount.Length];
                for (int l = 0; l < strCount.Length - 1; l++)
                {
                    ICount[l] = Convert.ToInt32(strCount[l]);
                }

                Point[] P = new Point[ICount.Length - 1];
                for (int j = 0; j < ICount.Length - 1; j++)
                {
                    P[j].X = 35 + 28 * j;
                    P[j].Y = this.panel1.Height - 20 - Convert.ToInt32(ICount[j] / f * (this.panel1.Height + 20));
                }
                f = 0.0f;
                str = null;
                gP.DrawLines(new Pen(new SolidBrush(Color.Red)), P);

                gP.DrawString("分析結果走勢圖", new Font("細明體", 16), bru, this.panel1.Width / 2 - 80, 10);
                this.panel1.BackgroundImage = bmpP;
            }
            catch
            {
                MessageBox.Show("此範圍內沒有任何訊息！！！");
                return;
            }

        }

        //------------------------------------------------------------  # 60個

        private void CreateImage(int ID)
        {
            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            int height = 440, width = 600;
            System.Drawing.Bitmap image = new System.Drawing.Bitmap(width, height);
            Graphics g = Graphics.FromImage(image);

            try
            {
                //清空圖片背景色
                g.Clear(Color.White);

                Font font = new System.Drawing.Font("Arial", 9, FontStyle.Regular);
                Font font1 = new System.Drawing.Font("細明體", 12, FontStyle.Regular);
                Font font2 = new System.Drawing.Font("Arial", 8, FontStyle.Regular);

                System.Drawing.Drawing2D.LinearGradientBrush brush = new System.Drawing.Drawing2D.LinearGradientBrush(new Rectangle(0, 0, image.Width, image.Height), Color.Blue, Color.Blue, 1.2f, true);
                g.FillRectangle(Brushes.AliceBlue, 0, 0, width, height);
                Brush brush1 = new SolidBrush(Color.Blue);
                Brush brush2 = new SolidBrush(Color.SaddleBrown);

                string str = "SELECT * FROM tb_curve WHERE Years=" + ID + "";
                SqlConnection Con = new SqlConnection(cnstr);
                Con.Open();
                SqlCommand Com = new SqlCommand(str, Con);
                SqlDataReader dr = Com.ExecuteReader();
                dr.Read();
                if (dr.HasRows)
                {
                    g.DrawString("" + ID + "年公司內部人員統計表", font1, brush1, new PointF(160, 30));
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
                String[] n = {"  一月", "  二月", "  三月", "  四月", "  五月", "  六月", "  七月",
                     "  八月", "  九月", "  十月", "十一月", "十二月"};
                x = 35;
                for (int i = 0; i < 12; i++)
                {
                    g.DrawString(n[i].ToString(), font, Brushes.Red, x, 348); //設定文字內容及輸出位置
                    x = x + 40;
                }

                //y軸
                String[] m = {"900人", " 800人", " 700人", "600人", " 500人", " 400人", " 300人", " 200人",
                     " 100人"};
                y = 100;
                for (int i = 0; i < 9; i++)
                {
                    g.DrawString(m[i].ToString(), font, Brushes.Red, 10, y); //設定文字內容及輸出位置
                    y = y + 26;
                }

                int[] Count1 = new int[12];
                int[] Count2 = new int[12];
                string[] NumChr = new string[12];
                string cmdtxt2 = "SELECT * FROM tb_curve WHERE Years=" + ID + "";
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
            catch
            { }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //多曲線數據分析

            //取得年分

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";

            using (SqlConnection con = new SqlConnection(cnstr))
            {
                SqlDataAdapter da = new SqlDataAdapter("select Years from tb_curve", con);
                DataTable dt = new DataTable();
                da.Fill(dt);
                this.comboBox1.DataSource = dt.DefaultView;
                this.comboBox1.DisplayMember = "Years";
                this.comboBox1.ValueMember = "Years";
            }

            //分析

            this.CreateImage(Convert.ToInt32(this.comboBox1.Text));
        }

        //------------------------------------------------------------  # 60個

        private void draw_picture()
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
            Font fontO = new System.Drawing.Font("Arial", 9, FontStyle.Regular);
            Font fontT = new System.Drawing.Font("華文新魏", 16, FontStyle.Regular);
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
            String[] n = {" 1月", " 2月", " 3月", " 4月", " 5月", " 6月", " 7月",
                     " 8月", " 9月", "10月", "11月", "12月"};
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
            String[] m = {"5500","5000","4500", "4000", "3500", "3000", "2500", "2000", "1500", "1000",
                     "  500"};
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

        private void button7_Click(object sender, EventArgs e)
        {
            //網站人氣指數曲線分析

            draw_picture();
        }

        //------------------------------------------------------------  # 60個

        private void ShowPic3(string SexCode, float f)
        {
            Graphics g = this.panel1.CreateGraphics();
            Pen p = new Pen(new SolidBrush(Color.Blue));
            Point p1 = new Point(0, 0);
            Size s = new Size(this.panel1.Width, this.panel1.Height);
            Rectangle trct = new Rectangle(p1, s);
            g.FillEllipse(new SolidBrush(Color.Red), trct);
            g.FillPie(new SolidBrush(Color.Blue), trct, 180, f * 360);
            Graphics ginfo = this.pictureBox1.CreateGraphics();
            Font font = new Font("細明體", 10, FontStyle.Regular);
            ginfo.DrawString(SexCode + " " + f.ToString().Substring(0, 4), font, new SolidBrush(Color.Blue), 0, 5);
            ginfo.DrawString("女" + " " + (1.0 - Convert.ToDouble(f.ToString().Substring(0, 4))).ToString().Substring(0, 4), font, new SolidBrush(Color.Red), 0, 25);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //利用餅型圖分析公司男女比率

            SqlConnection con;
            SqlCommand cmd;

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            con = new SqlConnection(cnstr);
            con.Open();

            using (cmd = new SqlCommand("SELECT sex,COUNT(sex) num FROM tb_sex group by sex", con))
            {
                SqlDataReader dr = cmd.ExecuteReader();
                string[] str = new string[2];
                int i = 0;
                while (dr.Read())
                {
                    str[i] = dr[0].ToString() + "," + dr[1].ToString();
                    i++;
                }
                float N = Convert.ToInt16(str[0].Substring(2)) + Convert.ToInt16(str[1].Substring(2));
                float f = Convert.ToInt16(str[0].Substring(2)) / N;
                ShowPic3(str[0].Substring(0, 1), f);
            }
        }

        //6060

        static int SumNum;
        static float TimeNum;
        //SqlConnection con;
        //SqlCommand cmd;
        Hashtable ht = new Hashtable();

        private void showPic4(float f, Brush B)
        {
            Graphics g = this.panel1.CreateGraphics();
            if (TimeNum == 0.0f)
            {
                g.FillPie(B, 0, 0, this.panel1.Width, this.panel1.Height, 0, f * 360);
            }
            else
            {
                g.FillPie(B, 0, 0, this.panel1.Width, this.panel1.Height, TimeNum, f * 360);
            }
            TimeNum += f * 360;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //利用餅型圖分析產品市場佔有率

            ht.Clear();

            // 連接字串
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_13.mdf;Integrated Security=True;Connect Timeout=30";
            con = new SqlConnection(cnstr);
            con.Open();

            using (cmd = new SqlCommand("select Sum(t_Num)  from tb_product", con))
            {
                SumNum = Convert.ToInt32(cmd.ExecuteScalar());
            }

            Random rnd = new Random();
            using (cmd = new SqlCommand("select t_Name,sum(t_Num) as Num  from tb_product group by t_Name", con))
            {
                Graphics g2 = this.pictureBox1.CreateGraphics();
                SqlDataReader dr = cmd.ExecuteReader();
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
                    showPic4(flo[T], Bru);
                    T++;
                }
            }
        }

        //6060

        private void ShowPic5(int Sum)
        {
            using (cmd = new SqlCommand("select t_Point,sum(t_Num) from tb_manpower group by t_Point order by sum(t_Num) desc", con))
            {
                Bitmap bmp = new Bitmap(this.panel1.Width, this.panel1.Height);
                Graphics g = Graphics.FromImage(bmp);
                cmd.Connection.Open();
                SqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
                {
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

        private void draw_sub_picture(Graphics g, float f, string str)
        {
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

        //SqlConnection con;
        //SqlCommand cmd;
        static int ConutNum = 0;
        static float floatNum = 0.0f;

        private void button10_Click(object sender, EventArgs e)
        {
            //利用多餅型圖分析企業人力資源情況

            con = new SqlConnection(cnstr);

            using (cmd = new SqlCommand("select sum(t_Num) from tb_manpower ", con))
            {
                con.Open();
                int Sum = Convert.ToInt32(cmd.ExecuteScalar());
                con.Close();
                ShowPic5(Sum);
            }

        }

        //6060


        private void button11_Click(object sender, EventArgs e)
        {
            //製作一個可以旋轉的餅型圖
            //D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\vcs程式開發範例集\13\Ex13_18\製作一個可以旋轉的餅型圖\製作一個可以旋轉的餅型圖
        }

        //6060


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

        private void button20_Click(object sender, EventArgs e)
        {
            //只是看一下db
            // 資料庫檔案
            string db_filename = "db_13.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM tb_lottery";

            sql_read_database(db_filename, sqlstr, dataGridView1);
            lb_dgv1.Text = "全部資料 tb_Employee";
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

