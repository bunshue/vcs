using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_GuessNumberGame2
{
    public partial class Form1 : Form
    {
        int[] ansArr = new int[4];
        TextBox[] guessText;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            guessText = new TextBox[4] { numText1, numText2, numText3, numText4 };
            reset();
        }

        //------------------------------------------------------------  # 60個

        private void resetButton_Click(object sender, EventArgs e)
        {
            reset();
        }

        private void reset()
        {
            logList.Items.Clear();
            Random rnd = new Random();
            for (int i = 0; i < 4; ++i)
            {
                guessText[i].Text = "";
                bool repeat = false;
                do
                {
                    ansArr[i] = rnd.Next(0, 10);
                    for (int j = 0; j < i; ++j)
                    {
                        if (ansArr[i] == ansArr[j])
                        {
                            repeat = true;
                        }
                    }
                }
                while (repeat);
            }
        }

        private void guessButton_Click(object sender, EventArgs e)
        {
            try
            {
                check();
                int a = 0, b = 0;
                for (int i = 0; i < 4; ++i)
                {
                    int num = int.Parse(guessText[i].Text);
                    for (int j = 0; j < 4; ++j)
                    {
                        if (num == ansArr[j])
                        {
                            if (i == j)
                            {
                                a++;
                            }
                            else
                            {
                                b++;
                            }
                        }
                    }
                }
                if (a == 4)
                {
                    MessageBox.Show("恭喜您猜中了!");
                    reset();
                }
                else
                {
                    string log = "";
                    for (int i = 0; i < 4; ++i)
                    {
                        log += guessText[i].Text;
                    }
                    logList.Items.Add(log + " -> " + a + "A" + b + "B");
                }
            }
            catch (ArgumentOutOfRangeException ex)
            {
                MessageBox.Show("您輸入數字的範圍有誤");
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show("你輸入的數字有重複");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void check()
        {
            for (int i = 0; i < 4; ++i)
            {
                int num = int.Parse(guessText[i].Text);
                if (num < 0 || num > 10)
                {
                    throw new ArgumentOutOfRangeException();
                }

                for (int j = 0; j < i; ++j)
                {
                    if (guessText[i].Text == guessText[j].Text)
                    {
                        throw new ArgumentException();
                    }
                }
            }
        }
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


