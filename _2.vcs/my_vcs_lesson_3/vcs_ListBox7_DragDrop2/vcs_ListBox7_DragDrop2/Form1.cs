using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListBox7_DragDrop2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

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
        private void listBox2_DragDorp(object sender, DragEventArgs e)
        {
            //加入型別判斷
            if (e.Data.GetData(typeof(string)) != null)
            {
                listBox2.Items.Add(e.Data.GetData(typeof(string)).ToString());                      
            }
        }
    }
}
