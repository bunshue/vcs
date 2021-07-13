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

        private void button5_Click(object sender, EventArgs e)
        {
            //動態產生button並且綁定click事件
            DynamicGenerateButton();
        }


        private void DynamicGenerateButton()
        {
            // 設定位置及按鈕寬高值
            int LEFTANCHOR = 40;
            int TOPANCHOR = 0;
            int BTN_HEIGHT = 60;
            int BTN_WIDTH = 130;

            int i;
            for (i = 0; i < 3; i++)
            {
                // 實例化按鈕
                Button btn = new Button();

                // 設定按鈕參數
                btn.Text = i.ToString();
                btn.Width = BTN_WIDTH;
                btn.Height = BTN_HEIGHT;
                btn.Left = LEFTANCHOR + BTN_WIDTH * i;
                btn.Top = TOPANCHOR + BTN_HEIGHT * 0;

                // 加入按鈕事件
                btn.Click += dynamic_Btn_Click;

                // 將按鈕加入Panel
                panel1.Controls.Add(btn);
            }
        }


        //加入按鈕事件
        private void dynamic_Btn_Click(object sender, EventArgs e)
        {
            // 撰寫事件內容
            //richTextBox1.Text += "XXXXXXXXXXXXXXX\n";

            //MessageBox.Show(((Button)sender).Text);
            richTextBox1.Text += "你按了按鈕 " + ((Button)sender).Text + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {


        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int count = 5;
            Button[] Button2 = new Button[count];
            for (int j = 0; j < count; j++)
            {
                //reader2.Read();
                Button2[j] = new Button();
                Button2[j].Name = "topic2" + j;
                Button2[j].Text = j.ToString();
                Button2[j].AutoSize = true;
                Button2[j].Location = new Point(100 * j, 30);
                Button2[j].Font = new Font("微軟正黑體", 12);
                Button2[j].ForeColor = Color.White;
                Button2[j].FlatStyle = FlatStyle.Flat;
                Button2[j].FlatAppearance.BorderColor = Color.FromArgb(((int)(((byte)(55)))), ((int)(((byte)(65)))), ((int)(((byte)(85)))));
                Button2[j].BackColor = Color.FromArgb(((int)(((byte)(55)))), ((int)(((byte)(65)))), ((int)(((byte)(85)))));
            }
            panel1.Controls.AddRange(Button2); 
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立新表單並新增控件於其上\n";
            //當有多個按鈕需要產生時, 如何用loop方式動態產生, 並加入對應的click event
            //產生一個新的form, 並在該form上面產生MxN組的按鈕

            int i;
            int j;
            //this.Size = new Size(800, 600);
            for (i = 0; i < m_cols; i++)
            {
                for (j = 0; j < m_rows; j++)
                {
                    Button btn = new Button();
                    this.AcceptButton = btn;
                    this.Controls.Add(btn);
                    btn.Left = m_btnWidth * i;
                    btn.Top = m_btnHeight * j;
                    btn.Width = m_btnWidth;
                    btn.Height = m_btnHeight;
                    btn.Text = (j + 1).ToString() + ", " + (i + 1).ToString();
                    btn.Click += new EventHandler(myClick);
                }
            }

        }

        private void button10_Click(object sender, EventArgs e)
        {
            PictureBox pb_new = new PictureBox();
            pb_new.Size = new Size(250, 250);
            pb_new.Left = 600;
            pb_new.Top = 50;
            pb_new.BackColor = Color.Pink;
            this.Controls.Add(pb_new);
            
            Button bt_new = new Button();
            this.Controls.Add(bt_new);
            //bt_new.Location = new Point(button10.Location.X, button10.Location.Y + 60);   same
            bt_new.Left = button10.Location.X;
            bt_new.Top = button10.Location.Y + 60;
            bt_new.Size = new Size(154, 42);
            bt_new.BackColor = Color.Red;
            bt_new.Text = "新增控件";
            bt_new.Click += new EventHandler(bt_new_Click);
        }

        private void bt_new_Click(System.Object sender, System.EventArgs e)
        {
            richTextBox1.Text += "你按了這個新控件\n";
        }


    }
}
