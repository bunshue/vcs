using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Xml;
using System.Collections;   //for Hashtable

/*
參考
C#学习笔记-中英文切换（XML）
https://www.cnblogs.com/Aries-rong/p/6673018.html
*/

namespace vcs_ChangeLanguage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string str = MultiLanguage.GetDefaultLanguage();
            richTextBox1.Text += str + "\n";

            MultiLanguage.LoadLanguage(this, str);

            //public static void LoadLanguage(Form form, string FormName)
        }

    }

    static class MultiLanguage
    {
        //当前默认语言
        public static string DefaultLanguage = "ChineseSimplified";

        /// <summary>
        /// 读取当前默认语言
        /// </summary>
        /// <returns>当前默认语言</returns>
        public static string GetDefaultLanguage()
        {
            string defaultLanguage = "ChineseSimplified";
            XmlReader reader = new XmlTextReader("../../Languages/DefaultLanguage.xml");
            XmlDocument doc = new XmlDocument();
            doc.Load(reader);
            XmlNode root = doc.DocumentElement;
            //选取DefaultLangugae节点
            XmlNode node = root.SelectSingleNode("DefaultLanguage");
            if (node != null)
            {
                //取出节点中的内容
                defaultLanguage = node.InnerText;
            }
            reader.Close();
            //reader.Dispose();
            return defaultLanguage;
        }

        /// <summary>
        /// 修改默认语言
        /// </summary>
        /// <param name="lang">待设置默认语言</param>
        public static void SetDefaultLanguage(string lang)
        {
            DataSet ds = new DataSet();
            ds.ReadXml("../../Languages/DefaultLanguage.xml");
            DataTable dt = ds.Tables["Softimite"];
            dt.Rows[0]["DefaultLanguage"] = lang;
            ds.AcceptChanges();
            ds.WriteXml("../../Languages/DefaultLanguage.xml");
            DefaultLanguage = lang;
        }

        /// <summary>
        /// 加载语言
        /// </summary>
        /// <param name="form">加载语言的窗口</param>
        public static void LoadLanguage(Form form, string FormName)
        {
            //根据用户选择的语言获得表的显示文字
            Hashtable hashText = ReadXMLText(form.Name, FormName);
            Hashtable hashHeaderText = ReadXMLHeaderText(form.Name, FormName);
            if (hashText == null)
            {
                return;
            }
            //获取当前窗口的所有控件
            Control.ControlCollection sonControls = form.Controls;
            try
            {
                //遍历所有控件
                foreach (Control control in sonControls)
                {
                    if (control.GetType() == typeof(Panel))     //Panel
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(GroupBox))     //GroupBox
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(TabControl))       //TabControl
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(TabPage))      //TabPage
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(DataGridView))     //DataGridView
                    {
                        GetSetHeaderCell((DataGridView)control, hashHeaderText);
                    }
                    if (hashText.Contains(control.Name.ToLower()))
                    {
                        control.Text = (string)hashText[control.Name.ToLower()];
                    }
                }
                //如果找到了控件，就将对应的名字赋值过去
                if (hashText.Contains(form.Name.ToLower()))
                {
                    form.Text = (string)hashText[form.Name.ToLower()];
                }
            }
            catch (Exception ex)
            {
                string s = ex.ToString();
            }
        }

        /// <summary>
        /// 获取并设置控件中的子控件
        /// </summary>
        /// <param name="controls">父控件</param>
        /// <param name="hashResult">哈希表</param>
        private static void GetSetSubControls(Control.ControlCollection controls, Hashtable hashText, Hashtable hashHeaderText)
        {
            try
            {
                foreach (Control control in controls)
                {
                    if (control.GetType() == typeof(Panel))     //Panel
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(GroupBox))     //GroupBox
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(TabControl))       //TabControl
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(TabPage))      //TabPage
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(TableLayoutPanel))     //TableLayoutPanel
                    {
                        GetSetSubControls(control.Controls, hashText, hashHeaderText);
                    }
                    else if (control.GetType() == typeof(DataGridView))
                    {
                        GetSetHeaderCell((DataGridView)control, hashHeaderText);
                    }
                    if (hashText.Contains(control.Name.ToLower()))
                    {
                        control.Text = (string)hashText[control.Name.ToLower()];
                    }
                }
            }
            catch (Exception ex)
            {
                throw new Exception(ex.Message);
            }
        }

        /// <summary>
        /// 从XML文件中读取需要修改Text的內容
        /// </summary>
        /// <param name="frmName">窗口名，用于获取对应窗口的那部分内容</param>
        /// <param name="xmlName">目标语言</param>
        /// <returns></returns>
        private static Hashtable ReadXMLText(string frmName, string xmlName)
        {
            Console.WriteLine(frmName + "\t" + xmlName);
            try
            {
                Console.WriteLine("filename : " + "../../Languages/" + xmlName + ".xml");
                Hashtable hashResult = new Hashtable();
                XmlReader reader = null;
                //判断是否存在该语言的配置文件
                if (!(new System.IO.FileInfo("../../Languages/" + xmlName + ".xml")).Exists)
                {
                    Console.WriteLine("11111");
                    return null;
                }
                else
                {
                    Console.WriteLine("22222");
                    reader = new XmlTextReader("../../Languages/" + xmlName + ".xml");
                }
                XmlDocument doc = new XmlDocument();
                doc.Load(reader);
                XmlNode root = doc.DocumentElement;
                //获取XML文件中对应该窗口的内容
                XmlNodeList nodeList = root.SelectNodes("Form[Name='" + frmName + "']/Controls/Control");
                foreach (XmlNode node in nodeList)
                {
                    try
                    {
                        //修改内容为控件的Text值
                        XmlNode node1 = node.SelectSingleNode("@name");
                        XmlNode node2 = node.SelectSingleNode("@text");
                        if (node1 != null)
                        {
                            hashResult.Add(node1.InnerText.ToLower(), node2.InnerText);
                        }
                    }
                    catch (Exception ex)
                    {
                        string s = ex.ToString();
                    }
                }
                reader.Close();
                //reader.Dispose();
                return hashResult;
            }
            catch
            {
                return null;
            }
        }

        /// <summary>
        /// 从XML文件中读取需要修改HeaderText的內容
        /// </summary>
        /// <param name="frmName">窗口名，用于获取对应窗口的那部分内容</param>
        /// <param name="xmlName">目标语言</param>
        /// <returns></returns>
        private static Hashtable ReadXMLHeaderText(string frmName, string xmlName)
        {
            try
            {
                Hashtable hashResult = new Hashtable();
                XmlReader reader = null;
                //判断是否存在该语言的配置文件
                if (!(new System.IO.FileInfo("../../Languages/" + xmlName + ".xml")).Exists)
                {
                    return null;
                }
                else
                {
                    reader = new XmlTextReader("../../Languages/" + xmlName + ".xml");
                }
                XmlDocument doc = new XmlDocument();
                doc.Load(reader);
                XmlNode root = doc.DocumentElement;
                //获取XML文件中对应该窗口的内容
                XmlNodeList nodeList = root.SelectNodes("Form[Name='" + frmName + "']/DataGridViewCells/DataGridViewCell");
                foreach (XmlNode node in nodeList)
                {
                    try
                    {
                        //修改内容为控件的Text值
                        XmlNode node1 = node.SelectSingleNode("@name");
                        XmlNode node2 = node.SelectSingleNode("@HeaderText");
                        if (node1 != null)
                        {
                            hashResult.Add(node1.InnerText.ToLower(), node2.InnerText);
                        }
                    }
                    catch { }
                }
                reader.Close();
                //reader.Dispose();
                return hashResult;
            }
            catch
            {
                return null;
            }
        }

        /// <summary>
        /// 获取并设置DataGridView的列头
        /// </summary>
        /// <param name="dataGridView">DataGridView名</param>
        /// <param name="hashResult">哈希表</param>
        private static void GetSetHeaderCell(DataGridView dataGridView, Hashtable hashHeaderText)
        {
            foreach (DataGridViewColumn column in dataGridView.Columns)
            {
                if (hashHeaderText.Contains(column.Name.ToLower()))
                {
                    column.HeaderText = (string)hashHeaderText[column.Name.ToLower()];
                }
            }
        }


    }
}
