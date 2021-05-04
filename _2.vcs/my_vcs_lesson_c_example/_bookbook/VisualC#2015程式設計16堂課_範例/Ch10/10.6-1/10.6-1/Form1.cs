using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void startButton_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            startButton.Text = "1";
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            TextBox[] textArray = new TextBox[] { numText1, numText2, numText3, numText4, numText5, numText6, numText7, numText8 };
            for (int i = 0; i < 8; i++)
                textArray[i].BackColor = SystemColors.Window;

            int check = int.Parse(startButton.Text);
            for (int j = 0; check > (7 - j); j++)
                check -= (7 - j);

            check--;
            textArray[check].BackColor = Color.LightBlue;
            textArray[check+1].BackColor = Color.LightBlue;
            string tmp;
            if (int.Parse(textArray[check].Text) > int.Parse(textArray[check+1].Text)) {
                textArray[check].BackColor = Color.Pink;
                textArray[check+1].BackColor = Color.Pink;
                tmp = textArray[check+1].Text;
                textArray[check+1].Text = textArray[check].Text;
                textArray[check].Text = tmp;
            }

            if (startButton.Text == "28") {
                timer1.Enabled = false;
                textArray[check].BackColor = SystemColors.Window;
                textArray[check + 1].BackColor = SystemColors.Window;
                startButton.Text = "開始排序";
            }
            else
                startButton.Text = (int.Parse(startButton.Text) + 1).ToString();
        }

    }
}
