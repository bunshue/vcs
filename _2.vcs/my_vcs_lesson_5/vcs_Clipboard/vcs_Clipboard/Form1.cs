using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Clipboard
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //把資料放到系統剪貼簿裏
            //System.Windows.Forms.Clipboard.SetDataObject(DateTime.Now.ToString());

            //把系統剪貼簿裏的資料拿出來
            System.Windows.Forms.IDataObject dataObject = System.Windows.Forms.Clipboard.GetDataObject();

            if (dataObject.GetData(typeof(string)) != null)
                richTextBox1.Text += dataObject.GetData(typeof(string)).ToString();
            else
                richTextBox1.Text += "no data\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //string poem = "唐王翰涼州詞\n葡萄美酒夜光杯，欲飲琵琶馬上催。醉臥沙場君莫笑，古來征戰幾人回。\n";
            //Clipboard.SetDataObject(poem);  //將poem字串填到Clipboard裏。

            //從Clipboard取出資料
            IDataObject tmpdata = Clipboard.GetDataObject();

            if (tmpdata.GetDataPresent(DataFormats.Text))
            {
                richTextBox1.Text += tmpdata.GetData(DataFormats.Text);
            }
            else
            {
                richTextBox1.Text += "can not get data from clipboard.\n";
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //(C#)取得剪貼簿Clipboard的內容
            IDataObject data = Clipboard.GetDataObject();
            if (data.GetDataPresent(DataFormats.Text))  //純文字類
            {
                richTextBox1.Text += "取得文字, 內容：\n";
                richTextBox1.Text += data.GetData(DataFormats.Text).ToString();
            }
            else if (data.GetDataPresent(DataFormats.Bitmap))  //圖片類
            {
                richTextBox1.Text += "取得圖片\n";
                pictureBox1.Image = (System.Drawing.Image)data.GetData(DataFormats.Bitmap);
            }


        }

        private void button6_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            //Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            Clipboard.SetDataObject("新增一些資料" + "\n");      //建議用此
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿 累計
            //Clipboard.SetData(DataFormats.Text, Clipboard.GetData(DataFormats.Text) + richTextBox1.Text + "\n");
            //Clipboard.SetDataObject(Clipboard.GetText() + richTextBox1.Text + "\n");      //建議用此
            Clipboard.SetDataObject(Clipboard.GetText() + "累計新增一些資料" + "\n");      //建議用此
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //C# – 貼上剪貼簿
            richTextBox1.Text += "\n";
            //richTextBox1.Text += Clipboard.GetData(DataFormats.Text);
            richTextBox1.Text += Clipboard.GetText();   //建議用此
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //C# – 清除剪貼簿
            Clipboard.Clear();
        }

        //Read text from clipboard
        private void button10_Click(object sender, EventArgs e)
        {
            string clipText = System.String.Empty;
            if (System.Windows.Forms.Clipboard.ContainsText())
            {
                clipText = System.Windows.Forms.Clipboard.GetText();
                richTextBox1.Text += clipText + "\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //C# – 貼上剪貼簿
            richTextBox1.Text += "\n";
            //richTextBox1.Text += Clipboard.GetData(DataFormats.Text);
            richTextBox1.Text += Clipboard.GetText();   //建議用此

            richTextBox1.Text += "\n";
            int len = Clipboard.GetText().Length;
            richTextBox1.Text += "Unicode (Big-Endian), len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += Clipboard.GetText()[i].ToString() + "\n";
                richTextBox1.Text += ((int)Clipboard.GetText()[i]).ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";
        }
    }
}
