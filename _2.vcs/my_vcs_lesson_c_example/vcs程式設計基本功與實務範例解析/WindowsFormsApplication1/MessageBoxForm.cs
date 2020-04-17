using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class MessageBoxForm : Form
    {
        public MessageBoxForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
           // SystemFonts.MessageBoxFont = fontDialog1.Font;

            string fs = SystemFonts.MessageBoxFont.FontFamily.Name;

            fs += ", " + SystemFonts.MessageBoxFont.Size;
            MessageBox.Show(fs);
        }
    }
}
