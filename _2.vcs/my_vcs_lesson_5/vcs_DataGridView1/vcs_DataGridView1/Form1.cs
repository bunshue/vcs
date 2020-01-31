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
        private DataGridView songsDataGridView = new DataGridView();

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

        private void songsDataGridView_CellFormatting(object sender, System.Windows.Forms.DataGridViewCellFormattingEventArgs e)
        {
            if (e != null)
            {
                if (this.songsDataGridView.Columns[e.ColumnIndex].Name == "Release Date")
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
            this.songsDataGridView.Rows.Add();
        }

        private void deleteRowButton_Click(object sender, EventArgs e)
        {
            if (this.songsDataGridView.SelectedRows.Count > 0 && this.songsDataGridView.SelectedRows[0].Index != this.songsDataGridView.Rows.Count - 1)
            {
                this.songsDataGridView.Rows.RemoveAt(this.songsDataGridView.SelectedRows[0].Index);
            }
        }

        private void infoDataGridView_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "ROWS = " + songsDataGridView.Rows.Count.ToString() + "\n";
            richTextBox1.Text += "COLS = " + songsDataGridView.Columns.Count.ToString() + "\n";
            richTextBox1.Text += "Content:\n";

            for (int i = 0; i <= songsDataGridView.Rows.Count - 1; i++)
            {
                for (int j = 0; j < songsDataGridView.Columns.Count; j++)
                {
                    DataGridViewCell dgvCell = songsDataGridView[j, i];
                    richTextBox1.Text += dgvCell.Value + "\t";
                }
                richTextBox1.Text += "\n";
            }

        }

        private void clearDataGridView_Click(object sender, EventArgs e)
        {
            this.songsDataGridView.Rows.Clear();
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
            this.Controls.Add(songsDataGridView);

            songsDataGridView.ColumnCount = 5;

            songsDataGridView.ColumnHeadersDefaultCellStyle.BackColor = Color.Navy;
            songsDataGridView.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            songsDataGridView.ColumnHeadersDefaultCellStyle.Font =
                new Font(songsDataGridView.Font, FontStyle.Bold);

            songsDataGridView.Name = "songsDataGridView";
            songsDataGridView.Location = new Point(8, 8);
            songsDataGridView.Size = new Size(500, 250);
            songsDataGridView.AutoSizeRowsMode =
                DataGridViewAutoSizeRowsMode.DisplayedCellsExceptHeaders;
            songsDataGridView.ColumnHeadersBorderStyle =
                DataGridViewHeaderBorderStyle.Single;
            songsDataGridView.CellBorderStyle = DataGridViewCellBorderStyle.Single;
            songsDataGridView.GridColor = Color.Black;
            songsDataGridView.RowHeadersVisible = false;

            songsDataGridView.Columns[0].Name = "Release Date";
            songsDataGridView.Columns[1].Name = "Track";
            songsDataGridView.Columns[2].Name = "Title";
            songsDataGridView.Columns[3].Name = "Artist";
            songsDataGridView.Columns[4].Name = "Album";
            songsDataGridView.Columns[4].DefaultCellStyle.Font = new Font(songsDataGridView.DefaultCellStyle.Font, FontStyle.Italic);

            songsDataGridView.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            songsDataGridView.MultiSelect = false;
            songsDataGridView.Dock = DockStyle.Fill;

            songsDataGridView.CellFormatting += new DataGridViewCellFormattingEventHandler(songsDataGridView_CellFormatting);
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

            songsDataGridView.Rows.Add(row0);
            songsDataGridView.Rows.Add(row1);
            songsDataGridView.Rows.Add(row2);
            songsDataGridView.Rows.Add(row3);
            songsDataGridView.Rows.Add(row4);
            songsDataGridView.Rows.Add(row5);
            songsDataGridView.Rows.Add(row6);

            songsDataGridView.Columns[0].DisplayIndex = 3;
            songsDataGridView.Columns[1].DisplayIndex = 4;
            songsDataGridView.Columns[2].DisplayIndex = 0;
            songsDataGridView.Columns[3].DisplayIndex = 1;
            songsDataGridView.Columns[4].DisplayIndex = 2;
        }


    }
}
