using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ResembleBrowser
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private bool State = false;//定义一个全局变量标识

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            comboBox1.Items.Add("http://www.mingribook.com/");
            comboBox1.Items.Add("http://www.baidu.com/");
            comboBox1.Items.Add("http://www.sina.com.cn/");
            comboBox1.Items.Add("http://www.163.com/");
            comboBox1.Items.Add("http://www.qq.com/");
            comboBox1.Items.Add("http://www.yahoo.com.tw/");
            comboBox1.Items.Add("http://www.google.com.tw/");
        }

        private void comboBox1_TextChanged(object sender, EventArgs e)
        {
            if (State == true)//当变量的值为真时
            {
                string importText = comboBox1.Text;//获得输入的文本
                int index = comboBox1.FindString(importText);//在ComboBox集合中查找匹配的文本
                if (index >= 0)//当有查找结果时 
                {
                    State = false;//关闭编辑状态
                    comboBox1.SelectedIndex = index;//找到对应项
                    State = true;//打开编辑状态
                    comboBox1.Select(importText.Length, comboBox1.Text.Length);//设定文本的选择长度
                }
            }
        }

        private void comboBox1_KeyDown(object sender, KeyEventArgs e)
        {
            State = (e.KeyCode != Keys.Back && e.KeyCode != Keys.Delete);//当按键既不是Back键又不是Delete键时
            comboBox1.DroppedDown = true;//当有按键被按下时显示下拉列表
        }
    }
}

