using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataGridView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //int index = dataGridView1.Rows.Add();
            //dataGridView1.Rows[index].Cells[0].Value = "123456";

            //string[] row0 = { "11/22/1968", "29", "Revolution 9", "Beatles"};
            //dataGridView1.Rows.Add(row0);

            DataGridViewRowCollection rows = dataGridView1.Rows;
            rows.Add(new Object[] { "紅茶", 25 });
            rows.Add(new Object[] { "綠茶", 25 });


        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }
}
