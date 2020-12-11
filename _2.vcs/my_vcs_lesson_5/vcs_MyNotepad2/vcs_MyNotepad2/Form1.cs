using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_MyNotepad2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const string NOTES_FILE = "Notes.dat";
        private string Password;
        private bool SaveChanges = false;

        // Load the encrypted notes.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Get the password.
            if (InputBox("Password", "", out Password) == DialogResult.Cancel)
            {
                Close();
                return;
            }

            // If the notes file exists, decrypt it.
            if (File.Exists(NOTES_FILE))
            {
                try
                {
                    richTextBox1.Rtf = File.ReadAllBytes(NOTES_FILE).Decrypt(Password);
                }
                catch
                {
                    MessageBox.Show("Invalid password");
                    Close();
                    return;
                }
            }

            // We're all logged in. If we close after this, save changes.
            SaveChanges = true;
        }

        // Save the encrypted notes.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (SaveChanges)
                File.WriteAllBytes(NOTES_FILE,
                    richTextBox1.Rtf.Encrypt(Password));
        }

        // Prompt the user for a simple text value.
        private DialogResult InputBox(string prompt, string default_value, out string result)
        {
            frmInputBox dlg = new frmInputBox();
            dlg.Text = prompt;
            dlg.lblPrompt.Text = prompt;
            dlg.txtValue.Text = default_value;

            DialogResult dialog_result = dlg.ShowDialog();

            result = dlg.txtValue.Text;
            return dialog_result;
        }
    }
}
