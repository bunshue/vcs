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
namespace 繪製柱形圖
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
                  g.Clear(Color.White);
                  for (int j = 0; j < 4; j++)
                  {
                      if (dr.Read())
                      {
                          int x, y, w, h;
                          g.DrawString(dr[0].ToString(), new Font("細明體", 8, FontStyle.Regular), new SolidBrush(Color.Black), 76 + 40 * j, this.panel1.Height - 16);
                          x = 78 + 40 * j;
                          y = this.panel1.Height - 20 - Convert.ToInt32((Convert.ToDouble(Convert.ToDouble(dr[1].ToString()) * 20 / 100)));
                          w = 24;
                          h = Convert.ToInt32(Convert.ToDouble(dr[1].ToString()) * 20 / 100);
                          g.FillRectangle(new SolidBrush(Color.FromArgb(56, 129, 78)), x, y, w, h);
                      }
                  }
                  this.panel1.BackgroundImage = bitM;
              }
          }
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click_1(object sender, EventArgs e)
        {
             ShowPic();
        }
    }
}
