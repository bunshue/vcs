using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_18_TabControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

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

        private void Form1_Load(object sender, EventArgs e)
        {
            tabControl1.SelectedIndex = 4;      //程式啟動時，直接跳到第5頁。
            label1.Text = "顯示所有頁面、tab選第5頁。";
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
    }
}
