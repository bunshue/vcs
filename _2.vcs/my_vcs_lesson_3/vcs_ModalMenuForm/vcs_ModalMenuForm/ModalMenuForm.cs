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
    public partial class ModalMenuForm : Form
    {
        public ModalMenuForm()
        {
            InitializeComponent();
        }

        // Return the color selected in the ListBox.
        public Color SelectedColor
        {
            get
            {
                if (lstItems.SelectedItem == null) return SystemColors.Control;
                string color_name = lstItems.SelectedItem.ToString().Replace(" ", "");
                return Color.FromName(color_name);
            }
        }

        // Get the form ready.
        private void ModalMenuForm_Load(object sender, EventArgs e)
        {
            // Make the ListBox owner-drawn.
            lstItems.DrawMode = DrawMode.OwnerDrawVariable;

            // Set form properties.
            this.FormBorderStyle = FormBorderStyle.None;
            this.KeyPreview = true;

            // Make the form fit the ListBox.
            this.ClientSize = lstItems.Size;
        }

        // Close the dialog if the user presses Escape or Enter.
        private void ModalMenuForm_KeyDown(object sender, KeyEventArgs e)
        {
            // If the user pressed Escape, return DialogResult.Cancel.
            if (e.KeyCode == Keys.Escape) DialogResult = DialogResult.Cancel;

            // If the user pressed Escape, return
            // DialogResult.OK if a color is selected.
            if (e.KeyCode == Keys.Enter)
            {
                if (lstItems.SelectedIndex < 0) DialogResult = DialogResult.Cancel;
                else DialogResult = DialogResult.OK;
            }
        }

        // Calculate the size of an item.
        private int ItemMargin = 5;
        private void lstItems_MeasureItem(object sender, MeasureItemEventArgs e)
        {
            // Get the ListBox and the item.
            ListBox lst = sender as ListBox;
            string txt = lst.Items[e.Index].ToString();

            // Measure the string.
            SizeF txt_size = e.Graphics.MeasureString(txt, this.Font);

            // Set the required size.
            e.ItemHeight = (int)txt_size.Height + 2 * ItemMargin;
            e.ItemWidth = (int)txt_size.Width;
        }

        // Draw the item.
        private void lstItems_DrawItem(object sender, DrawItemEventArgs e)
        {
            // Get the ListBox and the item.
            ListBox lst = sender as ListBox;
            string txt = lst.Items[e.Index].ToString();

            // Draw the background.
            e.DrawBackground();

            if ((e.State & DrawItemState.Selected) == DrawItemState.Selected)
            {
                // Selected. Draw with the system highlight color.
                e.Graphics.DrawString(txt, this.Font,
                    SystemBrushes.HighlightText, e.Bounds.Left, e.Bounds.Top + ItemMargin);
            }
            else
            {
                // Not selected. Draw with ListBox's foreground color.
                using (SolidBrush br = new SolidBrush(e.ForeColor))
                {
                    e.Graphics.DrawString(txt, this.Font, br,
                        e.Bounds.Left, e.Bounds.Top + ItemMargin);
                }
            }

            // Don't draw the focus rectangle for
            // this example because the user cannot use
            // the arrow keys to change the selection.
            //// Draw the focus rectangle if appropriate.
            //e.DrawFocusRectangle();
        }

        // Select the ListBox item under the mouse.
        private void lstItems_MouseMove(object sender, MouseEventArgs e)
        {
            int index = lstItems.IndexFromPoint(e.Location);
            if (lstItems.SelectedIndex != index) lstItems.SelectedIndex = index;
        }

        // If the form isn't closing, deselect the ListBox item.
        private void lstItems_MouseLeave(object sender, EventArgs e)
        {
            // If the form is closing, leave the selection alone.
            if (DialogResult != DialogResult.None) return;
            if (lstItems.SelectedIndex != -1) lstItems.SelectedIndex = -1;
        }

        private void lstItems_Click(object sender, EventArgs e)
        {
            if (lstItems.SelectedIndex < 0) DialogResult = DialogResult.Cancel;
            else DialogResult = DialogResult.OK;
        }
    }
}
