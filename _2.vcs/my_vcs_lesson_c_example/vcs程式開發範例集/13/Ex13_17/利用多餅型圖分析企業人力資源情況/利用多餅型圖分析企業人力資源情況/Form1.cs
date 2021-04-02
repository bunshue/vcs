using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;
namespace 利用多餅型圖分析企業人力資源情況
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_13");
        SqlCommand cmd;
        static int ConutNum = 0;
        static float floatNum=0.0f;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (cmd = new SqlCommand("select sum(t_Num) from tb_manpower ", con))
            {
                con.Open();
                int Sum = Convert.ToInt32(cmd.ExecuteScalar());
                con.Close();
                ShowPic(Sum);
            }
        }

        private void ShowPic(int Sum)
        {
            using (cmd = new SqlCommand("select t_Point,sum(t_Num) from tb_manpower group by t_Point order by sum(t_Num) desc", con))
            {
                Bitmap bmp = new Bitmap(this.panel1.Width, this.panel1.Height);
                Graphics g = Graphics.FromImage(bmp);
                cmd.Connection.Open();
                SqlDataReader dr=cmd.ExecuteReader();
                while (dr.Read())
                {
                    float f =Convert.ToSingle(dr[1]) / Sum;
                    string str = dr[0].ToString();
                    drowPic(g, f,str);
                }
                g.DrawLine(new Pen(Color.Black), 0, this.panel1.Height / 2, this.panel1.Width, this.panel1.Height / 2);
                g.DrawLine(new Pen(Color.Black), this.panel1.Width / 2, 0, this.panel1.Width / 2, this.panel1.Height);
                this.panel1.BackgroundImage = bmp;
                dr.Close();
                con.Close();
            }
        }

        private void drowPic(Graphics g, float f,string str)
        {
            if (ConutNum == 0)
            {
                g.FillPie(new SolidBrush(Color.Black), 0, 0, (this.panel1.Width) / 2, (this.panel1.Height - 10) / 2, 0, 360 * f);
                g.DrawString(str, new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Black), (this.panel1.Width) / 2-70, 10);
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
                g.FillPie(new SolidBrush(Color.Red), 0, (this.panel1.Height - 10) / 2+10, (this.panel1.Width) / 2, (this.panel1.Height - 10) / 2, floatNum, 360 * f);
                g.DrawString(str, new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Red), 10, (this.panel1.Height - 10) / 2+20);
                g.DrawString(Convert.ToString(f * 100).Substring(0, 5) + "%", new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Red), 10, (this.panel1.Height - 10) / 2 + 35);
                floatNum += 360 * f;
                ConutNum += 1;
            }
            else if (ConutNum == 3)
            {
                g.FillPie(new SolidBrush(Color.Blue), (this.panel1.Width) / 2-10, (this.panel1.Height - 10) / 2+10, (this.panel1.Width) / 2, (this.panel1.Height - 10) / 2, floatNum, 360 * f);
                g.DrawString(str, new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Blue), (this.panel1.Width) / 2 + 10, (this.panel1.Height - 10) / 2 + 20);
                g.DrawString(Convert.ToString(f * 100).Substring(0, 5) + "%", new Font("細明體", 10, FontStyle.Bold), new SolidBrush(Color.Blue), (this.panel1.Width) / 2 + 10, (this.panel1.Height - 10) / 2 + 35);
            }
        }

    }
}