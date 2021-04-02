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
    public partial class ResembleBrowser : Form
    {
        public ResembleBrowser()
        {
            InitializeComponent();
        }
        private bool EditState = false;//定義一個全局變量標識
        private void comboBox1_KeyDown(object sender, KeyEventArgs e)
        {
            EditState = (e.KeyCode != Keys.Back && e.KeyCode != Keys.Delete);//當按鍵既不是Back鍵又不是Delete鍵時
            comboBox1.DroppedDown = true;//當有按鍵被按下時顯示下拉列表
        }
        private void comboBox1_TextChanged(object sender, EventArgs e)
        {
            if (EditState)//當變量的值為真時
            {
                string importText = comboBox1.Text;//獲得輸入的文本
                int index = comboBox1.FindString(importText);//在ComboBox集合中查找匹配的文本
                if (index >= 0)                        //當有查找結果時 
                {
                    EditState = false;                //關閉編輯狀態
                    comboBox1.SelectedIndex = index;    //找到對應項
                    EditState = true;                 //打開編輯狀態
                    comboBox1.Select(importText.Length, comboBox1.Text.Length);//設定文本的選擇長度
                }
            }
        }
        private void ResembleBrowser_Load(object sender, EventArgs e)
        {
            this.comboBox1.Items.Add("http://www.yahoo.com/");//向ComboBox控件中添加網址「http://www.baidu.com/」
            this.comboBox1.Items.Add("http://www.sina.com/");//向ComboBox控件中添加網址「http://www.sina.com.cn/」
            this.comboBox1.Items.Add("http://www.google.com/");//向ComboBox控件中添加網址「http://www.163.com/」
            this.comboBox1.Items.Add("http://www.microsoft.com/");//向ComboBox控件中添加網址「http://www.qq.com/」
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
