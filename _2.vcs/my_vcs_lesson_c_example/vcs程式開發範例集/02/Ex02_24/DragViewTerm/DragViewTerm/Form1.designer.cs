namespace DragViewTerm
{
    partial class Form1
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
            if (disposing && (components != null))
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
            System.Windows.Forms.ListViewItem listViewItem6 = new System.Windows.Forms.ListViewItem("商品B", 0);
            System.Windows.Forms.ListViewItem listViewItem7 = new System.Windows.Forms.ListViewItem("商品A", 1);
            System.Windows.Forms.ListViewItem listViewItem8 = new System.Windows.Forms.ListViewItem("商品C", 2);
            System.Windows.Forms.ListViewItem listViewItem9 = new System.Windows.Forms.ListViewItem("商品D", 3);
            System.Windows.Forms.ListViewItem listViewItem10 = new System.Windows.Forms.ListViewItem("商品E", 4);
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.listView1 = new System.Windows.Forms.ListView();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.SuspendLayout();
            // 
            // listView1
            // 
            this.listView1.AllowDrop = true;
            this.listView1.Items.AddRange(new System.Windows.Forms.ListViewItem[] {
            listViewItem6,
            listViewItem7,
            listViewItem8,
            listViewItem9,
            listViewItem10});
            this.listView1.LargeImageList = this.imageList1;
            this.listView1.Location = new System.Drawing.Point(3, 12);
            this.listView1.Name = "listView1";
            this.listView1.Size = new System.Drawing.Size(262, 167);
            this.listView1.TabIndex = 0;
            this.listView1.UseCompatibleStateImageBehavior = false;
            this.listView1.DragDrop += new System.Windows.Forms.DragEventHandler(this.listView1_DragDrop);
            this.listView1.DragEnter += new System.Windows.Forms.DragEventHandler(this.listView1_DragEnter);
            this.listView1.ItemDrag += new System.Windows.Forms.ItemDragEventHandler(this.listView1_ItemDrag);
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "1.bmp");
            this.imageList1.Images.SetKeyName(1, "2.bmp");
            this.imageList1.Images.SetKeyName(2, "3.bmp");
            this.imageList1.Images.SetKeyName(3, "4.bmp");
            this.imageList1.Images.SetKeyName(4, "5.bmp");
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(286, 191);
            this.Controls.Add(this.listView1);
            this.Name = "Form1";
            this.Text = "在清單視界中拖曳圖項";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListView listView1;
        private System.Windows.Forms.ImageList imageList1;
    }
}

