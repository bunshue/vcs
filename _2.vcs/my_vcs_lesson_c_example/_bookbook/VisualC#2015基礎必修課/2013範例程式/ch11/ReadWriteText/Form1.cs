using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO; 

namespace ReadWriteText
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnRead_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //建立FileInfo類別的f物件，該物件可用來建立、複製、刪除檔案
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                //宣告StreamReader類別的sr物件, 用來讀出資料檔的資料
                StreamReader sr = f.OpenText();   
                //將資料一次讀出並放入richTextBox1
                richTextBox1.Text = sr.ReadToEnd();
                sr.Close();    //關閉目前的資料流
                MessageBox.Show("讀檔成功");
            }
        }

        private void btnWrite_Click(object sender, EventArgs e)
        {
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //建立FileInfo類別的f物件，該物件可用來建立、複製、刪除檔案 
                FileInfo f = new FileInfo(saveFileDialog1.FileName );
                //宣告StreamWriter類別的sw物件, 用來寫入資料到資料檔
                StreamWriter sw = f.CreateText();
                //將richTextBox1的資料寫入到指定的檔案
                sw.WriteLine (richTextBox1.Text);
                sw.Flush();    //將存在Buffer緩衝區內寫入指定的檔案內
                sw.Close();    //關閉目前的資料流
                MessageBox.Show("寫入成功");
            }
        }

        private void btnCls_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear(); 
        }
    }
}
