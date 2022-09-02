using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_get_form_or_control_image
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnForm_Click(object sender, EventArgs e)
        {
            ShowControlImage(this);
        }

        private void btnClientArea_Click(object sender, EventArgs e)
        {
            using (Bitmap bm = GetFormImageWithoutBorders(this))
            {
                SampleForm frm = new SampleForm();
                frm.BackgroundImage = bm;
                frm.ClientSize = bm.Size;
                frm.ShowDialog();
            }
        }

        private void btnGroupBox_Click(object sender, EventArgs e)
        {
            ShowControlImage(groupBox1);
        }

        private void btnPage1_Click(object sender, EventArgs e)
        {
            int selected = tabControl1.SelectedIndex;
            tabControl1.SelectedIndex = 0;

            ShowControlImage(tabPage1);

            tabControl1.SelectedIndex = selected;
        }

        private void btnPage2_Click(object sender, EventArgs e)
        {
            int selected = tabControl1.SelectedIndex;
            tabControl1.SelectedIndex = 1;

            ShowControlImage(tabPage2);
            
            tabControl1.SelectedIndex = selected;
        }

        private void ShowControlImage(Control ctl)
        {
            using (Bitmap bm = GetControlImage(ctl))
            {
                SampleForm frm = new SampleForm();
                frm.BackgroundImage = bm;
                frm.ClientSize = bm.Size;
                frm.ShowDialog();
            }
        }

        // Return a Bitmap holding an image of the control.
        private Bitmap GetControlImage(Control ctl)
        {
            Bitmap bm = new Bitmap(ctl.Width, ctl.Height);
            ctl.DrawToBitmap(bm, new Rectangle(0, 0, ctl.Width, ctl.Height));
            return bm;
        }

        // Return the form's image without its borders and decorations.
        private Bitmap GetFormImageWithoutBorders(Form frm)
        {
            // Get the form's whole image.
            using (Bitmap whole_form = GetControlImage(frm))
            {
                // See how far the form's upper left corner is
                // from the upper left corner of its client area.
                Point origin = frm.PointToScreen(new Point(0, 0));
                int dx = origin.X - frm.Left;
                int dy = origin.Y - frm.Top;

                // Copy the client area into a new Bitmap.
                int wid = frm.ClientSize.Width;
                int hgt = frm.ClientSize.Height;
                Bitmap bm = new Bitmap(wid, hgt);
                using (Graphics gr = Graphics.FromImage(bm))
                {
                    gr.DrawImage(whole_form, 0, 0,
                        new Rectangle(dx, dy, wid, hgt),
                        GraphicsUnit.Pixel);
                }
                return bm;
            }
        }
    }
}
