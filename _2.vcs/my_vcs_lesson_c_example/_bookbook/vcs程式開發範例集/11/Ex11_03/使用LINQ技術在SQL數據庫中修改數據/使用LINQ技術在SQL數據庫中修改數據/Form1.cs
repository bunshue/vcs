using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 使用LINQ技術在SQL數據庫中修改數據
{
    public partial class Form1 : Form
    {
        string strCon = "Data Source=(local);database=db_11;uid=sa;pwd=;";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            binginfo();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void binginfo()
        {
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            txtName.Focus();
        }

        private void dataGridView1_Click(object sender, EventArgs e)
        {

        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (dataGridView1.SelectedRows.Count != 0)
            {
                int id = Convert.ToInt32(dataGridView1.SelectedRows[0].Cells[0].Value);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (txtaddress.Text != "" && txtage.Text != "" && txtName.Text != "" && txtphone.Text != "")
            {
                if (txtphone.Text.Length != 11)
                {
                    MessageBox.Show("電話號碼位數不正確");
                }
                else
                {

                }
            }
        }

        private void txtage_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!(e.KeyChar <= '9' && e.KeyChar >= '0') && e.KeyChar != '\r' && e.KeyChar != '\b')
            {
                e.Handled = true;
            }
        }

        private void txtphone_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (!(e.KeyChar <= '9' && e.KeyChar >= '0') && e.KeyChar != '\r' && e.KeyChar != '\b')
            {
                e.Handled = true;
            }
        }

        private void txtage_KeyUp(object sender, KeyEventArgs e)
        {
            if (txtage.Text.StartsWith("0"))
            {
                MessageBox.Show("年齡不能以0開頭");
                txtage.Text = "";
            }
        }
    }
}
