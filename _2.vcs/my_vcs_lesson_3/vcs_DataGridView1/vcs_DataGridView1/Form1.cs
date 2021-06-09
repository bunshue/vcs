using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataGridView1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            print_dataGridView_data(dataGridView1);
        }

        void load_data()
        {
            SetupDataGridView();        //設定DGV
            PopulateDataGridView();     //填入資料
        }

        private void SetupDataGridView()
        {
            dataGridView1.ColumnCount = 5;

            dataGridView1.ColumnHeadersDefaultCellStyle.BackColor = Color.Navy;
            dataGridView1.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            dataGridView1.ColumnHeadersDefaultCellStyle.Font = new Font(dataGridView1.Font, FontStyle.Bold);

            dataGridView1.Name = "dataGridView1";
            dataGridView1.Location = new Point(8, 8);
            dataGridView1.Size = new Size(500, 250);
            dataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.DisplayedCellsExceptHeaders;
            dataGridView1.ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle.Single;
            dataGridView1.CellBorderStyle = DataGridViewCellBorderStyle.Single;
            dataGridView1.GridColor = Color.Black;
            dataGridView1.RowHeadersVisible = false;

            dataGridView1.Columns[0].Name = "Release Date";
            dataGridView1.Columns[1].Name = "Track";
            dataGridView1.Columns[2].Name = "Title";
            dataGridView1.Columns[3].Name = "Artist";
            dataGridView1.Columns[4].Name = "Album";
            dataGridView1.Columns[4].DefaultCellStyle.Font = new Font(dataGridView1.DefaultCellStyle.Font, FontStyle.Italic);

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.MultiSelect = false;
            dataGridView1.Dock = DockStyle.Fill;

            //dataGridView1.CellFormatting += new DataGridViewCellFormattingEventHandler(songsDataGridView_CellFormatting);
        }

        private void PopulateDataGridView()
        {
            string[] row0 = { "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" };
            string[] row1 = { "1960", "6", "Fools Rush In", "Frank Sinatra", "Nice 'N' Easy" };
            string[] row2 = { "11/11/1971", "1", "One of These Days", "Pink Floyd", "Meddle" };
            string[] row3 = { "1988", "7", "Where Is My Mind?", "Pixies", "Surfer Rosa" };
            string[] row4 = { "5/1981", "9", "Can't Find My Mind", "Cramps", "Psychedelic Jungle" };
            string[] row5 = { "6/10/2003", "13", "Scatterbrain. (As Dead As Leaves.)", "Radiohead", "Hail to the Thief" };
            string[] row6 = { "6/30/1992", "3", "Dress", "P J Harvey", "Dry" };

            dataGridView1.Rows.Add(row0);
            dataGridView1.Rows.Add(row1);
            dataGridView1.Rows.Add(row2);
            dataGridView1.Rows.Add(row3);
            dataGridView1.Rows.Add(row4);
            dataGridView1.Rows.Add(row5);
            dataGridView1.Rows.Add(row6);

            /*
            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 3;
            dataGridView1.Columns[1].DisplayIndex = 4;
            dataGridView1.Columns[2].DisplayIndex = 0;
            dataGridView1.Columns[3].DisplayIndex = 1;
            dataGridView1.Columns[4].DisplayIndex = 2;
            */
        }

        void print_dataGridView_data(DataGridView dgv)
        {
            int r;
            int c;
            int rows = dgv.RowCount;
            int cols = dgv.ColumnCount;
            richTextBox1.Text += "ROWS = " + rows.ToString() + "\n";
            richTextBox1.Text += "COLS = " + cols.ToString() + "\n";
            richTextBox1.Text += "Content:\n";

            for (r = 0; r < rows; r++)
            {
                richTextBox1.Text += "r = " + r.ToString() + "\t";
                for (c = 0; c < cols; c++)
                {
                    //richTextBox1.Text += dataGridView1[c, r].Value + "\t";
                    DataGridViewCell dgvCell = dgv[c, r];
                    richTextBox1.Text += dgvCell.Value + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            load_data();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //int index = dataGridView1.Rows.Add();
            //dataGridView1.Rows[index].Cells[0].Value = "123456";

            string[] row0 = { "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" };
            dataGridView1.Rows.Add(row0);

            //DataGridViewRowCollection rows = dataGridView1.Rows;
            //rows.Add(new Object[] { "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" });
        }

        private void button5_Click(object sender, EventArgs e)
        {
            dataGridView1.Rows.Clear();         //刪除row資料, 留下標題

            //dataGridView1.Columns.Clear();    //刪除標題

            //clear
            //dataGridView1.DataSource = null;
            //dataGridView1.Invalidate();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (this.dataGridView1.SelectedRows.Count > 0 && this.dataGridView1.SelectedRows[0].Index != this.dataGridView1.Rows.Count - 1)
            {
                this.dataGridView1.Rows.RemoveAt(this.dataGridView1.SelectedRows[0].Index);
            }

        }

        private void button7_Click(object sender, EventArgs e)
        {
            dataGridView1.ColumnCount = 2;
            dataGridView1.Columns[0].Name = "品名";
            dataGridView1.Columns[1].Name = "單價";

            dataGridView1.Rows.Add(new Object[] { "紅茶", 25 });
            dataGridView1.Rows.Add(new Object[] { "綠茶", 25 });
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //綁定數據集合
            dataGridView1.DataSource = new List<Fruit>()
            {
            new Fruit(){Name="蘋果",Price=30},
            new Fruit(){Name="橘子",Price=40},
            new Fruit(){Name="梨子",Price=33},
            new Fruit(){Name="水蜜桃",Price=31}
            };
            dataGridView1.Columns[0].Width = 200;
            dataGridView1.Columns[1].Width = 170;

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.Columns[0].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter; //設置對其方式   此欄置中對齊
        }

        private void button9_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < dataGridView1.Rows.Count; i++)
            {

                if (i % 2 == 0)
                    dataGridView1.Rows[i].DefaultCellStyle.
                        BackColor = Color.LightYellow;//隔行更换背景色
            }

        }

    }

    class Fruit
    {
        public string Name { get; set; }
        public float Price { get; set; }
    }
}

