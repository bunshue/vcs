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
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "製作一SVG檔案\n";

            richTextBox1.Text += "初始化SVG檔案\n";
            SvgDoc doc = new SvgDoc();

            SvgRoot root = doc.CreateNewDocument();
            root.Width = "500px";
            root.Height = "500px";
            richTextBox1.Text += "設定SVG圖紙大小為 500 X 500\n";

            SvgRect rect = new SvgRect(doc,
                                     "50px",
                                     "25px",
                                     "300px",
                                     "200px",
                                     "3px",
                                     Color.LightPink,
                                     Color.Black);
            doc.AddElement(root, rect);
            richTextBox1.Text += "畫長方形在(50, 25) 300 X 200\n";

            rect.RX = "2px";
            rect.RY = "2px";

            SvgCircle circle1 = new SvgCircle(doc,
                 "350px",
                 "200px",
                 "75px");
            doc.AddElement(root, circle1);
            circle1.Fill = Color.DarkBlue;
            richTextBox1.Text += "畫圓形在(350, 200) r=75, 深藍色填滿\n";

            SvgCircle circle2 = new SvgCircle(doc,
                 "50px",
                 "200px",
                 "50px");
            doc.AddElement(root, circle2);
            circle2.Fill = Color.DarkGreen;
            richTextBox1.Text += "畫圓形在(50, 200) r=50, 深綠色填滿\n";

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
