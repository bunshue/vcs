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
        public MainForm( )
        {
            InitializeComponent( );

            highlightTypeCombo.SelectedIndex = 0;
            showRectangleAroundSelectionCheck.Checked = blobsBrowser.ShowRectangleAroundSelection;
        }

        // On loading of the form
        private void MainForm_Load( object sender, EventArgs e )
        {
            LoadDemo( );
        }

        // Process image
        private void ProcessImage( Bitmap image )
        {
            int foundBlobsCount = blobsBrowser.SetImage( image );

            blobsCountLabel.Text = string.Format( "Found blobs' count: {0}", foundBlobsCount );
            propertyGrid.SelectedObject = null;
        }

        // Blob was selected - display its information
        private void blobsBrowser_BlobSelected( object sender, Blob blob )
        {
            propertyGrid.SelectedObject = blob;
            propertyGrid.ExpandAllGridItems( );
        }

        // Change type of blobs' highlighting
        private void highlightTypeCombo_SelectedIndexChanged( object sender, EventArgs e )
        {
            blobsBrowser.Highlighting = (BlobsBrowser.HightlightType) highlightTypeCombo.SelectedIndex;
        }

        // Toggle displaying of rectangle around selection
        private void showRectangleAroundSelectionCheck_CheckedChanged( object sender, EventArgs e )
        {
            blobsBrowser.ShowRectangleAroundSelection = showRectangleAroundSelectionCheck.Checked;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //open
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    ProcessImage((Bitmap)Bitmap.FromFile(openFileDialog.FileName));
                }
                catch
                {
                    MessageBox.Show("Failed loading selected image file.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //load demo image
            LoadDemo();

        }

        private void LoadDemo()
        {
            // load arrow bitmap
            Assembly assembly = this.GetType().Assembly;
            Bitmap image = new Bitmap(assembly.GetManifestResourceStream("BlobsExplorer.demo.png"));
            ProcessImage(image);
        }


    }
}
