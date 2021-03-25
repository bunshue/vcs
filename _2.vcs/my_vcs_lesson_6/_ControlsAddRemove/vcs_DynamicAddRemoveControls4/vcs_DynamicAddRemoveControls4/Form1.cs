using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DynamicAddRemoveControls4
{
    public partial class Form1 : Form
    {
        Color[] colorSet = { Color.Red, Color.Orange, Color.Yellow, Color.Lime };
        Label[] new_label = new Label[100];
        int x_st = 0;
        int y_st = 0;
        int not_empty = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            add_controls_example();
        }

        void add_controls_example()
        {
            int W = 45;
            int H = 45;
            int dx = 50;
            int dy = 50;

            //-----------隨機產生空位
            Random rand = new Random();
            not_empty = rand.Next(1, 100);

            richTextBox1.Text += "not_empty = " + not_empty.ToString() + "\n";

            //動態產生元件並指定屬性與事件
            for (int i = 0; i < new_label.Length; i++)
            {
                new_label[i] = new Label();
                new_label[i].AutoSize = false;
                new_label[i].Name = "label" + i.ToString();
                new_label[i].Text = (i + 1).ToString();
                new_label[i].MouseHover += MouseHover_Handler;
                new_label[i].MouseLeave += MouseLeave_Handler;
                new_label[i].Click += MouseClick_Handler;
                new_label[i].Location = new Point(x_st, y_st);
                new_label[i].Size = new Size(W, H);
                if (i > not_empty)  //空位
                {
                    new_label[i].Tag = "sample : " + i.ToString() + " is " + "empty";
                    new_label[i].BackColor = Color.Gray;
                }
                else
                {
                    new_label[i].Tag = "sample : " + i.ToString() + " is " + "red";
                    new_label[i].BackColor = Color.Red;
                }
                this.Controls.Add(new_label[i]);
                x_st += dx;

                if ((i % 10) == 9)
                {
                    x_st = 0;
                    y_st += dy;
                }
            }
        }

        private void MouseHover_Handler(object sender, EventArgs e)
        {
            //Application.DoEvents();
            ToolTip tooltip = new ToolTip();
            //this.Cursor = Cursors.Hand;
            for (int i = 0; i < new_label.Length; i++)
            {
                if (sender == new_label[i]) // event is from txtBox
                {
                    tooltip.AutoPopDelay = 10000;
                    tooltip.ToolTipIcon = ToolTipIcon.Info;
                    tooltip.ToolTipTitle = "Sample info";
                    tooltip.ShowAlways = true;
                    tooltip.SetToolTip(new_label[i], new_label[i].Tag.ToString());
                }
            }
        }

        private void MouseLeave_Handler(object sender, EventArgs e)
        {
            //this.Cursor = Cursors.Default;
        }

        private void MouseClick_Handler(object sender, EventArgs e)
        {
            for (int i = 0; i < new_label.Length; i++)
            {
                if (sender == new_label[i])
                {
                    //richTextBox1.Text += "click " + i.ToString() + "\n";
                    setup_next_color(new_label[i]);
                    break;
                }
            }
        }

        void setup_next_color(Label lbl)
        {
            bool flag_match = false;
            //richTextBox1.Text += "old color = " + lbl.BackColor + "\n";
            int i;
            int next = 0;
            for (i = 0; i < colorSet.Length; i++)
            {
                //richTextBox1.Text += colorSet[i].Name.ToString() + "\n";
                if (colorSet[i] == lbl.BackColor)
                {
                    next = (i + 1) % 4;
                    lbl.BackColor = colorSet[next];
                    flag_match = true;
                    break;
                }
            }
            if (flag_match == false)
            {
                lbl.BackColor = Color.Red;
            }
        }
    }
}
