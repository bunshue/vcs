using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_GuessNumberGame
{
    public partial class Form1 : Form
    {
        int[] answer = new int[4];
        Random rd = new Random();
        int guessCtr = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            textBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i = 0;
            while (i < 4) // 產生並檢查位置i的數字，i = 0, 1, 2, 3
            {
                answer[i] = rd.Next(0, 10); //隨機產生位置i的數字 

                // 檢查有否和之前的數字重複 (線性搜尋)
                bool isDuplicate = false; // 先假設未重複
                for (int j = 0; j < i; j++)
                    if (answer[j] == answer[i])
                    {
                        isDuplicate = true;
                        break;
                    }
                if (isDuplicate) continue; // 有重複，重新產生位置 i 的數字
                i = i + 1; // 沒有重複，處理下一個位置的數字
            }

            button2.Enabled = true;
            button3.Enabled = true;
            textBox1.Enabled = true;
            richTextBox1.Clear();
            textBox1.Clear();

            guessCtr = 0;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            string input = textBox1.Text;

            guessCtr += 1; // 猜測次數加1

            string message = "第" + guessCtr + "次" + input + ": ";//後接幾A幾B

            int A = 0, B = 0; //紀錄A、B的個數

            for (int i = 0; i < 4; i++)
            {
                //取出字串input在位置i的字元，轉成整數
                int num = input[i] - '0';

                //判斷num是否存在answer陣列中 (線性搜尋)
                bool isFound = false;
                int a; // 記錄answer陣列中的位置

                for (a = 0; a < 4; a++)
                    if (answer[a] == num)
                    {
                        isFound = true;
                        break;
                    }

                if (isFound)
                { //找到該數字，判斷位置是否相同
                    if (i == a) A++;
                    else B++;
                }

            }
            message += A + "A" + B + "B"; // 串接「幾A幾B」的輸出資訊

            //是否完全猜對4A
            if (A == 4)
            {
                richTextBox1.Text += message + "\n" + "你猜對了!\n";
                textBox1.Enabled = false;
                button2.Enabled = false;
            }
            else
            {
                richTextBox1.Text += message + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string output = "答案: ";

            for (int i = 0; i < 4; i++)
            {
                output += answer[i];
            }

            MessageBox.Show(output, "答案", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
