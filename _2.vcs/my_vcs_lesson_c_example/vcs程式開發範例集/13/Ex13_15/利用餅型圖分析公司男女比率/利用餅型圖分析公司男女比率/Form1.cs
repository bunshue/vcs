using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Drawing.Imaging;
namespace 利用餅型圖分析公司男女比率
{
    public partial class Form1 : Form
    {
        SqlConnection con;
        SqlCommand cmd;
        public Form1()
        {
            InitializeComponent();
        }

        private void Conn()
        {
            con = new SqlConnection("server=.;uid=sa;pwd=;database=db_13");
            con.Open();
        }
       
        private void Form1_Load(object sender, EventArgs e)
        {
            
        }
     
       
        private void ShowPic(string SexCode,float f)
        {
            Graphics g = this.panel1.CreateGraphics();
            Pen p=new Pen(new SolidBrush(Color.Blue));
            Point p1=new Point(0,0);
            Size s=new Size(this.panel1.Width,this.panel1.Height);
            Rectangle trct = new Rectangle(p1, s);
            g.FillEllipse(new SolidBrush(Color.Red), trct);
            g.FillPie(new SolidBrush(Color.Blue), trct, 180, f*360);
            Graphics ginfo = this.panel2.CreateGraphics();
            Font font=new Font("細明體",10,FontStyle.Regular);
            ginfo.DrawString(SexCode +" "+f.ToString().Substring(0,4), font, new SolidBrush(Color.Blue), 0, 5);
            ginfo.DrawString("女" + " " + (1.0 - Convert.ToDouble(f.ToString().Substring(0, 4))).ToString().Substring(0, 4), font, new SolidBrush(Color.Red), 0, 25);
            
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Conn();
            using (cmd = new SqlCommand("SELECT sex,COUNT(sex) num FROM tb_sex group by sex", con))
               {
                   SqlDataReader dr=cmd.ExecuteReader();
                   string[] str = new string[2];
                   int i=0;
                   while (dr.Read())
                   {
                       str[i] = dr[0].ToString() + "," + dr[1].ToString();
                       i++;
                   }
                   float N = Convert.ToInt16(str[0].Substring(2)) + Convert.ToInt16(str[1].Substring(2));
                   float f =  Convert.ToInt16(str[0].Substring(2))/N;
                   ShowPic(str[0].Substring(0,1), f);
               }
        }
    }
}