﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace HistoryMenu
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private void 打开ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";//设置默认打开文件名称
            openFileDialog1.ShowDialog();//弹出打开文件对话框

            //创建流写入器对象
            StreamWriter s = new StreamWriter("../../History.ini", true);
            s.WriteLine(openFileDialog1.FileName);//向文件中写入历史信息
            s.Flush();//将信息压入流
            s.Close();//关闭流
            ShowWindows(openFileDialog1.FileName);//打开新窗口
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //创建流读取器对象
            StreamReader sr = new StreamReader("../../History.ini");

            //得到菜单项索引
            int i = 文件ToolStripMenuItem.DropDownItems.Count - 2;

            //循环读取流中文本
            while (sr.Peek() >= 0)
            {
                //创建菜单项对象
                ToolStripMenuItem menuitem = new ToolStripMenuItem(sr.ReadLine());
                //向菜单中添加新项
                this.文件ToolStripMenuItem.DropDownItems.Insert(i, menuitem);
                i++;//向菜单中插入索引的位置

                //添加点击事件
                menuitem.Click += new EventHandler(menuitem_Click);
            }
            sr.Close();
        }

        private void menuitem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "menuitem_Click\n";

            //得到菜单项
            ToolStripMenuItem menu = (ToolStripMenuItem)sender;
            ShowWindows(menu.Text); //打开新窗口
        }

        public void ShowWindows(string fileName)
        {
            richTextBox1.Text += "用新表單開啟檔案 : " + fileName + "\n";

            Image p = Image.FromFile(fileName);//得到图像对象
            Form f = new Form();//创建窗体对象
            f.MdiParent = this;//设置父窗体
            f.BackgroundImage = p;//设置背景图片
            f.Show();//显示窗体
        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}

