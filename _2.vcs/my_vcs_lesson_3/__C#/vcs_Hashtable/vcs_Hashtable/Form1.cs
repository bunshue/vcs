using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for Hashtable

namespace vcs_Hashtable
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 80;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);


            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Hashtable的用法0\n";
            Hashtable mTable = new Hashtable();
            mTable.Add(5, "Apple");
            mTable.Add(1, "Banana");
            mTable.Add(4, "Cat");

            foreach (int ID in mTable.Keys)
            {
                richTextBox1.Text += ID.ToString() + "\n";
            }

            foreach (string name in mTable.Values)
            {
                richTextBox1.Text += name + "\n";
            }

            richTextBox1.Text += "直接列印某項\n";
            richTextBox1.Text += mTable[4] + "\n";

            richTextBox1.Text += "先檢查有無項目再列印\n";
            if (mTable.ContainsKey(4))
            {
                richTextBox1.Text += mTable[4] + "\n";
            }
            else
            {
                richTextBox1.Text += "無此項\n";
            }

            mTable.Remove(4);

            richTextBox1.Text += "先檢查有無項目再列印\n";
            if (mTable.ContainsKey(4))
            {
                richTextBox1.Text += mTable[4] + "\n";
            }
            else
            {
                richTextBox1.Text += "無此項\n";
            }



        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }
    }
}
