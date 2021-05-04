using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;


using System.Drawing.Imaging;
using System.Data.SqlClient;
namespace 對排序數據進行分析
{
    public partial class Form1 : Form
    {
        SqlConnection con;
        SqlCommand cmd;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }
        private void Conn()
        {
            con = new SqlConnection("server=.;uid=sa;pwd=;database=db_13");
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

        private void button1_Click(object sender, EventArgs e)
        {
            ShowPic("asc");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ShowPic("desc");
        }

    }
}
