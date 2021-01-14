using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TextBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Prepare the TextBox.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Register the TextChanged event handler.
            textBox1.TextChanged += textBox1_TextChanged;
            textBox1.Multiline = true;
            textBox1.ScrollBars = ScrollBars.None;

            // Make the TextBox fit its initial text.
            AutoSizeTextBox(textBox1);
        }

        // Make the TextBox fit its new contents.
        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            AutoSizeTextBox(sender as TextBox);
        }

        // Make the TextBox fit its contents.
        private void AutoSizeTextBox(TextBox txt)
        {
            const int x_margin = 0;
            const int y_margin = 2;
            Size size = TextRenderer.MeasureText(txt.Text, txt.Font);
            txt.ClientSize =
                new Size(size.Width + x_margin, size.Height + y_margin);
        }
    }
}
