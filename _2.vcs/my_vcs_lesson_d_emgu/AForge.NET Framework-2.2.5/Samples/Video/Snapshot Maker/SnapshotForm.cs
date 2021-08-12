using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Windows.Forms;
using System.IO;

namespace Snapshot_Maker
{
    public partial class SnapshotForm : Form
    {
        public SnapshotForm()
        {
            InitializeComponent();
        }

        private void SnapshotForm_Load(object sender, EventArgs e)
        {

        }

        public void SetImage(Bitmap bitmap)
        {
            timeBox.Text = DateTime.Now.ToLongTimeString();

            lock (this)
            {
                Bitmap old = (Bitmap)pictureBox.Image;
                pictureBox.Image = bitmap;

                if (old != null)
                {
                    old.Dispose();
                }
            }
        }

        private void saveButton_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\snapshot_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                lock (this)
                {
                    Bitmap bitmap1 = (Bitmap)pictureBox.Image;
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    //richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                MessageBox.Show("Failed saving the snapshot.\n" + ex.Message,
                    "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}

