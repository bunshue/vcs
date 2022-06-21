namespace ImageToPdf
{
    partial class MainForm
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
            this.btnSelectSrc = new System.Windows.Forms.Button();
            this.txbxSrcFile = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.txbxDestFile = new System.Windows.Forms.TextBox();
            this.btnSelectDest = new System.Windows.Forms.Button();
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripProgressBar1 = new System.Windows.Forms.ToolStripProgressBar();
            this.btnConvert = new System.Windows.Forms.Button();
            this.ofdSrcFile = new System.Windows.Forms.OpenFileDialog();
            this.sfdDestFile = new System.Windows.Forms.SaveFileDialog();
            this.errProv = new System.Windows.Forms.ErrorProvider(this.components);
            this.bw = new System.ComponentModel.BackgroundWorker();
            this.button1 = new System.Windows.Forms.Button();
            this.rbSrc = new System.Windows.Forms.RadioButton();
            this.rbDest = new System.Windows.Forms.RadioButton();
            this.statusStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.errProv)).BeginInit();
            this.SuspendLayout();
            // 
            // btnSelectSrc
            // 
            this.btnSelectSrc.Location = new System.Drawing.Point(377, 27);
            this.btnSelectSrc.Name = "btnSelectSrc";
            this.btnSelectSrc.Size = new System.Drawing.Size(51, 23);
            this.btnSelectSrc.TabIndex = 0;
            this.btnSelectSrc.Text = "...";
            this.btnSelectSrc.UseVisualStyleBackColor = true;
            this.btnSelectSrc.Click += new System.EventHandler(this.btnSelectSrc_Click);
            // 
            // txbxSrcFile
            // 
            this.txbxSrcFile.Location = new System.Drawing.Point(12, 27);
            this.txbxSrcFile.Name = "txbxSrcFile";
            this.txbxSrcFile.Size = new System.Drawing.Size(359, 20);
            this.txbxSrcFile.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 11);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(63, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Source File:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 62);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(82, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Destination File:";
            // 
            // txbxDestFile
            // 
            this.txbxDestFile.Location = new System.Drawing.Point(12, 78);
            this.txbxDestFile.Name = "txbxDestFile";
            this.txbxDestFile.Size = new System.Drawing.Size(359, 20);
            this.txbxDestFile.TabIndex = 4;
            // 
            // btnSelectDest
            // 
            this.btnSelectDest.Location = new System.Drawing.Point(377, 78);
            this.btnSelectDest.Name = "btnSelectDest";
            this.btnSelectDest.Size = new System.Drawing.Size(51, 23);
            this.btnSelectDest.TabIndex = 3;
            this.btnSelectDest.Text = "...";
            this.btnSelectDest.UseVisualStyleBackColor = true;
            this.btnSelectDest.Click += new System.EventHandler(this.btnSelectDest_Click);
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripProgressBar1});
            this.statusStrip1.Location = new System.Drawing.Point(0, 165);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(440, 22);
            this.statusStrip1.TabIndex = 6;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // toolStripProgressBar1
            // 
            this.toolStripProgressBar1.Name = "toolStripProgressBar1";
            this.toolStripProgressBar1.Size = new System.Drawing.Size(100, 16);
            // 
            // btnConvert
            // 
            this.btnConvert.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnConvert.Location = new System.Drawing.Point(285, 117);
            this.btnConvert.Name = "btnConvert";
            this.btnConvert.Size = new System.Drawing.Size(143, 23);
            this.btnConvert.TabIndex = 7;
            this.btnConvert.Text = "Convert Now";
            this.btnConvert.UseVisualStyleBackColor = true;
            this.btnConvert.Click += new System.EventHandler(this.btnConvert_Click);
            // 
            // ofdSrcFile
            // 
            this.ofdSrcFile.FileName = "openFileDialog1";
            this.ofdSrcFile.Filter = "Image Files(*.BMP;*.JPG;*.GIF;*.PNG;*.TIF;*.TIFF)|*.BMP;*.JPG;*.GIF;*.PNG;*.TIF;*" +
                ".TIFF|All files (*.*)|*.*";
            this.ofdSrcFile.Title = "Choose source image file";
            // 
            // sfdDestFile
            // 
            this.sfdDestFile.Title = "Choose save location of PDF file";
            // 
            // errProv
            // 
            this.errProv.ContainerControl = this;
            // 
            // bw
            // 
            this.bw.DoWork += new System.ComponentModel.DoWorkEventHandler(this.bw_DoWork);
            this.bw.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.bw_RunWorkerCompleted);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button1.Location = new System.Drawing.Point(12, 117);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(143, 23);
            this.button1.TabIndex = 8;
            this.button1.Text = "View File";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // rbSrc
            // 
            this.rbSrc.AutoSize = true;
            this.rbSrc.Checked = true;
            this.rbSrc.Location = new System.Drawing.Point(12, 146);
            this.rbSrc.Name = "rbSrc";
            this.rbSrc.Size = new System.Drawing.Size(59, 17);
            this.rbSrc.TabIndex = 9;
            this.rbSrc.TabStop = true;
            this.rbSrc.Text = "Source";
            this.rbSrc.UseVisualStyleBackColor = true;
            // 
            // rbDest
            // 
            this.rbDest.AutoSize = true;
            this.rbDest.Location = new System.Drawing.Point(77, 146);
            this.rbDest.Name = "rbDest";
            this.rbDest.Size = new System.Drawing.Size(78, 17);
            this.rbDest.TabIndex = 10;
            this.rbDest.Text = "Destination";
            this.rbDest.UseVisualStyleBackColor = true;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(440, 187);
            this.Controls.Add(this.rbDest);
            this.Controls.Add(this.rbSrc);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.btnConvert);
            this.Controls.Add(this.statusStrip1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txbxDestFile);
            this.Controls.Add(this.btnSelectDest);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txbxSrcFile);
            this.Controls.Add(this.btnSelectSrc);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "MainForm";
            this.Text = "Image => PDF Converter";
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.errProv)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnSelectSrc;
        private System.Windows.Forms.TextBox txbxSrcFile;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox txbxDestFile;
        private System.Windows.Forms.Button btnSelectDest;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripProgressBar toolStripProgressBar1;
        private System.Windows.Forms.Button btnConvert;
        private System.Windows.Forms.OpenFileDialog ofdSrcFile;
        private System.Windows.Forms.SaveFileDialog sfdDestFile;
        private System.Windows.Forms.ErrorProvider errProv;
        private System.ComponentModel.BackgroundWorker bw;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.RadioButton rbDest;
        private System.Windows.Forms.RadioButton rbSrc;
    }
}

