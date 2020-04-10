using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ReadWrite_XML2
{
    public partial class Form1 : Form
    {
        string filename = "C:\\______test_files\\__RW\\_xml\\person.xml";
        public Form1()
        {
            InitializeComponent();
        }

        DataSet ds = new DataSet();

        private void Form1_Load(object sender, EventArgs e)
        {
            // 讀取XML文件並放入DataSet
            ds.ReadXml(filename);
            dataGridView1.DataSource = ds.Tables["學生"];
            DataColumn dc = ds.Tables["學生"].Columns["學號"];
            // 在學生DataTable建立學號欄位為主鍵，主鍵名稱為「PK_學號」
            ds.Tables["學生"].Constraints.Add("PK_學號", dc, true);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "RowCount = " + dataGridView1.RowCount.ToString() + "\n";
            richTextBox1.Text += "ColumnCount = " + dataGridView1.ColumnCount.ToString() + "\n";
            richTextBox1.Text += "CurrentRow = " + dataGridView1.CurrentRow.Index.ToString() + "\n";
            //richTextBox1.Text += "CurrentRow = " + ds.Tables[0]. + "\n";

            richTextBox1.Text += "CurrentRow0 = " + dataGridView1.Columns[0].Name + "\n";
            richTextBox1.Text += "CurrentRow1 = " + dataGridView1.Columns[1].Name + "\n";
            richTextBox1.Text += "CurrentRow2 = " + dataGridView1.Columns[2].Name + "\n";
            //dataGridView1.data

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //int index = dataGridView1.Rows.Add();
            //dataGridView1.Rows[index].Cells[0].Value = "123456";

        //string[] row0 = { "11/22/1968", "29", "Revolution 9", "Beatles"};
        //dataGridView1.Rows.Add(row0);

            // Initialize the button column.
            DataGridViewButtonColumn buttonColumn =
                new DataGridViewButtonColumn();
            buttonColumn.Name = "Details";
            buttonColumn.HeaderText = "Details";
            buttonColumn.Text = "View Details";

            // Use the Text property for the button text for all cells rather
            // than using each cell's value as the text for its own button.
            buttonColumn.UseColumnTextForButtonValue = true;

            // Add the button column to the control.
            dataGridView1.Columns.Insert(4, buttonColumn);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //獲取當前值
            richTextBox1.Text += dataGridView1.CurrentCell.Value.ToString() + "\n";
            richTextBox1.Text += dataGridView1.CurrentCell.ColumnIndex.ToString() + "\n";
            richTextBox1.Text += dataGridView1.CurrentCell.RowIndex.ToString() + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            dataGridView1.CurrentCell = dataGridView1[2, 2];
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int row = this.dataGridView1.CurrentRow.Index + 1;
            if (row > this.dataGridView1.RowCount - 1)
                row = 0;
            this.dataGridView1.CurrentCell = this.dataGridView1[0, row]; 

        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "data : " + dataGridView1[2, 2].Value + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int row = this.dataGridView1.CurrentRow.Index - 1;
            if (row < 0)
                row = this.dataGridView1.RowCount - 1;
            this.dataGridView1.CurrentCell = this.dataGridView1[0, row]; 

        }

        private void button9_Click(object sender, EventArgs e)
        {
            int i;
            int j;
            int RowCount = dataGridView1.RowCount;
            int ColumnCount = dataGridView1.ColumnCount;
            richTextBox1.Text += "RowCount = " + RowCount.ToString() + "\n";
            richTextBox1.Text += "ColumnCount = " + ColumnCount.ToString() + "\n";

            //richTextBox1.Text += "CurrentRow = " + dataGridView1.CurrentRow.Index.ToString() + "\n";
            for (i = 0; i < RowCount; i++)
            {
                for (j = 0; j < ColumnCount; j++)
                {
                    richTextBox1.Text += "[" + j.ToString() + "," + i.ToString() + "]" + dataGridView1[j, i].Value + "\t";
                
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";


        }
    }
}
