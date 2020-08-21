using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_00_Control
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            button6.Click += new System.EventHandler(button6_Click);//按下button6觸發button1_Click
            button7.Click += new System.EventHandler(button6_Click);//按下button7觸發button1_Click
            button8.Click += new System.EventHandler(button6_Click);//按下button8觸發button1_Click
            button9.Click += new System.EventHandler(button6_Click);//按下button9觸發button1_Click
        }

        int i = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            i++;

            i %= 6;
            if (i == 1)
                button1.Dock = DockStyle.Left;
            else if (i == 2)
                button1.Dock = DockStyle.Right;
            else if (i == 3)
                button1.Dock = DockStyle.Top;
            else if (i == 4)
                button1.Dock = DockStyle.Bottom;
            else if (i == 5)
                button1.Dock = DockStyle.Fill;
            else
                button1.Dock = DockStyle.None;


        }

        private void button2_Click(object sender, EventArgs e)
        {
            AddMyGroupBox();
        }

        // Add a GroupBox to a form and set some of its common properties.
        private void AddMyGroupBox()
        {
            // Create a GroupBox and add a TextBox to it.
            GroupBox groupBox1 = new GroupBox();
            TextBox textBox1 = new TextBox();
            textBox1.Location = new Point(15, 15);
            groupBox1.Controls.Add(textBox1);

            // Set the Text and Dock properties of the GroupBox.
            groupBox1.Text = "MyGroupBox";
            groupBox1.Dock = DockStyle.Right;

            // Disable the GroupBox (which disables all its child controls)
            groupBox1.Enabled = true;

            // Add the Groupbox to the form.
            this.Controls.Add(groupBox1);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            CreateMyRichTextBox();
        }

        public void CreateMyRichTextBox()
        {
            RichTextBox richTextBox1 = new RichTextBox();
            richTextBox1.Dock = DockStyle.Fill;

            try
            {
                richTextBox1.LoadFile("C:\\______test_files\\VS2013Express.rtf");
                richTextBox1.Find("Text", RichTextBoxFinds.MatchCase);

                richTextBox1.SelectionFont = new Font("Verdana", 12, FontStyle.Bold);
                richTextBox1.SelectionColor = Color.Red;

                richTextBox1.SaveFile("C:\\______test_files\\MyDocument.rtf", RichTextBoxStreamType.RichText);

                this.Controls.Add(richTextBox1);
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "遍歷所有控件\n";
            foreach (Control con in this.Controls)
            {
                System.String strControl = con.GetType().ToString();//获得控件的类型
                System.String strControlName = con.Name.ToString();//获得控件的名称

                richTextBox1.Text += "Type\t" + strControl + "\tName\t" + strControlName + "\n";


            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Sender它代表的是引發這個事件的Object，所以我們可以把他轉型回來使用。
            richTextBox1.Text += "Name : " + ((Button)sender).Name.ToString() + "\n";
            richTextBox1.Text += "Size : " + ((Button)sender).Size.Width.ToString() + " X " + ((Button)sender).Size.Height.ToString() + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            Button btn = (Button)sender;
            richTextBox1.Text += "你按了 " + btn.Text + "\n";

            richTextBox1.Text += "你按了 " + ((Button)sender).Name.ToString() + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //Form.Controls 屬性是用來取得這張Form的控制項
            //Controls.GetType 是取得這個控制項的類別名稱

            for (int i = 0; i < this.Controls.Count; i++)
            {
                richTextBox1.Text += "Name: " + this.Controls[i].Name + "\t";
                richTextBox1.Text += "Text: " + this.Controls[i].Text + "\t";
                richTextBox1.Text += "這項是：" + this.Controls[i].GetType() + "\n";


                if (this.Controls[i] is Button)
                {
                    richTextBox1.Text += "這是Button" + "\n";
                }

            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //列舉控制項
            int i = 1;
            foreach (Control ctrl in this.Controls)
            {
                //取出控制項的類型
                string TypeName = ctrl.GetType().Name;
                //類型若是Label
                if (TypeName == "Button")
                {
                    ctrl.Name = "test" + i.ToString();
                    richTextBox1.Text += ctrl.Name + "\n";
                    i++;
                }
            }

        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //依字串長度改變控件大小
            //AutoSizeControl
            int textPadding = 10;   //表示要套用至控制項所有邊緣的填補量
            button13.Text = "012345678901234567890123456789012345";
            Graphics g = button2.CreateGraphics();      //// Create a Graphics object for the Control.
            // Get the Size needed to accommodate the formatted Text.
            Size preferredSize = g.MeasureString(button13.Text, button13.Font).ToSize();
            richTextBox1.Text += "size W = " + preferredSize.Width.ToString() + "\n";
            richTextBox1.Text += "size H = " + preferredSize.Height.ToString() + "\n";
            // Pad the text and resize the control.
            button13.ClientSize = new Size(
                preferredSize.Width + (textPadding * 2),
                preferredSize.Height + (textPadding * 2));
            g.Dispose();    // Clean up the Graphics object.

        }
    }
}
