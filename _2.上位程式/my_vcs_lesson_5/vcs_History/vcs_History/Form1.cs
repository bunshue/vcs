using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_History
{
    public partial class Form1 : Form
    {
        Graphics g;

        int life_st = 0;
        int life_sp = 0;
        int year_min = 10000;
        int year_max = 0;
        int position_st = 1;

        public Form1()
        {
            InitializeComponent();
            g = panel1.CreateGraphics();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);     //清除整個繪圖介面，並使用指定的背景色彩填滿它。
        }

        void find_position_st(int position)
        {
            if (position > position_st)
                position_st = position;
        }

        void find_max_min(int year)
        {
            if (year < year_min)
                year_min = year;
            if (year > year_max)
                year_max = year;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string[,] person = new string[19, 4] { 
            { "寇準", "961", "1023" , "0"},
            { "范仲淹", "989", "1052" , "2"},
            { "包拯", "999", "1062" , "4"},
            { "司馬光", "1019", "1086" , "3"},
            { "王安石", "1021", "1086" , "5"},
            { "歐陽修", "1007", "1072" , "1"},
            { "秦觀", "1049", "1100" , "-1"},
            { "黃庭堅", "1045", "1105" , "6"},
            { "宋高宗", "1107", "1187" , "6"},
            { "宋理宗", "1205", "1264" , "6"},
            { "宋度宗", "1240", "1274" , "3"},
            { "蘇軾", "1037", "1101" , "0"},
            { "岳飛", "1103", "1142" , "0"},
            { "李清照", "1084", "1155" , "1"},
            { "朱熹", "1130", "1200" , "3"},
            { "辛棄疾", "1140", "1207" , "4"},
            { "文天祥", "1236", "1283" , "4"},
            { "宋徽宗", "1082", "1135" , "2"},
            { "宋欽宗", "1100", "1156" , "5"}
            };
            int[,] data = new int[19, 4];
            
            int i;
            int age;
            int position;
            int BORDER = 50;
            int HEIGHT = 50;

            for (i = 0; i < 19; i++)
            {
                life_st = int.Parse(person[i, 1]);
                find_max_min(life_st);
                data[i, 0] = life_st;
                life_sp = int.Parse(person[i, 2]);
                find_max_min(life_sp);
                data[i, 1] = life_sp;
                age = life_sp - life_st;
                data[i, 2] = age;
                position = int.Parse(person[i, 3]);
                find_position_st(position);
                data[i, 3] = position;
                richTextBox1.Text += person[i, 0] + "\t" + life_st.ToString() + "\t" + life_sp.ToString() + "\t" + age.ToString() + "\t" + position.ToString() + "\n";
            }
            richTextBox1.Text += "min = " + year_min.ToString() + "\tmax = " + year_max.ToString() + "\n";
            richTextBox1.Text += "W = " + panel1.Width.ToString() + "\tH = " + panel1.Height.ToString() + "\n";


            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, BORDER, BORDER));
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, panel1.Width - 10, panel1.Height - 10));

            int total_width = panel1.Width;
            int total_length = year_max - year_min;
            int ratio = (total_width - 200) / total_length;

            richTextBox1.Text += "total_width = " + total_width.ToString() + "\ttotal_length = " + total_length.ToString() + "\n";
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            int offset = year_min - BORDER;

            //int position_st = 8;

            g.DrawRectangle(new Pen(Color.Green), new Rectangle(BORDER, 10, total_length * ratio, 30));
            int x;
            int y;
            int w;
            int h;
            for (i = 0; i < 19; i++)
            {
                if (data[i, 3] != -1)
                {
                    richTextBox1.Text += "AAA" + person[i, 0] + "\n";

                    x = (data[i, 0] - year_min) * ratio + BORDER;
                    y = BORDER + HEIGHT * data[i, 3];
                    w = data[i, 2] * ratio;
                    h = HEIGHT - 10;
                    g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x, y, w, h));
                    g.DrawRectangle(new Pen(Color.Black), new Rectangle(x, y, w, h));
                    g.DrawString(person[i, 0], this.Font, new SolidBrush(Color.Black), (data[i, 0] - year_min) * ratio + data[i, 2] * ratio / 2 + BORDER, BORDER + HEIGHT * data[i, 3] + 20);
                }
                else
                {
                    position_st++;
                    richTextBox1.Text += "BBB" + person[i, 0] + "\n";
                    x = (data[i, 0] - year_min) * ratio + BORDER;
                    y = BORDER + HEIGHT * position_st;
                    w = data[i, 2] * ratio;
                    h = HEIGHT - 10;
                    g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x, y, w, h));
                    g.DrawRectangle(new Pen(Color.Black), new Rectangle(x, y, w, h));
                    g.DrawString(person[i, 0], this.Font, new SolidBrush(Color.Black), (data[i, 0] - year_min) * ratio + data[i, 2] * ratio / 2 + BORDER, BORDER + HEIGHT * position_st + 20);
                }
            }

            //g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 100, 100);



        }
    }
}
