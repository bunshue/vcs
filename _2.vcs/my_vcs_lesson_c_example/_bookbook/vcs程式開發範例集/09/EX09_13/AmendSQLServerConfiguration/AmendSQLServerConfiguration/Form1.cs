using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace AmendSQLServerConfiguration
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string tag = "null";
        SqlConnection con = new SqlConnection("Data Source=(local);Initial Catalog=db_09;Integrated Security=SSPI");
        DataTable dt;
        private void Form1_Load(object sender, EventArgs e)
        {
            showTrack();
            types();
        }
      
        private void dataGridView1_Click(object sender, EventArgs e)
        {
            this.textBox1.Text = this.dataGridView1.SelectedCells[0].Value.ToString();
            this.comboBox1.Text = this.dataGridView1.SelectedCells[1].Value.ToString();
            this.textBox2.Text = this.dataGridView1.SelectedCells[2].Value.ToString();
            this.textBox1.Enabled = false;
        }
        private void showTrack()
        {
            con.Open();
            dt = new DataTable();
            SqlDataAdapter da = new SqlDataAdapter();
            SqlCommand cmd = new SqlCommand();
            cmd.CommandType = CommandType.StoredProcedure;
            cmd.CommandText = "Poc_Linshi";
            cmd.Connection = con;
            da.SelectCommand = cmd;
            da.Fill(dt);
            this.dataGridView1.DataSource = dt.DefaultView;
            con.Close();
        }
        private void types()
        {
            string[] strtype ={ "varchar", "char"};
            this.comboBox1.DataSource = strtype;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.button4.Enabled = true;
            this.textBox1.Enabled = true;
            this.textBox1.Text = "";
            this.textBox2.Text = "";
            tag = "add";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.button4.Enabled = true;
            tag = "update";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(MessageBox.Show("是否刪除","提示",MessageBoxButtons.OKCancel,MessageBoxIcon.Question)==DialogResult.OK)
            {
                con.Open();
                string str = "alter table tb_11 drop column " + this.textBox1.Text + "";
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = str;
                cmd.Connection = con;
                cmd.ExecuteNonQuery();
                con.Close();
                showTrack();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                con.Open();
                string str = string.Empty;
                if (tag == "add")
                {
                    str += "alter table tb_11 add " + this.textBox1.Text + " ";
                    str += "" + this.comboBox1.Text + "(" + this.textBox2.Text + ")";
                }
                else if (tag == "update")
                {
                    str += "alter table tb_11 alter column " + this.textBox1.Text + " ";
                    str += "" + this.comboBox1.Text + "(" + this.textBox2.Text + ")";
                }
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = str;
                cmd.Connection = con;
                cmd.ExecuteNonQuery();
                con.Close();
                showTrack();
                this.button4.Enabled = false;
            }
            catch
            {
                con.Close();
                MessageBox.Show("請輸入有效訊息");
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}