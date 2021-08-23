namespace BlobsExplorer
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
        protected override void Dispose( bool disposing )
        {
            if ( disposing && ( components != null ) )
            {
                components.Dispose( );
            }
            base.Dispose( disposing );
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent( )
        {
            this.statusStrip = new System.Windows.Forms.StatusStrip();
            this.blobsCountLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.openFileDialog = new System.Windows.Forms.OpenFileDialog();
            this.splitContainer = new System.Windows.Forms.SplitContainer();
            this.blobsBrowser = new BlobsExplorer.BlobsBrowser();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.showRectangleAroundSelectionCheck = new System.Windows.Forms.CheckBox();
            this.highlightTypeCombo = new System.Windows.Forms.ComboBox();
            this.propertyGrid = new System.Windows.Forms.PropertyGrid();
            this.statusStrip.SuspendLayout();
            this.splitContainer.Panel1.SuspendLayout();
            this.splitContainer.Panel2.SuspendLayout();
            this.splitContainer.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // statusStrip
            // 
            this.statusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.blobsCountLabel});
            this.statusStrip.Location = new System.Drawing.Point(0, 717);
            this.statusStrip.Name = "statusStrip";
            this.statusStrip.Size = new System.Drawing.Size(1166, 22);
            this.statusStrip.TabIndex = 1;
            // 
            // blobsCountLabel
            // 
            this.blobsCountLabel.AutoSize = false;
            this.blobsCountLabel.BorderSides = ((System.Windows.Forms.ToolStripStatusLabelBorderSides)((((System.Windows.Forms.ToolStripStatusLabelBorderSides.Left | System.Windows.Forms.ToolStripStatusLabelBorderSides.Top)
                        | System.Windows.Forms.ToolStripStatusLabelBorderSides.Right)
                        | System.Windows.Forms.ToolStripStatusLabelBorderSides.Bottom)));
            this.blobsCountLabel.BorderStyle = System.Windows.Forms.Border3DStyle.SunkenInner;
            this.blobsCountLabel.Name = "blobsCountLabel";
            this.blobsCountLabel.Size = new System.Drawing.Size(1151, 17);
            this.blobsCountLabel.Spring = true;
            this.blobsCountLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // openFileDialog
            // 
            this.openFileDialog.Filter = "Image files (*.jpg,*.png,*.tif,*.bmp,*.gif)|*.jpg;*.png;*.tif;*.bmp;*.gif|JPG fil" +
                "es (*.jpg)|*.jpg|PNG files (*.png)|*.png|TIF files (*.tif)|*.tif|BMP files (*.bm" +
                "p)|*.bmp|GIF files (*.gif)|*.gif";
            this.openFileDialog.Title = "Open image file";
            // 
            // splitContainer
            // 
            this.splitContainer.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer.Location = new System.Drawing.Point(0, 0);
            this.splitContainer.Name = "splitContainer";
            // 
            // splitContainer.Panel1
            // 
            this.splitContainer.Panel1.Controls.Add(this.blobsBrowser);
            // 
            // splitContainer.Panel2
            // 
            this.splitContainer.Panel2.Controls.Add(this.button2);
            this.splitContainer.Panel2.Controls.Add(this.button1);
            this.splitContainer.Panel2.Controls.Add(this.groupBox1);
            this.splitContainer.Panel2.Controls.Add(this.propertyGrid);
            this.splitContainer.Panel2MinSize = 100;
            this.splitContainer.Size = new System.Drawing.Size(1166, 717);
            this.splitContainer.SplitterDistance = 815;
            this.splitContainer.TabIndex = 2;
            // 
            // blobsBrowser
            // 
            this.blobsBrowser.Highlighting = BlobsExplorer.BlobsBrowser.HightlightType.Quadrilateral;
            this.blobsBrowser.Location = new System.Drawing.Point(246, 237);
            this.blobsBrowser.Name = "blobsBrowser";
            this.blobsBrowser.ShowRectangleAroundSelection = false;
            this.blobsBrowser.Size = new System.Drawing.Size(322, 242);
            this.blobsBrowser.TabIndex = 0;
            this.blobsBrowser.BlobSelected += new BlobsExplorer.BlobSelectionHandler(this.blobsBrowser_BlobSelected);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(140, 80);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(117, 42);
            this.button2.TabIndex = 3;
            this.button2.Text = "Load Demo image";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(17, 80);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(117, 42);
            this.button1.TabIndex = 2;
            this.button1.Text = "Open";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.showRectangleAroundSelectionCheck);
            this.groupBox1.Controls.Add(this.highlightTypeCombo);
            this.groupBox1.Location = new System.Drawing.Point(3, 3);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(338, 60);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Highlight Type";
            // 
            // showRectangleAroundSelectionCheck
            // 
            this.showRectangleAroundSelectionCheck.AutoSize = true;
            this.showRectangleAroundSelectionCheck.Location = new System.Drawing.Point(6, 42);
            this.showRectangleAroundSelectionCheck.Name = "showRectangleAroundSelectionCheck";
            this.showRectangleAroundSelectionCheck.Size = new System.Drawing.Size(174, 16);
            this.showRectangleAroundSelectionCheck.TabIndex = 1;
            this.showRectangleAroundSelectionCheck.Text = "Show rectangle around selection";
            this.showRectangleAroundSelectionCheck.UseVisualStyleBackColor = true;
            this.showRectangleAroundSelectionCheck.CheckedChanged += new System.EventHandler(this.showRectangleAroundSelectionCheck_CheckedChanged);
            // 
            // highlightTypeCombo
            // 
            this.highlightTypeCombo.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.highlightTypeCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.highlightTypeCombo.FormattingEnabled = true;
            this.highlightTypeCombo.Items.AddRange(new object[] {
            "Convex Hull",
            "Left/Right Edges",
            "Top/Bottom Edges",
            "Quadrilateral"});
            this.highlightTypeCombo.Location = new System.Drawing.Point(6, 18);
            this.highlightTypeCombo.Name = "highlightTypeCombo";
            this.highlightTypeCombo.Size = new System.Drawing.Size(326, 20);
            this.highlightTypeCombo.TabIndex = 0;
            this.highlightTypeCombo.SelectedIndexChanged += new System.EventHandler(this.highlightTypeCombo_SelectedIndexChanged);
            // 
            // propertyGrid
            // 
            this.propertyGrid.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
                        | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.propertyGrid.HelpVisible = false;
            this.propertyGrid.Location = new System.Drawing.Point(17, 263);
            this.propertyGrid.Name = "propertyGrid";
            this.propertyGrid.Size = new System.Drawing.Size(309, 384);
            this.propertyGrid.TabIndex = 0;
            this.propertyGrid.ToolbarVisible = false;
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1166, 739);
            this.Controls.Add(this.splitContainer);
            this.Controls.Add(this.statusStrip);
            this.MinimumSize = new System.Drawing.Size(480, 335);
            this.Name = "MainForm";
            this.Text = "Blobs Explorer";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.statusStrip.ResumeLayout(false);
            this.statusStrip.PerformLayout();
            this.splitContainer.Panel1.ResumeLayout(false);
            this.splitContainer.Panel2.ResumeLayout(false);
            this.splitContainer.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.StatusStrip statusStrip;
        private System.Windows.Forms.OpenFileDialog openFileDialog;
        private System.Windows.Forms.SplitContainer splitContainer;
        private System.Windows.Forms.PropertyGrid propertyGrid;
        private BlobsBrowser blobsBrowser;
        private System.Windows.Forms.ToolStripStatusLabel blobsCountLabel;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ComboBox highlightTypeCombo;
        private System.Windows.Forms.CheckBox showRectangleAroundSelectionCheck;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button1;
    }
}

