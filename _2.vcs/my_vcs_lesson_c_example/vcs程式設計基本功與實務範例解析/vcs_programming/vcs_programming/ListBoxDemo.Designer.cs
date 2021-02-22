namespace vcs_programming
{
    partial class ListBoxDemo
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
            this.TypeList = new System.Windows.Forms.ListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.ItemsList = new System.Windows.Forms.ListBox();
            this.btnToRight = new System.Windows.Forms.Button();
            this.btnToLeft = new System.Windows.Forms.Button();
            this.BuyList = new System.Windows.Forms.ListBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.txtName = new System.Windows.Forms.TextBox();
            this.lblOutout = new System.Windows.Forms.Label();
            this.TypeComboBox = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // TypeList
            // 
            this.TypeList.FormattingEnabled = true;
            this.TypeList.ItemHeight = 16;
            this.TypeList.Location = new System.Drawing.Point(12, 59);
            this.TypeList.Name = "TypeList";
            this.TypeList.Size = new System.Drawing.Size(120, 52);
            this.TypeList.TabIndex = 0;
            this.TypeList.SelectedIndexChanged += new System.EventHandler(this.TypeList_SelectedIndexChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 22);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(72, 16);
            this.label1.TabIndex = 1;
            this.label1.Text = "商品種類";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 130);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(72, 16);
            this.label2.TabIndex = 3;
            this.label2.Text = "商品清單";
            // 
            // ItemsList
            // 
            this.ItemsList.FormattingEnabled = true;
            this.ItemsList.ItemHeight = 16;
            this.ItemsList.Location = new System.Drawing.Point(12, 167);
            this.ItemsList.Name = "ItemsList";
            this.ItemsList.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
            this.ItemsList.Size = new System.Drawing.Size(134, 180);
            this.ItemsList.TabIndex = 2;
            // 
            // btnToRight
            // 
            this.btnToRight.Location = new System.Drawing.Point(168, 210);
            this.btnToRight.Name = "btnToRight";
            this.btnToRight.Size = new System.Drawing.Size(75, 32);
            this.btnToRight.TabIndex = 4;
            this.btnToRight.Text = ">";
            this.btnToRight.UseVisualStyleBackColor = true;
            this.btnToRight.Click += new System.EventHandler(this.btnToRight_Click);
            // 
            // btnToLeft
            // 
            this.btnToLeft.Location = new System.Drawing.Point(168, 281);
            this.btnToLeft.Name = "btnToLeft";
            this.btnToLeft.Size = new System.Drawing.Size(75, 32);
            this.btnToLeft.TabIndex = 5;
            this.btnToLeft.Text = "<";
            this.btnToLeft.UseVisualStyleBackColor = true;
            this.btnToLeft.Click += new System.EventHandler(this.btnToLeft_Click);
            // 
            // BuyList
            // 
            this.BuyList.FormattingEnabled = true;
            this.BuyList.ItemHeight = 16;
            this.BuyList.Location = new System.Drawing.Point(269, 167);
            this.BuyList.Name = "BuyList";
            this.BuyList.SelectionMode = System.Windows.Forms.SelectionMode.MultiExtended;
            this.BuyList.Size = new System.Drawing.Size(134, 180);
            this.BuyList.TabIndex = 6;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(266, 130);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(72, 16);
            this.label3.TabIndex = 7;
            this.label3.Text = "購物清單";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(276, 22);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(40, 16);
            this.label4.TabIndex = 8;
            this.label4.Text = "姓名";
            // 
            // txtName
            // 
            this.txtName.Location = new System.Drawing.Point(279, 59);
            this.txtName.Name = "txtName";
            this.txtName.Size = new System.Drawing.Size(100, 27);
            this.txtName.TabIndex = 9;
            // 
            // lblOutout
            // 
            this.lblOutout.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.lblOutout.Location = new System.Drawing.Point(12, 371);
            this.lblOutout.Name = "lblOutout";
            this.lblOutout.Size = new System.Drawing.Size(396, 52);
            this.lblOutout.TabIndex = 10;
            this.lblOutout.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // TypeComboBox
            // 
            this.TypeComboBox.FormattingEnabled = true;
            this.TypeComboBox.Location = new System.Drawing.Point(138, 62);
            this.TypeComboBox.Name = "TypeComboBox";
            this.TypeComboBox.Size = new System.Drawing.Size(121, 24);
            this.TypeComboBox.TabIndex = 11;
            this.TypeComboBox.SelectedIndexChanged += new System.EventHandler(this.TypeComboBox_SelectedIndexChanged);
            // 
            // ListBoxDemo
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(420, 444);
            this.Controls.Add(this.TypeComboBox);
            this.Controls.Add(this.lblOutout);
            this.Controls.Add(this.txtName);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.BuyList);
            this.Controls.Add(this.btnToLeft);
            this.Controls.Add(this.btnToRight);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.ItemsList);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.TypeList);
            this.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "ListBoxDemo";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "ListBoxDemo";
            this.Load += new System.EventHandler(this.ListBoxDemo_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListBox TypeList;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ListBox ItemsList;
        private System.Windows.Forms.Button btnToRight;
        private System.Windows.Forms.Button btnToLeft;
        private System.Windows.Forms.ListBox BuyList;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtName;
        private System.Windows.Forms.Label lblOutout;
        private System.Windows.Forms.ComboBox TypeComboBox;
    }
}