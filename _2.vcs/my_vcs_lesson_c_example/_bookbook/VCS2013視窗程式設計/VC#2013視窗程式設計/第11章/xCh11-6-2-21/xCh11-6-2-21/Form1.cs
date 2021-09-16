using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Xml.Linq;

namespace xCh11_6_2_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            XElement root = XElement.Load(@"c:\進貨訂單.xml");
            var tests =
                from el in root.Elements("地址")
                select new
                {
                    姓名 = (string)el.Element("姓名"),
                    街道 = (string)el.Element("街道"),
                    城市 = (string)el.Element("城市"),
                    郵遞區號 = (string)el.Element("郵遞區號")
                };

            dataGridView1.DataSource = tests.ToList();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // 利用特定的值尋找具有子項目的特定項目。
            XElement root = XElement.Load(@"c:\進貨訂單.xml");
            var tests =
                from el in root.Elements("地址")
                where (string)el.Element("城市") == textBox1.Text
                select new
                {
                    姓名 = (string)el.Element("姓名"),
                    城市 = (string)el.Element("城市"),
                    郵遞區號 = (string)el.Element("郵遞區號")
                };

            dataGridView1.DataSource = tests.ToList();
        }
    }
}
