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

namespace 利用圖表分析產品銷售走勢
{
    public partial class Form1 : Form
    {
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_13");
        SqlDataAdapter sqlAda;
        SqlCommand cmd;
        DataSet ds;
        static int G = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            G++;
            DrowFont(this.comboBox1.Text.ToString());
            DrowInfo(this.comboBox1.Text.ToString());
            DrowPic(this.comboBox1.Text.ToString());
        }

        private void DrowPic(string str)
        {
            int MaxValue, MinValue;
            using (cmd = new SqlCommand("select Max(t_price) from tb_merchandise where t_name='" + str + "'", con))
            {
                con.Open();
                MaxValue = Convert.ToInt16(cmd.ExecuteScalar());
                con.Close();
            }

            using (cmd = new SqlCommand("select Min(t_price) from tb_merchandise where t_name='" + str + "'", con))
            {
                con.Open();
                MinValue = Convert.ToInt16(cmd.ExecuteScalar());
                con.Close();
            }
            Graphics g = this.groupBox1.CreateGraphics();
            g.Clear(Color.SeaShell);
            Brush b = new SolidBrush(Color.Blue);
            Font f = new Font("Arial", 9, FontStyle.Regular);
            Pen p=new Pen(b);
            using (sqlAda = new SqlDataAdapter("select * from tb_merchandise where t_name='" + str + "' order by t_date", con))
            {
                ds = new DataSet();
                sqlAda.Fill(ds,"t_date");
                int M = MaxValue / 50+1;//最大值
                int N = MinValue / 50;//最小值
                int T = N;
               for(int i=0;i<=M-N;i++)
               {
                   g.DrawString(Convert.ToString(T * 50), f, b,0, 190 - 30 * i);
                   g.DrawLine(p, 30, 200 - 30 * i, 260, 200 -30 * i);
                   T++;
               }

               int Num = ds.Tables[0].Rows.Count;
               int[] Values = new int[Num];
               for (int C = 0; C <Num; C++)
               {
                   Values[C] =Convert.ToInt32(ds.Tables[0].Rows[C][3].ToString());
                   g.DrawString(Convert.ToDateTime(ds.Tables[0].Rows[C][2].ToString()).Month + "月", f, b, 30 * (C + 1)-10, 15);
                   g.DrawLine(p, 30*(C+1), 200, 30*(C+1), 30); 
               }

               Point[] P = new Point[Num];
               for (int i = 0; i < Num; i++)
               {
                   P[i].X=30*(i+1);
                   P[i].Y = 290 - Convert.ToInt32(Values[i] / 50f* 30);
               }
               g.DrawLines(p, P);
             
            }
        }
        private void DrowInfo(string str)
        {
            Graphics g = this.groupBox2.CreateGraphics();
            g.Clear(Color.SeaShell);
            Brush b=new SolidBrush(Color.Blue);
            Font f=new Font("Arial", 9, FontStyle.Regular);

            using (sqlAda = new SqlDataAdapter("select * from tb_merchandise where t_name='" + str + "' order by t_date", con))
            {
                DataSet ds = new DataSet();
                sqlAda.Fill(ds, "tb_merchandise");
                g.DrawString( "月份：       " + "價格", f, b, 10.0f,  25.0f);
                for (int i = 0; i < ds.Tables[0].Rows.Count; i++)
                {
                    int month=Convert.ToDateTime(ds.Tables[0].Rows[i][2].ToString()).Month;
                    if (month >= 10)
                    {
                        g.DrawString(month + "月：       " + "『" + ds.Tables[0].Rows[i][3].ToString() + " 』", f, b, 10.0f, (i + 2) * 25.0f);
                    }
                    else
                    {
                        g.DrawString("0"+month + "月：       " + "『" + ds.Tables[0].Rows[i][3].ToString() + " 』", f, b, 10.0f, (i + 2) * 25.0f);
                    }
                }
            }
        }
        private void DrowFont(string str)
        {
            using(Graphics GrapFont = this.panel1.CreateGraphics())
            {
                GrapFont.Clear(Color.SeaShell);
                Pen p = new Pen(Color.Blue, 2.0f);
                Font f = new Font("華文新魏", 12, FontStyle.Regular);
                Brush b = new SolidBrush(Color.Blue);
                GrapFont.DrawString("『" + str + "』"+"利用圖表分析產品銷售走勢", f, b, 4.0f, 5.0f);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (sqlAda = new SqlDataAdapter("select distinct(t_name) from tb_merchandise", con))
            {
                DataSet ds = new DataSet();
                sqlAda.Fill(ds, "tb_merchandise");
                this.comboBox1.DataSource = ds.Tables[0];
                this.comboBox1.DisplayMember = "t_name";
            }
        }
    }
}