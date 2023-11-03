namespace CH1109
{
    partial class Form1
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.btnRemove = new System.Windows.Forms.Button();
            this.btnAdd = new System.Windows.Forms.Button();
            this.txtItem = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.clstCourse = new System.Windows.Forms.CheckedListBox();
            this.SuspendLayout();
            // 
            // btnRemove
            // 
            this.btnRemove.Location = new System.Drawing.Point(263, 96);
            this.btnRemove.Name = "btnRemove";
            this.btnRemove.Size = new System.Drawing.Size(75, 35);
            this.btnRemove.TabIndex = 9;
            this.btnRemove.Text = "刪除";
            this.btnRemove.UseVisualStyleBackColor = true;
            this.btnRemove.Click += new System.EventHandler(this.btnRemove_Click);
            // 
            // btnAdd
            // 
            this.btnAdd.Location = new System.Drawing.Point(180, 96);
            this.btnAdd.Name = "btnAdd";
            this.btnAdd.Size = new System.Drawing.Size(75, 35);
            this.btnAdd.TabIndex = 8;
            this.btnAdd.Text = "新增";
            this.btnAdd.UseVisualStyleBackColor = true;
            this.btnAdd.Click += new System.EventHandler(this.btnAdd_Click);
            // 
            // txtItem
            // 
            this.txtItem.Location = new System.Drawing.Point(179, 56);
            this.txtItem.Name = "txtItem";
            this.txtItem.Size = new System.Drawing.Size(135, 22);
            this.txtItem.TabIndex = 7;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(177, 26);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(149, 12);
            this.label1.TabIndex = 6;
            this.label1.Text = "請選擇要新增或刪除的選項";
            // 
            // clstCourse
            // 
            this.clstCourse.FormattingEnabled = true;
            this.clstCourse.Location = new System.Drawing.Point(21, 21);
            this.clstCourse.Name = "clstCourse";
            this.clstCourse.Size = new System.Drawing.Size(150, 157);
            this.clstCourse.TabIndex = 5;
            this.clstCourse.ItemCheck += new System.Windows.Forms.ItemCheckEventHandler(this.clstCourse_ItemCheck);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(375, 200);
            this.Controls.Add(this.btnRemove);
            this.Controls.Add(this.btnAdd);
            this.Controls.Add(this.txtItem);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.clstCourse);
            this.Name = "Form1";
            this.Text = "CH1109";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnRemove;
        private System.Windows.Forms.Button btnAdd;
        private System.Windows.Forms.TextBox txtItem;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.CheckedListBox clstCourse;
    }
}

