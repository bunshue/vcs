
/* GPS Viewer & KML Logging Application                                      
 * Copyright (C) 2011 Craig Peacock                                           
 * Version 1.0 16th June 2011
 * 
 * This program is free software; you can redistribute it and/or modify it 
 * under the terms of the GNU General Public License as published by the Free 
 * Software Foundation; either version 2 of the License, or (at your option) 
 * any later version.

 * This program is distributed in the hope that it will be useful, but 
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
 * or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License 
 * for more details.

 * You should have received a copy of the GNU General Public License along 
 * with this program; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA. */

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading;
using System.Diagnostics;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void btnFileOpenDialog_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Filter = "kml files (*.kml)|*.kml";
            saveFileDialog1.ShowDialog();
            tbFilename.Text = saveFileDialog1.FileName;
        }

        private void btnCreate_Click(object sender, EventArgs e)
        {
            TextWriter fs;

            try
            {
                fs = new StreamWriter(tbFilename.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "KML Filename");
                return;
            }

            fs.WriteLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?>");
            fs.WriteLine("<kml xmlns=\"http://www.opengis.net/kml/2.2\">");
            fs.WriteLine("  <Placemark>");
            fs.WriteLine("    <name>" + tbName.Text + "</name>");
            fs.WriteLine("    <description>" + tbDescription.Text + "\n</description>");
            fs.WriteLine("    <Point>");
            fs.WriteLine("     <coordinates>" + tbLongitude.Text + "," + tbLatitude.Text + ",0</coordinates>");
            fs.WriteLine("    </Point>");
            fs.WriteLine("  </Placemark>");
            fs.WriteLine("</kml>");
            fs.Close();
            this.Close();

            if (checkBox_Spawn.Checked)
            {
                Process process = Process.Start(tbFilename.Text);
            }
        }
    }
}
