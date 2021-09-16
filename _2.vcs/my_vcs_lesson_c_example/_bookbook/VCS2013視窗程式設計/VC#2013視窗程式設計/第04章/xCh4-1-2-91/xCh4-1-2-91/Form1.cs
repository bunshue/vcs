using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_2_91
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.DefaultExt = "bmp";
            openFileDialog1.Filter = "Bitmap 檔|*.bmp|JPEG 檔|*.jpg";
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.ShowDialog();
            if (openFileDialog1.FileName == "")
            {
                return;
            }

            try
            {
                Image myImage= 
                    Image.FromFile(openFileDialog1.FileName);
                Clipboard.SetImage(myImage);

                DataFormats.Format df = 
                    DataFormats.GetFormat(DataFormats.Bitmap);
                 if (richTextBox1.CanPaste(df))
                {
                    richTextBox1.Paste(df);
                }
            }
            catch
            {
                MessageBox.Show("無法插入圖片", "錯誤", 
                    MessageBoxButtons.OK, 
                    MessageBoxIcon.Error);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionLength == 0)
                richTextBox1.SelectAll();
            richTextBox1.Cut();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (richTextBox1.SelectionLength == 0)
                richTextBox1.SelectAll();
            richTextBox1.Copy();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox2.Paste();
        }
    }
}
