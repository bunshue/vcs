using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DragControl
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.TransparencyKey = SystemColors.Control;
            foreach (Control subCtrl in this.Controls)
            {
                new MoveControl(subCtrl);   
            }
        }
    }
}
