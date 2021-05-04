using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OleDb;

namespace Access2000Path
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__RW\_mdb\db_09.mdb";

        OleDbConnection Olecon;
        OleDbDataAdapter OleDat;

        DataTable dt;
        int MaxValue = 0, State = 1;
        string ConStr;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //ConStr = "Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename;
            //ConStr = "Provider=Microsoft.ACE.OLEDB.12.0;Data source='" + filename + "'";
            ConStr = "Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename;
            Olecon = new OleDbConnection(ConStr);

            //顯示在dataGridView1 ST
            OleDat = new OleDbDataAdapter("select * from 帳目", Olecon);
            DataSet ds = new DataSet();
            OleDat.Fill(ds, "帳目");
            this.dataGridView1.DataSource = ds.Tables[0].DefaultView;
            //顯示在dataGridView1 SP

            Olecon.Open();
            MaxValue = Convert.ToInt32(new OleDbCommand("select Count(*) from 帳目", Olecon).ExecuteScalar());
            Olecon.Close();
            showInfo(0, 1);
        }

        private void showInfo(int first, int next)
        {
            dt = new DataTable();
            OleDat = new OleDbDataAdapter("select * from 帳目", ConStr);
            OleDat.Fill(first, next, dt);
            this.textBox1.Text = dt.Rows[0][1].ToString();
            this.textBox2.Text = dt.Rows[0][2].ToString();
            this.textBox3.Text = dt.Rows[0][4].ToString();
            this.textBox4.Text = dt.Rows[0][5].ToString();
        }
        //第一條
        private void button1_Click(object sender, EventArgs e)
        {
            showInfo(0, 1);
            State = 1;
        }
        //最後一條
        private void button4_Click(object sender, EventArgs e)
        {
            showInfo(MaxValue - 1, MaxValue);
            State = MaxValue;
        }
        //下一條
        private void button3_Click(object sender, EventArgs e)
        {
            if (State < 7)
            {
                showInfo(State, State + 1);
                State = State + 1;
            }
            else
            {
                State = 0;
                showInfo(State, 1);
                State += 1;
            }
        }
        //上一條
        private void button2_Click(object sender, EventArgs e)
        {

            if (State > 1)
            {
                showInfo(State - 1, State);
                State = State - 1;
            }
            else
            {
                State = 7;
                showInfo(State - 1, State);
                State -= 1;
            }
        }

    }
}