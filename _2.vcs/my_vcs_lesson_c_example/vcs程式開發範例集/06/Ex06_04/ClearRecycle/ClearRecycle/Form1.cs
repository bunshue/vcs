using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace ClearRecycle
{
    public partial class Form1 : Form
    {
        const int SHERB_NOCONFIRMATION = 0x000001;
        const int SHERB_NOPROGRESSUI = 0x000002;
        const int SHERB_NOSOUND = 0x000004;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SHEmptyRecycleBin(this.Handle, "", SHERB_NOCONFIRMATION + SHERB_NOPROGRESSUI + SHERB_NOSOUND);
        }
        [DllImportAttribute("shell32.dll")]
        private static extern  int SHEmptyRecycleBin(IntPtr handle, string root, int falgs);
    }
}