using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_2_4_51
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void toolStripComboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            toolStripTextBox1.Font = new Font(
                toolStripTextBox1.Font.Name,
                Convert.ToSingle(toolStripComboBox1.SelectedItem),
                toolStripTextBox1.Font.Style);
        }

        private void toolStripTextBox1_TextChanged(object sender, EventArgs e)
        {
            if (toolStripMenuItem2.Checked)
                if (toolStripMenuItem3.Checked)
                    toolStripTextBox1.Font = new Font(Font, FontStyle.Bold | FontStyle.Italic);
                else
                    toolStripTextBox1.Font = new Font(Font, FontStyle.Bold);
            else
                if (toolStripMenuItem3.Checked)
                    toolStripTextBox1.Font = new Font(Font, FontStyle.Italic);
                else
                    toolStripTextBox1.Font = new Font(Font, FontStyle.Regular);
        }
    }
}
