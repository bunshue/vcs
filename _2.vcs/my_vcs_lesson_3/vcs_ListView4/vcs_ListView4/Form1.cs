using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;//聲明與文件的輸入輸出流有關的命名空間

namespace vcs_ListView4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public static bool flag = false;//定義一個全局變量標識
        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.GridLines = true;//設置是否在listView1控件中顯示網格線
            listView1.Dock = DockStyle.Fill;//設置listView1控件在其父容器中的停靠方式
            listView1.Columns.Add("文件名稱", 120, HorizontalAlignment.Left);//在listView1中添加「文件名稱」列
            listView1.Columns.Add("文件屬性", 210, HorizontalAlignment.Left);//在listView1中添加「文件屬性」列
            listView1.Columns.Add("創建時間", 200, HorizontalAlignment.Left);//在listView1中添加「創建時間」列
            foreach (String fileName in Directory.GetFiles("C:\\"))//循環遍歷C盤目錄空間
            {
                FileInfo file = new FileInfo(fileName);//聲明一個操作文件的實例
                ListViewItem OptionItem = new ListViewItem(file.Name);//實例化一個listView控件中選擇項的實例
                OptionItem.SubItems.Add(file.Attributes.ToString());//在listView控件中添加文件屬性列
                OptionItem.SubItems.Add(file.CreationTime.ToString());//在listView控件中文件創建時間列
                listView1.Items.Add(OptionItem);//向listView控件中追加新添加的各列
            }
            listView1.HideSelection = true;//設置控件的高亮顯示屬性為true
        }

        private void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            listView1.SelectedItems[0].ForeColor = Color.Red;//設置當前選擇項為紅色
        }

        private void 取消選擇ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count != 0)//當listView1控件中的選擇項不為0時
            {
                for (int i = 0; i < listView1.SelectedItems.Count; i++)//循環遍歷控件中的每一個選擇項
                {
                    if (listView1.SelectedItems[i].ForeColor == Color.Red)//當選擇項為紅顏色時
                    {
                        listView1.SelectedItems[i].ForeColor = Color.Black;//設置選擇項為黑顏色
                    }
                }
            }
        }
    }
}
