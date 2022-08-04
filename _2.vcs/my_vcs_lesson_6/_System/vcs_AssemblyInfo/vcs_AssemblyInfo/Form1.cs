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

        private void button2_Click(object sender, EventArgs e)
        {
            //組件資訊  Assembly Info

            //方案總管/專案屬性/應用程式/組件資訊 內 修改組件資訊

            //方案總管/加入/現有項目/選取AssemblyInfo.cs, 把 namespace 改成 vcs_System1
            // Get the AssemblyInfo class.
            AssemblyInfo info = new AssemblyInfo();

            // Display the values.
            richTextBox1.Text += "Title\t" + info.Title + "\n";
            richTextBox1.Text += "Description\t" + info.Description + "\n";
            richTextBox1.Text += "Company\t" + info.Company + "\n";
            richTextBox1.Text += "Product\t" + info.Product + "\n";
            richTextBox1.Text += "Copyright\t" + info.Copyright + "\n";
            richTextBox1.Text += "Trademark\t" + info.Trademark + "\n";
            richTextBox1.Text += "Assembly Version\t" + info.AssemblyVersion + "\n";
            richTextBox1.Text += "File Version\t" + info.FileVersion + "\n";
            richTextBox1.Text += "GUID\t" + info.Guid + "\n";
            richTextBox1.Text += "Neutral Language\t" + info.NeutralLanguage + "\n";
            richTextBox1.Text += "COM Visible\t" + info.IsComVisible.ToString() + "\n";

        }
    }
}
