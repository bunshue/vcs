using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.DefaultExt = "*.rtf";
            openFileDialog1.Filter = "RTF檔|*.rtf";

            if(openFileDialog1.ShowDialog()==
                System.Windows.Forms.DialogResult.OK &&
                openFileDialog1.FileName.Length>0)
            {
                richTextBox1.LoadFile(openFileDialog1.FileName);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "純文字檔|*.txt";

            if (openFileDialog1.ShowDialog() ==System.Windows.Forms.DialogResult.OK )
            {
                richTextBox1.LoadFile(
                    openFileDialog1.FileName,
                    RichTextBoxStreamType.PlainText);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Filter = "RTF檔|*.rtf";
 
            if (saveFileDialog1.ShowDialog() ==
                System.Windows.Forms.DialogResult.OK &&
                saveFileDialog1.FileName.Length > 0)
            {
                richTextBox1.SaveFile(saveFileDialog1.FileName);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Filter = "RTF檔|*.rtf";

            if (saveFileDialog1.ShowDialog() ==
                 System.Windows.Forms.DialogResult.OK &&
                 saveFileDialog1.FileName.Length > 0)
            {
                richTextBox1.LoadFile(
                   saveFileDialog1.FileName,
                    RichTextBoxStreamType.PlainText);
            }
        }
    }
}
