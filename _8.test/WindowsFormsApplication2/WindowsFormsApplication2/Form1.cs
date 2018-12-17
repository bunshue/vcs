using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace WindowsFormsApplication2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += File.ReadAllText(openFileDialog1.FileName, Encoding.Default);
                //richTextBox1.Text += File.ReadAllText(openFileDialog1.FileName, Encoding.Unicode);
                richTextBox2.Text += "filename : " + openFileDialog1.FileName + "\n";
                richTextBox2.Text += "length = " + richTextBox1.Text.Length.ToString() + "\n";
                richTextBox2.Text += "lines = " + richTextBox1.Lines.Length.ToString() + "\n";
                richTextBox2.Text += "TextLength = " + richTextBox1.TextLength.ToString() + "\n";

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
            int i;
            for (i = 0; i < 256; i++)
            {
                richTextBox2.Text += i.ToString();
            }
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                File.WriteAllText(saveFileDialog1.FileName, richTextBox2.Text, Encoding.Default);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
            int i;
            byte[] aaaaa = new byte[256];
            for (i = 0; i < 256; i++)
            {
                //richTextBox2.Text += i.ToString();
                aaaaa[i] = (byte)i;
            }
            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                File.WriteAllBytes(saveFileDialog1.FileName, aaaaa);
            }

        }

    }
}
