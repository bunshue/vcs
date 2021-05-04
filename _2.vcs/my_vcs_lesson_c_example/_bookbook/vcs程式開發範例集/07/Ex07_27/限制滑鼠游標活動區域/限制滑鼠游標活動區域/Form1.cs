using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 限制滑鼠游標活動區域
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Cursor = new Cursor(Cursor.Current.Handle);
            Cursor.Position = new Point(Cursor.Position.X, Cursor.Position.Y);
            Cursor.Clip = new Rectangle(this.Location, this.Size);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Screen[] screens = Screen.AllScreens;
            this.Cursor = new Cursor(Cursor.Current.Handle);
            Cursor.Clip = screens[0].Bounds;
        }
    }
}