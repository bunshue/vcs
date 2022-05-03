using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_PictureList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_pictures();
        }

        // The currently loaded pictures.
        private List<Bitmap> Pictures = new List<Bitmap>();
        private const int PictureMargin = 8;

        // The index of the picture we clicked or
        // the picture before which we clicked.
        private int ClickedIndex = -1;

        private void ArrangePanel()
        {
            panel1.Controls.Clear();
            int x = PictureMargin;
            int y = PictureMargin;
            foreach (Bitmap picture in Pictures)
            {
                PictureBox pic = new PictureBox();
                pic.SizeMode = PictureBoxSizeMode.AutoSize;
                pic.Location = new Point(x, y);
                pic.Image = picture;
                pic.Visible = true;
                pic.MouseDown += pic_MouseDown;
                panel1.Controls.Add(pic);

                x += pic.Width + PictureMargin;
            }

            // Add one placeholder PictureBox.
            PictureBox placeholder = new PictureBox();
            placeholder.Location = new Point(x, y);
            placeholder.Size = new Size(0, 0);
            placeholder.Visible = true;
            placeholder.MouseDown += pic_MouseDown;
            panel1.Controls.Add(placeholder);
        }

        private void pic_MouseDown(object sender, MouseEventArgs e)
        {
            // Ignore left mouse clicks.
            if (e.Button != MouseButtons.Right) return;

            // Display the context menu.
            PictureBox pic = sender as PictureBox;
            ShowContextMenu(new Point(pic.Left + e.X, pic.Top + e.Y));
        }

        private void panel1_MouseDown(object sender, MouseEventArgs e)
        {
            // Ignore left mouse clicks.
            if (e.Button != MouseButtons.Right) return;

            // Display the context menu.
            ShowContextMenu(e.Location);
        }

        private void mnuMoveLeft_Click(object sender, EventArgs e)
        {
            Bitmap bm = Pictures[ClickedIndex];
            Pictures.RemoveAt(ClickedIndex);
            Pictures.Insert(ClickedIndex - 1, bm);
            ArrangePanel();
        }

        private void mnuMoveRight_Click(object sender, EventArgs e)
        {
            Bitmap bm = Pictures[ClickedIndex];
            Pictures.RemoveAt(ClickedIndex);
            Pictures.Insert(ClickedIndex + 1, bm);
            ArrangePanel();
        }

        private void mnuDeletePicture_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show(
                "Are you sure you want to delete this picture?",
                "Delete Picture?", MessageBoxButtons.YesNo) == DialogResult.Yes)
            {
                Pictures.RemoveAt(ClickedIndex);
                ArrangePanel();
            }
        }

        // Let the user insert a picture.
        private void mnuInsertPicture_Click(object sender, EventArgs e)
        {
            try
            {
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    int i = 0;
                    foreach (string filename in openFileDialog1.FileNames)
                    {
                        Bitmap bm = new Bitmap(filename);
                        Pictures.Insert(ClickedIndex + i, bm);
                        i++;
                    }
                    ArrangePanel();
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
            ClickedIndex = Pictures.Count;

            // See if we clicked on or before a picture.
            int x = location.X + panel1.HorizontalScroll.Value;
            for (int i = 0; i < Pictures.Count; i++)
            {
                // See if we are before the next picture.
                x -= PictureMargin;
                if (x < 0)
                {
                    ClickedIndex = i;
                    break;
                }   

                // See if we are on this picture.
                x -= panel1.Controls[i].Width;
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
                (clicked_on_picture && (ClickedIndex < Pictures.Count - 1));
            mnuDeletePicture.Enabled = clicked_on_picture;
            mnuInsertPicture.Enabled = !clicked_on_picture;

            // Display the context menu.
            contextMenuStrip1.Show(panel1, location);
        }

        private void show_pictures()
        {
            int i = 0;

            //撈出資料夾內所有png檔
            string folder_name = @"C:\______test_files\__pic\_book_magazine\_books2";

            List<String> filenames = find_all_files(folder_name);

            // 取出單一個List 裡的值，如同陣列(Array)用法
            for (i = 0; i < filenames.Count; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }

            i = 0;

            try
            {
                foreach (string filename in filenames)
                {
                    Bitmap bm = new Bitmap(filename);
                    Pictures.Insert(i, bm);
                    i++;
                }
                ArrangePanel();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        List<String> find_all_files(string folder_name)
        {
            List<String> filenames = new List<String>();

            var dirnames = Directory.GetDirectories(folder_name);
            try
            {
                foreach (var dir in dirnames)
                {
                    var fnames = Directory.GetFiles(dir);
                    foreach (var f in fnames)
                    {
                        //richTextBox1.Text += f + "\n";
                        if (f.ToLower().EndsWith(".jpg") || f.ToLower().EndsWith(".png"))
                            filenames.Add(f);
                    }
                }
                var fnames2 = Directory.GetFiles(folder_name);
                foreach (var f in fnames2)
                {
                    //richTextBox1.Text += f + "\n";
                    if (f.ToLower().EndsWith(".jpg") || f.ToLower().EndsWith(".png"))
                        filenames.Add(f);
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            return filenames;
        }
    }
}
