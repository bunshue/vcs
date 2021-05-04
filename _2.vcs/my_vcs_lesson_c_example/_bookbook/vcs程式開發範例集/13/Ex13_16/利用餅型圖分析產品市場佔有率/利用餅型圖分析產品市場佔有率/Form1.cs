using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;
using System.Collections;
namespace 利用餅型圖分析產品市場佔有率
{
    public partial class Form1 : Form
    {
        static int SumNum;
        static float TimeNum;
        SqlConnection con;
        SqlCommand cmd;
        Hashtable ht = new Hashtable();
        public Form1()
        {
            InitializeComponent();
        }
        private void Conn()
        {
            con = new SqlConnection("server=.;uid=sa;pwd=;database=db_13");
            con.Open();
        }

        private void showPic(float f,Brush B)
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
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            ht.Clear();
            Conn();
            Random rnd = new Random();
            using (cmd = new SqlCommand("select t_Name,sum(t_Num) as Num  from tb_product group by t_Name", con))
            {
                Graphics g2 = this.panel2.CreateGraphics();
                SqlDataReader dr = cmd.ExecuteReader();
                while (dr.Read())
                {
                    ht.Add(dr[0],Convert.ToInt32(dr[1]));
                }
                float[] flo = new float[ht.Count];
                int T = 0;
                foreach (DictionaryEntry de in ht)
                {
                    flo[T] = Convert.ToSingle((Convert.ToDouble(de.Value) / SumNum).ToString().Substring(0, 6));
                    Brush Bru = new SolidBrush(Color.FromArgb(rnd.Next(255), rnd.Next(255), rnd.Next(255)));
                    g2.DrawString(de.Key + "        " + flo[T] * 100 + "%", new Font("Arial", 8, FontStyle.Regular), Bru, 7, 5 + T * 18);
                    showPic(flo[T], Bru);
                    T++;
                }  
            }
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            Conn();
            using (cmd = new SqlCommand("select Sum(t_Num)  from tb_product", con))
            {
               SumNum=Convert.ToInt32(cmd.ExecuteScalar());
            }
        }
    }
}