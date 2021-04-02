using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace SnatchAtMouse
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            Graphics myGraphics = this.CreateGraphics();
            Cursor.Draw(myGraphics, new Rectangle(e.X, e.Y, 10, 10));
        }
    }
}