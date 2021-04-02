using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;
namespace 多曲線數據分析
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_13"))
            {
                SqlDataAdapter da = new SqlDataAdapter("select Years from tb_curve", con);
                DataTable dt = new DataTable();
                da.Fill(dt);
                this.comboBox1.DataSource = dt.DefaultView;
                this.comboBox1.DisplayMember = "Years";
                this.comboBox1.ValueMember = "Years";

            }
        }
        private void CreateImage(int ID)
        {
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
                SqlConnection Con = new SqlConnection("server=.;pwd=;uid=sa;database=db_13");
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
            {}
        }

        private void button1_Click(object sender, EventArgs e)
        {          
            this.CreateImage(Convert.ToInt32(this.comboBox1.Text));
        }
     
    }
}