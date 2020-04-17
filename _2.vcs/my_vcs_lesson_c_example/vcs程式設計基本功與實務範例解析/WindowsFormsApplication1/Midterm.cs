using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace WindowsFormsApplication1
{
    public partial class Midterm : Form
    {
        public Midterm()
        {
            InitializeComponent();
        }

        const int MAX_CAPACITY = 50;
        string[] name = new string[MAX_CAPACITY];
        int[,] scores = new int[2, MAX_CAPACITY];
        int counter = 0;

        void showData()
        {
            lblCounter.Text = "共有" + counter + "人";

            string res = "名字\t國文\t數學\r\n";
            res += "====\t====\t====\r\n";
            for (int i = 0; i < counter; i++)
            {
                res += name[i] + "\t" + scores[0, i] + "\t" + scores[1, i] + "\r\n";
            }
            txtOutput.Text = res;
        }

        private void 結束ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void Midterm_Load(object sender, EventArgs e)
        {
           
        }

        private void btn_input_Click(object sender, EventArgs e)
        {
            if (counter < MAX_CAPACITY)
            {
                name[counter] = txtName.Text;
                scores[0, counter] = Convert.ToInt32(txtChinese.Text);
                scores[1, counter] = Convert.ToInt32(txtMath.Text);
                counter++;

                showData();

                txtName.Text = "";
                txtChinese.Text = "";
                txtMath.Text = "";
                txtName.Focus();
            }
            else
                MessageBox.Show("容量已滿", "錯誤",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        private void mSave_Click(object sender, EventArgs e)
        {
            if (sfdSave.ShowDialog() == DialogResult.OK)
            {
                //MessageBox.Show(sfdSave.FileName);
                FileInfo finfo = new FileInfo(sfdSave.FileName);
                StreamWriter sw = finfo.CreateText();

                for (int i = 0; i < counter; i++)
                {
                    sw.WriteLine(name[i]);
                    sw.WriteLine(scores[0, i]);
                    sw.WriteLine(scores[1, i]);
                }

                sw.Flush();
                sw.Close();
            }
        }

        private void mLoad_Click(object sender, EventArgs e)
        {
            if (ofdOpen.ShowDialog() == DialogResult.OK)
            {
                FileInfo finfo = new FileInfo(ofdOpen.FileName);
                StreamReader sr = finfo.OpenText();

                int i = 0;

                while (sr.Peek() >= 0)
                {
                    name[i] = sr.ReadLine();
                    scores[0, i] = Convert.ToInt32(sr.ReadLine());
                    scores[1, i] = Convert.ToInt32(sr.ReadLine());
                    i++;
                }

                sr.Close();

                counter = i;
                showData();
            }
        }

        private void mSumRank_Click(object sender, EventArgs e)
        {
            int[] sum = new int[counter];

            for (int i = 0; i < counter; i++)
                    sum[i] = scores[0, i] + scores[1, i];

            int[] rank = new int[counter];

           
            for (int i = 0; i < counter; i++)
            {
                rank[i] = 1;
                for (int j = 0; j < counter; j++)
                    if (scores[0, j] + scores[1, j] > sum[i]) rank[i]++;
            }

            lblCounter.Text = "共有" + counter + "人";

            string res = "名字\t國文\t數學\t總分\t名次\r\n";
            res += "====\t====\t====\t====\t====\r\n";
            for (int i = 0; i < counter; i++)
            {
                res += name[i] + "\t" + scores[0, i] + "\t" + scores[1, i];
                res += "\t" + sum[i] + "\t" + rank[i] + "\r\n";
            }
            txtOutput.Text = res;
           
        }

        private void mScoreStatistics_Click(object sender, EventArgs e)
        {

            lblCounter.Text = "共有" + counter + "人";

            string res = "名字\t國文\t數學\r\n";
            res += "====\t====\t====\r\n";
            for (int i = 0; i < counter; i++)
            {
                res += name[i] + "\t" + scores[0, i] + "\t" + scores[1, i] + "\r\n";
            }

           
            int pass1 = 0, pass2 = 0;

            for (int i = 0; i < counter; i++)
            {
                if (scores[0, i] >= 60) pass1++;
                if (scores[1, i] >= 60) pass2++;
            }

            res += "====\t====\t====\r\n";

            res += "及格:\t" + pass1 + "人\t" + pass2 + "人\r\n";
            res += "不及格:\t" + (counter-pass1) + "人\t" + (counter-pass2) + "人\r\n";

            txtOutput.Text = res;
        }
    }
}
