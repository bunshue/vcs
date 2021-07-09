using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security.Cryptography;

namespace vcs_Cryptography4_MD5_SHA2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Start with the executable selected.
        private void Form1_Load(object sender, EventArgs e)
        {
            txtFile.Text = Application.ExecutablePath;
        }

        // Compute the file's hash code.
        private void btnHash_Click(object sender, EventArgs e)
        {
            txtMd5.Text = BytesToString(GetHashMD5(txtFile.Text));
            txtSha256.Text = BytesToString(GetHashSha256(txtFile.Text));
        }

        // Let the user select a file.
        private void btnBrowse_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = txtFile.Text;
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                txtFile.Text = openFileDialog1.FileName;
                txtMd5.Clear();
                txtSha256.Clear();
            }
        }

        // The cryptographic service provider.
        private MD5 Md5 = MD5.Create();

        // Compute the file's hash.
        private byte[] GetHashMD5(string filename)
        {
            using (FileStream stream = File.OpenRead(filename))
            {
                return Md5.ComputeHash(stream);
            }
        }

        // The cryptographic service provider.
        private SHA256 Sha256 = SHA256.Create();

        // Compute the file's hash.
        private byte[] GetHashSha256(string filename)
        {
            using (FileStream stream = File.OpenRead(filename))
            {
                return Sha256.ComputeHash(stream);
            }
        }

        // Return a byte array as a sequence of hex values.
        public static string BytesToString(byte[] bytes)
        {
            string result = "";
            foreach (byte b in bytes)
            {
                result += b.ToString("x2");
            }
            return result;
        }
    }
}
