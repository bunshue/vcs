using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//C# 動態產生或移除多組按鈕

namespace vcs_DynamicAddRemoveControls5
{
    public partial class Form1 : Form
    {
        int m_cols = 4;
        int m_rows = 3;
        int m_btnWidth = 100;
        int m_btnHeight = 50;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            int i;
            int j;
            Form frm = new Form();
            frm.Size = new Size(800, 600);
            for (i = 0; i < m_cols; i++)
            {
                for (j = 0; j < m_rows; j++)
                {
                    Button btn = new Button();
                    frm.AcceptButton = btn;
                    frm.Controls.Add(btn);
                    btn.Left = m_btnWidth * i;
                    btn.Top = m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(myClick);
                }
            }
            frm.Show();
        }

        private void myClick(object sender, EventArgs e)
        {
            //MessageBox.Show(((Button)sender).Text);
            richTextBox1.Text += "你按了按鈕 " + ((Button)sender).Text + "\n";
        }

        //指派一個panel, 在該panels上面產生MxN組的按鈕
        public void showOnPanel(Panel panel)
        {
            int i;
            int j;

            removeAllBtns(panel);
            for (i = 0; i < m_cols; i++)
            {
                for (j = 0; j < m_rows; j++)
                {
                    Button btn = new Button();
                    panel.Controls.Add(btn);
                    btn.Left = m_btnWidth * i;
                    btn.Top = m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(myClick);
                }
            }
        }

        //移除按鈕部分,  一趟並不會將所有panel上的button回傳, 所以加入while迴圈, 真是神奇驚訝 
        private static void removeAllBtns(Panel panel)
        {
            while (panel.Controls.Count > 0)
            {
                foreach (Control item in panel.Controls.OfType<Button>())
                {
                    Button btn = (Button)item;
                    MessageBox.Show("移除" + btn.Text);
                    panel.Controls.Remove(item);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "在panel1上新增控件於其上\n";
            showOnPanel(panel1);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "移除panel1上的控件\n";
            removeAllBtns(panel1);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //動態加入控制項( Controls.Add() )

            Label myLabel = new Label();
            myLabel.Text = "Sample Label";

            Panel pp = new Panel();
            pp.Controls.Add(myLabel);

            this.Controls.Add(pp);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            int x_st = 700;
            int y_st = 10;
            int i;
            int j;

            for (i = 0; i < m_cols; i++)
            {
                for (j = 0; j < m_rows; j++)
                {
                    Button btn = new Button();
                    this.AcceptButton = btn;
                    this.Controls.Add(btn);
                    btn.Left = x_st+m_btnWidth * i;
                    btn.Top = y_st+m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(myClick);
                }
            }

        }


    }
}

