using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.Reflection;

namespace vcs_SetupCursor
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll")]
        public static extern IntPtr LoadCursorFromFile(string fileName);

        [DllImport("user32.dll")]
        public static extern IntPtr SetCursor(IntPtr cursorHandle);

        [DllImport("user32.dll")]
        public static extern uint DestroyCursor(IntPtr cursorHandle);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Cursor myCursor = new Cursor(Cursor.Current.Handle);
            //dinosau2.ani為Windows自帶的光標：
            IntPtr colorCursorHandle = LoadCursorFromFile(@"C:\Windows\Cursors\aero_link_il.cur");
            myCursor.GetType().InvokeMember("handle", BindingFlags.Public |
            BindingFlags.NonPublic | BindingFlags.Instance |
            BindingFlags.SetField, null, myCursor, new object[] { colorCursorHandle });
            this.Cursor = myCursor;

        }
    }
}
