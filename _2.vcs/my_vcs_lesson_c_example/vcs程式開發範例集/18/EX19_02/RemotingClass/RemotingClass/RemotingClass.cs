using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace RemotingClass
{
    public partial class FarClass : Form
    {
        public static int i;
        public FarClass()
        {
            InitializeComponent();
           
        }
        public int GetTime()
        {
            StreamWriter sw = new StreamWriter("hb.txt", true);
            sw.WriteLine("遠程類別對像被第" +i + "次呼叫" + DateTime.Now.ToString());
            sw.Close();
            i++;
            MessageBox.Show("遠程類別在服務器端對像被"+i+"次呼叫"+DateTime.Now.ToString());
            return i;
        }
        public FileStream GetFile(string fileName)
        {
            FileStream fs = new FileStream(fileName, FileMode.Open, FileAccess.Read, FileShare.ReadWrite);
            return fs;
        }

        private void FarClass_Load(object sender, EventArgs e)
        {

        }
    }
}