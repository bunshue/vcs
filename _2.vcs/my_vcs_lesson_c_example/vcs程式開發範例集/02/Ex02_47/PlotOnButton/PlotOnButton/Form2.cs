using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.Runtime.InteropServices;

namespace PlotOnButton
{
    /// <summary>
    /// Summary description for Form1.
    /// </summary>
    public class Form2 : System.Windows.Forms.Form
    {
        private IContainer components;

        Bitmap bmp;
        private System.Windows.Forms.MainMenu mainMenu1;
        private System.Windows.Forms.MenuItem menuItem1;
        private Button button1;
        private System.Windows.Forms.MenuItem menuItem2;

        

        public Form2()
        {
            InitializeComponent();            
        }

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        protected override void Dispose( bool disposing )
        {
            if( disposing )
            {
                if (components != null) 
                {
                    components.Dispose();
                }
            }
            base.Dispose( disposing );
        }

        #region Windows Form Designer generated code
        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.mainMenu1 = new System.Windows.Forms.MainMenu(this.components);
            this.menuItem1 = new System.Windows.Forms.MenuItem();
            this.menuItem2 = new System.Windows.Forms.MenuItem();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // mainMenu1
            // 
            this.mainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.menuItem1});
            // 
            // menuItem1
            // 
            this.menuItem1.Index = 0;
            this.menuItem1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.menuItem2});
            this.menuItem1.Text = "Fie";
            this.menuItem1.Click += new System.EventHandler(this.menuItem1_Click);
            // 
            // menuItem2
            // 
            this.menuItem2.Checked = true;
            this.menuItem2.Index = 0;
            this.menuItem2.Text = "open";
            this.menuItem2.Click += new System.EventHandler(this.menuItem2_Click);
            // 
            // button1
            // 
            this.button1.AutoSize = true;
            this.button1.BackgroundImage = global::PlotOnButton.Properties.Resources._8;
            this.button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.button1.Location = new System.Drawing.Point(146,12);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(294,159);
            this.button1.TabIndex = 1;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Paint += new System.Windows.Forms.PaintEventHandler(this.button1_Paint);
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form2
            // 
            this.AutoScaleBaseSize = new System.Drawing.Size(6,14);
            this.ClientSize = new System.Drawing.Size(452,195);
            this.Controls.Add(this.button1);
            this.Menu = this.mainMenu1;
            this.Name = "Form2";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form2_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }
        #endregion

        private void Form2_Resize(object sender, System.EventArgs e)
        {
            this.Invalidate();
        }

        string _fileName = "";

        //File open click
        private void menuItem2_Click(object sender, System.EventArgs e)
        {
            OpenFileDialog dlg = new OpenFileDialog();

            if(dlg.ShowDialog() == DialogResult.OK)
            {
                _fileName = dlg.FileName;
            }
            bmp = new Bitmap(_fileName);
            this.AutoScrollMinSize = bmp.Size;
            button1.AutoSizeMode = AutoSizeMode.GrowOnly;
            this.Invalidate();
        }

        [DllImport("gdi32.dll")]
        static extern bool StretchBlt(IntPtr hdcDest, int nXOriginDest,
            int nYOriginDest, int nWidthDest, int nHeightDest, IntPtr hdcSrc,
            int nXOriginSrc, int nYOriginSrc, int nWidthSrc, int nHeightSrc,     
            TernaryRasterOperations dwRop );
        [DllImport("gdi32.dll", ExactSpelling=true, SetLastError=true)]
        static extern IntPtr CreateCompatibleDC(IntPtr hdc);
        [DllImport("gdi32.dll", ExactSpelling=true, SetLastError=true)]
        static extern bool DeleteDC(IntPtr hdc);
        [DllImport("gdi32.dll", ExactSpelling=true, SetLastError=true)]
        static extern IntPtr SelectObject(IntPtr hdc, IntPtr hgdiobj);
        [DllImport("gdi32.dll", ExactSpelling=true, SetLastError=true)]
        static extern bool DeleteObject(IntPtr hObject);
        [DllImport("gdi32.dll")]
        static extern bool SetStretchBltMode(IntPtr hdc, StretchMode iStretchMode);
        
        
        public enum StretchMode
        {
            STRETCH_ANDSCANS    =1,
            STRETCH_ORSCANS     =2,
            STRETCH_DELETESCANS =3,
            STRETCH_HALFTONE    =4,
        }



        public enum TernaryRasterOperations
        {
            SRCCOPY     = 0x00CC0020, /* dest = source*/
            SRCPAINT    = 0x00EE0086, /* dest = source OR dest*/
            SRCAND      = 0x008800C6, /* dest = source AND dest*/
            SRCINVERT   = 0x00660046, /* dest = source XOR dest*/
            SRCERASE    = 0x00440328, /* dest = source AND (NOT dest )*/
            NOTSRCCOPY  = 0x00330008, /* dest = (NOT source)*/
            NOTSRCERASE = 0x001100A6, /* dest = (NOT src) AND (NOT dest) */
            MERGECOPY   = 0x00C000CA, /* dest = (source AND pattern)*/
            MERGEPAINT  = 0x00BB0226, /* dest = (NOT source) OR dest*/
            PATCOPY     = 0x00F00021, /* dest = pattern*/
            PATPAINT    = 0x00FB0A09, /* dest = DPSnoo*/
            PATINVERT   = 0x005A0049, /* dest = pattern XOR dest*/
            DSTINVERT   = 0x00550009, /* dest = (NOT dest)*/
            BLACKNESS   = 0x00000042, /* dest = BLACK*/
            WHITENESS   = 0x00FF0062, /* dest = WHITE*/
        };

        private void Form2_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("adf");
        }

        private void button1_Paint(object sender, PaintEventArgs e)
        {
            if (bmp != null)
            {
                Graphics g = e.Graphics;
                
                TextureBrush myBrush = new TextureBrush(bmp);
                //g.FillRectangle(myBrush, button1.ClientRectangle);
         
                g.FillRectangle(myBrush,this.ClientRectangle);
                
                
                

            }
        }

        private void menuItem1_Click(object sender, EventArgs e)
        {

        }

    }
}

