using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace 網站人氣指數曲線分析
{
    public partial class Form1 : Form
    {
        static int i = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            i += 1;
        }
        private void drowPic()
        {
            //清空圖片背景色
            Graphics g = this.CreateGraphics();
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
            SqlConnection Con = new SqlConnection("Server=(local);DataBase=db_13;Uid=sa;Pwd=");
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
      
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (i != 0)
                drowPic();
        }
    }
}