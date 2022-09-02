using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace howto_file_replace
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Make sure all of the files exist.
            if (!File.Exists("MainFile.txt")) File.WriteAllText("MainFile.txt", "");
            if (!File.Exists("Backup1.txt")) File.WriteAllText("Backup1.txt", "");
            if (!File.Exists("Backup2.txt")) File.WriteAllText("Backup2.txt", "");

            // Display the files.
            ShowFileContents();
        }

        // Display the files' contents.
        private void ShowFileContents()
        {
            txtFile.Text = File.ReadAllText("MainFile.txt");
            txtBackup1.Text = File.ReadAllText("Backup1.txt");
            txtBackup2.Text = File.ReadAllText("Backup2.txt");
        }

        // Revise the backups and then write the new value into the file.
        private void btnSave_Click(object sender, EventArgs e)
        {
            // Move the backup files.
            File.Replace("MainFile.txt", "Backup1.txt", "Backup2.txt");

            // Write into the main file.
            File.WriteAllText("MainFile.txt", txtComment.Text);

            // Display the files' contents.
            ShowFileContents();

            // Clear the input TextBox.
            txtComment.Clear();
        }
    }
}
