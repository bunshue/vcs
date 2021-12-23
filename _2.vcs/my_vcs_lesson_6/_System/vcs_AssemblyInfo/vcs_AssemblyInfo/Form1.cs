using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_AssemblyInfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Get the AssemblyInfo class.
            AssemblyInfo info = new AssemblyInfo();

            // Display the values.
            richTextBox1.Text += "Title : " + info.Title + "\n";
            richTextBox1.Text += "Description : " + info.Description + "\n";
            richTextBox1.Text += "Company : " + info.Company + "\n";
            richTextBox1.Text += "Product : " + info.Product + "\n";
            richTextBox1.Text += "Copyright : " + info.Copyright + "\n";
            richTextBox1.Text += "Trademark : " + info.Trademark + "\n";
            richTextBox1.Text += "Assembly Version : " + info.AssemblyVersion + "\n";
            richTextBox1.Text += "File Version : " + info.FileVersion + "\n";
            richTextBox1.Text += "GUID : " + info.Guid + "\n";
            richTextBox1.Text += "Neutral Language : " + info.NeutralLanguage + "\n";
            richTextBox1.Text += "COM Visible : " + info.IsComVisible.ToString() + "\n";



        }
    }
}
