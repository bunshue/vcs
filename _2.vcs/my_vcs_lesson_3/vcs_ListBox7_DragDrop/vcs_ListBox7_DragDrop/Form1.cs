using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListBox7_DragDrop
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //兩個listBox都要設AllowDrop為true

        //listBox1 DragOver
        private void listBox1_DragOver(object sender, DragEventArgs e)
        {
            e.Effect = DragDropEffects.Copy;
            listBox1.SelectionMode = SelectionMode.MultiSimple;
        }

        //listBox1 MouseMove
        private void listBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if ((e.Button & MouseButtons.Left) == MouseButtons.Left)
            {
                listBox1.SelectionMode = SelectionMode.One;
                string r = listBox1.SelectedItem.ToString();
                this.listBox1.DoDragDrop(r, DragDropEffects.Copy);
            }
        }

        //listBox2 DragEnter
        private void listBox2_DragEnter(object sender, DragEventArgs e)
        {
            //加入型別判斷，不符合的排除
            if (e.Data.GetDataPresent(typeof(string)))
            {
                e.Effect = DragDropEffects.Copy;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }


        }

        //listBox2 DragDorp
        private void listBox2_DragDrop(object sender, DragEventArgs e)
        {
            //加入型別判斷
            if (e.Data.GetData(typeof(string)) != null)
            {
                listBox2.Items.Add(e.Data.GetData(typeof(string)).ToString());
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "listBox1 的內容 : \n";
            foreach (string sss in listBox1.Items)
            {
                richTextBox1.Text += sss + "\n";
            }
            richTextBox1.Text += "\nlistBox2 的內容 : \n";
            foreach (string sss in listBox2.Items)
            {
                richTextBox1.Text += sss + "\n";
            }

        }
    }
}
