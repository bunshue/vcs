using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;
namespace 利用控制元件完成柱形圖分析
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection con = new SqlConnection("server=.;uid=sa;pwd=;database=db_13"))
            {
                int XValse = 20;
                DataSet ds = new DataSet();
                SqlCommand cmd = new SqlCommand("select * from tb_Rectangle select Sum(t_Num) from tb_Rectangle", con);
                SqlDataAdapter da = new SqlDataAdapter();
                da.SelectCommand = cmd;
                da.Fill(ds);
                Panel[] p = new Panel[ds.Tables[0].Rows.Count];
                int Values = Convert.ToInt32(ds.Tables[1].Rows[0][0].ToString());
                for (int i = 0; i < ds.Tables[0].Rows.Count; i++)
                {

                    ds.Tables[0].Rows[i][0].ToString();
                    float f = Convert.ToInt32(ds.Tables[0].Rows[i][1].ToString());
                    Size s = new Size();
                    s.Width = 30;
                    s.Height = Convert.ToInt32(f/Values*200);

                    Point pint = new Point();
                    pint.X = XValse;
                    pint.Y = this.Height-50-s.Height;
                    p[i] = new Panel();
                    p[i].Location = pint;
                    p[i].BackColor = Color.Red;
                    p[i].Size = s;
                    XValse += 40;
                    Label lbl = new Label();
                    lbl.Text = ds.Tables[0].Rows[i][0].ToString();
                    lbl.Font = new Font("細明體", 9, FontStyle.Regular);
                    lbl.ForeColor = Color.White;
                    p[i].Controls.Add(lbl);
                   this.Controls.Add(p[i]);
                }   
            }
        }
    }
}