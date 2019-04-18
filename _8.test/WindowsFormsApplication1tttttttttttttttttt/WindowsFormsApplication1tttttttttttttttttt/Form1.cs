using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for WebClient

namespace WindowsFormsApplication1tttttttttttttttttt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //richTextBox2.Text += Clipboard.GetData(DataFormats.Text);
            richTextBox2.Text += Clipboard.GetText();   //建議用此
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Clipboard.Clear();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿 累計
            //Clipboard.SetData(DataFormats.Text, Clipboard.GetData(DataFormats.Text) + richTextBox1.Text + "\n");
            Clipboard.SetDataObject(Clipboard.GetText() + richTextBox1.Text + "\n");      //建議用此

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            try
            {
                //下載純文字
                WebClient wc = new WebClient();
                string somestring = wc.DownloadString("http://snowball.tartarus.org/otherlangs/english_cpp.txt");
                richTextBox2.Text += somestring;
            }
            catch (WebException we)
            {
                // add some kind of error processing
                MessageBox.Show(we.ToString());
            }

        }


    }
}
