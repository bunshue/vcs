using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Xml;
using System.Xml.Linq;

namespace vcs_ReadWrite_XML6
{
    public partial class Frm_Main : Form
    {
        static string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\_xml\Employee.xml";
        static string strID = "";

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            getXmlInfo();
        }

        void show_item_location()
        {
            int W = 200;
            int H = 370;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;

            richTextBox1.Size = new Size(420, 750);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1300, 810);
            this.Text = "vcs_ReadWrite_XML6";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        //創建XML文件
        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"tmp_Employee.xml";

            XDocument doc = new XDocument(
                new XDeclaration("1.0", "utf-8", "yes"),
                new XElement(textBox1.Text,
                    new XElement(textBox2.Text, new XAttribute(textBox3.Text, textBox10.Text),
                        new XElement(textBox4.Text, textBox5.Text),
                        new XElement(textBox6.Text, textBox7.Text),
                        new XElement(textBox8.Text, textBox9.Text))
                    )
                );
            doc.Save(filename);
            getXmlInfo();
        }

        //添加XML元素
        private void button2_Click(object sender, EventArgs e)
        {
            XElement xe = XElement.Load(filename);
            IEnumerable<XElement> elements1 = from element in xe.Elements("People")
                                              select element;
            //生成新的編號
            string str = (Convert.ToInt32(elements1.Max(element => element.Attribute("ID").Value)) + 1).ToString("000");
            XElement people = new XElement(
                "People", new XAttribute("ID", str),
                new XElement("Name", textBox11.Text),
                new XElement("Sex", comboBox1.Text),
                new XElement("Salary", textBox12.Text)
                );
            xe.Add(people);
            xe.Save(filename);
            getXmlInfo();
        }

        //修改XML元素
        private void button3_Click(object sender, EventArgs e)
        {
            if (strID != "")
            {
                XElement xe = XElement.Load(filename);
                IEnumerable<XElement> elements = from element in xe.Elements("People")
                                                 where element.Attribute("ID").Value == strID
                                                 select element;
                if (elements.Count() > 0)
                {
                    XElement newXE = elements.First();
                    newXE.SetAttributeValue("ID", strID);
                    newXE.ReplaceNodes(
                        new XElement("Name", textBox11.Text),
                        new XElement("Sex", comboBox1.Text),
                        new XElement("Salary", textBox12.Text)
                        );
                }
                xe.Save(filename);
            }
            getXmlInfo();
        }

        //刪除XML元素
        private void button4_Click(object sender, EventArgs e)
        {
            if (strID != "")
            {
                XElement xe = XElement.Load(filename);
                IEnumerable<XElement> elements = from element in xe.Elements("People")
                                                 where element.Attribute("ID").Value == strID
                                                 select element;
                if (elements.Count() > 0)
                    elements.First().Remove();
                xe.Save(filename);
            }
            getXmlInfo();
        }

        //顯示選中XML節點的詳細信息
        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            strID = dataGridView1.Rows[e.RowIndex].Cells[3].Value.ToString();
            XElement xe = XElement.Load(filename);
            IEnumerable<XElement> elements = from PInfo in xe.Elements("People")
                                             where PInfo.Attribute("ID").Value == strID
                                             select PInfo;
            foreach (XElement element in elements)
            {
                textBox11.Text = element.Element("Name").Value;
                comboBox1.SelectedItem = element.Element("Sex").Value;
                textBox12.Text = element.Element("Salary").Value;
            }
        }

        /// 將XML文件內容綁定到DataGridView控件
        /// <summary>
        /// 將XML文件內容綁定到DataGridView控件
        /// </summary>
        private void getXmlInfo()
        {
            DataSet myds = new DataSet();
            myds.ReadXml(filename);
            dataGridView1.DataSource = myds.Tables[0];
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //讀取
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //建立

        }

    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


