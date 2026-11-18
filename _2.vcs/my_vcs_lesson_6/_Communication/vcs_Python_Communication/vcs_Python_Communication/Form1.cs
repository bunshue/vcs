using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

// 目前只能做到 Python 發送資料、vcs接收資料

namespace vcs_Python_Communication
{
    public partial class Form1 : Form
    {
        const int WM_COPYDATA = 0x004A;

        [StructLayout(LayoutKind.Sequential)]
        public struct COPYDATASTRUCT
        {
            public IntPtr dwData;
            public int cbData;
            public IntPtr lpData;
        }

        //覆寫 WndProc
        protected override void WndProc(ref Message m)
        {
            if (m.Msg == WM_COPYDATA)
            {
                COPYDATASTRUCT cds =
                    (COPYDATASTRUCT)Marshal.PtrToStructure(
                        m.LParam,
                        typeof(COPYDATASTRUCT));

                string msg =
                    Marshal.PtrToStringUni(cds.lpData);

                richTextBox1.AppendText(
                    msg + Environment.NewLine);
            }

            base.WndProc(ref m);
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = "CSharpReceiver";  // 讓 Python 知道要傳訊息給誰
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }
    }
}
