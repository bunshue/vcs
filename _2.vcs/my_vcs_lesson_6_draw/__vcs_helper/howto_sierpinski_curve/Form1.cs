using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_sierpinski_curve
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private bool m_Refresh;
        private Bitmap m_Bm;

        private void btnGo_Click(object sender, EventArgs e)
        {
            int depth = int.Parse(txtDepth.Text);
            if (depth > 8)
            {
                if (MessageBox.Show("A large depth may take a long time to draw. Do you want to continue?",
                    "Continue?", MessageBoxButtons.YesNo,
                    MessageBoxIcon.Question) == DialogResult.No)
                {
                    return;
                }
            }

            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();

            // See if we should refresh as we draw.
            m_Refresh = chkRefresh.Checked;

            m_Bm = new Bitmap(picCanvas.ClientSize.Width, picCanvas.ClientSize.Height);
            picCanvas.Image = m_Bm;

            using (Graphics gr = Graphics.FromImage(m_Bm))
            {
                // Draw the curve.
                gr.Clear(picCanvas.BackColor);

                float dx = (float)(m_Bm.Width / Math.Pow(2, depth - 1) / 8);
                float dy = (float)(m_Bm.Height / Math.Pow(2, depth - 1) / 8);
                Sierpinski(gr, depth, dx, dy);
            }

            // Display the result.
            picCanvas.Refresh();
            this.Cursor = Cursors.Default;
        }

        // Draw a Sierpinski curve.
        private void Sierpinski(Graphics gr, int depth, float dx, float dy)
        {
            float x = 2 * dx;
            float y = dy;

            SierpA(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, dx, dy);
            SierpB(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, -dx, dy);
            SierpC(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, -dx, -dy);
            SierpD(gr, depth, dx, dy, ref x, ref y);
            DrawRel(gr, ref x, ref y, dx, -dy);

            picCanvas.Refresh();
        }

        // Draw right across the top.
        private void SierpA(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;

                SierpA(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, dy);
                SierpB(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, 2 * dx, 0);
                SierpD(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, -dy);
                SierpA(gr, depth, dx, dy, ref x, ref y);
            }

            if (m_Refresh) picCanvas.Refresh();
        }

        // Draw down on the right.
        private void SierpB(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;
                SierpB(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, dy);
                SierpC(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, 0, 2 * dy);
                SierpA(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, dy);
                SierpB(gr, depth, dx, dy, ref x, ref y);
            }

            if (m_Refresh) picCanvas.Refresh();
        }

        // Draw left across the bottom.
        private void SierpC(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;
                SierpC(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, -dy);
                SierpD(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -2 * dx, 0);
                SierpB(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, dy);
                SierpC(gr, depth, dx, dy, ref x, ref y);
            }

            if (m_Refresh) picCanvas.Refresh();
        }

        // Draw up along the left.
        private void SierpD(Graphics gr, float depth, float dx, float dy, ref float x, ref float y)
        {
            if (depth > 0)
            {
                depth--;
                SierpD(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, dx, -dy);
                SierpA(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, 0, -2 * dy);
                SierpC(gr, depth, dx, dy, ref x, ref y);
                DrawRel(gr, ref x, ref y, -dx, -dy);
                SierpD(gr, depth, dx, dy, ref x, ref y);
            }

            if (m_Refresh) picCanvas.Refresh();
        }

        // Draw a line between (x, y) and (x + dx, y + dy).
        // Update x and y.
        private void DrawRel(Graphics gr, ref float x, ref float y, float dx, float dy)
        {
            gr.DrawLine(Pens.Black, x, y, x + dx, y + dy);
            x += dx;
            y += dy;
        }
    }
}
