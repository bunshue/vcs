using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_CompareDirectory
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = @"C:\_git\vcs\_1.data\______test_files1\Dir1";
            textBox2.Text = @"C:\_git\vcs\_1.data\______test_files1\Dir2";

            SizeColumns();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            SizeColumns();
        }

        private void SizeColumns()
        {
            int wid = (int)((dataGridView1.Width - 50) / 2);
            if (wid < 10) wid = 10;
            dataGridView1.Columns[0].Width = wid;
            dataGridView1.Columns[1].Width = wid;
        }

        // Compare the files in each directory.
        private void btnCompare_Click(object sender, EventArgs e)
        {
            // Clear previous results.
            dataGridView1.Rows.Clear();

            // Get sorted lists of files in the directories.
            string dir1 = textBox1.Text;
            if (!dir1.EndsWith("\\")) dir1 += "\\";
            string[] file_names1 = Directory.GetFiles(dir1);
            for (int i = 0; i < file_names1.Length; i++)
            {
                file_names1[i] = file_names1[i].Replace(dir1, "");
            }
            Array.Sort(file_names1);

            string dir2 = textBox2.Text;
            if (!dir2.EndsWith("\\")) dir2 += "\\";
            string[] file_names2 = Directory.GetFiles(dir2);
            for (int i = 0; i < file_names2.Length; i++)
            {
                file_names2[i] = file_names2[i].Replace(dir2, "");
            }
            Array.Sort(file_names2);

            // Compare.
            int i1 = 0, i2 = 0;
            while ((i1 < file_names1.Length) && (i2 < file_names2.Length))
            {
                if (file_names1[i1] == file_names2[i2])
                {
                    // They match. Display them both.
                    dataGridView1.Rows.Add(new Object[] { file_names1[i1], file_names2[i2] });
                    i1++;
                    i2++;
                }
                else if (file_names1[i1].CompareTo(file_names2[i2]) < 0)
                {
                    // Display the directory 1 file.
                    dataGridView1.Rows.Add(new Object[] { file_names1[i1], null });
                    i1++;
                }
                else
                {
                    // Display the directory 2 file.
                    dataGridView1.Rows.Add(new Object[] { null, file_names2[i2] });
                    i2++;
                }
            }

            // Display remaining directory 1 files.
            for (int i = i1; i < file_names1.Length; i++)
            {
                dataGridView1.Rows.Add(new Object[] { file_names1[i], null });
            }

            // Display remaining directory 2 files.
            for (int i = i2; i < file_names2.Length; i++)
            {
                dataGridView1.Rows.Add(new Object[] { null, file_names2[i] });
            }
        }
    }
}
