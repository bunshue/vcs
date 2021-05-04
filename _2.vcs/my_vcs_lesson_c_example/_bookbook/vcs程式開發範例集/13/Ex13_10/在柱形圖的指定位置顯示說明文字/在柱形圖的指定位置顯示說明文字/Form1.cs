using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging;
using System.Data.SqlClient;
namespace 在柱形圖的指定位置顯示說明文字
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection con;
        SqlCommand cmd;
        private void button1_Click(object sender, EventArgs e)
        {

        }
          private void Conn()
        {
            con = new SqlConnection("server=.;uid=sa;pwd=;database=db_13");
            con.Open();
        }
          private void ShowPic()
          {
              Conn();
              using (cmd = new SqlCommand("SELECT TOP 3 * FROM tb_Rectangle order by t_Num desc", con))
              {
                  SqlDataReader dr = cmd.ExecuteReader();

                  Bitmap bitM = new Bitmap(this.panel1.Width, this.panel1.Height);
                  Graphics g = Graphics.FromImage(bitM);
                  Pen p = new Pen(new SolidBrush(Color.SlateGray), 1.0f);
                  p.DashStyle= System.Drawing.Drawing2D.DashStyle.Dash;
                  g.Clear(Color.White);
                  for (int i = 0; i < 5; i++)
                  {
                      g.DrawLine(p, 50, this.panel1.Height - 20 - i * 20, this.panel1.Width - 40, this.panel1.Height - 20 - i * 20);
                      g.DrawString(Convert.ToString(i * 100), new Font("Times New Roman", 10, FontStyle.Regular), new SolidBrush(Color.Black), 20, this.panel1.Height - 27 - i * 20);
                  }

                  for (int j = 0; j < 4; j++)
                  {
                      g.DrawLine(p, 50 , this.panel1.Height - 20, 50, 20);
                      if (dr.Read())
                      {
                          int x, y, w, h;
                          g.DrawString(dr[0].ToString(), new Font("細明體", 9, FontStyle.Regular), new SolidBrush(Color.Black), 76 + 40 * j, this.panel1.Height - 16);
                          x = 78 + 40 * j;
                          y = this.panel1.Height - 20 - Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100)));
                          w = 24;
                          h = Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100);
                          g.FillRectangle(new SolidBrush(Color.SlateGray), x, y, w, h);
                          g.DrawString((h*100/20).ToString(), new Font("細明體", 8,FontStyle.Bold), new SolidBrush(Color.Tomato), new Point(x+4,y-10));
                      }

                  }
                  this.panel1.BackgroundImage = bitM;
              }
          }

        private void button1_Click_1(object sender, EventArgs e)
        {
             ShowPic();
        }
    }
}
