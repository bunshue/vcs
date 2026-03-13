namespace vcs_ListView4
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
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
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
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.listView_use_imageList = new System.Windows.Forms.ListView();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.listView_use_imageList);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(583, 435);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "ListView 使用 ImageList";
            // 
            // listView_use_imageList
            // 
            this.listView_use_imageList.Location = new System.Drawing.Point(6, 21);
            this.listView_use_imageList.Name = "listView_use_imageList";
            this.listView_use_imageList.Size = new System.Drawing.Size(571, 408);
            this.listView_use_imageList.TabIndex = 1;
            this.listView_use_imageList.UseCompatibleStateImageBehavior = false;
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "1345915697_Gmail.ico");
            this.imageList1.Images.SetKeyName(1, "1345915707_YouTube.ico");
            this.imageList1.Images.SetKeyName(2, "1345915717_FireFox.ico");
            this.imageList1.Images.SetKeyName(3, "1345915795_GMail.ico");
            this.imageList1.Images.SetKeyName(4, "1345918094_preferences-system-login.ico");
            this.imageList1.Images.SetKeyName(5, "favicon.ico");
            this.imageList1.Images.SetKeyName(6, "Print.ico");
            this.imageList1.Images.SetKeyName(7, "Rotate1.ico");
            this.imageList1.Images.SetKeyName(8, "Rotate2.ico");
            this.imageList1.Images.SetKeyName(9, "Rotate3.ico");
            this.imageList1.Images.SetKeyName(10, "Rotate4.ico");
            this.imageList1.Images.SetKeyName(11, "Save.ico");
            this.imageList1.Images.SetKeyName(12, "spyder_reset.ico");
            this.imageList1.Images.SetKeyName(13, "SysReqMet.ico");
            this.imageList1.Images.SetKeyName(14, "VeryCD.ico");
            this.imageList1.Images.SetKeyName(15, "warn.ico");
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(649, 555);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ListView listView_use_imageList;
        private System.Windows.Forms.ImageList imageList1;
    }
}

