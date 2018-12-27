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

        public Form1()
        {
            InitializeComponent();
            g = panel1.CreateGraphics();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            g.Clear(BackColor);     //清除整個繪圖介面，並使用指定的背景色彩填滿它。
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
            string[,] person = new string[8, 3] { { "蘇軾", "1037", "1101" }, { "岳飛", "1103", "1142" }, { "李清照", "1084", "1155" }, { "朱熹", "1130", "1200" },
            { "辛棄疾", "1140", "1207" }, { "文天祥", "1236", "1283" }, { "宋徽宗", "1082", "1135" }, { "宋欽宗", "1100", "1156" } };
            int[,] data = new int[8, 3];
            
            int i;
            int age;
            for (i = 0; i < 8; i++)
            {
                life_st = int.Parse(person[i, 1]);
                find_max_min(life_st);
                data[i, 0] = life_st;
                life_sp = int.Parse(person[i, 2]);
                find_max_min(life_sp);
                data[i, 1] = life_sp;
                age = life_sp - life_st;
                data[i, 2] = age;
                richTextBox1.Text += person[i, 0] + "\t" + life_st.ToString() + "\t" + life_sp.ToString() + "\t" + age.ToString() + "\n";


            }
            richTextBox1.Text += "min = " + year_min.ToString() + "\tmax = " + year_max.ToString() + "\n";
            richTextBox1.Text += "W = " + panel1.Width.ToString() + "\tH = " + panel1.Height.ToString() + "\n";


            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, 100, 100));
            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, panel1.Width - 10, panel1.Height - 10));

            int total_width = panel1.Width;
            int total_length = year_max - year_min;
            int ratio = (total_width - 200) / total_length;

            richTextBox1.Text += "total_width = " + total_width.ToString() + "\ttotal_length = " + total_length.ToString() + "\n";
            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";
            
            int offset = year_min - 100;

            g.DrawRectangle(new Pen(Color.Green), new Rectangle(100, 30, total_length * ratio, 30));
            for (i = 0; i < 8; i++)
            {
                g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle((data[i, 0] - year_min) * ratio + 100, 100 + 50 * i, data[i, 2] * ratio, 40));
                g.DrawRectangle(new Pen(Color.Black), new Rectangle((data[i, 0] - year_min) * ratio + 100, 100 + 50 * i, data[i, 2] * ratio, 40));
                g.DrawString(person[i, 0], this.Font, new SolidBrush(Color.Black), (data[i, 0] - year_min) * ratio + data[i, 2] * ratio / 2 + 100, 100 + 50 * i + 20);
            }

            //g.DrawString("畫字串", this.Font, new SolidBrush(Color.Black), 100, 100);



        }
    }
}
