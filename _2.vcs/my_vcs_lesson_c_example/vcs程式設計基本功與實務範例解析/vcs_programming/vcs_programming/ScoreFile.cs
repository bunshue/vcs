using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace vcs_programming
{
    public partial class ScoreFile : Form
    {
        public ScoreFile()
        {
            InitializeComponent();
        }

        const int MAX_CAPACITY = 50;
        string[] name = new string[MAX_CAPACITY];
        int[,] scores = new int[2, MAX_CAPACITY];
        int counter = 0;
        
        private void ScoreFile_Load(object sender, EventArgs e)
        {

        }

        void ShowData() {
            // 更新界面上顯示的訊息
            lblCounter.Text = "共有" + counter + "人";

            string res = "名字\t國文\t數學\r\n";
            for (int i = 0; i < counter; i++)
            {
                res += name[i] + "\t" + scores[0, i] + "\t" + scores[1, i] + "\r\n";
            }
            txtOutput.Text = res;
        }

        private void btn_input_Click(object sender, EventArgs e)
        {
            if (counter < MAX_CAPACITY)
            {
                name[counter] = txtName.Text;
                scores[0, counter] = Convert.ToInt32(txtChinese.Text);
                scores[1, counter] = Convert.ToInt32(txtMath.Text);
                counter++;

                ShowData(); // 更新界面上顯示的訊息
            }
            else
                MessageBox.Show("容量已滿","錯誤",
                    MessageBoxButtons.OK, MessageBoxIcon.Error);
        }

        private void btn_save_Click(object sender, EventArgs e)
        {
            sfdSave.Filter = "文字檔案(*.txt)|*.txt";

            if (sfdSave.ShowDialog() == DialogResult.OK)
            {
                //MessageBox.Show(sfdSave.FileName);
                //StreamWriter sw = new StreamWriter(sfdSave.FileName);
                FileInfo finfo = new FileInfo(sfdSave.FileName);
                StreamWriter sw = finfo.CreateText();

                // 透過StreamWriter物件sw來寫入資料
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

        private void btn_read_Click(object sender, EventArgs e)
        {
            ofdOpen.Filter = "文字檔案(*.txt)|*.txt";

            if (ofdOpen.ShowDialog() == DialogResult.OK)
            {
                FileInfo finfo = new FileInfo(ofdOpen.FileName);
                StreamReader sr = finfo.OpenText();

                int i = 0;

                while(sr.Peek() >= 0){
                    name[i] = sr.ReadLine();
                    scores[0, i] = Convert.ToInt32(sr.ReadLine());
                    scores[1, i] = Convert.ToInt32(sr.ReadLine());
                    i++;
                }

                sr.Close();

                counter = i;
                ShowData();
            }
        }

        private void btn_b_save_Click(object sender, EventArgs e)
        {
            sfdSave.Filter = "二元檔案(*.dat)|*.dat";
            
            if (sfdSave.ShowDialog() == DialogResult.OK)
            {
                //MessageBox.Show(sfdSave.FileName);
                FileStream fs = new FileStream(sfdSave.FileName,
                                      FileMode.Create);
                BinaryWriter bw = new BinaryWriter(fs);

                for (int i = 0; i < counter; i++)
                {
                    bw.Write(name[i]);
                    bw.Write(scores[0, i]);
                    bw.Write(scores[1, i]);
                }

                bw.Flush();
                bw.Close();
                fs.Close();
            }
        }

        private void btn_b_read_Click(object sender, EventArgs e)
        {
            ofdOpen.Filter = "二元檔案(*.dat)|*.dat";
            
            if (ofdOpen.ShowDialog() == DialogResult.OK)
            {
                FileStream fs = new FileStream(ofdOpen.FileName,
                                      FileMode.Open);
                BinaryReader br = new BinaryReader(fs);

                int i = 0;

                while (br.PeekChar() >= 0)
                {
                    name[i] = br.ReadString();
                    scores[0, i] = br.ReadInt32();
                    scores[1, i] = br.ReadInt32();
                    i++;
                }

                br.Close();
                fs.Close();

                counter = i;
                ShowData();
            }
        }
    }
}
