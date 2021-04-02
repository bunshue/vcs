using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace 製作一個可以旋轉的餅型圖
{
    public partial class Form1 : Form
    {
        public class PyPanel : Panel
        {
            public PyPanel()
            {
                SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint, true);
                UpdateStyles();
            }
        }
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection con;
        SqlCommand cmd;
        
        private void Conn()
        {
            con = new SqlConnection("server=.;uid=sa;pwd=;database=db_13");
            con.Open();
        }

        Bitmap bt;
        Bitmap bt1;
        int flag = 0;
        PyPanel panel1 = new PyPanel();
        private void ShowPic(string SexCode, float f)
        {
            this.Controls.Add(panel1);
            panel1.Width = 230;
            panel1.Height = 230;
            bt = new Bitmap(panel1.Width,panel1.Height);
            Graphics g = Graphics.FromImage(bt);
            Pen p = new Pen(new SolidBrush(Color.Blue));
            Point p1 = new Point(0, 0);
            Size s = new Size(this.panel1.Width, this.panel1.Height);
            Rectangle trct = new Rectangle(p1, s);
            g.FillEllipse(new SolidBrush(Color.Red), trct);
            g.FillPie(new SolidBrush(Color.Blue), trct, flag, f * 360);
            bt1 = new Bitmap(panel2.Width,panel2.Height);
            Graphics ginfo = Graphics.FromImage(bt1);
            Font font = new Font("細明體", 10, FontStyle.Regular);
            ginfo.DrawString(SexCode + " " + f.ToString().Substring(0, 4), font, new SolidBrush(Color.Blue), 0, 5);
            ginfo.DrawString("女" + " " + (1.0 - Convert.ToDouble(f.ToString().Substring(0, 4))).ToString().Substring(0, 4), font, new SolidBrush(Color.Red), 0, 25);
            panel1.BackgroundImage = bt;
            panel2.BackgroundImage = bt1;
        }
        private void Form1_Load(object sender, EventArgs e)
        {
 
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Conn();
            using (cmd = new SqlCommand("SELECT sex,COUNT(sex) num FROM tb_employee group by sex", con))
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
                flag = 180;
                ShowPic(str[0].Substring(0, 1), f);
            }
            con.Close();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            flag += 1;
            Conn();
            using (cmd = new SqlCommand("SELECT sex,COUNT(sex) num FROM tb_employee group by sex", con))
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
                ShowPic(str[0].Substring(0, 1), f);
            }
            con.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (button2.Text =="旋轉")
            {
                timer1.Start();
                button2.Text = "停止";
            }
            else
            {
                timer1.Stop();
                button2.Text = "旋轉";
            }
        }
    }
}
