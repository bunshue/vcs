using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace 格式化磁盤
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("shell32.dll")]
        private static extern int SHFormatDrive(IntPtr hWnd, int drive, long fmtID, int Options);

        public const long SHFMT_ID_DEFAULT = 0xFFFF;
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                SHFormatDrive(this.Handle, comboBox1.SelectedIndex, SHFMT_ID_DEFAULT, 0);
                MessageBox.Show("格式化完成", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch
            {
                MessageBox.Show("格式化失敗", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}