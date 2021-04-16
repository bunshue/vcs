using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_INI5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string filename = @"c:\______test_files\__RW\_ini\vcs_ReadWrite_INI5.ini";

        private void button1_Click(object sender, EventArgs e)
        {
            //使用 StreamReader 讀取
            try
            {
                using (StreamReader oStreamReader = new StreamReader(filename, Encoding.Default))
                {
                    int iResult = -1;

                    //listBox1.Items.Clear();

                    do
                    {
                        richTextBox1.Text += oStreamReader.ReadLine() + "\n";
                        iResult = oStreamReader.Peek();

                    } while (iResult != -1);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用 Win32 API 讀取
            using (TINI oTINI = new TINI(filename))
            {
                string sResult = oTINI.getKeyValue("Test5", "1");　//Test5： Section；1：Key
                richTextBox1.Text += sResult + "\n";
            }
        }
    }
}
