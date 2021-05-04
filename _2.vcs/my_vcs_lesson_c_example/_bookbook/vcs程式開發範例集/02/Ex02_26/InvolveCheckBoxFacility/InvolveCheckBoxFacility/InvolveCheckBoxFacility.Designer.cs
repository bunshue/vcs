namespace InvolveCheckBoxFacility
{
    partial class InvolveCheckBoxFacility
    {
        /// <summary>
        /// 必需的設計器變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的資源。
        /// </summary>
        /// <param name="disposing">如果應釋放托管資源，為 true；否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if(disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 視窗設計器產生的代碼

        /// <summary>
        /// 設計器支援所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.listView1 = new System.Windows.Forms.ListView();
            this.checkAll = new System.Windows.Forms.Button();
            this.cleanUp = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // listView1
            // 
            this.listView1.Location = new System.Drawing.Point(4, 13);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(371, 196);
            this.listView1.TabIndex = 0;
            this.listView1.UseCompatibleStateImageBehavior = false;
            // 
            // checkAll
            // 
            this.checkAll.Location = new System.Drawing.Point(48, 17);
            this.checkAll.Name = "checkAll";
            this.checkAll.Size = new System.Drawing.Size(55, 23);
            this.checkAll.TabIndex = 1;
            this.checkAll.Text = "全選";
            this.checkAll.UseVisualStyleBackColor = true;
            this.checkAll.Click += new System.EventHandler(this.checkAll_Click);
            // 
            // cleanUp
            // 
            this.cleanUp.Location = new System.Drawing.Point(247, 17);
            this.cleanUp.Name = "cleanUp";
            this.cleanUp.Size = new System.Drawing.Size(55, 23);
            this.cleanUp.TabIndex = 2;
            this.cleanUp.Text = "清空";
            this.cleanUp.UseVisualStyleBackColor = true;
            this.cleanUp.Click += new System.EventHandler(this.cleanUp_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.listView1);
            this.groupBox1.Location = new System.Drawing.Point(7, 7);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(380, 214);
            this.groupBox1.TabIndex = 3;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "ListView控制元件";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.checkAll);
            this.groupBox2.Controls.Add(this.cleanUp);
            this.groupBox2.Location = new System.Drawing.Point(7, 226);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(380, 46);
            this.groupBox2.TabIndex = 4;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "操作類型";
            // 
            // InvolveCheckBoxFacility
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(394, 278);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "InvolveCheckBoxFacility";
            this.Text = "具有多選核取框的ListView控制元件";
            this.Load += new System.EventHandler(this.InvolveCheckBoxFacility_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.Button checkAll;
        private System.Windows.Forms.Button cleanUp;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
    }
}

