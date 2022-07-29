using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_TabControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.tabPage1.Parent = this.tabControl1;    //顯示
            this.tabPage2.Parent = this.tabControl1;    //顯示
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = this.tabControl1;    //顯示
            this.tabPage5.Parent = this.tabControl1;    //顯示
            this.tabPage6.Parent = null;                //隱藏
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = null;                //隱藏
            this.tabPage10.Parent = null;               //隱藏

            radioButton1.Checked = false;
            radioButton2.Checked = false;
            radioButton3.Checked = false;
            radioButton4.Checked = true;
            radioButton5.Checked = false;

            tabControl1.SelectedIndex = 4;      //程式啟動時，直接跳到第5頁。
            label1.Text = "顯示所有頁面、tab選第5頁。";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = this.tabControl1;    //顯示
            this.tabPage2.Parent = null;                //隱藏
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = null;                //隱藏
            this.tabPage5.Parent = this.tabControl1;    //顯示
            this.tabPage6.Parent = null;                //隱藏
            this.tabPage7.Parent = this.tabControl1;    //顯示
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = this.tabControl1;    //顯示
            this.tabPage10.Parent = null;               //隱藏
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "A計畫，顯示單數頁面、tab選第3頁。";
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = null;                //隱藏
            this.tabPage2.Parent = this.tabControl1;    //顯示
            this.tabPage3.Parent = null;                //隱藏
            this.tabPage4.Parent = this.tabControl1;    //顯示
            this.tabPage5.Parent = null;                //隱藏
            this.tabPage6.Parent = this.tabControl1;    //顯示
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = this.tabControl1;    //顯示
            this.tabPage9.Parent = null;                //隱藏
            this.tabPage10.Parent = this.tabControl1;   //顯示
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "B計畫，顯示雙數頁面、tab選第3頁。";
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = null;                //隱藏
            this.tabPage2.Parent = null;                //隱藏
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = null;                //隱藏
            this.tabPage5.Parent = null;                //隱藏
            this.tabPage6.Parent = this.tabControl1;    //顯示
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = this.tabControl1;    //顯示
            this.tabPage10.Parent = null;               //隱藏
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "C計畫，顯示三倍數頁面、tab選第3頁。";
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = this.tabControl1;    //顯示
            this.tabPage2.Parent = this.tabControl1;    //顯示
            this.tabPage3.Parent = this.tabControl1;    //顯示
            this.tabPage4.Parent = this.tabControl1;    //顯示
            this.tabPage5.Parent = this.tabControl1;    //顯示
            this.tabPage6.Parent = this.tabControl1;    //顯示
            this.tabPage7.Parent = this.tabControl1;    //顯示
            this.tabPage8.Parent = this.tabControl1;    //顯示
            this.tabPage9.Parent = this.tabControl1;    //顯示
            this.tabPage10.Parent = this.tabControl1;   //顯示
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "全開，顯示所有頁面、tab選第3頁。";
        }

        private void radioButton5_CheckedChanged(object sender, EventArgs e)
        {
            this.tabPage1.Parent = null;                //隱藏
            this.tabPage2.Parent = null;                //隱藏
            this.tabPage3.Parent = null;                //隱藏
            this.tabPage4.Parent = null;                //隱藏
            this.tabPage5.Parent = null;                //隱藏
            this.tabPage6.Parent = null;                //隱藏
            this.tabPage7.Parent = null;                //隱藏
            this.tabPage8.Parent = null;                //隱藏
            this.tabPage9.Parent = null;                //隱藏
            this.tabPage10.Parent = null;               //隱藏
            tabControl1.SelectedIndex = 2;              //接跳到第3頁。
            label1.Text = "全關，顯示所有頁面、tab選第3頁。";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (radioButton3.Checked == true)
            {
                this.tabPage1.Parent = this.tabControl1;
                this.tabPage2.Parent = this.tabControl1;
                this.tabPage4.Parent = this.tabControl1;
                this.tabPage5.Parent = this.tabControl1;
                this.tabPage7.Parent = this.tabControl1;
                this.tabPage8.Parent = this.tabControl1;
            }
        }

        private void bt_info_Click(object sender, EventArgs e)
        {
            //把所有TabPage的資訊掃瞄一次

            foreach (TabPage tp in tabControl1.TabPages)
            {
                richTextBox1.Text += "tab page name : " + tp.Name + "\n";

                /*
                // Add the Panel to the list.
                Panel panel = page.Controls[0] as Panel;

                this.Controls.Add(panel);
                //Panels.Add(panel);

                // Reparent and move the Panel.
                panel.Parent = tabControl1.Parent;
                panel.Location = tabControl1.Location;
                panel.Visible = false;
                */
            }


        }

    }
}
