namespace vcs_TreeView1
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
            System.Windows.Forms.TreeNode treeNode1 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode2 = new System.Windows.Forms.TreeNode("Documents");
            System.Windows.Forms.TreeNode treeNode3 = new System.Windows.Forms.TreeNode("Environment", new System.Windows.Forms.TreeNode[] {
            treeNode1,
            treeNode2});
            System.Windows.Forms.TreeNode treeNode4 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode5 = new System.Windows.Forms.TreeNode("Defaults");
            System.Windows.Forms.TreeNode treeNode6 = new System.Windows.Forms.TreeNode("Projects", new System.Windows.Forms.TreeNode[] {
            treeNode4,
            treeNode5});
            System.Windows.Forms.TreeNode treeNode7 = new System.Windows.Forms.TreeNode("All Languages");
            System.Windows.Forms.TreeNode treeNode8 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode9 = new System.Windows.Forms.TreeNode("Tabs");
            System.Windows.Forms.TreeNode treeNode10 = new System.Windows.Forms.TreeNode("Advanced");
            System.Windows.Forms.TreeNode treeNode11 = new System.Windows.Forms.TreeNode("C#", new System.Windows.Forms.TreeNode[] {
            treeNode8,
            treeNode9,
            treeNode10});
            System.Windows.Forms.TreeNode treeNode12 = new System.Windows.Forms.TreeNode("General");
            System.Windows.Forms.TreeNode treeNode13 = new System.Windows.Forms.TreeNode("Tabs");
            System.Windows.Forms.TreeNode treeNode14 = new System.Windows.Forms.TreeNode("Advanced");
            System.Windows.Forms.TreeNode treeNode15 = new System.Windows.Forms.TreeNode("Visual Basic", new System.Windows.Forms.TreeNode[] {
            treeNode12,
            treeNode13,
            treeNode14});
            System.Windows.Forms.TreeNode treeNode16 = new System.Windows.Forms.TreeNode("Text Editor", new System.Windows.Forms.TreeNode[] {
            treeNode7,
            treeNode11,
            treeNode15});
            this.bt_clear = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button0 = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.treeView3 = new System.Windows.Forms.TreeView();
            this.treeView4 = new System.Windows.Forms.TreeView();
            this.treeView5 = new System.Windows.Forms.TreeView();
            this.treeView0 = new System.Windows.Forms.TreeView();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.treeView2 = new System.Windows.Forms.TreeView();
            this.label0 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.treeView6 = new System.Windows.Forms.TreeView();
            this.treeView7 = new System.Windows.Forms.TreeView();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // bt_clear
            // 
            this.bt_clear.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_clear.Location = new System.Drawing.Point(704, 264);
            this.bt_clear.Name = "bt_clear";
            this.bt_clear.Size = new System.Drawing.Size(66, 40);
            this.bt_clear.TabIndex = 140;
            this.bt_clear.Text = "Clear";
            this.bt_clear.UseVisualStyleBackColor = true;
            this.bt_clear.Click += new System.EventHandler(this.bt_clear_Click);
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(636, 168);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(150, 150);
            this.richTextBox1.TabIndex = 141;
            this.richTextBox1.Text = "";
            // 
            // button0
            // 
            this.button0.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button0.Location = new System.Drawing.Point(646, 12);
            this.button0.Name = "button0";
            this.button0.Size = new System.Drawing.Size(140, 60);
            this.button0.TabIndex = 149;
            this.button0.Text = "全部摺疊";
            this.button0.UseVisualStyleBackColor = true;
            this.button0.Click += new System.EventHandler(this.button0_Click);
            // 
            // button1
            // 
            this.button1.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.button1.Location = new System.Drawing.Point(646, 74);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(140, 60);
            this.button1.TabIndex = 147;
            this.button1.Text = "全部展開";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // treeView1
            // 
            this.treeView1.Location = new System.Drawing.Point(12, 168);
            this.treeView1.Name = "treeView1";
            this.treeView1.Size = new System.Drawing.Size(150, 150);
            this.treeView1.TabIndex = 152;
            // 
            // treeView3
            // 
            this.treeView3.Location = new System.Drawing.Point(168, 168);
            this.treeView3.Name = "treeView3";
            this.treeView3.Size = new System.Drawing.Size(150, 150);
            this.treeView3.TabIndex = 154;
            // 
            // treeView4
            // 
            this.treeView4.Location = new System.Drawing.Point(324, 12);
            this.treeView4.Name = "treeView4";
            this.treeView4.Size = new System.Drawing.Size(150, 150);
            this.treeView4.TabIndex = 155;
            // 
            // treeView5
            // 
            this.treeView5.Location = new System.Drawing.Point(324, 168);
            this.treeView5.Name = "treeView5";
            this.treeView5.Size = new System.Drawing.Size(150, 150);
            this.treeView5.TabIndex = 156;
            // 
            // treeView0
            // 
            this.treeView0.Location = new System.Drawing.Point(12, 12);
            this.treeView0.Name = "treeView0";
            this.treeView0.Size = new System.Drawing.Size(150, 150);
            this.treeView0.TabIndex = 157;
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "open.png");
            this.imageList1.Images.SetKeyName(1, "text.png");
            // 
            // treeView2
            // 
            this.treeView2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.treeView2.Location = new System.Drawing.Point(168, 12);
            this.treeView2.Name = "treeView2";
            treeNode1.Name = "Node1";
            treeNode1.Tag = "0";
            treeNode1.Text = "General";
            treeNode2.Name = "Node2";
            treeNode2.Tag = "1";
            treeNode2.Text = "Documents";
            treeNode3.Name = "Node0";
            treeNode3.Tag = "0";
            treeNode3.Text = "Environment";
            treeNode4.Name = "Node5";
            treeNode4.Tag = "2";
            treeNode4.Text = "General";
            treeNode5.Name = "Node6";
            treeNode5.Tag = "3";
            treeNode5.Text = "Defaults";
            treeNode6.Name = "Node4";
            treeNode6.Tag = "2";
            treeNode6.Text = "Projects";
            treeNode7.Name = "Node8";
            treeNode7.Tag = "4";
            treeNode7.Text = "All Languages";
            treeNode8.Name = "Node12";
            treeNode8.Tag = "5";
            treeNode8.Text = "General";
            treeNode9.Name = "Node13";
            treeNode9.Tag = "6";
            treeNode9.Text = "Tabs";
            treeNode10.Name = "Node14";
            treeNode10.Tag = "7";
            treeNode10.Text = "Advanced";
            treeNode11.Name = "Node9";
            treeNode11.Tag = "5";
            treeNode11.Text = "C#";
            treeNode12.Name = "Node15";
            treeNode12.Tag = "8";
            treeNode12.Text = "General";
            treeNode13.Name = "Node16";
            treeNode13.Tag = "9";
            treeNode13.Text = "Tabs";
            treeNode14.Name = "Node17";
            treeNode14.Tag = "10";
            treeNode14.Text = "Advanced";
            treeNode15.Name = "Node11";
            treeNode15.Tag = "8";
            treeNode15.Text = "Visual Basic";
            treeNode16.Name = "Node7";
            treeNode16.Tag = "4";
            treeNode16.Text = "Text Editor";
            this.treeView2.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode3,
            treeNode6,
            treeNode16});
            this.treeView2.Size = new System.Drawing.Size(150, 150);
            this.treeView2.TabIndex = 158;
            // 
            // label0
            // 
            this.label0.AutoSize = true;
            this.label0.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label0.Location = new System.Drawing.Point(12, 331);
            this.label0.Name = "label0";
            this.label0.Size = new System.Drawing.Size(64, 24);
            this.label0.TabIndex = 159;
            this.label0.Text = "label0";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(12, 362);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(64, 24);
            this.label1.TabIndex = 160;
            this.label1.Text = "label1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label2.Location = new System.Drawing.Point(82, 331);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(64, 24);
            this.label2.TabIndex = 161;
            this.label2.Text = "label2";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label3.Location = new System.Drawing.Point(82, 362);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(64, 24);
            this.label3.TabIndex = 162;
            this.label3.Text = "label3";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label4.Location = new System.Drawing.Point(152, 331);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(64, 24);
            this.label4.TabIndex = 163;
            this.label4.Text = "label4";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(152, 362);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(64, 24);
            this.label5.TabIndex = 164;
            this.label5.Text = "label5";
            // 
            // treeView6
            // 
            this.treeView6.Location = new System.Drawing.Point(480, 12);
            this.treeView6.Name = "treeView6";
            this.treeView6.Size = new System.Drawing.Size(150, 150);
            this.treeView6.TabIndex = 165;
            // 
            // treeView7
            // 
            this.treeView7.Location = new System.Drawing.Point(480, 168);
            this.treeView7.Name = "treeView7";
            this.treeView7.Size = new System.Drawing.Size(150, 150);
            this.treeView7.TabIndex = 166;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label6.Location = new System.Drawing.Point(222, 331);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(64, 24);
            this.label6.TabIndex = 167;
            this.label6.Text = "label6";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label7.Location = new System.Drawing.Point(222, 360);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(64, 24);
            this.label7.TabIndex = 168;
            this.label7.Text = "label7";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(817, 401);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.treeView7);
            this.Controls.Add(this.treeView6);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label0);
            this.Controls.Add(this.treeView2);
            this.Controls.Add(this.treeView0);
            this.Controls.Add(this.treeView5);
            this.Controls.Add(this.treeView4);
            this.Controls.Add(this.treeView3);
            this.Controls.Add(this.treeView1);
            this.Controls.Add(this.button0);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.bt_clear);
            this.Controls.Add(this.richTextBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button bt_clear;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button0;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.TreeView treeView3;
        private System.Windows.Forms.TreeView treeView4;
        private System.Windows.Forms.TreeView treeView5;
        private System.Windows.Forms.TreeView treeView0;
        private System.Windows.Forms.ImageList imageList1;
        private System.Windows.Forms.TreeView treeView2;
        private System.Windows.Forms.Label label0;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TreeView treeView6;
        private System.Windows.Forms.TreeView treeView7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
    }
}

