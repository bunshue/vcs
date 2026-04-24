// Blobs Browser sample application
// AForge.NET framework
// http://www.aforgenet.com/framework/
//
// Copyright © AForge.NET, 2006-2011
// contacts@aforgenet.com
//

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Resources;

using System.Reflection;

using AForge.Imaging;

/*
Convex Hull 凸面 殼體
Left/Right Edges 左右邊緣
Top/Bottom Edges 上下邊緣
Quadrilateral 四邊形的
*/

namespace BlobsExplorer
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {
            highlightTypeCombo.SelectedIndex = 0;
            showRectangleAroundSelectionCheck.Checked = blobsBrowser.ShowRectangleAroundSelection;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\gear-wrench-icon-512-278694.png";
            //string filename = @"D:\_git\vcs\_4.python\opencv\data\_Hough\shapes.jpg";

            ProcessImage((Bitmap)Bitmap.FromFile(filename));


            /*
            //使用預設圖
            // load arrow bitmap
            Assembly assembly = this.GetType().Assembly;
            Bitmap image = new Bitmap(assembly.GetManifestResourceStream("BlobsExplorer.demo.png"));
            ProcessImage(image);
            */
        }

        // Process image
        private void ProcessImage(Bitmap image)
        {
            int foundBlobsCount = blobsBrowser.SetImage(image);
            richTextBox1.Text += "Found blobs' count: " + foundBlobsCount.ToString() + "\n";

            propertyGrid.SelectedObject = null;            
        }

        // Blob was selected - display its information
        private void blobsBrowser_BlobSelected(object sender, Blob blob)
        {
            propertyGrid.SelectedObject = blob;
            propertyGrid.ExpandAllGridItems();
        }

        // Change type of blobs' highlighting
        private void highlightTypeCombo_SelectedIndexChanged(object sender, EventArgs e)
        {
            blobsBrowser.Highlighting = (BlobsBrowser.HightlightType)highlightTypeCombo.SelectedIndex;
        }

        // Toggle displaying of rectangle around selection
        private void showRectangleAroundSelectionCheck_CheckedChanged(object sender, EventArgs e)
        {
            blobsBrowser.ShowRectangleAroundSelection = showRectangleAroundSelectionCheck.Checked;
        }
    }
}

