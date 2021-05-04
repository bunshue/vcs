using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Resize
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int[] score = new int[0];
            string s = "";
            do
            {
                s = Microsoft.VisualBasic.Interaction.InputBox("請輸入成績");
                if (s != "")   //若s不是空字串
                {
                    Array.Resize(ref score, score.Length + 1);    //陣列大小+1
                    score[score.Length - 1] = Convert.ToInt32(s); //存入最後元素中
                }
            } while (s != "");      //s不是空字串就繼續迴圈
            int sum = 0;           //預設總和sum = 0
            foreach (int x in score) //用foreach迴圈逐一讀取陣列元素值
            {
                sum += x;        //總和加陣列元素值
            }
            MessageBox.Show("平均分數=" + (sum / score.Length).ToString());
            Application.Exit();
        }
    }
}
