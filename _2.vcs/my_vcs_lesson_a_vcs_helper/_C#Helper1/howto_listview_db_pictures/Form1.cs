using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// At design time:
//   Set the ImageList's ImageSize properties to the correct values:
//      imlSmallIcons.ImageSize = 32,32
//      imlLargeIcons.ImageSize = 64,64
//   Set the ImageList's ColorDepth properties to the correct values:
//      imlSmallIcons.ColorDepth = Depth32bit
//      imlLargeIcons.ColorDepth = Depth32bit

using System.Data.OleDb;
using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

// Add the database to the project and set its
// "Copy to Output Directory" properties
// to "Copy if Newer."

// IMPORTANT: Do not open the database in Access or it
// may erase all of the image data.

namespace howto_listview_db_pictures
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Select the first style.
            cboStyle.SelectedIndex = 0;

            // Initialize the ListView.
            lvwBooks.SmallImageList = imlSmallIcons;
            lvwBooks.LargeImageList = imlLargeIcons;

            // Make the column headers.
            lvwBooks.MakeColumnHeaders(
                "Title", 230, HorizontalAlignment.Left,
                "URL", 220, HorizontalAlignment.Left,
                "ISBN", 130, HorizontalAlignment.Left,
                "Picture", 230, HorizontalAlignment.Left,
                "Pages", 50, HorizontalAlignment.Right,
                "Year", 60, HorizontalAlignment.Right);

            // Compose the database file name.
            // This assumes it's in the executable's directory.
            string db_name = Application.StartupPath +
                "\\books_with_images.mdb";

            // Connect to the database
            using (OleDbConnection conn =
                new OleDbConnection(
                    "Provider=Microsoft.ACE.OLEDB.12.0;" +
                    "Data Source=" + db_name + ";" +
                    "Mode=Share Deny None"))
            {
                // Get the book information.
                OleDbCommand cmd = new OleDbCommand(
                    "SELECT Title, URL, ISBN, CoverUrl, " +
                    "Pages, Year, CoverImage FROM Books ORDER BY Year DESC",
                    conn);
                conn.Open();
                using (OleDbDataReader reader = cmd.ExecuteReader())
                {
                    lvwBooks.Items.Clear();
                    imlLargeIcons.Images.Clear();
                    imlSmallIcons.Images.Clear();
                    while (reader.Read())
                    {
                        // Make the images.
                        if (!reader.IsDBNull(6))
                        {
                            // Get the image.
                            Bitmap bm = BytesToImage((byte[])reader.GetValue(6));
                            float source_aspect = bm.Width / (float)bm.Height;

                            // Make the large image.
                            AddImageToImageList(imlLargeIcons,
                                bm, reader[0].ToString(),
                                imlLargeIcons.ImageSize.Width,
                                imlLargeIcons.ImageSize.Height);

                            // Make the small image.
                            AddImageToImageList(imlSmallIcons,
                                bm, reader[0].ToString(),
                                imlLargeIcons.ImageSize.Width,
                                imlLargeIcons.ImageSize.Height);
                        }

                        // Add the data row.
                        lvwBooks.AddRow(
                            reader[0].ToString(),   // Image key
                            reader[0].ToString(),   // Title
                            reader[1].ToString(),   // URL
                            reader[2].ToString(),   // ISBN
                            reader[3].ToString(),   // CoverUrl
                            reader[4].ToString(),   // Pages
                            reader[5].ToString());  // Year
                    }
                }
            }
        }

        // Scale the image to fit in the ImageList and add it.
        private void AddImageToImageList(ImageList iml, Bitmap bm,
            string key, float wid, float hgt)
        {
            // Make the bitmap.
            Bitmap iml_bm = new Bitmap(
                iml.ImageSize.Width,
                iml.ImageSize.Height);
            using (Graphics gr = Graphics.FromImage(iml_bm))
            {
                gr.Clear(Color.Transparent);
                gr.InterpolationMode = InterpolationMode.High;

                // See where we need to draw the image to scale it properly.
                RectangleF source_rect = new RectangleF(
                    0, 0, bm.Width, bm.Height);
                RectangleF dest_rect = new RectangleF(
                    0, 0, iml_bm.Width, iml_bm.Height);
                dest_rect = ScaleRect(source_rect, dest_rect);

                // Draw the image.
                gr.DrawImage(bm, dest_rect, source_rect,
                    GraphicsUnit.Pixel);
            }

            // Add the image to the ImageList.
            iml.Images.Add(key, iml_bm);
        }

        // Convert a byte array into an image.
        private Bitmap BytesToImage(byte[] bytes)
        {
            using (MemoryStream image_stream =
                new MemoryStream(bytes))
            {
                Bitmap bm = new Bitmap(image_stream);
                return bm;
            }
        }

        // Scale an image without disorting it.
        // Return a centered rectangle in the destination area.
        private RectangleF ScaleRect(
            RectangleF source_rect, RectangleF dest_rect)
        {
            float source_aspect =
                source_rect.Width / source_rect.Height;
            float wid = dest_rect.Width;
            float hgt = dest_rect.Height;
            float dest_aspect = wid / hgt;

            if (source_aspect > dest_aspect)
            {
                // The source is relatively short and wide.
                // Use all of the available width.
                hgt = wid / source_aspect;
            }
            else
            {
                // The source is relatively tall and thin.
                // Use all of the available height.
                wid = hgt * source_aspect;
            }

            // Center it.
            float x = dest_rect.Left + (dest_rect.Width - wid) / 2;
            float y = dest_rect.Top + (dest_rect.Height - hgt) / 2;
            return new RectangleF(x, y, wid, hgt);
        }

        // Change the ListView's display style.
        private void cboStyle_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (cboStyle.Text)
            {
                case "Large Icons":
                    lvwBooks.View = View.LargeIcon;
                    break;
                case "Small Icons":
                    lvwBooks.View = View.SmallIcon;
                    break;
                case "List":
                    lvwBooks.View = View.List;
                    break;
                case "Tile":
                    lvwBooks.View = View.Tile;
                    break;
                case "Details":
                    lvwBooks.View = View.Details;
                    break;
            }
        }
    }
}
