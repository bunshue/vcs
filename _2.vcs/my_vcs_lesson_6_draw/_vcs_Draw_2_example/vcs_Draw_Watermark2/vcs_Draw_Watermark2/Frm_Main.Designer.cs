﻿namespace vcs_Draw_Watermark2
{
    partial class Frm_Main
    {
        /// <summary>
        /// 必需的設計器變量。
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

        #region Windows 窗體設計器生成的代碼

        /// <summary>
        /// 設計器支持所需的方法 - 不要
        /// 使用代碼編輯器修改此方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.lbImgList = new System.Windows.Forms.ListBox();
            this.button2 = new System.Windows.Forms.Button();
            this.txtSavaPath = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.btnPreview = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.btnPerform = new System.Windows.Forms.Button();
            this.btnLoadImg = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.label6 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.cbbPosition = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.trackBar1 = new System.Windows.Forms.TrackBar();
            this.rbPIC = new System.Windows.Forms.RadioButton();
            this.rbTxt = new System.Windows.Forms.RadioButton();
            this.txtWaterMarkFont = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.txtWaterMarkImg = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.btnSelect = new System.Windows.Forms.Button();
            this.pbImgPreview = new System.Windows.Forms.PictureBox();
            this.fontDialog1 = new System.Windows.Forms.FontDialog();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.openFileDialog2 = new System.Windows.Forms.OpenFileDialog();
            this.folderBrowserDialog1 = new System.Windows.Forms.FolderBrowserDialog();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbImgPreview)).BeginInit();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.lbImgList);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(189, 359);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "加水印圖片列表";
            // 
            // lbImgList
            // 
            this.lbImgList.FormattingEnabled = true;
            this.lbImgList.ItemHeight = 12;
            this.lbImgList.Location = new System.Drawing.Point(6, 13);
            this.lbImgList.Name = "lbImgList";
            this.lbImgList.Size = new System.Drawing.Size(177, 340);
            this.lbImgList.TabIndex = 0;
            this.lbImgList.SelectedIndexChanged += new System.EventHandler(this.lbImgList_SelectedIndexChanged);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(523, 298);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(65, 23);
            this.button2.TabIndex = 8;
            this.button2.Text = "瀏覽...";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // txtSavaPath
            // 
            this.txtSavaPath.BackColor = System.Drawing.Color.White;
            this.txtSavaPath.Enabled = false;
            this.txtSavaPath.Location = new System.Drawing.Point(280, 299);
            this.txtSavaPath.Name = "txtSavaPath";
            this.txtSavaPath.ReadOnly = true;
            this.txtSavaPath.Size = new System.Drawing.Size(239, 22);
            this.txtSavaPath.TabIndex = 7;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(215, 303);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(65, 12);
            this.label5.TabIndex = 6;
            this.label5.Text = "保存位置：";
            // 
            // btnPreview
            // 
            this.btnPreview.Location = new System.Drawing.Point(316, 334);
            this.btnPreview.Name = "btnPreview";
            this.btnPreview.Size = new System.Drawing.Size(75, 23);
            this.btnPreview.TabIndex = 5;
            this.btnPreview.Text = "水印預覽";
            this.btnPreview.UseVisualStyleBackColor = true;
            this.btnPreview.Click += new System.EventHandler(this.btnPreview_Click);
            // 
            // btnExit
            // 
            this.btnExit.Location = new System.Drawing.Point(503, 334);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(75, 23);
            this.btnExit.TabIndex = 4;
            this.btnExit.Text = "關閉退出";
            this.btnExit.UseVisualStyleBackColor = true;
            this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
            // 
            // btnPerform
            // 
            this.btnPerform.Location = new System.Drawing.Point(409, 334);
            this.btnPerform.Name = "btnPerform";
            this.btnPerform.Size = new System.Drawing.Size(75, 23);
            this.btnPerform.TabIndex = 3;
            this.btnPerform.Text = "開始執行";
            this.btnPerform.UseVisualStyleBackColor = true;
            this.btnPerform.Click += new System.EventHandler(this.btnPerform_Click);
            // 
            // btnLoadImg
            // 
            this.btnLoadImg.Location = new System.Drawing.Point(216, 334);
            this.btnLoadImg.Name = "btnLoadImg";
            this.btnLoadImg.Size = new System.Drawing.Size(75, 23);
            this.btnLoadImg.TabIndex = 2;
            this.btnLoadImg.Text = "加載圖片";
            this.btnLoadImg.UseVisualStyleBackColor = true;
            this.btnLoadImg.Click += new System.EventHandler(this.btnLoadImg_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.label6);
            this.groupBox2.Controls.Add(this.label4);
            this.groupBox2.Controls.Add(this.cbbPosition);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.button1);
            this.groupBox2.Controls.Add(this.trackBar1);
            this.groupBox2.Controls.Add(this.rbPIC);
            this.groupBox2.Controls.Add(this.rbTxt);
            this.groupBox2.Controls.Add(this.txtWaterMarkFont);
            this.groupBox2.Controls.Add(this.label1);
            this.groupBox2.Controls.Add(this.txtWaterMarkImg);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.btnSelect);
            this.groupBox2.Controls.Add(this.pbImgPreview);
            this.groupBox2.Location = new System.Drawing.Point(217, 12);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(383, 274);
            this.groupBox2.TabIndex = 0;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "水印設置";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(10, 171);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(257, 12);
            this.label6.TabIndex = 16;
            this.label6.Text = "注意：水印圖片建議使用分辨率為368*75的圖片";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(244, 145);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(65, 12);
            this.label4.TabIndex = 4;
            this.label4.Text = "水印位置：";
            // 
            // cbbPosition
            // 
            this.cbbPosition.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbbPosition.FormattingEnabled = true;
            this.cbbPosition.Items.AddRange(new object[] {
            "正中",
            "左上",
            "左下",
            "右上",
            "右下"});
            this.cbbPosition.Location = new System.Drawing.Point(315, 141);
            this.cbbPosition.Name = "cbbPosition";
            this.cbbPosition.Size = new System.Drawing.Size(65, 20);
            this.cbbPosition.TabIndex = 15;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(8, 147);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 12);
            this.label2.TabIndex = 14;
            this.label2.Text = "透明設置：";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(315, 48);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(65, 23);
            this.button1.TabIndex = 13;
            this.button1.Text = "字體設置";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // trackBar1
            // 
            this.trackBar1.AutoSize = false;
            this.trackBar1.Enabled = false;
            this.trackBar1.LargeChange = 1;
            this.trackBar1.Location = new System.Drawing.Point(69, 140);
            this.trackBar1.Maximum = 255;
            this.trackBar1.Name = "trackBar1";
            this.trackBar1.Size = new System.Drawing.Size(179, 22);
            this.trackBar1.TabIndex = 12;
            this.trackBar1.Value = 255;
            this.trackBar1.ValueChanged += new System.EventHandler(this.trackBar1_ValueChanged);
            this.trackBar1.Enter += new System.EventHandler(this.trackBar1_Enter);
            // 
            // rbPIC
            // 
            this.rbPIC.AutoSize = true;
            this.rbPIC.Location = new System.Drawing.Point(10, 82);
            this.rbPIC.Name = "rbPIC";
            this.rbPIC.Size = new System.Drawing.Size(95, 16);
            this.rbPIC.TabIndex = 11;
            this.rbPIC.Text = "添加圖片水印";
            this.rbPIC.UseVisualStyleBackColor = true;
            this.rbPIC.CheckedChanged += new System.EventHandler(this.rbPIC_CheckedChanged);
            // 
            // rbTxt
            // 
            this.rbTxt.AutoSize = true;
            this.rbTxt.Checked = true;
            this.rbTxt.Location = new System.Drawing.Point(8, 22);
            this.rbTxt.Name = "rbTxt";
            this.rbTxt.Size = new System.Drawing.Size(95, 16);
            this.rbTxt.TabIndex = 10;
            this.rbTxt.TabStop = true;
            this.rbTxt.Text = "添加文字水印";
            this.rbTxt.UseVisualStyleBackColor = true;
            this.rbTxt.CheckedChanged += new System.EventHandler(this.rbTxt_CheckedChanged);
            // 
            // txtWaterMarkFont
            // 
            this.txtWaterMarkFont.Location = new System.Drawing.Point(75, 49);
            this.txtWaterMarkFont.Name = "txtWaterMarkFont";
            this.txtWaterMarkFont.Size = new System.Drawing.Size(239, 22);
            this.txtWaterMarkFont.TabIndex = 2;
            this.txtWaterMarkFont.TextChanged += new System.EventHandler(this.txtWaterMarkFont_TextChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(8, 53);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(65, 12);
            this.label1.TabIndex = 1;
            this.label1.Text = "水印文字：";
            // 
            // txtWaterMarkImg
            // 
            this.txtWaterMarkImg.BackColor = System.Drawing.Color.White;
            this.txtWaterMarkImg.Enabled = false;
            this.txtWaterMarkImg.Location = new System.Drawing.Point(75, 109);
            this.txtWaterMarkImg.Name = "txtWaterMarkImg";
            this.txtWaterMarkImg.ReadOnly = true;
            this.txtWaterMarkImg.Size = new System.Drawing.Size(239, 22);
            this.txtWaterMarkImg.TabIndex = 1;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(8, 114);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(65, 12);
            this.label3.TabIndex = 0;
            this.label3.Text = "水印圖片：";
            // 
            // btnSelect
            // 
            this.btnSelect.Location = new System.Drawing.Point(315, 108);
            this.btnSelect.Name = "btnSelect";
            this.btnSelect.Size = new System.Drawing.Size(65, 23);
            this.btnSelect.TabIndex = 2;
            this.btnSelect.Text = "瀏覽...";
            this.btnSelect.UseVisualStyleBackColor = true;
            this.btnSelect.Click += new System.EventHandler(this.btnSelect_Click);
            // 
            // pbImgPreview
            // 
            this.pbImgPreview.BackColor = System.Drawing.Color.WhiteSmoke;
            this.pbImgPreview.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.pbImgPreview.Location = new System.Drawing.Point(9, 191);
            this.pbImgPreview.Name = "pbImgPreview";
            this.pbImgPreview.Size = new System.Drawing.Size(368, 75);
            this.pbImgPreview.SizeMode = System.Windows.Forms.PictureBoxSizeMode.CenterImage;
            this.pbImgPreview.TabIndex = 3;
            this.pbImgPreview.TabStop = false;
            // 
            // openFileDialog1
            // 
            this.openFileDialog1.Filter = "圖片文件|*.jpeg;*.jpg;*.png;*.bmp;*.gif";
            this.openFileDialog1.Multiselect = true;
            // 
            // openFileDialog2
            // 
            this.openFileDialog2.Filter = "圖片文件|*.jpeg;*.jpg;*.png;*.bmp";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(606, 14);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(410, 585);
            this.richTextBox1.TabIndex = 9;
            this.richTextBox1.Text = "";
            // 
            // Frm_Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1028, 644);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.txtSavaPath);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.btnPreview);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.btnLoadImg);
            this.Controls.Add(this.btnPerform);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Frm_Main";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "批量添加圖片水印";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.trackBar1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbImgPreview)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.ListBox lbImgList;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.TextBox txtWaterMarkFont;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.FontDialog fontDialog1;
        private System.Windows.Forms.Button btnSelect;
        private System.Windows.Forms.TextBox txtWaterMarkImg;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.PictureBox pbImgPreview;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button btnLoadImg;
        private System.Windows.Forms.Button btnPreview;
        private System.Windows.Forms.Button btnExit;
        private System.Windows.Forms.Button btnPerform;
        private System.Windows.Forms.RadioButton rbPIC;
        private System.Windows.Forms.RadioButton rbTxt;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.TrackBar trackBar1;
        private System.Windows.Forms.OpenFileDialog openFileDialog2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox cbbPosition;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TextBox txtSavaPath;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.FolderBrowserDialog folderBrowserDialog1;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}
