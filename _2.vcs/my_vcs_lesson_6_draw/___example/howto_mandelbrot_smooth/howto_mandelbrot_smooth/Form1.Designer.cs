namespace howto_mandelbrot
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.MainMenu1 = new System.Windows.Forms.MainMenu(this.components);
            this.mnuScaleMnu = new System.Windows.Forms.MenuItem();
            this.mnuScale_2 = new System.Windows.Forms.MenuItem();
            this.mnuScale_4 = new System.Windows.Forms.MenuItem();
            this.mnuScale_8 = new System.Windows.Forms.MenuItem();
            this.mnuScaleFull = new System.Windows.Forms.MenuItem();
            this.mnuScaleRefreshSep = new System.Windows.Forms.MenuItem();
            this.mnuScaleRefresh = new System.Windows.Forms.MenuItem();
            this.mnuOpt = new System.Windows.Forms.MenuItem();
            this.mnuOptOptions = new System.Windows.Forms.MenuItem();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // MainMenu1
            // 
            this.MainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuScaleMnu,
            this.mnuOpt});
            // 
            // mnuScaleMnu
            // 
            this.mnuScaleMnu.Index = 0;
            this.mnuScaleMnu.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuScale_2,
            this.mnuScale_4,
            this.mnuScale_8,
            this.mnuScaleFull,
            this.mnuScaleRefreshSep,
            this.mnuScaleRefresh});
            this.mnuScaleMnu.Text = "&Scale";
            // 
            // mnuScale_2
            // 
            this.mnuScale_2.Index = 0;
            this.mnuScale_2.Tag = "2";
            this.mnuScale_2.Text = "x&2";
            this.mnuScale_2.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale_4
            // 
            this.mnuScale_4.Index = 1;
            this.mnuScale_4.Tag = "4";
            this.mnuScale_4.Text = "x&4";
            this.mnuScale_4.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScale_8
            // 
            this.mnuScale_8.Index = 2;
            this.mnuScale_8.Tag = "8";
            this.mnuScale_8.Text = "x&8";
            this.mnuScale_8.Click += new System.EventHandler(this.mnuScale_Click);
            // 
            // mnuScaleFull
            // 
            this.mnuScaleFull.Index = 3;
            this.mnuScaleFull.Tag = "";
            this.mnuScaleFull.Text = "&Full Scale";
            this.mnuScaleFull.Click += new System.EventHandler(this.mnuScaleFull_Click);
            // 
            // mnuScaleRefreshSep
            // 
            this.mnuScaleRefreshSep.Index = 4;
            this.mnuScaleRefreshSep.Text = "-";
            // 
            // mnuScaleRefresh
            // 
            this.mnuScaleRefresh.Index = 5;
            this.mnuScaleRefresh.Shortcut = System.Windows.Forms.Shortcut.F5;
            this.mnuScaleRefresh.Text = "&Refresh";
            this.mnuScaleRefresh.Click += new System.EventHandler(this.mnuScaleRefresh_Click);
            // 
            // mnuOpt
            // 
            this.mnuOpt.Index = 1;
            this.mnuOpt.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuOptOptions});
            this.mnuOpt.Text = "&Options";
            // 
            // mnuOptOptions
            // 
            this.mnuOptOptions.Index = 0;
            this.mnuOptOptions.Text = "&Set Options";
            this.mnuOptOptions.Click += new System.EventHandler(this.mnuOptOptions_Click);
            // 
            // picCanvas
            // 
            this.picCanvas.BackColor = System.Drawing.Color.Black;
            this.picCanvas.Location = new System.Drawing.Point(0, 0);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(684, 541);
            this.picCanvas.TabIndex = 1;
            this.picCanvas.TabStop = false;
            this.picCanvas.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseDown);
            this.picCanvas.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseMove);
            this.picCanvas.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseUp);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(701, 0);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(411, 541);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1124, 559);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.picCanvas);
            this.Menu = this.MainMenu1;
            this.Name = "Form1";
            this.Text = "howto_mandelbrot";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        public System.Windows.Forms.MainMenu MainMenu1;
        public System.Windows.Forms.MenuItem mnuScaleMnu;
        public System.Windows.Forms.MenuItem mnuScale_2;
        public System.Windows.Forms.MenuItem mnuScale_4;
        public System.Windows.Forms.MenuItem mnuScale_8;
        public System.Windows.Forms.MenuItem mnuScaleFull;
        public System.Windows.Forms.MenuItem mnuScaleRefreshSep;
        public System.Windows.Forms.MenuItem mnuScaleRefresh;
        public System.Windows.Forms.MenuItem mnuOpt;
        public System.Windows.Forms.MenuItem mnuOptOptions;
        internal System.Windows.Forms.PictureBox picCanvas;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

