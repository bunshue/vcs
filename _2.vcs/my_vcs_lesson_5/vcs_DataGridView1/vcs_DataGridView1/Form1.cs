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
        private Panel buttonPanel = new Panel();
        private DataGridView dataGridView1 = new DataGridView();

        private Button setupDataGridView = new Button();
        private Button addDataGridView = new Button();
        private Button addNewRowButton = new Button();
        private Button deleteRowButton = new Button();
        private Button infoDataGridView = new Button();
        private Button clearDataGridView = new Button();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetupLayout();
        }

        private void dataGridView1_CellFormatting(object sender, System.Windows.Forms.DataGridViewCellFormattingEventArgs e)
        {
            if (e != null)
            {
                if (this.dataGridView1.Columns[e.ColumnIndex].Name == "Release Date")
                {
                    if (e.Value != null)
                    {
                        try
                        {
                            e.Value = DateTime.Parse(e.Value.ToString())
                                .ToLongDateString();
                            e.FormattingApplied = true;
                        }
                        catch (FormatException)
                        {
                            Console.WriteLine("{0} is not a valid date.", e.Value.ToString());
                        }
                    }
                }
            }
        }

        private void setupDataGridView_Click(object sender, EventArgs e)
        {
            SetupDataGridView();
        }

        private void addDataGridView_Click(object sender, EventArgs e)
        {
            PopulateDataGridView();
        }

        private void addNewRowButton_Click(object sender, EventArgs e)
        {
            this.dataGridView1.Rows.Add();
        }

        private void deleteRowButton_Click(object sender, EventArgs e)
        {
            if (this.dataGridView1.SelectedRows.Count > 0 && this.dataGridView1.SelectedRows[0].Index != this.dataGridView1.Rows.Count - 1)
            {
                this.dataGridView1.Rows.RemoveAt(this.dataGridView1.SelectedRows[0].Index);
            }
        }

        private void infoDataGridView_Click(object sender, EventArgs e)
        {
            print_dataGridView_data(dataGridView1);
        }

        private void clearDataGridView_Click(object sender, EventArgs e)
        {
            this.dataGridView1.Rows.Clear();
        }

        private void SetupLayout()
        {
            //this.Size = new Size(900, 660);

            setupDataGridView.Text = "Setup DGV";
            setupDataGridView.Location = new Point(10, 10);
            setupDataGridView.Click += new EventHandler(setupDataGridView_Click);

            addDataGridView.Text = "Add DGB";
            addDataGridView.Location = new Point(110, 10);
            addDataGridView.Click += new EventHandler(addDataGridView_Click);

            addNewRowButton.Text = "Add Row";
            addNewRowButton.Location = new Point(210, 10);
            addNewRowButton.Click += new EventHandler(addNewRowButton_Click);

            deleteRowButton.Text = "Delete Row";
            deleteRowButton.Location = new Point(310, 10);
            deleteRowButton.Click += new EventHandler(deleteRowButton_Click);

            infoDataGridView.Text = "Info";
            infoDataGridView.Location = new Point(410, 10);
            infoDataGridView.Click += new EventHandler(infoDataGridView_Click);

            clearDataGridView.Text = "Clear";
            clearDataGridView.Location = new Point(510, 10);
            clearDataGridView.Click += new EventHandler(clearDataGridView_Click);

            buttonPanel.Controls.Add(setupDataGridView);
            buttonPanel.Controls.Add(addDataGridView);
            buttonPanel.Controls.Add(addNewRowButton);
            buttonPanel.Controls.Add(deleteRowButton);
            buttonPanel.Controls.Add(infoDataGridView);
            buttonPanel.Controls.Add(clearDataGridView);
            buttonPanel.Height = 50;
            buttonPanel.Dock = DockStyle.Bottom;

            this.Controls.Add(this.buttonPanel);
        }

        private void SetupDataGridView()
        {
            this.Controls.Add(dataGridView1);

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

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            dataGridView1.MultiSelect = false;
            dataGridView1.Dock = DockStyle.Fill;

            dataGridView1.CellFormatting += new DataGridViewCellFormattingEventHandler(dataGridView1_CellFormatting);
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

            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 3;
            dataGridView1.Columns[1].DisplayIndex = 4;
            dataGridView1.Columns[2].DisplayIndex = 0;
            dataGridView1.Columns[3].DisplayIndex = 1;
            dataGridView1.Columns[4].DisplayIndex = 2;
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



    }
}
