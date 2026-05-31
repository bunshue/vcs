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
            List<FileInfo> fi = new List<FileInfo>();
            foreach (string strFile in Directory.GetFiles(textBox1.Text))
            {
                fi.Add(new FileInfo(strFile));
            }
            var values = from strFile in fi
                         group strFile by strFile.Extension into FExten
                         orderby FExten.Key
                         select FExten;
            foreach (var vFiles in values)
            {
                foreach (var f in vFiles)
                {
                    listView1.Items.Add(f.FullName);
                }
            }
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            //richTextBox1.Size = new Size(300, 690);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(950, 750);
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
                List<FileInfo> fi = new List<FileInfo>();
                foreach (string strFile in Directory.GetFiles(textBox1.Text))
                {
                    fi.Add(new FileInfo(strFile));
                }
                var values = from strFile in fi
                             group strFile by strFile.Extension into FExten
                             orderby FExten.Key
                             select FExten;
                foreach (var vFiles in values)
                {
                    foreach (var f in vFiles)
                    {
                        listView1.Items.Add(f.FullName);
                    }
                }
            }
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count != 0)
            {
                FileInfo fi = new FileInfo(listView1.SelectedItems[0].Text);
                string[] strAttribute = new string[] { fi.Name, Convert.ToDouble(fi.Length / 1024).ToString(), fi.Extension, fi.CreationTime.ToString(), fi.IsReadOnly.ToString(), fi.LastWriteTime.ToString() };
                var values = from str in strAttribute
                             select new
                             {
                                 Name = strAttribute[0].ToString(),
                                 Size = strAttribute[1].ToString(),
                                 Exten = strAttribute[2].ToString(),
                                 CTime = strAttribute[3].ToString(),
                                 ReadOnly = strAttribute[4].ToString(),
                                 WTime = strAttribute[5].ToString()
                             };
                foreach (var v in values)
                {
                    string fileinfo = string.Empty;
                    fileinfo += "檔案訊息 :\n";
                    fileinfo += "檔案名 : \t" + v.Name.ToString() + "\n";
                    fileinfo += "副檔名 : \t" + v.Exten.ToString() + "\n";
                    fileinfo += "檔案大小 : \t" + v.Size.ToString() + " KB\n";
                    fileinfo += "建立時間 : \t" + v.CTime.ToString() + "\n";
                    fileinfo += "最後修改時間 : \t" + v.WTime.ToString() + "\n";
                    fileinfo += "唯讀 : \t" + v.ReadOnly.ToString() + "\n";

                    richTextBox_fileinfo.Text = fileinfo;
                }

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

