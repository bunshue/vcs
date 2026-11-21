using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_CompareKatfile
{
    public partial class Form1 : Form
    {
        string foldername1 = @"D:\_git\vcs\_1.data\______test_files1\Dir1";
        string foldername2 = @"D:\_git\vcs\_1.data\______test_files1\Dir2";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            dataGridView1.Columns[0].Width = 190;
            dataGridView1.Columns[1].Width = 190;

            dataGridView1.Size = new Size(410, 480);
            richTextBox_katfile1.Size = new Size(200, 480);
            richTextBox_katfile2.Size = new Size(200, 480);
            dataGridView1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            richTextBox_katfile1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            richTextBox_katfile2.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox1.Size = new Size(830, 200);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            btnCompare.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - btnCompare.Size.Width, richTextBox1.Location.Y);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(richTextBox1.Right + 10, richTextBox1.Bottom + 10);

            this.Text = "比較Katfile";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void btnCompare_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "比較\n";

            dataGridView1.Rows.Clear();

            int len1 = richTextBox_katfile1.Lines.Length;
            int len2 = richTextBox_katfile2.Lines.Length;
            //richTextBox1.Text += "len1 = " + len1.ToString() + "\n";
            //richTextBox1.Text += "len2 = " + len2.ToString() + "\n";

            // Compare.
            int i1 = 0, i2 = 0;
            while ((i1 < len1) && (i2 < len2))
            {
                if (richTextBox_katfile1.Lines[i1] == richTextBox_katfile2.Lines[i2])
                {
                    // They match. Display them both.
                    dataGridView1.Rows.Add(new Object[] { richTextBox_katfile1.Lines[i1], richTextBox_katfile2.Lines[i2] });
                    i1++;
                    i2++;
                }
                else if (richTextBox_katfile1.Lines[i1].CompareTo(richTextBox_katfile2.Lines[i2]) < 0)
                {
                    // Display the directory 1 file.
                    dataGridView1.Rows.Add(new Object[] { richTextBox_katfile1.Lines[i1], null });
                    i1++;
                }
                else
                {
                    // Display the directory 2 file.
                    dataGridView1.Rows.Add(new Object[] { null, richTextBox_katfile2.Lines[i2] });
                    i2++;
                }
            }

            // Display remaining directory 1 files.
            for (int i = i1; i < richTextBox_katfile1.Lines.Length; i++)
            {
                dataGridView1.Rows.Add(new Object[] { richTextBox_katfile1.Lines[i], null });
            }

            // Display remaining directory 2 files.
            for (int i = i2; i < richTextBox_katfile2.Lines.Length; i++)
            {
                dataGridView1.Rows.Add(new Object[] { null, richTextBox_katfile2.Lines[i] });
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

