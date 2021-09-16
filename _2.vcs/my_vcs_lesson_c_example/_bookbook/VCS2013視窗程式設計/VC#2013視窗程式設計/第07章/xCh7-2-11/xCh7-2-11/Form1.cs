using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh7_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            fontDialog1.AllowScriptChange = false;
            fontDialog1.AllowVectorFonts = false;
            fontDialog1.AllowVerticalFonts = false;
            fontDialog1.ShowApply = false;
            fontDialog1.ShowColor = false;
            fontDialog1.ShowEffects = false;
            fontDialog1.ShowHelp = false;
            fontDialog1.FixedPitchOnly = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (fontDialog1.ShowDialog() != DialogResult.Cancel)
            {
                textBox1.Font = fontDialog1.Font;
                textBox1.ForeColor = fontDialog1.Color;
                textBox1.Text = "已完成設定";
            }
        }

        private void fontDialog1_Apply(object sender, EventArgs e)
        {
            textBox1.Font = fontDialog1.Font;
            textBox1.ForeColor = fontDialog1.Color;
            textBox1.Text = "已完成設定";
        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
            fontDialog1.ShowApply = checkBox4.Checked;
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            fontDialog1.MaxSize = Convert.ToInt32(numericUpDown1.Value);
        }

        private void numericUpDown2_ValueChanged(object sender, EventArgs e)
        {
            fontDialog1.MinSize = Convert.ToInt32(numericUpDown2.Value);
        }
    }
}
