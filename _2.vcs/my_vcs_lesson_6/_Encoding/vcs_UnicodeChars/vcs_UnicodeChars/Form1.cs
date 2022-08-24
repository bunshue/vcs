using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_UnicodeChars
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the desired Unicode characters
        private void btnList_Click(object sender, EventArgs e)
        {
            txtChars.Clear();
            txtCharCode.Clear();
            lblSample.Text = "";
            Cursor = Cursors.WaitCursor;
            Refresh();

            // Set the font size.
            float font_size = float.Parse(txtFontSize.Text);
            Font font = new Font("Times New Roman", font_size);
            txtChars.Font = font;
            lblSample.Font = font;

            // Display the characters.
            int min = int.Parse(txtMin.Text);
            int max = int.Parse(txtMax.Text);
            StringBuilder sb = new StringBuilder();
            for (int i = min; i <= max; i++)
                sb.Append(((char)i).ToString());
            txtChars.Text = sb.ToString();
            txtChars.Select(0, 0);

            Cursor = Cursors.Default;
        }

        // Display the code for the character under the mouse.
        private void txtChars_MouseMove(object sender, MouseEventArgs e)
        {
            char ch = txtChars.GetCharFromPosition(e.Location);
            lblSample.Text = ch.ToString();
            txtCharCode.Text = ((int)ch).ToString();
        }
    }
}
