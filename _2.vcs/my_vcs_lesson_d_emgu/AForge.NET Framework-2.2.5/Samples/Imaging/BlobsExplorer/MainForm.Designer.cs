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
            this.splitContainer = new System.Windows.Forms.SplitContainer();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.showRectangleAroundSelectionCheck = new System.Windows.Forms.CheckBox();
            this.highlightTypeCombo = new System.Windows.Forms.ComboBox();
            this.propertyGrid = new System.Windows.Forms.PropertyGrid();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.blobsBrowser = new BlobsExplorer.BlobsBrowser();
            this.splitContainer.Panel1.SuspendLayout();
            this.splitContainer.Panel2.SuspendLayout();
            this.splitContainer.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
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
            this.splitContainer.Panel2.Controls.Add(this.richTextBox1);
            this.splitContainer.Panel2.Controls.Add(this.groupBox1);
            this.splitContainer.Panel2.Controls.Add(this.propertyGrid);
            this.splitContainer.Panel2MinSize = 100;
            this.splitContainer.Size = new System.Drawing.Size(1166, 739);
            this.splitContainer.SplitterDistance = 815;
            this.splitContainer.TabIndex = 2;
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.groupBox1.Controls.Add(this.showRectangleAroundSelectionCheck);
            this.groupBox1.Controls.Add(this.highlightTypeCombo);
            this.groupBox1.Location = new System.Drawing.Point(3, 3);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(338, 107);
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
            this.propertyGrid.Location = new System.Drawing.Point(9, 129);
            this.propertyGrid.Name = "propertyGrid";
            this.propertyGrid.Size = new System.Drawing.Size(309, 293);
            this.propertyGrid.TabIndex = 0;
            this.propertyGrid.ToolbarVisible = false;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(9, 406);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(309, 294);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // blobsBrowser
            // 
            this.blobsBrowser.Highlighting = BlobsExplorer.BlobsBrowser.HightlightType.Quadrilateral;
            this.blobsBrowser.Location = new System.Drawing.Point(246, 248);
            this.blobsBrowser.Name = "blobsBrowser";
            this.blobsBrowser.ShowRectangleAroundSelection = false;
            this.blobsBrowser.Size = new System.Drawing.Size(322, 242);
            this.blobsBrowser.TabIndex = 0;
            this.blobsBrowser.BlobSelected += new BlobsExplorer.BlobSelectionHandler(this.blobsBrowser_BlobSelected);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1166, 739);
            this.Controls.Add(this.splitContainer);
            this.MinimumSize = new System.Drawing.Size(480, 335);
            this.Name = "MainForm";
            this.Text = "Blobs Explorer";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.splitContainer.Panel1.ResumeLayout(false);
            this.splitContainer.Panel2.ResumeLayout(false);
            this.splitContainer.ResumeLayout(false);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer splitContainer;
        private System.Windows.Forms.PropertyGrid propertyGrid;
        private BlobsBrowser blobsBrowser;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ComboBox highlightTypeCombo;
        private System.Windows.Forms.CheckBox showRectangleAroundSelectionCheck;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

