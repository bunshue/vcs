using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File

namespace vcs_test_all_01_Richtextbox6_Code
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            byte[] bytes = File.ReadAllBytes(Application.ExecutablePath);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < bytes.Length; i++)
            {
                string value = Convert.ToString(bytes[i], 2);
                value = value.PadLeft(8, '0');
                sb.Append(value + ' ');
            }
            richTextBox1.Text = sb.ToString();

            //byte[] bytes = File.ReadAllBytes(Application.ExecutablePath);
            //string[] strings = Array.ConvertAll(bytes,
            //    b => Convert.ToString(b, 2).PadLeft(8, '0'));
            //richTextBox1.Text = string.Join(" ", strings);

            //var query =
            //    from byte b in File.ReadAllBytes(Application.ExecutablePath)
            //    select Convert.ToString(b, 2).PadLeft(8, '0');
            //richTextBox1.Text = string.Join(" ", query.ToArray());

        }
    }
}
