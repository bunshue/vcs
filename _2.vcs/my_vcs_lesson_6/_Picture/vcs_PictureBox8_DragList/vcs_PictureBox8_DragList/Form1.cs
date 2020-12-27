using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureBox8_DragList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The currently loaded PictureBoxes.
        private List<PictureBox> PictureBoxes =
            new List<PictureBox>();
        private const int PictureMargin = 8;

        // A placeholder to ensure that the Panel
        // control has some empty area to the right.
        PictureBox Placeholder;

        // The index of the picture we clicked or
        // the picture before which we clicked.
        private int ClickedIndex = -1;

        // Used to drag PictureBoxes.
        private PictureBox DragPic = null;
        private Point DragOffset;

        // Create the placeholder PictureBox.
        private void Form1_Load(object sender, EventArgs e)
        {
            Placeholder = new PictureBox();
            Placeholder.Location = new Point(PictureMargin, PictureMargin);
            Placeholder.Size = new Size(0, 0);
            Placeholder.Visible = true;
            panPictures.Controls.Add(Placeholder);
        }

        // Arrange the PictureBoxes.
        private void ArrangePictureBoxes()
        {
            int ymax = 0;
            int x = PictureMargin;
            int y = PictureMargin;
            foreach (PictureBox pic in PictureBoxes)
            {
                pic.Location = new Point(x, y);
                x += pic.Width + PictureMargin;
                if (ymax < pic.Height) ymax = pic.Height;
            }

            // Position one placeholder PictureBox.
            y = ymax + 2 * PictureMargin;
            Placeholder.Location = new Point(x, y);
        }

        // Rearrange the picture list so the controls
        // are ordered by their X coordinates.
        private void OrderPictureBoxes()
        {
            // Sort the PictureBoxes list.
            PictureBoxes.Sort((pic1, pic2) =>
                pic1.Location.X.CompareTo(pic2.Location.X));

            // Rearrange the controls.
            ArrangePictureBoxes();
        }

        // Start dragging the control or display the context menu.
        private void pic_MouseDown(object sender, MouseEventArgs e)
        {
            PictureBox pic = sender as PictureBox;

            if (e.Button == MouseButtons.Left)
            {
                // Start dragging.
                DragPic = pic;
                int dx = -e.Location.X;
                int dy = -e.Location.Y;
                DragOffset = new Point(dx, dy);

                // Move the PictureBox to the top of the
                // panPictures stacking order.
                panPictures.Controls.SetChildIndex(pic, 0);

                // Let panPictures handle the MouseMove and MouseUp.
                DragPic.Capture = false;
                panPictures.Capture = true;
                panPictures.MouseMove += panPictures_MouseMove;
                panPictures.MouseUp += panPictures_MouseUp;
            }
            else
            {
                // Get the mouse's location in panPictures coordinates.
                Point screen_point = pic.PointToScreen(e.Location);
                Point parent_point = panPictures.PointToClient(screen_point);

                // Display the context menu.
                ShowContextMenu(new Point(
                    parent_point.X,
                    parent_point.Y));
            }
        }

        // Move a PictureBox.
        private void panPictures_MouseMove(object sender, MouseEventArgs e)
        {
            int x = e.Location.X + DragOffset.X;
            int y = e.Location.Y + DragOffset.Y;
            DragPic.Location = new Point(x, y);
        }

        // Stop dragging DragPic.
        private void panPictures_MouseUp(object sender, MouseEventArgs e)
        {
            DragPic = null;
            panPictures.MouseMove -= panPictures_MouseMove;
            panPictures.MouseUp -= panPictures_MouseUp;
            OrderPictureBoxes();
        }

        // Display the context menu.
        private void panPictures_MouseDown(object sender, MouseEventArgs e)
        {
            // Ignore left mouse clicks.
            if (e.Button != MouseButtons.Right) return;

            // Display the context menu.
            ShowContextMenu(e.Location);
        }

        private void mnuMoveLeft_Click(object sender, EventArgs e)
        {
            PictureBox pic = PictureBoxes[ClickedIndex];
            PictureBoxes.RemoveAt(ClickedIndex);
            PictureBoxes.Insert(ClickedIndex - 1, pic);
            ArrangePictureBoxes();
        }

        private void mnuMoveRight_Click(object sender, EventArgs e)
        {
            PictureBox pic = PictureBoxes[ClickedIndex];
            PictureBoxes.RemoveAt(ClickedIndex);
            PictureBoxes.Insert(ClickedIndex + 1, pic);
            ArrangePictureBoxes();
        }

        private void mnuDeletePicture_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show(
                "Are you sure you want to delete this picture?",
                "Delete Picture?", MessageBoxButtons.YesNo) == DialogResult.Yes)
            {
                panPictures.Controls.Remove(PictureBoxes[ClickedIndex]);
                PictureBoxes.RemoveAt(ClickedIndex);
                ArrangePictureBoxes();
            }
        }

        // Let the user insert a picture.
        private void mnuInsertPicture_Click(object sender, EventArgs e)
        {
            try
            {
                if (ofdPicture.ShowDialog() == DialogResult.OK)
                {
                    int i = 0;
                    foreach (string filename in ofdPicture.FileNames)
                    {
                        Bitmap bm = new Bitmap(filename);

                        PictureBox pic = new PictureBox();
                        pic.SizeMode = PictureBoxSizeMode.AutoSize;
                        pic.Image = bm;
                        pic.Visible = true;
                        pic.BorderStyle = BorderStyle.Fixed3D;
                        pic.MouseDown += pic_MouseDown;
                        panPictures.Controls.Add(pic);

                        PictureBoxes.Insert(ClickedIndex + i, pic);
                        i++;
                    }
                    ArrangePictureBoxes();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        // Prepare the context menu and display it.
        private void ShowContextMenu(Point location)
        {
            // Assume we click after the final picture.
            bool clicked_on_picture = false;
            ClickedIndex = PictureBoxes.Count;

            // See if we clicked on or before a picture.
            int x = location.X + panPictures.HorizontalScroll.Value;
            for (int i = 0; i < PictureBoxes.Count; i++)
            {
                // See if we are before the next picture.
                x -= PictureMargin;
                if (x < 0)
                {
                    ClickedIndex = i;
                    break;
                }   

                // See if we are on this picture.
                x -= PictureBoxes[i].Width;
                if (x < 0)
                {
                    ClickedIndex = i;
                    clicked_on_picture = true;
                    break;
                }
            }

            // Enable and disable contect menu items.
            mnuMoveLeft.Enabled =
                (clicked_on_picture && (ClickedIndex > 0));
            mnuMoveRight.Enabled =
                (clicked_on_picture && (ClickedIndex < PictureBoxes.Count - 1));
            mnuDeletePicture.Enabled = clicked_on_picture;
            mnuInsertPicture.Enabled = !clicked_on_picture;

            // Display the context menu.
            ctxPictures.Show(panPictures, location);
        }
    }
}
