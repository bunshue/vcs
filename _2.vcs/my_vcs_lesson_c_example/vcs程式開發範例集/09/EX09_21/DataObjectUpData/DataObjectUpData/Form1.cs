using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace DataObjectUpData
{
    public partial class Form1 : Form
    {
        static int Num = 0;
        int Count = 0;
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        private void button6_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Resultinfo(Num);
            using (SqlCommand cmd = new SqlCommand("select Count(*) from 員工表", con))
            {
                con.Open();
                Count = Convert.ToInt32(cmd.ExecuteScalar());
                con.Close();
            }
        }

        private DataSet DtReslut(int i)
        {
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                da.SelectCommand = new SqlCommand("select * from 員工表", con);
                DataSet ds = new DataSet();
                da.Fill(ds, i, i + 1, "員工表");
                return ds;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Num = 0;
            Resultinfo(Num);
        }

        private void Resultinfo(int j)
        {
            DataSet dsNew = DtReslut(j);
            this.textBox1.Text = dsNew.Tables[0].Rows[0][0].ToString();
            this.textBox2.Text = dsNew.Tables[0].Rows[0][1].ToString();
            this.textBox4.Text = dsNew.Tables[0].Rows[0][2].ToString();
            this.textBox5.Text = dsNew.Tables[0].Rows[0][3].ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Num -= 1;
            if (Num >= 0)
            {
                Resultinfo(Num);
            }
            else
            {
                MessageBox.Show("現已是首條記錄");
                Num = 0;
                return; ;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Num += 1;
            if (Num < Count)
            {
                Resultinfo(Num);
            }
            else
            {
                MessageBox.Show("現已是末條記錄");
                Num = Count - 1;
                return;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Num = Count;
            Resultinfo(Num - 1);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (update())
            {
                MessageBox.Show("成功修改");
            }
        }

        private bool update()
        {

            using (SqlCommand command = new SqlCommand("update 員工表 set" +
               " 員工姓名=@員工姓名,基本工資=@基本工資,工作評價=@工作評價 where 員工編號=@員工編號 ", con))
            {
                con.Open();
                try
                {
                    command.Parameters.Add("@員工編號", SqlDbType.VarChar, 50, "員工編號").Value = this.textBox1.Text;
                    command.Parameters.Add("@員工姓名", SqlDbType.VarChar, 50, "員工姓名").Value = this.textBox2.Text;
                    command.Parameters.Add("@基本工資", SqlDbType.Float, 8, "基本工資").Value = Convert.ToString(this.textBox4.Text);
                    command.Parameters.Add("@工作評價", SqlDbType.VarChar, 50, "工作評價").Value = this.textBox5.Text;
                    command.ExecuteNonQuery();
                    con.Close();
                    return true;
                }
                catch { return false; }

            }

        }
    }
}