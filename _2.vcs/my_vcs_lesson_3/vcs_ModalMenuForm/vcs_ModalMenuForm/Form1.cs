using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ModalMenuForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Display the "modal context menu."
        private void btnModalMenu_Click(object sender, EventArgs e)
        {
            // Create and initialize the dialog.
            ModalMenuForm dlg = new ModalMenuForm();
            Point pt = new Point(btnModalMenu.Right, btnModalMenu.Bottom);
            PositionDialog(dlg, pt);

            // Display the dialog.
            if (dlg.ShowDialog() == DialogResult.OK)
            {
                this.BackColor = dlg.SelectedColor;
            }
        }

        // Position the dialog over the indicated point in this form's coordinates.
        private void PositionDialog(Form dlg, Point location)
        {
            // Translate into screen coordinates.
            Point pt = this.PointToScreen(location);
            Screen screen = Screen.FromControl(dlg);

            // Adjust if this is at an edge of the screen.
            if (pt.X < screen.WorkingArea.X)
                pt.X = screen.WorkingArea.X;
            if (pt.Y < screen.WorkingArea.Y)
                pt.Y = screen.WorkingArea.Y;
            if (pt.X > screen.WorkingArea.Right - dlg.Width)
                pt.X = screen.WorkingArea.Right - dlg.Width;
            if (pt.Y > screen.WorkingArea.Bottom - dlg.Height)
                pt.Y = screen.WorkingArea.Bottom - dlg.Height;

            // Position the dialog.
            dlg.StartPosition = FormStartPosition.Manual;
            dlg.Location = pt;
        }
    }
}
