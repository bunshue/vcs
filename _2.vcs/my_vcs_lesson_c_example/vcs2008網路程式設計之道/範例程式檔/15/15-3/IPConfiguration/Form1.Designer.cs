namespace IPConfiguration
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
          this.Label1 = new System.Windows.Forms.Label();
          this.cboInterfaces = new System.Windows.Forms.ComboBox();
          this.statusStrip1 = new System.Windows.Forms.StatusStrip();
          this.StatusBar = new System.Windows.Forms.ToolStripStatusLabel();
          this.tabControl1 = new System.Windows.Forms.TabControl();
          this.tabPage1 = new System.Windows.Forms.TabPage();
          this.lstAddress = new System.Windows.Forms.ListView();
          this.clmnType = new System.Windows.Forms.ColumnHeader();
          this.clmnAddress = new System.Windows.Forms.ColumnHeader();
          this.tabPage2 = new System.Windows.Forms.TabPage();
          this.lstInformation = new System.Windows.Forms.ListView();
          this.clmnItem = new System.Windows.Forms.ColumnHeader();
          this.clmnDescription = new System.Windows.Forms.ColumnHeader();
          this.statusStrip1.SuspendLayout();
          this.tabControl1.SuspendLayout();
          this.tabPage1.SuspendLayout();
          this.tabPage2.SuspendLayout();
          this.SuspendLayout();
          // 
          // Label1
          // 
          this.Label1.Location = new System.Drawing.Point(10, 17);
          this.Label1.Margin = new System.Windows.Forms.Padding(3, 3, 0, 3);
          this.Label1.Name = "Label1";
          this.Label1.Size = new System.Drawing.Size(72, 15);
          this.Label1.TabIndex = 18;
          this.Label1.Text = "網路介面卡:";
          // 
          // cboInterfaces
          // 
          this.cboInterfaces.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
          this.cboInterfaces.DropDownWidth = 400;
          this.cboInterfaces.FormattingEnabled = true;
          this.cboInterfaces.Location = new System.Drawing.Point(83, 12);
          this.cboInterfaces.Margin = new System.Windows.Forms.Padding(1, 3, 3, 3);
          this.cboInterfaces.Name = "cboInterfaces";
          this.cboInterfaces.Size = new System.Drawing.Size(306, 20);
          this.cboInterfaces.TabIndex = 17;
          this.cboInterfaces.SelectedIndexChanged += new System.EventHandler(this.cboInterfaces_SelectedIndexChanged);
          // 
          // statusStrip1
          // 
          this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.StatusBar});
          this.statusStrip1.Location = new System.Drawing.Point(0, 213);
          this.statusStrip1.Name = "statusStrip1";
          this.statusStrip1.Size = new System.Drawing.Size(399, 22);
          this.statusStrip1.TabIndex = 82;
          // 
          // StatusBar
          // 
          this.StatusBar.Name = "StatusBar";
          this.StatusBar.Size = new System.Drawing.Size(0, 17);
          // 
          // tabControl1
          // 
          this.tabControl1.Controls.Add(this.tabPage1);
          this.tabControl1.Controls.Add(this.tabPage2);
          this.tabControl1.Location = new System.Drawing.Point(12, 44);
          this.tabControl1.Name = "tabControl1";
          this.tabControl1.SelectedIndex = 0;
          this.tabControl1.Size = new System.Drawing.Size(375, 155);
          this.tabControl1.TabIndex = 83;
          // 
          // tabPage1
          // 
          this.tabPage1.Controls.Add(this.lstAddress);
          this.tabPage1.Location = new System.Drawing.Point(4, 21);
          this.tabPage1.Name = "tabPage1";
          this.tabPage1.Padding = new System.Windows.Forms.Padding(3);
          this.tabPage1.Size = new System.Drawing.Size(367, 130);
          this.tabPage1.TabIndex = 0;
          this.tabPage1.Text = "IP位址";
          this.tabPage1.UseVisualStyleBackColor = true;
          // 
          // lstAddress
          // 
          this.lstAddress.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.clmnType,
            this.clmnAddress});
          this.lstAddress.Dock = System.Windows.Forms.DockStyle.Fill;
          this.lstAddress.FullRowSelect = true;
          this.lstAddress.GridLines = true;
          this.lstAddress.Location = new System.Drawing.Point(3, 3);
          this.lstAddress.Name = "lstAddress";
          this.lstAddress.Size = new System.Drawing.Size(361, 124);
          this.lstAddress.TabIndex = 20;
          this.lstAddress.UseCompatibleStateImageBehavior = false;
          this.lstAddress.View = System.Windows.Forms.View.Details;
          // 
          // clmnType
          // 
          this.clmnType.Text = "類型";
          this.clmnType.Width = 170;
          // 
          // clmnAddress
          // 
          this.clmnAddress.Text = "IP位址";
          this.clmnAddress.Width = 180;
          // 
          // tabPage2
          // 
          this.tabPage2.Controls.Add(this.lstInformation);
          this.tabPage2.Location = new System.Drawing.Point(4, 21);
          this.tabPage2.Name = "tabPage2";
          this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
          this.tabPage2.Size = new System.Drawing.Size(367, 131);
          this.tabPage2.TabIndex = 1;
          this.tabPage2.Text = "統計資料";
          this.tabPage2.UseVisualStyleBackColor = true;
          // 
          // lstInformation
          // 
          this.lstInformation.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.clmnItem,
            this.clmnDescription});
          this.lstInformation.Dock = System.Windows.Forms.DockStyle.Fill;
          this.lstInformation.FullRowSelect = true;
          this.lstInformation.GridLines = true;
          this.lstInformation.Location = new System.Drawing.Point(3, 3);
          this.lstInformation.Name = "lstInformation";
          this.lstInformation.Size = new System.Drawing.Size(361, 125);
          this.lstInformation.TabIndex = 21;
          this.lstInformation.UseCompatibleStateImageBehavior = false;
          this.lstInformation.View = System.Windows.Forms.View.Details;
          // 
          // clmnItem
          // 
          this.clmnItem.Text = "項目";
          this.clmnItem.Width = 170;
          // 
          // clmnDescription
          // 
          this.clmnDescription.Text = "描述";
          this.clmnDescription.Width = 180;
          // 
          // Form1
          // 
          this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
          this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          this.ClientSize = new System.Drawing.Size(399, 235);
          this.Controls.Add(this.tabControl1);
          this.Controls.Add(this.statusStrip1);
          this.Controls.Add(this.cboInterfaces);
          this.Controls.Add(this.Label1);
          this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
          this.MaximizeBox = false;
          this.Name = "Form1";
          this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
          this.Text = "Network Configurations";
          this.Load += new System.EventHandler(this.Form1_Load);
          this.statusStrip1.ResumeLayout(false);
          this.statusStrip1.PerformLayout();
          this.tabControl1.ResumeLayout(false);
          this.tabPage1.ResumeLayout(false);
          this.tabPage2.ResumeLayout(false);
          this.ResumeLayout(false);
          this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Label1;
        private System.Windows.Forms.ComboBox cboInterfaces;
        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel StatusBar;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage tabPage1;
        private System.Windows.Forms.ListView lstAddress;
        private System.Windows.Forms.ColumnHeader clmnType;
        private System.Windows.Forms.ColumnHeader clmnAddress;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.ListView lstInformation;
        private System.Windows.Forms.ColumnHeader clmnItem;
        private System.Windows.Forms.ColumnHeader clmnDescription;
    }
}

