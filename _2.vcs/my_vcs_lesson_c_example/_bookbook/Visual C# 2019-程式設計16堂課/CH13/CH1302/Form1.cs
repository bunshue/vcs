using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1302
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void tsbOpen_Click(object sender, EventArgs e)
        {
            rtxtShow.LoadFile("D:\\C#Lab\\CH13\\Demo01.rtf");
        }

        private void tsbSave_Click(object sender, EventArgs e)
        {
            rtxtShow.SaveFile("D:\\C#Lab\\CH13\\change.rtf");
        }

        private void tscobFont_SelectedIndexChanged(
              object sender, EventArgs e)
        {
            if (tscobFont.SelectedIndex == 0)
                rtxtShow.Font = new Font("Arial", 12);
            else if (tscobFont.SelectedIndex == 1)
                rtxtShow.Font = new Font("Garamond", 14);
            else
                rtxtShow.Font = new Font("Times New Roman", 16);
        }
    }
}