using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace howto_thumbnail_web_table
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Select default directories.
        private void Form1_Load(object sender, EventArgs e)
        {
            DirectoryInfo dir_info;
            dir_info = new DirectoryInfo(
                Path.Combine(Application.StartupPath, "..\\..\\Input"));
            txtInputDir.Text = dir_info.FullName;

            dir_info = new DirectoryInfo(
                Path.Combine(Application.StartupPath, "..\\..\\Output"));
            txtOutputDir.Text = dir_info.FullName;
        }

        // Let the user select the input directory.
        private void btnPickInputDirectory_Click(object sender, EventArgs e)
        {
            fbdDirectory.SelectedPath = txtInputDir.Text;
            if (fbdDirectory.ShowDialog() == DialogResult.OK)
            {
                txtInputDir.Text = fbdDirectory.SelectedPath;
            }
        }

        // Let the user select the output directory.
        private void btnPickOutputDirectory_Click(object sender, EventArgs e)
        {
            fbdDirectory.SelectedPath = txtOutputDir.Text;
            if (fbdDirectory.ShowDialog() == DialogResult.OK)
            {
                txtOutputDir.Text = fbdDirectory.SelectedPath;
            }
        }

        // Make the web page and thumbnails.
        private void btnGo_Click(object sender, EventArgs e)
        {
            // Get inputs.
            string input_dir = txtInputDir.Text;
            if (!input_dir.EndsWith("\\")) input_dir += "\\";
            string output_dir = txtOutputDir.Text;
            if (!output_dir.EndsWith("\\")) output_dir += "\\";
            string url_prefix = txtUrlPrefix.Text;
            if ((url_prefix.Length > 0) && (!url_prefix.EndsWith("/"))) url_prefix += "/";
            int thumb_width = int.Parse(txtThumbWidth.Text);
            int thumb_height = int.Parse(txtThumbHeight.Text);

            // Do the work.
            MakeWebPage(input_dir, output_dir, url_prefix,
                txtWebPage.Text, thumb_width, thumb_height);
        }

        // Make the web page and thumbnails.
        private void MakeWebPage(string input_dir, string output_dir, string url_prefix, string web_page, int thumb_width, int thumb_height)
        {
            // Open the HTML file.
            string html_filename = output_dir + web_page;
            using (StreamWriter html_file = new StreamWriter(html_filename))
            {
                // Start the table.
                html_file.WriteLine("<table width=\"100%\" border=\"1\">");

                // Start the table's first row.
                html_file.WriteLine("  <tr>");

                // Keep track of the number of images in a row.
                const int thumbs_per_row = 4;
                int thumbs_this_row = 0;

                // Make a list of the image files.
                List<string> files =
                    FindFiles(input_dir, "*.bmp;*.gif;*.jpg;*.png;*.tif", false);

                // Process the files.
                foreach (string image_filename in files)
                {
                    // Copy the file to the destination directory.
                    FileInfo image_fileinfo = new FileInfo(image_filename);
                    string dest_filename = output_dir + image_fileinfo.Name;
                    File.Copy(image_filename, dest_filename, true);

                    // Get the image.
                    using (Bitmap bm = new Bitmap(image_filename))
                    {
                        // Get the original size.
                        Rectangle src_rect =
                            new Rectangle(0, 0, bm.Width, bm.Height);

                        // Shrink the image.
                        double scale = Math.Min(
                            (double)thumb_width / bm.Width,
                            (double)thumb_height / bm.Height);
                        int shrunk_width = (int)(bm.Width * scale);
                        int shrunk_height = (int)(bm.Height * scale);
                        Rectangle dest_rect =
                            new Rectangle(0, 0, shrunk_width, shrunk_height);

                        using (Bitmap thumbnail = new Bitmap(shrunk_width, shrunk_height))
                        {
                            // Copy the image at reduced scale.
                            using (Graphics gr = Graphics.FromImage(thumbnail))
                            {
                                gr.DrawImage(bm, dest_rect, src_rect, GraphicsUnit.Pixel);
                            }

                            // Save the thumbnail image.
                            string thumb_filename =
                                dest_filename.Substring(0,
                                    dest_filename.Length - image_fileinfo.Extension.Length) +
                                "_thumb.png";
                            thumbnail.Save(thumb_filename, ImageFormat.Png);

                            // Add the thumbnail image to the HTML page.
                            FileInfo thumb_fileinfo = new FileInfo(thumb_filename);

                            // See if we need to start a new row.
                            if (++thumbs_this_row > thumbs_per_row)
                            {
                                thumbs_this_row = 1;
                                html_file.WriteLine("  </tr>");
                                html_file.WriteLine("  <tr>");
                            }

                            // Add the thumbnail, the file's name, and its size.
                            html_file.WriteLine("    <td align=\"center\">");
                            html_file.WriteLine("      " +
                                "<a href=\"" + url_prefix + image_fileinfo.Name + "\">" +
                                "<img src=\"" + url_prefix + thumb_fileinfo.Name + "\">" +
                                "</a>");
                            html_file.WriteLine("      <br>");
                            html_file.WriteLine("      " + image_fileinfo.Name);
                            html_file.WriteLine("      <br>");
                            html_file.WriteLine("      (" +
                                image_fileinfo.Length.ToFileSizeApi() + ")");
                            html_file.WriteLine("    </td>");
                        } // using (Bitmap thumbnail = new Bitmap(shrunk_width, shrunk_height))
                    } // using (Bitmap bm = new Bitmap(image_file))
                } // foreach (string image_file in files)

                // End the table's final row and the table.
                html_file.WriteLine("  </tr>");
                html_file.WriteLine("</table>");

                // Close the HTML file.
                html_file.Close();

                MessageBox.Show("Processed " + files.Count + " images.");
            } // using (StreamWriter html_file = new StreamWriter(html_filename))
        } // MakeWebPage

        // Search for files matching the patterns.
        private List<string> FindFiles(string dir_name, string patterns, bool search_subdirectories)
        {
            // Make the result list.
            List<string> files = new List<string>();

            // Get the patterns.
            string[] pattern_array = patterns.Split(';');

            // Search.
            SearchOption search_option = SearchOption.TopDirectoryOnly;
            if (search_subdirectories) search_option = SearchOption.AllDirectories;
            foreach (string pattern in pattern_array)
            {
                foreach (string filename in Directory.GetFiles(dir_name, pattern, search_option))
                {
                    if (!files.Contains(filename)) files.Add(filename);
                }
            }

            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }
    }
}
