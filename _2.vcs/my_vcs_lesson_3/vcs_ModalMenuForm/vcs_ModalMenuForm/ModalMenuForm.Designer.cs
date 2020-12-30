namespace vcs_ModalMenuForm
{
    partial class ModalMenuForm
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
            this.lstItems = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // lstItems
            // 
            this.lstItems.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.lstItems.FormattingEnabled = true;
            this.lstItems.IntegralHeight = false;
            this.lstItems.Items.AddRange(new object[] {
            "Pink",
            "Light Green",
            "Light Blue"});
            this.lstItems.Location = new System.Drawing.Point(0, 0);
            this.lstItems.Name = "lstItems";
            this.lstItems.Size = new System.Drawing.Size(96, 75);
            this.lstItems.TabIndex = 0;
            this.lstItems.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.lstItems_DrawItem);
            this.lstItems.MeasureItem += new System.Windows.Forms.MeasureItemEventHandler(this.lstItems_MeasureItem);
            this.lstItems.MouseMove += new System.Windows.Forms.MouseEventHandler(this.lstItems_MouseMove);
            this.lstItems.MouseLeave += new System.EventHandler(this.lstItems_MouseLeave);
            this.lstItems.Click += new System.EventHandler(this.lstItems_Click);
            // 
            // ModalMenuForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(110, 110);
            this.Controls.Add(this.lstItems);
            this.Name = "ModalMenuForm";
            this.Text = "ModalMenuForm";
            this.Load += new System.EventHandler(this.ModalMenuForm_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.ModalMenuForm_KeyDown);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox lstItems;


    }
}