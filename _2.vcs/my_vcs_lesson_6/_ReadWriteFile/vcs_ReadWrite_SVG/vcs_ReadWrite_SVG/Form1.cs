using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考/加入參考/SVGLib.dll

using SVGLib;

namespace vcs_ReadWrite_SVG
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
            SvgDoc doc = new SvgDoc();
            SvgRoot root = doc.CreateNewDocument();
            root.Width = "500px";
            root.Height = "500px";

            SvgRect rect = new SvgRect(doc,
                                     "50px",
                                     "25px",
                                     "300px",
                                     "200px",
                                     "3px",
                                     Color.LightPink,
                                     Color.Black);
            doc.AddElement(root, rect);

            rect.RX = "2px";
            rect.RY = "2px";

            SvgCircle circle1 = new SvgCircle(doc,
                 "350px",
                 "200px",
                 "50px");
            doc.AddElement(root, circle1);

            circle1.Fill = Color.DarkBlue;

            SvgCircle circle2 = new SvgCircle(doc,
                 "50px",
                 "200px",
                 "50px");
            doc.AddElement(root, circle2);

            circle2.Fill = Color.DarkBlue;


            string filename = Application.StartupPath + "\\svg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".svg";
            try
            {
                doc.SaveToFile(filename);

                richTextBox1.Text += "存檔成功\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }
    }
}

