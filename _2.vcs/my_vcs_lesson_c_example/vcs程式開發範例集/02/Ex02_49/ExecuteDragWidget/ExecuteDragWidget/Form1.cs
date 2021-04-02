using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ExecuteDragWidget
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //調用移動方法
        private void button1_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(button1, DragDropEffects.Move);
        }
        private void button2_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(button2, DragDropEffects.Move);
        }
        private void button3_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(button3, DragDropEffects.Move);
        }
        private void button4_MouseDown(object sender, MouseEventArgs e)
        {
            DoDragDrop(button4, DragDropEffects.Move);
        }
        //在
        private void Form1_DragDrop(object sender, DragEventArgs e)
        {
            //判斷接對哪個按鈕操作//移動後的坐標
            object data = e.Data.GetData(typeof(Button));
            if (data == button1)
            {
                button1.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                button1.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }
            if (data == button2)
            {
                button2.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                button2.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }
            if (data == button3)
            {
                button3.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                button3.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }
            if (data == button4)
            {
                button4.Top = this.PointToClient(new Point(e.X, e.Y)).Y;
                button4.Left = this.PointToClient(new Point(e.X, e.Y)).X;
            }

        }
        //設置以何種方式移動
        private void Form1_DragEnter(object sender, DragEventArgs e)
        {
            object data = e.Data.GetData(typeof(Button));
            if (data != null)
            {
                e.Effect = DragDropEffects.Move;
            }
            else e.Effect = DragDropEffects.None;
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}