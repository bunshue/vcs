namespace PrettifyListedBelow
{
    partial class PrettifyListedBelow
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(PrettifyListedBelow));
            this.label1 = new System.Windows.Forms.Label();
            this.beautyComboBox = new System.Windows.Forms.ComboBox();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(-2, 72);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(120, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "ComboBox控制元件：";
            // 
            // beautyComboBox
            // 
            this.beautyComboBox.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.beautyComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.beautyComboBox.FormattingEnabled = true;
            this.beautyComboBox.Location = new System.Drawing.Point(124, 69);
            this.beautyComboBox.Name = "beautyComboBox";
            this.beautyComboBox.Size = new System.Drawing.Size(151, 23);
            this.beautyComboBox.TabIndex = 1;
            this.beautyComboBox.DrawItem += new System.Windows.Forms.DrawItemEventHandler(this.beautyComboBox_DrawItem);
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "200812120301473636752.gif");
            this.imageList1.Images.SetKeyName(1, "200812120304155365081.jpg");
            this.imageList1.Images.SetKeyName(2, "200812120310127302145.gif");
            this.imageList1.Images.SetKeyName(3, "Image3.gif");
            this.imageList1.Images.SetKeyName(4, "Image6.gif");
            // 
            // PrettifyListedBelow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(301, 195);
            this.Controls.Add(this.beautyComboBox);
            this.Controls.Add(this.label1);
            this.Name = "PrettifyListedBelow";
            this.Text = "美化ComboBox控制元件下拉選單";
            this.Load += new System.EventHandler(this.PrettifyListedBelow_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox beautyComboBox;
        private System.Windows.Forms.ImageList imageList1;
    }
}

