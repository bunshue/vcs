using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FILE
using System.Xml;

using System.Xml.Linq;  //for XDocument, XElement
// XElement物件預設是以序列的方式處理xml資料，可以直接根據xml資料的階層結構，透過XElement物件建立資料

namespace vcs_ReadWrite_XML2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 20;
            y_st = 20;
            dx = 240;
            dy = 460;

            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            dataGridView1.Size = new Size(400, 400);

            treeView1.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            treeView1.Size = new Size(400, 400);

            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            richTextBox1.Size = new Size(400, 1000);

            x_st = 20;
            y_st = 20;
            dx = 100;
            dy = 80;
            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button04.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button10.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            button50.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button51.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button52.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button53.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button54.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //XML操作0
        private void button00_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_xml\person.xml";
            //開啟一XML文件檔並顯示在DataGridView上
            //使用DataSet讀XML文件

            DataSet ds = new DataSet();
            ds.ReadXmlSchema(filename);
            ds.ReadXml(filename);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void button01_Click(object sender, EventArgs e)
        {

        }

        private void button02_Click(object sender, EventArgs e)
        {

        }

        private void button03_Click(object sender, EventArgs e)
        {

        }

        private void button04_Click(object sender, EventArgs e)
        {

        }

        //開啟XML檔案到TreeView 1 ST
        private void button10_Click(object sender, EventArgs e)
        {
            //開啟XML檔案到TreeView 1
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_xml\vcs_ReadWrite_XML6.xml";
            LoadTreeViewFromXmlFile(filename, treeView1);
        }

        // Load a TreeView control from an XML file.
        private void LoadTreeViewFromXmlFile(string filename, TreeView trv)
        {
            // Load the XML document.
            XmlDocument xml_doc = new XmlDocument();
            xml_doc.Load(filename);

            // Add the root node's children to the TreeView.
            trv.Nodes.Clear();
            AddTreeViewChildNodes(trv.Nodes, xml_doc.DocumentElement);
        }

        // Add the children of this XML node 
        // to this child nodes collection.
        private void AddTreeViewChildNodes(TreeNodeCollection parent_nodes, XmlNode xml_node)
        {
            foreach (XmlNode child_node in xml_node.ChildNodes)
            {
                // Make the new TreeView node.
                TreeNode new_node = parent_nodes.Add(child_node.Name);

                // Recursively make this node's descendants.
                AddTreeViewChildNodes(new_node.Nodes, child_node);

                // If this is a leaf node, make sure it's visible.
                if (new_node.Nodes.Count == 0) new_node.EnsureVisible();
            }
        }
        //開啟XML檔案到TreeView 1 SP

        //開啟XML檔案到TreeView 2 ST
        private void button11_Click(object sender, EventArgs e)
        {
            //開啟XML檔案到TreeView 2
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_xml\NexusPoint.xml";
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_xml\vcs_ReadWrite_XML6.xml";

            XmlDocument NexusDocument = new XmlDataDocument();//定義一個XML文檔對像
            NexusDocument.Load(filename);//加載XML文件
            RecursionTreeControl(NexusDocument.DocumentElement, treeView1.Nodes);//將加載完成的XML文件顯示在TreeView控件中
            treeView1.ExpandAll();//展開TreeView控件中的所有項
        }

        /// <summary>
        /// RecursionTreeControl:表示將XML文件的內容顯示在TreeView控件中
        /// </summary>
        /// <param name="xmlNode">將要加載的XML文件中的節點元素</param>
        /// <param name="nodes">將要加載的XML文件中的節點集合</param>
        private void RecursionTreeControl(XmlNode xmlNode, TreeNodeCollection nodes)
        {
            foreach (XmlNode node in xmlNode.ChildNodes)//循環遍歷當前元素的子元素集合
            {
                string temp = (node.Value != null ? node.Value : (node.Attributes != null && node.Attributes.Count > 0) ? node.Attributes[0].Value : node.Name);//表示TreeNode節點的文本內容
                TreeNode new_child = new TreeNode(temp);//定義一個TreeNode節點對像
                nodes.Add(new_child);//向當前TreeNodeCollection集合中添加當前節點
                RecursionTreeControl(node, new_child.Nodes);//調用本方法進行遞歸
            }
        }
        //開啟XML檔案到TreeView 2 SP

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //讀取XML
            //C#讀取XML中元素和屬性值的實現代碼

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_xml\school.xml";
            XmlDocument doc = new XmlDocument();
            doc.Load(filename);

            //學校  使用xpath表達式選擇文檔中所有的schoo的子節點
            XmlNodeList schoolNodeList = doc.SelectNodes("/school");
            if (schoolNodeList != null)
            {
                foreach (XmlNode schoolNode in schoolNodeList)
                {
                    //通過Attributes獲得屬性名為name的屬性
                    string schoolName = schoolNode.Attributes["name"].Value;
                    richTextBox1.Text += "學校：" + schoolName + "\n";

                    #region 年級
                    //通過SelectSingleNode方法獲得當前節點下的grades子節點
                    XmlNode gradesNode = schoolNode.SelectSingleNode("grades");
                    if (gradesNode != null)
                    {
                        //通過ChildNodes屬性獲得grades的所有一級子節點
                        XmlNodeList gradeNodeList = gradesNode.ChildNodes;
                        if (gradeNodeList != null)
                        {
                            foreach (XmlNode gradeNode in gradeNodeList)
                            {
                                richTextBox1.Text += "\t年級：" + gradeNode.Attributes["name"].Value + "   ID:" + gradeNode.Attributes["id"].Value + "\n";

                                #region 班級
                                //通過SelectSingleNode方法獲得當前節點下的classes子節點
                                XmlNode classesNode = gradeNode.SelectSingleNode("classes");
                                if (classesNode != null)
                                {
                                    //通過ChildNodes屬性獲得classes的所有一級子節點
                                    XmlNodeList classNodeList = classesNode.ChildNodes;
                                    if (classNodeList != null)
                                    {
                                        foreach (XmlNode classNode in classNodeList)
                                        {
                                            richTextBox1.Text += "  班級：" + classNode.Attributes["name"].Value + "    ID:" + classNode.Attributes["id"].Value + "\n";

                                            #region 老師
                                            XmlNode teachersNode = classNode.SelectSingleNode("teachers");
                                            if (teachersNode != null)
                                            {
                                                XmlNodeList teacherNodeList = teachersNode.ChildNodes;
                                                if (teacherNodeList != null)
                                                {
                                                    foreach (XmlNode teacherNode in teacherNodeList)
                                                    {
                                                        XmlNode teacherNameNode = teacherNode.FirstChild;
                                                        XmlCDataSection cdate = (XmlCDataSection)teacherNameNode.FirstChild;
                                                        if (cdate != null)
                                                        {
                                                            richTextBox1.Text += "   " + teacherNode.Attributes["teach"].Value + "老師：" + cdate.InnerText.Trim() + "\n";
                                                        }
                                                    }
                                                }
                                            }
                                            #endregion  老師

                                            #region 所有學生
                                            XmlNode studentsNode = classNode.SelectSingleNode("students");
                                            if (studentsNode != null)
                                            {
                                                XmlNodeList studentNodeList = studentsNode.ChildNodes;
                                                if (studentNodeList != null)
                                                {
                                                    foreach (XmlNode studentNode in studentNodeList)
                                                    {
                                                        richTextBox1.Text += "    學生：" + studentNode.Attributes["id"].Value + "\n";

                                                        //獲取student的屬性值name和文本
                                                        XmlNode stu1 = studentNode.FirstChild;
                                                        XmlElement xe1 = (XmlElement)stu1;
                                                        if (xe1 != null)
                                                        {
                                                            richTextBox1.Text += "        姓名：" + xe1.InnerText.Trim() + "\n";
                                                        }
                                                        //獲取student的屬性值sex和文本
                                                        XmlNode stu2 = studentNode.LastChild;
                                                        XmlElement xe2 = (XmlElement)stu2;
                                                        if (xe2 != null)
                                                        {
                                                            richTextBox1.Text += "        姓別：" + xe2.InnerText.Trim() + "\n";
                                                        }
                                                    }
                                                }
                                            #endregion 所有學生
                                            }
                                        }
                                    }
                                #endregion 班級
                                }
                            }
                        }
                    #endregion  年級
                    }
                }
            }
        }

        //XML To TreeView ST
        //讀取XML文檔 →獲取XML根元素→ 遞歸添加根元素的子元素(因為樹形的結構和XML很像)
        private void button21_Click(object sender, EventArgs e)
        {
            //讀取XML至TreeView
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_xml\school.xml";

            //讀取Xml文件   this.txt_XmlPath.Text是文件路徑       
            XDocument xmlfile = XDocument.Load(filename);

            //取根元素
            XElement rootElement = xmlfile.Root;

            //給第TreeView 添加根節點 
            TreeNode node = this.treeView1.Nodes.Add(rootElement.Name.ToString());

            RecursionAddNode(node.Nodes, rootElement);
        }

        private void RecursionAddNode(TreeNodeCollection nodes, XElement xElement)
        {
            //獲取嵌套的元素
            IEnumerable<XElement> elements = xElement.Elements();
            //遞歸添加
            foreach (XElement element in elements)
            {
                TreeNode node = nodes.Add(element.Name.ToString() + ":" + GetAttributes(element));
                RecursionAddNode(node.Nodes, element);
            }
        }

        //如果要獲取屬性 就要再添加一個方法GetAttributes(element)
        private static string GetAttributes(XElement xElement)
        {
            IEnumerable<XAttribute> attributes = xElement.Attributes();

            foreach (XAttribute attribute in attributes)
            {
                return attribute.Name + "=" + attribute.Value;
            }
            return null;
        }
        //XML To TreeView SP

        private void button22_Click(object sender, EventArgs e)
        {
            //讀取XML至TreeView b

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_xml\student.xml";

            //使用xDocument来读取xml文件
            XDocument document = XDocument.Load(filename);
            //取出根节点
            XElement rootElement = document.Root;
            //将xml文件的根元素加载到treeview的根节点上
            TreeNode rootNode = treeView1.Nodes.Add(rootElement.Name.ToString());
            //用递归加载XML到TreeView中
            LoadxmlToTreeView(rootElement, rootNode.Nodes);
        }

        private void LoadxmlToTreeView(XElement rootElement, TreeNodeCollection treeNodeCollection)
        {
            foreach (XElement x in rootElement.Elements())
            {
                IEnumerable<XElement> elements = x.Elements();
                //判断该元素是否是叶子元素，即下面是否还有子元素
                //如果有子元素则只添加元素名称，如果是叶子元素则添加元素名称和元素内容
                if (ReturnNumber(elements) == 0)
                {
                    TreeNode xnode = treeNodeCollection.Add(x.Name.ToString()).Nodes.Add(x.Value.ToString());
                }
                else
                {
                    TreeNode xnode = treeNodeCollection.Add(x.Name.ToString());
                    LoadxmlToTreeView(x, xnode.Nodes);
                }

            }
        }

        /// <summary>
        /// 返回传入的集合中元素的个数
        /// </summary>
        /// <param name="xElements"></param>
        /// <returns></returns>
        private int ReturnNumber(IEnumerable<XElement> xElements)
        {
            int count = 0;
            foreach (var x in xElements)
            {
                count++;
            }
            return count;
        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        //XML操作3
        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {

        }

        private void button34_Click(object sender, EventArgs e)
        {

        }

        private void button40_Click(object sender, EventArgs e)
        {

        }

        private void button41_Click(object sender, EventArgs e)
        {

        }

        private void button42_Click(object sender, EventArgs e)
        {

        }

        private void button43_Click(object sender, EventArgs e)
        {

        }

        private void button44_Click(object sender, EventArgs e)
        {

        }

        private void button50_Click(object sender, EventArgs e)
        {

        }

        private void button51_Click(object sender, EventArgs e)
        {

        }

        private void button52_Click(object sender, EventArgs e)
        {

        }

        private void button53_Click(object sender, EventArgs e)
        {

        }

        private void button54_Click(object sender, EventArgs e)
        {

        }
    }
}
