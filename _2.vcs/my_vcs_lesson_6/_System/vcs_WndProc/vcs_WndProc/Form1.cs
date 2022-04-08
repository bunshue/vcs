using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//覆寫 WndProc 方法，以處理結構中所識別的作業系統訊息 Message

namespace vcs_WndProc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "擷取Windows作業系統訊息\n";
        }

        private const int WM_ACTIVATEAPP = 0x001C;
        private const int WM_NCHITTEST = 0x84;
        private const int HTCLIENT = 0x1;
        private const int HTCAPTION = 0x2;
        private const int WM_SYSCOMMAND = 0x0112;
        private const int SC_CLOSE = 0xF060;
        private const int WM_HOTKEY = 0x0312;

        protected override void WndProc(ref Message m)
        {
            //按快捷键     
            switch (m.Msg)
            {
                // The WM_ACTIVATEAPP message occurs when the application
                // becomes the active application or becomes inactive.
                case WM_ACTIVATEAPP:

                    // The WParam value identifies what is occurring.
                    bool appActive = (((int)m.WParam != 0));
                    if (appActive == true)
                    {
                        richTextBox1.Text += "Active\n";
                    }
                    else
                    {
                        richTextBox1.Text += "Inactive\n";
                    }
                    break;

                case WM_HOTKEY:
                    switch (m.WParam.ToInt32())
                    {
                        case 81:    //按下的是CTRL+F / ESC
                            //Clipboard.SetText(label3.Text.Trim());
                            richTextBox1.Text += "你按了 CTRL + F / ESC\n";
                            this.Text = "你按了 CTRL + F / ESC";
                            break;
                    }
                    break;
                case WM_NCHITTEST:
                    //this.Text = "移動無邊框窗體";
                    //richTextBox1.Text += "移動鼠標，按住或釋放鼠標時發生\n";
                    base.WndProc(ref m);
                    if ((int)m.Result == HTCLIENT)
                    {
                        m.Result = (IntPtr)HTCAPTION;
                        return;
                    }
                    break;
                case WM_SYSCOMMAND:
                    this.Text = "截獲關閉程式命令";
                    if ((int)m.WParam == SC_CLOSE)
                    {
                        // 顯示MessageBox 
                        DialogResult Result = MessageBox.Show("確定關閉表單", "表單訊息", MessageBoxButtons.YesNo);
                        if (Result == System.Windows.Forms.DialogResult.Yes)
                        {
                            // 關閉Form 
                            this.Close();
                        }
                        else
                        {
                            return;
                        }
                    }
                    break;
                case 0x0011://WM_QUERYENDSESSION
                    //m.Result = (IntPtr)1;
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    break;
            }
            base.WndProc(ref m);
        }

    }
}
