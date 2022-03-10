using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;

namespace vcs_CommandLine2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Initialize.
        private void Form1_Load(object sender, EventArgs e)
        {
            txtProgram.Text = Path.GetFullPath(Path.Combine(
                    Application.StartupPath, "..\\..\\hello.bat"));
            txtProgram.Select(0, 0);
        }

        // Run the DOS program.
        private void btnRun_Click(object sender, EventArgs e)
        {
            // Set start information.
            ProcessStartInfo start_info = new ProcessStartInfo(txtProgram.Text);
            start_info.UseShellExecute = false;
            start_info.CreateNoWindow = true;
            start_info.RedirectStandardOutput = true;
            start_info.RedirectStandardError = true;

            // Make the process and set its start information.
            using (Process proc = new Process())
            {
                proc.StartInfo = start_info;

                // Start the process.
                proc.Start();

                // Attach to stdout and stderr.
                using (StreamReader std_out = proc.StandardOutput)
                {
                    using (StreamReader std_err = proc.StandardError)
                    {
                        // Display the results.
                        txtStdout.Text = std_out.ReadToEnd();
                        txtStderr.Text = std_err.ReadToEnd();

                        // Clean up.
                        std_err.Close();
                        std_out.Close();
                        proc.Close();
                    }
                }
            }
        }
    }
}
