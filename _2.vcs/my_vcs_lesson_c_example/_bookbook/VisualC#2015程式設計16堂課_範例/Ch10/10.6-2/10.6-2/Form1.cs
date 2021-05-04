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

        private void stepButton_Click(object sender, EventArgs e)
        {
            TextBox[] textArray = new TextBox[] { numText1, numText2, numText3, numText4, numText5, numText6, numText7, numText8 };

            if (stepButton.Text == "開始") {
                stepButton.Text = "下一步";

                for (int i = 7; i > 0; i--) {
                    for (int j = 0; j < i; j++) {
                         if (int.Parse(textArray[j].Text) > int.Parse(textArray[j+1].Text)) {
                            string tmp = textArray[j+1].Text;
                            textArray[j+1].Text = textArray[j].Text;
                            textArray[j].Text = tmp;
                        }
                    }
                }
                for (int i = 0; i < 8; i++)
                    textArray[i].BackColor = Color.LightBlue;

                targetText.Enabled = false;
            }
            else {
                int i, lowIndex = 0, highIndex = 0;

                for (i = 0; i < 8; i++)
                    if (textArray[i].BackColor == Color.LightBlue)
                        break;
                lowIndex = i;

                for (i = 7; i > 0; i--)
                    if (textArray[i].BackColor == Color.LightBlue)
                        break;
                highIndex = i;

                for (i = 0; i < 8; i++)
                    textArray[i].BackColor = SystemColors.Window;


                int midIndex = (highIndex + lowIndex) / 2;
                if (textArray[midIndex].Text == targetText.Text) {
                    MessageBox.Show("你所指定的數字在索引 " + midIndex + "的位置!");
                    stepButton.Text = "開始";
                    targetText.Enabled = true;
                }
                else {
                    if (int.Parse(textArray[midIndex].Text) > int.Parse(targetText.Text))
                        highIndex = midIndex - 1;
                    else
                        lowIndex = midIndex + 1;

                    if (lowIndex > highIndex) {
                        MessageBox.Show("程式在陣列中沒有找到你所指定的數字!");
                        stepButton.Text = "開始";
                        targetText.Enabled = true;
                    }
                    else
                        for (i = lowIndex; i <= highIndex; i++)
                            textArray[i].BackColor = Color.LightBlue;
                }
            }
        }

    }
}
