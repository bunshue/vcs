namespace howto_newtons_method_fractal3
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
            this.MenuItem1 = new System.Windows.Forms.MenuItem();
            this.mnuSetToolsPower = new System.Windows.Forms.MenuItem();
            this.mnuToolsRedraw = new System.Windows.Forms.MenuItem();
            this.mnuToolsFullScale = new System.Windows.Forms.MenuItem();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).BeginInit();
            this.SuspendLayout();
            // 
            // MainMenu1
            // 
            this.MainMenu1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.MenuItem1});
            // 
            // MenuItem1
            // 
            this.MenuItem1.Index = 0;
            this.MenuItem1.MenuItems.AddRange(new System.Windows.Forms.MenuItem[] {
            this.mnuSetToolsPower,
            this.mnuToolsRedraw,
            this.mnuToolsFullScale});
            this.MenuItem1.Text = "&Tools";
            // 
            // mnuSetToolsPower
            // 
            this.mnuSetToolsPower.Index = 0;
            this.mnuSetToolsPower.Text = "&Set Power";
            this.mnuSetToolsPower.Click += new System.EventHandler(this.mnuToolsSetPower_Click);
            // 
            // mnuToolsRedraw
            // 
            this.mnuToolsRedraw.Index = 1;
            this.mnuToolsRedraw.Shortcut = System.Windows.Forms.Shortcut.F5;
            this.mnuToolsRedraw.Text = "&Redraw";
            this.mnuToolsRedraw.Click += new System.EventHandler(this.mnuToolsRedraw_Click);
            // 
            // mnuToolsFullScale
            // 
            this.mnuToolsFullScale.Index = 2;
            this.mnuToolsFullScale.Text = "&Full Scale";
            this.mnuToolsFullScale.Click += new System.EventHandler(this.mnuToolsFullScale_Click);
            // 
            // picCanvas
            // 
            this.picCanvas.BackColor = System.Drawing.Color.Black;
            this.picCanvas.Dock = System.Windows.Forms.DockStyle.Fill;
            this.picCanvas.Location = new System.Drawing.Point(0, 0);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(684, 541);
            this.picCanvas.TabIndex = 5;
            this.picCanvas.TabStop = false;
            this.picCanvas.MouseDown += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseDown);
            this.picCanvas.MouseMove += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseMove);
            this.picCanvas.MouseUp += new System.Windows.Forms.MouseEventHandler(this.picCanvas_MouseUp);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(684, 541);
            this.Controls.Add(this.picCanvas);
            this.Menu = this.MainMenu1;
            this.Name = "Form1";
            this.Text = "howto_newtons_method_fractal3";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        internal System.Windows.Forms.MainMenu MainMenu1;
        internal System.Windows.Forms.MenuItem MenuItem1;
        private System.Windows.Forms.MenuItem mnuSetToolsPower;
        private System.Windows.Forms.MenuItem mnuToolsRedraw;
        internal System.Windows.Forms.MenuItem mnuToolsFullScale;
        internal System.Windows.Forms.PictureBox picCanvas;
    }
}

