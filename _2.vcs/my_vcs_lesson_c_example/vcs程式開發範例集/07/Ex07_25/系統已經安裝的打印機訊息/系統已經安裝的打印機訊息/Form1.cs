using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 系統已經安裝的打印機訊息
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            foreach (string mPrinterName in System.Drawing.Printing.PrinterSettings.InstalledPrinters)
            {
                textBox1.Text = mPrinterName;
                System.Drawing.Printing.PrinterSettings mprinter = new System.Drawing.Printing.PrinterSettings();
                mprinter.PrinterName = mPrinterName;
                if (mprinter.IsValid)
                {
                    foreach (System.Drawing.Printing.PrinterResolution resolution in mprinter.PrinterResolutions)
                    {
                        comboBox1.Items.Add(resolution.ToString());
                    }
                    string prinsize = "";
                    foreach (System.Drawing.Printing.PaperSize size in mprinter.PaperSizes)
                    {
                        if (Enum.IsDefined(size.Kind.GetType(), size.Kind))
                            prinsize += size.ToString() + "\n";
                    }
                    richTextBox1.AppendText(prinsize + "\n");
                }
            }
        }

    }
}
