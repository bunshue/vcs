using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Time_Notifier
{
    public partial class Form1 : Form
    {
        int check_list_index = 1;
        private const int BORDER = 20;
        //List<DateTime> check_list_data = new List<DateTime>();

        List<Check_List_Data> check_list_data = new List<Check_List_Data>();

        public class Check_List_Data
        {
            public int index;
            public int type;
            public DateTime date_time_data;
            public Check_List_Data(int i, int n, DateTime dt)
            {
                this.index = i;
                this.type = n;
                this.date_time_data = dt;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            DateTime dt = DateTime.Now;

            digitalDisplayControl1.DigitText = dt.ToString("HH:mm:ss");

            numericUpDown1.Value = dt.Year;
            numericUpDown2.Value = dt.Month;
            numericUpDown3.Value = dt.Day;

            textBox1.Text = dt.ToString("HHmm");
        }

        void show_item_location()
        {
            int W = 1920;
            int H = 1080;
            int w = 640;
            int h = 480;
            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = BORDER;
            y_st = BORDER;
            digitalDisplayControl1.Location = new Point(x_st, y_st);

            groupBox1.Size = new Size(500, 140);
            groupBox1.Location = new Point(x_st, y_st + 100);

            groupBox2.Size = new Size(500, 250);
            groupBox2.Location = new Point(x_st, y_st + 100 + 140);

            //button
            x_st = BORDER;
            y_st = BORDER;
            dx = 110;
            dy = 60;
            numericUpDown1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            numericUpDown2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            numericUpDown3.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            textBox1.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 3);

            dx = 90;
            rb0.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            rb1.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            rb2.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            rb3.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 1);

            richTextBox1.Location = new Point(BORDER + 500 + BORDER, BORDER);
            richTextBox1.Size = new Size(300, 500);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            W = BORDER + 500 + BORDER + 300 + BORDER;
            H = BORDER + 500 + BORDER;
            this.ClientSize = new Size(W, H);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt_now = DateTime.Now;
            toolStripStatusLabel1.Text = dt_now.ToString();

            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");


            int i;
            for (i = 0; i < check_list_data.Count; i++)
            {
                //richTextBox1.Text += "name : " + folderinfos[i].foldername + " path : " + folderinfos[i].folderpath + " size : " + folderinfos[i].filesize.ToString() + "\n";
                int ii = check_list_data[i].index;
                int tt = check_list_data[i].type;
                DateTime dd = check_list_data[i].date_time_data;

                //if ((dd - dt_now).TotalSeconds < 0)
                if (dd < dt_now)
                {
                    richTextBox1.Text += ii.ToString() + "\t" + tt.ToString() + "\t" + dd.ToString("yyyy/MM/dd HH:mm:ss") + "\t時間到";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string dt = textBox1.Text;
            int len = dt.Length;
            if (len != 4)
            {
                richTextBox1.Text += "時間錯誤\n";
                textBox1.Clear();
                return;
            }
            int i;
            for (i = 0; i < 4; i++)
            {
                if (((int)dt[i] < '0') || ((int)dt[i] > '9'))
                {
                    richTextBox1.Text += "時間錯誤\n";
                    textBox1.Clear();
                    return;

                }
            }
            //int hh = int.Parse(dt[0].ToString() + dt[1].ToString());
            //int mm = int.Parse(dt[2].ToString() + dt[3].ToString());

            int hh = int.Parse(dt.Substring(0, 2));
            int mm = int.Parse(dt.Substring(2, 2));

            if ((hh < 0) || hh > 23)
            {
                richTextBox1.Text += "時間錯誤\n";
                textBox1.Clear();
                return;
            }

            if ((mm < 0) || mm > 59)
            {
                richTextBox1.Text += "時間錯誤\n";
                textBox1.Clear();
                return;
            }

            richTextBox1.Text += "時間正確\t" + hh.ToString() + " 時 " + mm.ToString() + " 分" + "\n";

            int type = 0;
            int add_minutes = 0;
            if (rb0.Checked == true)
            {
                type = 0;
                //add_minutes = 60;
                add_minutes = 3;
            }
            else if (rb1.Checked == true)
            {
                type = 1;
                add_minutes = 60 * 2 - 30;
            }
            else if (rb2.Checked == true)
            {
                type = 2;
                add_minutes = 60 * 2 - 10;
            }
            else if (rb1.Checked == true)
            {
                type = 3;
                add_minutes = 0;
            }
            else
            {
                type = 3;
                add_minutes = 0;
            }

            int year = (int)numericUpDown1.Value;
            int month = (int)numericUpDown2.Value;
            int day = (int)numericUpDown3.Value;

            DateTime dt_target = new DateTime(year, month, day, hh, mm, 0, 0);	//年月日時分秒毫秒
            dt_target = dt_target.AddMinutes(add_minutes);
            richTextBox1.Text += "目標 :" + dt_target.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            check_list_data.Add(new Check_List_Data(check_list_index, type, dt_target));
            check_list_index++;


        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            for (i = 0; i < check_list_data.Count; i++)
            {
                //richTextBox1.Text += "name : " + folderinfos[i].foldername + " path : " + folderinfos[i].folderpath + " size : " + folderinfos[i].filesize.ToString() + "\n";
                int ii = check_list_data[i].index;
                int tt = check_list_data[i].type;
                DateTime dd = check_list_data[i].date_time_data;
                richTextBox1.Text += ii.ToString() + "\t" + tt.ToString() + "\t" + dd.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
            }

            /*
            check_list_data.Add(type, dt_target);

            foreach (DateTime dddd in check_list_data)
            {
                richTextBox1.Text += "目標 :" + dddd.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                //this.listBox1.Items.Add(sss);
            }
            */

        }

        void remove_check_list_data(int index)
        {
            int i;
            for (i = 0; i < check_list_data.Count; i++)
            {
                int ii = check_list_data[i].index;
                if (ii == index)
                {
                    richTextBox1.Text += "找到 index 在i = " + i.ToString() + "\n";
                    int tt = check_list_data[i].type;
                    DateTime dd = check_list_data[i].date_time_data;
                    richTextBox1.Text += ii.ToString() + "\t" + tt.ToString() + "\t" + dd.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

                    richTextBox1.Text += "刪除這個項目\n";

                    check_list_data.RemoveAt(i);

                }

            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int index = 3;
            remove_check_list_data(index);
        }
    }
}


//check_list_data.Add(p);       //目前只能 儲存/加入 一個路徑
//check_list_data.Remove(folderBrowserDialog1.SelectedPath);
//check_list_data.Clear();


