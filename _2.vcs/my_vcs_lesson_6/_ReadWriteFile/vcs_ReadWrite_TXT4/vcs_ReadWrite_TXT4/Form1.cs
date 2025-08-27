using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_TXT4
{
    public partial class Form1 : Form
    {
        const int MAX_CAPACITY = 50;
        string[] name = new string[MAX_CAPACITY];
        int[,] scores = new int[2, MAX_CAPACITY];
        int counter = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
        }

        // 更新界面上顯示的訊息
        void ShowData()
        {
            label1.Text = "共有" + counter + "人";

            string res = "名字\t國文\t數學\r\n";
            for (int i = 0; i < counter; i++)
            {
                res += name[i] + "\t" + scores[0, i] + "\t" + scores[1, i] + "\r\n";
            }
            richTextBox1.Text = res;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (counter < MAX_CAPACITY)
            {
                name[counter] = "david";
                scores[0, counter] = 100;
                scores[1, counter] = 90;

                counter++;

                ShowData(); // 更新界面上顯示的訊息
            }
            else
            {
                richTextBox2.Text += "容量已滿\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\score.txt";

            richTextBox2.Text += "開啟檔案 : " + filename + "\n";

            FileInfo finfo = new FileInfo(filename);
            StreamReader sr = finfo.OpenText();

            int i = 0;

            while (sr.Peek() >= 0)
            {
                name[i] = sr.ReadLine();
                scores[0, i] = Convert.ToInt32(sr.ReadLine());
                scores[1, i] = Convert.ToInt32(sr.ReadLine());
                i++;
            }

            sr.Close();

            counter = i;
            ShowData();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\score_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            FileInfo finfo = new FileInfo(filename);
            StreamWriter sw = finfo.CreateText();

            // 透過StreamWriter物件sw來寫入資料
            for (int i = 0; i < counter; i++)
            {
                sw.WriteLine(name[i]);
                sw.WriteLine(scores[0, i]);
                sw.WriteLine(scores[1, i]);
            }

            sw.Flush();
            sw.Close();

            richTextBox2.Text += "已存檔 : " + filename + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_bin\score.dat";

            richTextBox2.Text += "開啟檔案 : " + filename + "\n";

            FileStream fs = new FileStream(filename, FileMode.Open);
            BinaryReader br = new BinaryReader(fs);

            int i = 0;

            while (br.PeekChar() >= 0)
            {
                name[i] = br.ReadString();
                scores[0, i] = br.ReadInt32();
                scores[1, i] = br.ReadInt32();
                i++;
            }

            br.Close();
            fs.Close();

            counter = i;
            ShowData();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\score_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".dat";

            FileStream fs = new FileStream(filename, FileMode.Create);
            BinaryWriter bw = new BinaryWriter(fs);

            for (int i = 0; i < counter; i++)
            {
                bw.Write(name[i]);
                bw.Write(scores[0, i]);
                bw.Write(scores[1, i]);
            }

            bw.Flush();
            bw.Close();
            fs.Close();

            richTextBox2.Text += "已存檔 : " + filename + "\n";
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            for (int i = 0; i < counter; i++)
            {
                name[i] = "";
                scores[0, i] = 0;
                scores[1, i] = 0;
            }
            counter = 0;
            label1.Text = "共有" + counter + "人";
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }
    }
}
