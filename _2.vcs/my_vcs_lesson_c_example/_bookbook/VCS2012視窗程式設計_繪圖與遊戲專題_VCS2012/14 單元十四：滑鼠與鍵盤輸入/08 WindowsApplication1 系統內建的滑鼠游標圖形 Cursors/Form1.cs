/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        Cursor[] cursorList = new Cursor[] {  // 系統內建的全部滑鼠游標圖形 
               Cursors.AppStarting, Cursors.Arrow, Cursors.Cross,
               Cursors.Default, Cursors.Hand, Cursors.Help,
               Cursors.HSplit, Cursors.IBeam, Cursors.No,
               Cursors.NoMove2D, Cursors.NoMoveHoriz, Cursors.NoMoveVert,
               Cursors.PanEast, Cursors.PanNE, Cursors.PanNorth,
               Cursors.PanNW, Cursors.PanSE, Cursors.PanSouth,
               Cursors.PanSW, Cursors.PanWest, Cursors.SizeAll,
               Cursors.SizeNESW, Cursors.SizeNS, Cursors.SizeNWSE,
               Cursors.SizeWE, Cursors.UpArrow, Cursors.VSplit, Cursors.WaitCursor};

        public Form1()
        {
            InitializeComponent();

            foreach (Cursor cursor in cursorList)
                comboBox1.Items.Add(cursor);  // 加入到 comboBox1 清單內
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Point pt = Cursor.Position; // 滑鼠座標
            pt = this.PointToClient(pt); // 螢幕座標 -> 視窗客戶區座標
            label1.Text = pt.X.ToString() + ", " + pt.Y.ToString();
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Invalidate();  // 要求表單重畫
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();  // 要求表單重畫
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.Cursor = (Cursor)comboBox1.SelectedItem; // 取出 選定的 滑鼠游標
        }
    }
}