using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml.Linq;
// XElement物件預設是以序列的方式處理xml資料，可以直接根據xml資料的階層結構，透過XElement物件建立資料

namespace vcs_ReadWrite_XML4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            XElement company =
new XElement("Company",
new XElement("Employee",
new XElement("ID", "001"),
new XElement("Name", "胖虎")),
new XElement("Employee",
new XElement("ID", "002"),
new XElement("Name", "小夫")
)
);
            richTextBox1.Text += company.ToString();

        }
    }
}
