using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_GetFileInfo
{
    public partial class Form1 : Form
    {
        string foldername = @"D:\_git\vcs\_1.data\______test_files1";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            textBox1.Text = foldername;

            listView1.Items.Clear();

            foreach (string strFile in Directory.GetFiles(textBox1.Text))
            {
                FileInfo fi = new FileInfo(strFile);
                richTextBox1.Text += "加入 : " + fi.FullName + "\n";
                listView1.Items.Add(fi.FullName);
            }
        }

        void show_item_location()
        {
            //button
            int W = 200;
            int H = 60;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;

            listView1.Size = new Size(W * 3 + 20, H * 11 + 10);
            pictureBox1.Size = new Size(W * 2, H * 5);
            richTextBox1.Size = new Size(W * 2, H * 7+10);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            listView1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 5-40);

            //richTextBox1.Size = new Size(300, 690);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(W * 5 + 70, 800);
            this.Text = "vcs_GetFileInfo";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                listView1.Items.Clear();
                textBox1.Text = folderBrowserDialog1.SelectedPath;

                foreach (string strFile in Directory.GetFiles(textBox1.Text))
                {
                    FileInfo fi = new FileInfo(strFile);
                    richTextBox1.Text += "加入 : " + fi.FullName + "\n";
                    listView1.Items.Add(fi.FullName);
                }
            }
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += listView1.SelectedItems.Count.ToString() + "\n";

            if (listView1.SelectedItems.Count != 0)
            {
                richTextBox1.Text += listView1.SelectedItems[0].Text + "\n";
                FileInfo fi = new FileInfo(listView1.SelectedItems[0].Text);

                string Name = fi.Name;
                string Size = Convert.ToDouble(fi.Length / 1024).ToString();
                string Exten = fi.Extension;
                string CTime = fi.CreationTime.ToString();
                string ReadOnly = fi.IsReadOnly.ToString();
                string WTime = fi.LastWriteTime.ToString();

                string fileinfo = string.Empty;
                fileinfo += "檔案訊息 :\n";
                fileinfo += "檔案名 : \t" + Name.ToString() + "\n";
                fileinfo += "副檔名 : \t" + Exten.ToString() + "\n";
                fileinfo += "檔案大小 : \t" + Size.ToString() + " KB\n";
                fileinfo += "建立時間 : \t" + CTime.ToString() + "\n";
                fileinfo += "最後修改時間 : \t" + WTime.ToString() + "\n";
                fileinfo += "唯讀 : \t" + ReadOnly.ToString() + "\n";

                richTextBox1.Text += fileinfo;

                string ext = fi.Extension.ToLower();
                if ((ext == ".bmp") || (ext == ".jpg") || (ext == ".png"))
                {
                    pictureBox1.Image = Image.FromFile(listView1.SelectedItems[0].Text);
                }
                else
                {
                    pictureBox1.Image = null;
                }
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

/*  可搬出

*/

