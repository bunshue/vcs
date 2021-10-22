using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace test_usb
{
    public partial class Form1 : Form
    {
        //C#獲取USB事件API ST
        const int WM_DEVICECHANGE = 0x2190;
        const int DBT_DEVICEARRIVAL = 0x8000;
        const int DBT_DEVICEREMOVECOMPLETE = 0x8004;
        protected override void WndProc(ref Message m)
        {
            try
            {
                //if (m.Msg == WM_DEVICECHANGE)
                //{
                switch (m.WParam.ToInt32())
                {
                    case DBT_DEVICEARRIVAL: // U盤插入
                        DriveInfo[] s = DriveInfo.GetDrives();
                        foreach (DriveInfo drive in s)
                        {
                            if (drive.DriveType == DriveType.Removable)
                            {
                                richTextBox1.Text += "USB插入\n";
                                break;
                            }
                        }
                        break;
                    case DBT_DEVICEREMOVECOMPLETE: //U盤卸載
                        //
                        richTextBox1.Text += "USB拔出\n";
                        break;
                    default:
                        break;
                }
                //}
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            base.WndProc(ref m);
        }
        //C#獲取USB事件API SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}
