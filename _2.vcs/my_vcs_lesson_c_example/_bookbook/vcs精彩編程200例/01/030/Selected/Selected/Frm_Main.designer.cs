namespace Selected
{
    partial class Frm_Main
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.button2 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.ckInfo = new System.Windows.Forms.CheckBox();
            this.cklMange = new System.Windows.Forms.CheckedListBox();
            this.cklSell = new System.Windows.Forms.CheckedListBox();
            this.cklShop = new System.Windows.Forms.CheckedListBox();
            this.ckLinfo = new System.Windows.Forms.CheckedListBox();
            this.ckMange = new System.Windows.Forms.CheckBox();
            this.ckSell = new System.Windows.Forms.CheckBox();
            this.ckShop = new System.Windows.Forms.CheckBox();
            this.checkBox3 = new System.Windows.Forms.CheckBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.textBox1);
            this.groupBox1.Controls.Add(this.button2);
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(13, 2);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(158, 271);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "用户注册";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(54, 34);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 22);
            this.textBox1.TabIndex = 7;
            this.textBox1.Text = "david";
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(83, 238);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 6;
            this.button2.Text = "取消(&E)";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(6, 238);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 5;
            this.button1.Text = "确定(&D)";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(7, 37);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 12);
            this.label1.TabIndex = 0;
            this.label1.Text = "姓名：";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.ckInfo);
            this.groupBox2.Controls.Add(this.cklMange);
            this.groupBox2.Controls.Add(this.cklSell);
            this.groupBox2.Controls.Add(this.cklShop);
            this.groupBox2.Controls.Add(this.ckLinfo);
            this.groupBox2.Controls.Add(this.ckMange);
            this.groupBox2.Controls.Add(this.ckSell);
            this.groupBox2.Controls.Add(this.ckShop);
            this.groupBox2.Controls.Add(this.checkBox3);
            this.groupBox2.Location = new System.Drawing.Point(177, 2);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(140, 448);
            this.groupBox2.TabIndex = 1;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "用户权限";
            // 
            // ckInfo
            // 
            this.ckInfo.AutoSize = true;
            this.ckInfo.Location = new System.Drawing.Point(29, 16);
            this.ckInfo.Name = "ckInfo";
            this.ckInfo.Size = new System.Drawing.Size(72, 16);
            this.ckInfo.TabIndex = 26;
            this.ckInfo.Text = "基本档案";
            this.ckInfo.UseVisualStyleBackColor = true;
            this.ckInfo.CheckedChanged += new System.EventHandler(this.ckInfo_CheckedChanged);
            // 
            // cklMange
            // 
            this.cklMange.FormattingEnabled = true;
            this.cklMange.Items.AddRange(new object[] {
            "库存调配",
            "库存警报"});
            this.cklMange.Location = new System.Drawing.Point(42, 351);
            this.cklMange.Name = "cklMange";
            this.cklMange.Size = new System.Drawing.Size(85, 72);
            this.cklMange.TabIndex = 25;
            this.cklMange.Visible = false;
            // 
            // cklSell
            // 
            this.cklSell.FormattingEnabled = true;
            this.cklSell.Items.AddRange(new object[] {
            "商品销售",
            "客户退货"});
            this.cklSell.Location = new System.Drawing.Point(42, 243);
            this.cklSell.Name = "cklSell";
            this.cklSell.Size = new System.Drawing.Size(85, 55);
            this.cklSell.TabIndex = 24;
            this.cklSell.Visible = false;
            // 
            // cklShop
            // 
            this.cklShop.FormattingEnabled = true;
            this.cklShop.Items.AddRange(new object[] {
            "采购进货",
            "采购退货"});
            this.cklShop.Location = new System.Drawing.Point(42, 142);
            this.cklShop.Name = "cklShop";
            this.cklShop.Size = new System.Drawing.Size(85, 72);
            this.cklShop.TabIndex = 23;
            this.cklShop.Visible = false;
            // 
            // ckLinfo
            // 
            this.ckLinfo.FormattingEnabled = true;
            this.ckLinfo.Items.AddRange(new object[] {
            "员工信息",
            "往来单位",
            "客户档案"});
            this.ckLinfo.Location = new System.Drawing.Point(42, 38);
            this.ckLinfo.Name = "ckLinfo";
            this.ckLinfo.Size = new System.Drawing.Size(85, 72);
            this.ckLinfo.TabIndex = 22;
            this.ckLinfo.Visible = false;
            // 
            // ckMange
            // 
            this.ckMange.AutoSize = true;
            this.ckMange.Location = new System.Drawing.Point(29, 328);
            this.ckMange.Name = "ckMange";
            this.ckMange.Size = new System.Drawing.Size(72, 16);
            this.ckMange.TabIndex = 21;
            this.ckMange.Text = "库存管理";
            this.ckMange.UseVisualStyleBackColor = true;
            this.ckMange.CheckedChanged += new System.EventHandler(this.ckMange_CheckedChanged);
            // 
            // ckSell
            // 
            this.ckSell.AutoSize = true;
            this.ckSell.Location = new System.Drawing.Point(29, 222);
            this.ckSell.Name = "ckSell";
            this.ckSell.Size = new System.Drawing.Size(72, 16);
            this.ckSell.TabIndex = 20;
            this.ckSell.Text = "销售管理";
            this.ckSell.UseVisualStyleBackColor = true;
            this.ckSell.CheckedChanged += new System.EventHandler(this.ckSell_CheckedChanged);
            // 
            // ckShop
            // 
            this.ckShop.AutoSize = true;
            this.ckShop.Location = new System.Drawing.Point(29, 121);
            this.ckShop.Name = "ckShop";
            this.ckShop.Size = new System.Drawing.Size(72, 16);
            this.ckShop.TabIndex = 19;
            this.ckShop.Text = "进货管理";
            this.ckShop.UseVisualStyleBackColor = true;
            this.ckShop.CheckedChanged += new System.EventHandler(this.ckShop_CheckedChanged);
            // 
            // checkBox3
            // 
            this.checkBox3.AutoSize = true;
            this.checkBox3.Location = new System.Drawing.Point(18, -43);
            this.checkBox3.Name = "checkBox3";
            this.checkBox3.Size = new System.Drawing.Size(72, 16);
            this.checkBox3.TabIndex = 18;
            this.checkBox3.Text = "基本档案";
            this.checkBox3.UseVisualStyleBackColor = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(323, 2);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(379, 448);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // Frm_Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(714, 460);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Frm_Main";
            this.Text = "利用选择控件实现权限设置";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.CheckedListBox cklMange;
        private System.Windows.Forms.CheckedListBox cklSell;
        private System.Windows.Forms.CheckedListBox cklShop;
        private System.Windows.Forms.CheckedListBox ckLinfo;
        private System.Windows.Forms.CheckBox ckMange;
        private System.Windows.Forms.CheckBox ckSell;
        private System.Windows.Forms.CheckBox ckShop;
        private System.Windows.Forms.CheckBox checkBox3;
        private System.Windows.Forms.CheckBox ckInfo;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}

