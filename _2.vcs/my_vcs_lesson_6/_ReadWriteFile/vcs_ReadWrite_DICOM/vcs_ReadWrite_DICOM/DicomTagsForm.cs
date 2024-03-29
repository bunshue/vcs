﻿using System;
using System.Collections.Generic;
using System.Windows.Forms;

using System.IO;

// Program to view simple DICOM images.
// Written by Amarnath S, Mahesh Reddy S, Bangalore, India, April 2009.
// Updated by Amarnath, July 2010 to include "Save As Text".

namespace vcs_ReadWrite_DICOM
{
    public partial class DicomTagsForm : Form
    {
        List<string> str;

        public DicomTagsForm()
        {
            InitializeComponent();
        }

        // Extract the substrings within the DICOM tags main string 
        //  to populate the list box
        public void SetString(ref List<string> strg)
        {
            str = strg;
            string s1, s4, s5, s11, s12;

            // Add items to the List View Control
            for (int i = 0; i < str.Count; ++i)
            {
                s1 = str[i];
                ExtractStrings(s1, out s4, out s5, out s11, out s12);

                ListViewItem lvi = new ListViewItem(s11);
                lvi.SubItems.Add(s12);
                lvi.SubItems.Add(s4);
                lvi.SubItems.Add(s5);
                listView.Items.Add(lvi);
            }
        }

        // Saving DICOM tags as Text file
        private void bnSaveAs_Click(object sender, System.EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            string s1, s4, s5, s11, s12;

            StreamWriter file = new StreamWriter(filename);
            for (int i = 0; i < str.Count; ++i)
            {
                s1 = str[i];
                ExtractStrings(s1, out s4, out s5, out s11, out s12);
                file.WriteLine("(" + s11 + "," + s12 + ")\t" + s4 + "\t\t" + s5);
            }
            file.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        // This method was extracted using the Refactoring facility in Visual Studio
        void ExtractStrings(string s1, out string s4, out string s5, out string s11, out string s12)
        {
            int ind;
            string s2, s3;
            ind = s1.IndexOf("//");
            s2 = s1.Substring(0, ind);
            s11 = s1.Substring(0, 4);
            s12 = s1.Substring(4, 4);
            s3 = s1.Substring(ind + 2);
            ind = s3.IndexOf(":");
            s4 = s3.Substring(0, ind);
            s5 = s3.Substring(ind + 1);
        }
    }
}
