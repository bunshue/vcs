using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;


namespace test_read_write_binary
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\bear.bmp";
            string filename2 = @"C:\______test_files\bear2.bmp";

            using (FileStream fsWriter = new FileStream(filename2, FileMode.Create, FileAccess.Write))
            {

                using (FileStream fsReader = new FileStream(filename1, FileMode.Open, FileAccess.Read))
                {
                    byte[] bytes = new byte[1024 * 4];//4kB是合適的；
                    int readNum;
                    while ((readNum = fsReader.Read(bytes, 0, bytes.Length)) != 0)//小於說明讀完了
                    {
                        fsWriter.Write(bytes, 0, readNum);
                    }


                }//suing reader
            }//using writer


        }
    }
}
