using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;
using System.Data.SqlClient;

namespace 利用圖表分析彩票中獎情況
{
    public partial class Form1 : Form
    {
        SqlConnection con;
        SqlCommand cmd;
        SqlDataAdapter da;
        DataSet ds;
        public Form1()
        {
            InitializeComponent();
        }

        private void Conn()
        {
            con = new SqlConnection("server=.;uid=sa;pwd=;database=db_13");
            con.Open();
        }
      
        private void button1_Click(object sender, EventArgs e)
        {
            string str = "select * from tb_lottery where t_year between '" + Convert.ToDateTime(this.dateTimePicker1.Text).ToShortDateString() + "' and '" + Convert.ToDateTime(this.dateTimePicker2.Text).ToShortDateString() + "' order by t_year";
            DrowInfo(str);

        }

        private void DrowInfo(string SQL)
        {
            try
            {
                System.Drawing.Bitmap bmp = new Bitmap(this.panel1.Width, this.panel1.Height);
                Graphics g = Graphics.FromImage(bmp);
                g.Clear(Color.White);
                Brush bru = new SolidBrush(Color.Blue);
                Pen p = new Pen(bru);
                Font font = new Font("Arial", 9, FontStyle.Bold);
                Conn();
                cmd = new SqlCommand(SQL, con);
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


                Bitmap bmpP = new Bitmap(this.panel3.Width, this.panel3.Height);

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
                    P[j].Y = this.panel3.Height - 20 - Convert.ToInt32(ICount[j] / f * (this.panel3.Height + 20));
                }
                f = 0.0f;
                str = null;
                gP.DrawLines(new Pen(new SolidBrush(Color.Red)), P);

                gP.DrawString("分析結果走勢圖", new Font("細明體", 16), bru, this.panel3.Width / 2 - 80, 10);
                this.panel3.BackgroundImage = bmpP;
            }
            catch
            {
                MessageBox.Show("此範圍內沒有任何訊息！！！");
                return;
            }
        
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }
    }
}