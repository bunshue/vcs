namespace ExifLibrary
{
    partial class FormMain
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
            ExifLibrary.MemoryBinStream memoryBinStream2 = new ExifLibrary.MemoryBinStream();
            this.fdOpen = new System.Windows.Forms.OpenFileDialog();
            this.toolStripContainer1 = new System.Windows.Forms.ToolStripContainer();
            this.ssExif = new System.Windows.Forms.StatusStrip();
            this.lblStatus = new System.Windows.Forms.ToolStripStatusLabel();
            this.lblByteOrder = new System.Windows.Forms.ToolStripStatusLabel();
            this.lblThumbnail = new System.Windows.Forms.ToolStripStatusLabel();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.splitContainer3 = new System.Windows.Forms.SplitContainer();
            this.lvExif = new System.Windows.Forms.ListView();
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader3 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.tbField = new System.Windows.Forms.TextBox();
            this.splitContainer2 = new System.Windows.Forms.SplitContainer();
            this.binaryMapViewer1 = new ExifLibrary.BinaryMapViewer();
            this.pbThumb = new System.Windows.Forms.PictureBox();
            this.tsExif = new System.Windows.Forms.ToolStrip();
            this.btnOpen = new System.Windows.Forms.ToolStripButton();
            this.fdSave = new System.Windows.Forms.SaveFileDialog();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.toolStripContainer1.BottomToolStripPanel.SuspendLayout();
            this.toolStripContainer1.ContentPanel.SuspendLayout();
            this.toolStripContainer1.TopToolStripPanel.SuspendLayout();
            this.toolStripContainer1.SuspendLayout();
            this.ssExif.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer3)).BeginInit();
            this.splitContainer3.Panel1.SuspendLayout();
            this.splitContainer3.Panel2.SuspendLayout();
            this.splitContainer3.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).BeginInit();
            this.splitContainer2.Panel1.SuspendLayout();
            this.splitContainer2.Panel2.SuspendLayout();
            this.splitContainer2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pbThumb)).BeginInit();
            this.tsExif.SuspendLayout();
            this.SuspendLayout();
            // 
            // fdOpen
            // 
            this.fdOpen.Filter = "JPEG Images *.jpg|*.jpg";
            // 
            // toolStripContainer1
            // 
            // 
            // toolStripContainer1.BottomToolStripPanel
            // 
            this.toolStripContainer1.BottomToolStripPanel.Controls.Add(this.ssExif);
            // 
            // toolStripContainer1.ContentPanel
            // 
            this.toolStripContainer1.ContentPanel.Controls.Add(this.splitContainer1);
            this.toolStripContainer1.ContentPanel.Size = new System.Drawing.Size(961, 485);
            this.toolStripContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.toolStripContainer1.Location = new System.Drawing.Point(0, 0);
            this.toolStripContainer1.Name = "toolStripContainer1";
            this.toolStripContainer1.Size = new System.Drawing.Size(961, 538);
            this.toolStripContainer1.TabIndex = 0;
            this.toolStripContainer1.Text = "toolStripContainer1";
            // 
            // toolStripContainer1.TopToolStripPanel
            // 
            this.toolStripContainer1.TopToolStripPanel.Controls.Add(this.tsExif);
            // 
            // ssExif
            // 
            this.ssExif.Dock = System.Windows.Forms.DockStyle.None;
            this.ssExif.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.lblStatus,
            this.lblByteOrder,
            this.lblThumbnail});
            this.ssExif.Location = new System.Drawing.Point(0, 0);
            this.ssExif.Name = "ssExif";
            this.ssExif.Size = new System.Drawing.Size(961, 22);
            this.ssExif.TabIndex = 0;
            // 
            // lblStatus
            // 
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(43, 17);
            this.lblStatus.Text = "Ready";
            // 
            // lblByteOrder
            // 
            this.lblByteOrder.Name = "lblByteOrder";
            this.lblByteOrder.Size = new System.Drawing.Size(80, 17);
            this.lblByteOrder.Text = "#ByteOrder#";
            // 
            // lblThumbnail
            // 
            this.lblThumbnail.Name = "lblThumbnail";
            this.lblThumbnail.Size = new System.Drawing.Size(83, 17);
            this.lblThumbnail.Text = "#Thumbnail#";
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.splitContainer3);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.splitContainer2);
            this.splitContainer1.Size = new System.Drawing.Size(961, 485);
            this.splitContainer1.SplitterDistance = 580;
            this.splitContainer1.TabIndex = 5;
            // 
            // splitContainer3
            // 
            this.splitContainer3.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer3.Location = new System.Drawing.Point(0, 0);
            this.splitContainer3.Name = "splitContainer3";
            this.splitContainer3.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer3.Panel1
            // 
            this.splitContainer3.Panel1.Controls.Add(this.lvExif);
            // 
            // splitContainer3.Panel2
            // 
            this.splitContainer3.Panel2.Controls.Add(this.tbField);
            this.splitContainer3.Size = new System.Drawing.Size(580, 485);
            this.splitContainer3.SplitterDistance = 345;
            this.splitContainer3.TabIndex = 0;
            // 
            // lvExif
            // 
            this.lvExif.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader1,
            this.columnHeader2,
            this.columnHeader3});
            this.lvExif.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lvExif.HideSelection = false;
            this.lvExif.Location = new System.Drawing.Point(0, 0);
            this.lvExif.MultiSelect = false;
            this.lvExif.Name = "lvExif";
            this.lvExif.Size = new System.Drawing.Size(580, 345);
            this.lvExif.Sorting = System.Windows.Forms.SortOrder.Ascending;
            this.lvExif.TabIndex = 2;
            this.lvExif.UseCompatibleStateImageBehavior = false;
            this.lvExif.View = System.Windows.Forms.View.Details;
            this.lvExif.ColumnClick += new System.Windows.Forms.ColumnClickEventHandler(this.lvExif_ColumnClick);
            this.lvExif.SelectedIndexChanged += new System.EventHandler(this.lvExif_SelectedIndexChanged);
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "Exif Tag";
            this.columnHeader1.Width = 160;
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "Value";
            this.columnHeader2.Width = 128;
            // 
            // columnHeader3
            // 
            this.columnHeader3.Text = "IFD";
            // 
            // tbField
            // 
            this.tbField.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tbField.Location = new System.Drawing.Point(0, 0);
            this.tbField.Multiline = true;
            this.tbField.Name = "tbField";
            this.tbField.ReadOnly = true;
            this.tbField.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.tbField.Size = new System.Drawing.Size(580, 136);
            this.tbField.TabIndex = 0;
            // 
            // splitContainer2
            // 
            this.splitContainer2.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer2.Location = new System.Drawing.Point(0, 0);
            this.splitContainer2.Name = "splitContainer2";
            this.splitContainer2.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer2.Panel1
            // 
            this.splitContainer2.Panel1.Controls.Add(this.button1);
            this.splitContainer2.Panel1.Controls.Add(this.richTextBox1);
            this.splitContainer2.Panel1.Controls.Add(this.binaryMapViewer1);
            // 
            // splitContainer2.Panel2
            // 
            this.splitContainer2.Panel2.Controls.Add(this.pbThumb);
            this.splitContainer2.Size = new System.Drawing.Size(377, 485);
            this.splitContainer2.SplitterDistance = 322;
            this.splitContainer2.TabIndex = 0;
            // 
            // binaryMapViewer1
            // 
            this.binaryMapViewer1.BinSize = 8;
            this.binaryMapViewer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.binaryMapViewer1.Location = new System.Drawing.Point(0, 0);
            memoryBinStream2.Position = ((long)(0));
            this.binaryMapViewer1.Map = memoryBinStream2;
            this.binaryMapViewer1.Name = "binaryMapViewer1";
            this.binaryMapViewer1.Size = new System.Drawing.Size(377, 322);
            this.binaryMapViewer1.TabIndex = 3;
            this.binaryMapViewer1.BinSelect += new ExifLibrary.BinaryMapViewer.OnBinSelect(this.binaryMapViewer1_BinSelect);
            // 
            // pbThumb
            // 
            this.pbThumb.BackColor = System.Drawing.Color.Black;
            this.pbThumb.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pbThumb.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pbThumb.Location = new System.Drawing.Point(0, 0);
            this.pbThumb.Name = "pbThumb";
            this.pbThumb.Size = new System.Drawing.Size(377, 159);
            this.pbThumb.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pbThumb.TabIndex = 2;
            this.pbThumb.TabStop = false;
            // 
            // tsExif
            // 
            this.tsExif.Dock = System.Windows.Forms.DockStyle.None;
            this.tsExif.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden;
            this.tsExif.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.btnOpen});
            this.tsExif.Location = new System.Drawing.Point(0, 0);
            this.tsExif.Name = "tsExif";
            this.tsExif.Size = new System.Drawing.Size(961, 31);
            this.tsExif.Stretch = true;
            this.tsExif.TabIndex = 0;
            // 
            // btnOpen
            // 
            this.btnOpen.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.btnOpen.Image = global::ExifLibrary.Properties.Resources.open_document_24;
            this.btnOpen.ImageScaling = System.Windows.Forms.ToolStripItemImageScaling.None;
            this.btnOpen.ImageTransparentColor = System.Drawing.Color.Magenta;
            this.btnOpen.Name = "btnOpen";
            this.btnOpen.Size = new System.Drawing.Size(28, 28);
            this.btnOpen.Text = "&Open";
            this.btnOpen.Click += new System.EventHandler(this.btnOpen_Click);
            // 
            // fdSave
            // 
            this.fdSave.Filter = "JPEG Images *.jpg|*.jpg";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(3, 134);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(374, 257);
            this.richTextBox1.TabIndex = 1;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(290, 146);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 4;
            this.button1.Text = "button1";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // FormMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(961, 538);
            this.Controls.Add(this.toolStripContainer1);
            this.Name = "FormMain";
            this.Text = "Exif Test";
            this.toolStripContainer1.BottomToolStripPanel.ResumeLayout(false);
            this.toolStripContainer1.BottomToolStripPanel.PerformLayout();
            this.toolStripContainer1.ContentPanel.ResumeLayout(false);
            this.toolStripContainer1.TopToolStripPanel.ResumeLayout(false);
            this.toolStripContainer1.TopToolStripPanel.PerformLayout();
            this.toolStripContainer1.ResumeLayout(false);
            this.toolStripContainer1.PerformLayout();
            this.ssExif.ResumeLayout(false);
            this.ssExif.PerformLayout();
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.splitContainer3.Panel1.ResumeLayout(false);
            this.splitContainer3.Panel2.ResumeLayout(false);
            this.splitContainer3.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer3)).EndInit();
            this.splitContainer3.ResumeLayout(false);
            this.splitContainer2.Panel1.ResumeLayout(false);
            this.splitContainer2.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer2)).EndInit();
            this.splitContainer2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pbThumb)).EndInit();
            this.tsExif.ResumeLayout(false);
            this.tsExif.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.OpenFileDialog fdOpen;
        private System.Windows.Forms.ToolStripContainer toolStripContainer1;
        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.SplitContainer splitContainer2;
#if DEBUG
        private BinaryMapViewer binaryMapViewer1;
#endif
        private System.Windows.Forms.PictureBox pbThumb;
        private System.Windows.Forms.ToolStrip tsExif;
        private System.Windows.Forms.ToolStripButton btnOpen;
        private System.Windows.Forms.StatusStrip ssExif;
        private System.Windows.Forms.ToolStripStatusLabel lblStatus;
        private System.Windows.Forms.ToolStripStatusLabel lblByteOrder;
        private System.Windows.Forms.ToolStripStatusLabel lblThumbnail;
        private System.Windows.Forms.SplitContainer splitContainer3;
        private System.Windows.Forms.ListView lvExif;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.ColumnHeader columnHeader3;
        private System.Windows.Forms.TextBox tbField;
        private System.Windows.Forms.SaveFileDialog fdSave;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
    }
}

