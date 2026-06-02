using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Collections;   //for Hashtable

namespace vcs_ComboBox1
{
    public partial class Form1 : Form
    {
        private ImageList G_ImageList;//聲明ImageList字段

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //年月日

            // 年下拉式清單預設值100年前
            comboBox_year.Text = (DateTime.Now.Year - 100).ToString();
            comboBox_month.Text = "1"; // 月下拉式清單預設值1
            comboBox_day.Text = "1";      // 日下拉式清單預設值 1

            // 年下拉式清單的範圍100年前~今年
            for (int i = DateTime.Now.Year - 100; i <= DateTime.Now.Year; i++)
            {
                comboBox_year.Items.Add(i.ToString());
            }

            for (int i = 1; i <= 12; i++) // 月下拉式清單的範圍是1-12
            {
                comboBox_month.Items.Add(i.ToString());
            }

            for (int i = 1; i <= 31; i++) // 日下拉式清單的範圍是1-31
            {
                comboBox_day.Items.Add(i.ToString());
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int w = 400;
            int h = 150;

            groupBox2.Size = new Size(w, h * 2 / 2);
            groupBox6.Size = new Size(w, h * 3 / 2);

            x_st = 10;
            y_st = 10;
            dx = w + 10;
            dy = h + 10;
            groupBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox6.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox1.Size = new Size(200, 150);
            pictureBox1.BackColor = Color.Pink;

            richTextBox1.Size = new Size(320, 600);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 800);
            this.Text = "vcs_ComboBox1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //6060

        Hashtable ht = new Hashtable();
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU";

        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();  // 獲取所有的文件
            foreach (FileSystemInfo fi in fileinfo)  // 遍歷獲取到的文件
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        //ht.add(key, value), key不能重複
                        ht.Add(forename, fullname);

                        richTextBox1.Text += "加入 前檔名 : " + forename + "\t長檔名 : " + fullname + "\n";
                    }
                }
            }
        }

        private void showPic(string name)
        {
            this.pictureBox1.ImageLocation = name;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //尋找檔案
            GetAllFiles(foldername);

            foreach (DictionaryEntry de in ht)
            {
                this.comboBox6.Items.Add(de.Key);
            }
            if (comboBox6.Items.Count > 0)
            {
                comboBox6.SelectedIndex = 0;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //顯示
            richTextBox1.Text += comboBox6.SelectedIndex.ToString() + "\n";

            if (comboBox6.SelectedIndex == -1)
            {
                return;
            }
            if (ht.Values.Count > 0)
            {
                showPic(ht[this.comboBox6.Text].ToString());
            }
            else
            {
                MessageBox.Show("目前還沒有圖片相關訊息！！！");
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Info
            int len = ht.Count;

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            //方法一：遍歷traversal 1:
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "key = " + de.Key + "\t" + "value = " + de.Value + "\n";
            }

            //方法二：遍歷traversal 2:
            IDictionaryEnumerator d = ht.GetEnumerator();
            while (d.MoveNext())
            {
                //richTextBox1.Text += "key = " + d.Entry.Key + "\t" + "value = " + d.Entry.Value + "\n";
            }
        }

        private void bt_add_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "加入 : " + comboBox_add.Text + "\n";
            // 將下拉式清單所輸入的值放入下拉式清單的選項內
            comboBox_add.Items.Add(comboBox_add.Text);
        }
    }
}
