using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace ExchangeDatum
{
    public partial class frmListBox : Form
    {
        public frmListBox()
        {
            InitializeComponent();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        public void AddList()//�K�[�ƾ�
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02_1");
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_student", con);
            SqlDataReader dr = com.ExecuteReader();
            this.lbSocure.Items.Clear();
            while (dr.Read())
            {
                this.lbSocure.Items.Add(dr[1].ToString());
            }
            dr.Close();
            con.Close();
        }

        private void button2_Click(object sender, EventArgs e)//�����K�[���ܪ�����
        {
            for (int i = 0; i < lbSocure.Items.Count; i++)
            {
                lbSocure.SelectedIndex = i;
                lbChoose.Items.Add(lbSocure.SelectedItem.ToString());
            }
            lbSocure.Items.Clear();
        }

        private void button3_Click(object sender, EventArgs e)//�����K�[��ƾڷ���
        {
            for (int i = 0; i < lbChoose.Items.Count; i++)
            {
                lbChoose.SelectedIndex = i;
                lbSocure.Items.Add(lbChoose.SelectedItem.ToString());
            }
            lbChoose.Items.Clear();
        }
        private void frmListBox_Load(object sender, EventArgs e)
        {
            AddList();
        }

        private void button1_Click(object sender, EventArgs e)//��ӲK�[���ܪ�����
        {
            if (lbSocure.SelectedIndex != -1)
            {
                this.lbChoose.Items.Add(this.lbSocure.SelectedItem.ToString());
                this.lbSocure.Items.Remove(this.lbSocure.SelectedItem);
            }
        }

        private void button4_Click(object sender, EventArgs e)//��ӲK�[��ƾڷ���
        {
            if (lbChoose.SelectedIndex != -1)
            {
                this.lbSocure.Items.Add(this.lbChoose.SelectedItem.ToString());
                this.lbChoose.Items.Remove(this.lbChoose.SelectedItem);
            }

        }
    }
}