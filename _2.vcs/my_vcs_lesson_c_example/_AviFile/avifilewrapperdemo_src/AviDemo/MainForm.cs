#region Using directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

#endregion

namespace AviDemo {
    partial class MainForm : Form {

        [STAThread]
        public static void Main() {
            Application.Run(new MainForm());
        }
        
        public MainForm() {
            InitializeComponent();
        }
    }
}