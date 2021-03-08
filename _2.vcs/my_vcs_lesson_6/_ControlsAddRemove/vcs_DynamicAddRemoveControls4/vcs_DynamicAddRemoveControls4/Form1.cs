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
        Color[] colorSet = { Color.Red, Color.Blue, Color.Green, Color.Gray };
        Label[] in_ner = new Label[100];
        int x = 0, y = 0, not_empty = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            add_controls_example();

            for (int i = 0; i < 4; i++)
            {
                richTextBox1.Text += colorSet[i].Name.ToString() + "\n";


            }
        }

        void add_controls_example()
        {
            int W = 35;
            int H = 35;
            int dx = 40;
            int dy = 40;

            //-----------隨機產生空位
            Random rnd = new Random();
            not_empty = rnd.Next(1, 100);

            richTextBox1.Text += "not_empty = " + not_empty.ToString() + "\n";

            //動態產生元件並指定屬性與事件
            for (int i = 0; i < in_ner.Length; ++i)
            {
                if (i > not_empty)  //空位
                {
                    in_ner[i] = new Label();
                    in_ner[i].AutoSize = false;
                    //in_ner [i+1].Name = "label" + i;
                    //-------
                    //statets = new tray_state();
                    //ts.number = i + 1;
                    //ts.state = "empty";
                    in_ner[i].Tag = "sample : " + i.ToString() + " is " + "empty";
                    in_ner[i].MouseHover += MouseHover_Handler;
                    in_ner[i].MouseLeave += MouseLeave_Handler;
                    in_ner[i].Click += MouseClick_Handler;
                    //-------
                    in_ner[i].Text = "  ";
                    in_ner[i].BackColor = Color.Gray;
                    in_ner[i].Location = new Point(x, y);
                    in_ner[i].Size = new Size(W, H);
                    this.Controls.Add(in_ner[i]);

                    //richTextBox1.Text += in_ner[i].Width.ToString() + " " + in_ner[i].Height.ToString() + ", ";
                    x += dx;
                    if ((i + 1) % 10 == 0)
                    {
                        x = 0;
                        y += dy;
                    }
                }
                else
                {
                    in_ner[i] = new Label();
                    in_ner[i].AutoSize = false;
                    //in_ner [i+1].Name = "label" + i;
                    //-------
                    //statets = new state();
                    //ts.number = i + 1;
                    //ts.state = "red";
                    in_ner[i].Tag = "sample : " + i.ToString() + " is " + "red";
                    in_ner[i].MouseHover += MouseHover_Handler;
                    in_ner[i].MouseLeave += MouseLeave_Handler;
                    in_ner[i].Click += MouseClick_Handler;
                    //-------
                    in_ner[i].Text = "  ";
                    in_ner[i].BackColor = Color.Red;
                    in_ner[i].Location = new Point(x, y);
                    in_ner[i].Size = new Size(W, H);
                    this.Controls.Add(in_ner[i]);
                    x += dx;

                    if ((i + 1) % 10 == 0)
                    {
                        x = 0;
                        y += dy;
                    }
                }
            }
        }

        private void MouseHover_Handler(object sender, EventArgs e)
        {
            Application.DoEvents();
            ToolTip tooltip = new ToolTip();
            this.Cursor = Cursors.Hand;
            for (int i = 0; i < in_ner.Length; i++)
            {
                if (sender == in_ner[i]) // event is from txtBox
                {
                    tooltip.AutoPopDelay = 10000;
                    tooltip.ToolTipIcon = ToolTipIcon.Info;
                    tooltip.ToolTipTitle = "Sample info";
                    tooltip.ShowAlways = true;
                    tooltip.SetToolTip(in_ner[i], in_ner[i].Tag.ToString());
                }
            }
        }

        private void MouseLeave_Handler(object sender, EventArgs e)
        {
            this.Cursor = Cursors.Default;
        }

        private void MouseClick_Handler(object sender, EventArgs e)
        {
            for (int i = 0; i < in_ner.Length; i++)
            {
                if (sender == in_ner[i])
                {
                    //richTextBox1.Text += "click " + i.ToString() + "\n";
                    setup_next_color(in_ner[i]);
                    break;
                }
            }
        }

        void setup_next_color(Label lbl)
        {
            richTextBox1.Text += "old color = " + lbl.BackColor + "\n";

            int i;
            int next = 0;
            for (i = 0; i < colorSet.Length; i++)
            {
                richTextBox1.Text += colorSet[i].Name.ToString() + "\n";
                if (colorSet[i] == lbl.BackColor)
                {
                    next = (i + 1) % 4;
                    //richTextBox1.Text += "XXXXXXXX new color = " + colorSet[next] + "\n";
                    lbl.BackColor = colorSet[next];
                    break;
                }
            }
        }
    }
}
