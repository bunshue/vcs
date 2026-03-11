using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_ToolStrip4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void tsbOpen_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 開檔\n";
        }

        private void tsbSave_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 存檔\n";
        }

        private void tscobFont_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (tscobFont.SelectedIndex == 0)
            {
                rtxtShow.Font = new Font("Arial", 12);
            }
            else if (tscobFont.SelectedIndex == 1)
            {
                rtxtShow.Font = new Font("Garamond", 14);
            }
            else
            {
                rtxtShow.Font = new Font("Times New Roman", 16);
            }
        }
    }
}
