namespace howto_buddhabrot
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
            this.mnuFileSave = new System.Windows.Forms.MenuItem();
            this.sfdBrot = new System.Windows.Forms.SaveFileDialog();
            this.txtDrawEvery = new System.Windows.Forms.TextBox();
            this.Label7 = new System.Windows.Forms.Label();
            this.txtStopAfter = new System.Windows.Forms.TextBox();
            this.Label6 = new System.Windows.Forms.Label();
            this.btnDraw = new System.Windows.Forms.Button();
            this.picCanvas = new System.Windows.Forms.PictureBox();
            this.txtBlueCutoff = new System.Windows.Forms.TextBox();
            this.Label5 = new System.Windows.Forms.Label();
            this.txtGreenCutoff = new System.Windows.Forms.TextBox();
            this.Label3 = new System.Windows.Forms.Label();
            this.txtRedCutoff = new System.Windows.Forms.TextBox();
            this.Label4 = new System.Windows.Forms.Label();
            this.txtHeight = new System.Windows.Forms.TextBox();
            this.Label2 = new System.Windows.Forms.Label();
            this.txtWidth = new System.Windows.Forms.TextBox();
            this.Label1 = new System.Windows.Forms.Label();
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
            this.mnuFileSave});
            this.MenuItem1.Text = "&File";
            // 
            // mnuFileSave
            // 
            this.mnuFileSave.Enabled = false;
            this.mnuFileSave.Index = 0;
            this.mnuFileSave.Shortcut = System.Windows.Forms.Shortcut.CtrlS;
            this.mnuFileSave.Text = "&Save...";
            this.mnuFileSave.Click += new System.EventHandler(this.mnuFileSave_Click);
            // 
            // sfdBrot
            // 
            this.sfdBrot.Filter = "Bitmaps|*.bmp|JPEGs|*.jpeg;*.jpg|GIFs|*.gif|All Files|*.*";
            // 
            // txtDrawEvery
            // 
            this.txtDrawEvery.Location = new System.Drawing.Point(92, 159);
            this.txtDrawEvery.Name = "txtDrawEvery";
            this.txtDrawEvery.Size = new System.Drawing.Size(72, 22);
            this.txtDrawEvery.TabIndex = 45;
            this.txtDrawEvery.Text = "100000";
            this.txtDrawEvery.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label7
            // 
            this.Label7.AutoSize = true;
            this.Label7.Location = new System.Drawing.Point(12, 159);
            this.Label7.Name = "Label7";
            this.Label7.Size = new System.Drawing.Size(64, 12);
            this.Label7.TabIndex = 44;
            this.Label7.Text = "Draw Every:";
            // 
            // txtStopAfter
            // 
            this.txtStopAfter.Location = new System.Drawing.Point(92, 137);
            this.txtStopAfter.Name = "txtStopAfter";
            this.txtStopAfter.Size = new System.Drawing.Size(72, 22);
            this.txtStopAfter.TabIndex = 43;
            this.txtStopAfter.Text = "10000000";
            this.txtStopAfter.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label6
            // 
            this.Label6.AutoSize = true;
            this.Label6.Location = new System.Drawing.Point(12, 137);
            this.Label6.Name = "Label6";
            this.Label6.Size = new System.Drawing.Size(56, 12);
            this.Label6.TabIndex = 42;
            this.Label6.Text = "Stop After:";
            // 
            // btnDraw
            // 
            this.btnDraw.Location = new System.Drawing.Point(28, 196);
            this.btnDraw.Name = "btnDraw";
            this.btnDraw.Size = new System.Drawing.Size(75, 21);
            this.btnDraw.TabIndex = 41;
            this.btnDraw.Text = "Draw";
            this.btnDraw.Click += new System.EventHandler(this.btnDraw_Click);
            // 
            // picCanvas
            // 
            this.picCanvas.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.picCanvas.Location = new System.Drawing.Point(172, 11);
            this.picCanvas.Name = "picCanvas";
            this.picCanvas.Size = new System.Drawing.Size(24, 24);
            this.picCanvas.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize;
            this.picCanvas.TabIndex = 40;
            this.picCanvas.TabStop = false;
            // 
            // txtBlueCutoff
            // 
            this.txtBlueCutoff.Location = new System.Drawing.Point(92, 107);
            this.txtBlueCutoff.Name = "txtBlueCutoff";
            this.txtBlueCutoff.Size = new System.Drawing.Size(72, 22);
            this.txtBlueCutoff.TabIndex = 39;
            this.txtBlueCutoff.Text = "50";
            this.txtBlueCutoff.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label5
            // 
            this.Label5.AutoSize = true;
            this.Label5.Location = new System.Drawing.Point(12, 107);
            this.Label5.Name = "Label5";
            this.Label5.Size = new System.Drawing.Size(64, 12);
            this.Label5.TabIndex = 38;
            this.Label5.Text = "Blue Cutoff:";
            // 
            // txtGreenCutoff
            // 
            this.txtGreenCutoff.Location = new System.Drawing.Point(92, 85);
            this.txtGreenCutoff.Name = "txtGreenCutoff";
            this.txtGreenCutoff.Size = new System.Drawing.Size(72, 22);
            this.txtGreenCutoff.TabIndex = 37;
            this.txtGreenCutoff.Text = "250";
            this.txtGreenCutoff.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label3
            // 
            this.Label3.AutoSize = true;
            this.Label3.Location = new System.Drawing.Point(12, 85);
            this.Label3.Name = "Label3";
            this.Label3.Size = new System.Drawing.Size(70, 12);
            this.Label3.TabIndex = 36;
            this.Label3.Text = "Green Cutoff:";
            // 
            // txtRedCutoff
            // 
            this.txtRedCutoff.Location = new System.Drawing.Point(92, 63);
            this.txtRedCutoff.Name = "txtRedCutoff";
            this.txtRedCutoff.Size = new System.Drawing.Size(72, 22);
            this.txtRedCutoff.TabIndex = 35;
            this.txtRedCutoff.Text = "1250";
            this.txtRedCutoff.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label4
            // 
            this.Label4.AutoSize = true;
            this.Label4.Location = new System.Drawing.Point(12, 63);
            this.Label4.Name = "Label4";
            this.Label4.Size = new System.Drawing.Size(61, 12);
            this.Label4.TabIndex = 34;
            this.Label4.Text = "Red Cutoff:";
            // 
            // txtHeight
            // 
            this.txtHeight.Location = new System.Drawing.Point(92, 33);
            this.txtHeight.Name = "txtHeight";
            this.txtHeight.Size = new System.Drawing.Size(72, 22);
            this.txtHeight.TabIndex = 33;
            this.txtHeight.Text = "200";
            this.txtHeight.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label2
            // 
            this.Label2.AutoSize = true;
            this.Label2.Location = new System.Drawing.Point(12, 33);
            this.Label2.Name = "Label2";
            this.Label2.Size = new System.Drawing.Size(39, 12);
            this.Label2.TabIndex = 32;
            this.Label2.Text = "Height:";
            // 
            // txtWidth
            // 
            this.txtWidth.Location = new System.Drawing.Point(92, 11);
            this.txtWidth.Name = "txtWidth";
            this.txtWidth.Size = new System.Drawing.Size(72, 22);
            this.txtWidth.TabIndex = 31;
            this.txtWidth.Text = "200";
            this.txtWidth.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // Label1
            // 
            this.Label1.AutoSize = true;
            this.Label1.Location = new System.Drawing.Point(12, 11);
            this.Label1.Name = "Label1";
            this.Label1.Size = new System.Drawing.Size(37, 12);
            this.Label1.TabIndex = 30;
            this.Label1.Text = "Width:";
            // 
            // Form1
            // 
            this.AcceptButton = this.btnDraw;
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(694, 458);
            this.Controls.Add(this.txtDrawEvery);
            this.Controls.Add(this.Label7);
            this.Controls.Add(this.txtStopAfter);
            this.Controls.Add(this.Label6);
            this.Controls.Add(this.btnDraw);
            this.Controls.Add(this.picCanvas);
            this.Controls.Add(this.txtBlueCutoff);
            this.Controls.Add(this.Label5);
            this.Controls.Add(this.txtGreenCutoff);
            this.Controls.Add(this.Label3);
            this.Controls.Add(this.txtRedCutoff);
            this.Controls.Add(this.Label4);
            this.Controls.Add(this.txtHeight);
            this.Controls.Add(this.Label2);
            this.Controls.Add(this.txtWidth);
            this.Controls.Add(this.Label1);
            this.Menu = this.MainMenu1;
            this.Name = "Form1";
            this.Text = "howto_buddhabrot";
            ((System.ComponentModel.ISupportInitialize)(this.picCanvas)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        internal System.Windows.Forms.MainMenu MainMenu1;
        internal System.Windows.Forms.MenuItem MenuItem1;
        internal System.Windows.Forms.MenuItem mnuFileSave;
        internal System.Windows.Forms.SaveFileDialog sfdBrot;
        internal System.Windows.Forms.TextBox txtDrawEvery;
        internal System.Windows.Forms.Label Label7;
        internal System.Windows.Forms.TextBox txtStopAfter;
        internal System.Windows.Forms.Label Label6;
        internal System.Windows.Forms.Button btnDraw;
        internal System.Windows.Forms.PictureBox picCanvas;
        internal System.Windows.Forms.TextBox txtBlueCutoff;
        internal System.Windows.Forms.Label Label5;
        internal System.Windows.Forms.TextBox txtGreenCutoff;
        internal System.Windows.Forms.Label Label3;
        internal System.Windows.Forms.TextBox txtRedCutoff;
        internal System.Windows.Forms.Label Label4;
        internal System.Windows.Forms.TextBox txtHeight;
        internal System.Windows.Forms.Label Label2;
        internal System.Windows.Forms.TextBox txtWidth;
        internal System.Windows.Forms.Label Label1;
    }
}

