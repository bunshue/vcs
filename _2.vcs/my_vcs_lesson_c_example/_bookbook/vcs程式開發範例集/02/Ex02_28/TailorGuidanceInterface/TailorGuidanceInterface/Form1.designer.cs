namespace TailorGuidanceInterface
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
            System.Windows.Forms.TreeNode treeNode1 = new System.Windows.Forms.TreeNode("公司信息", 1, 2);
            System.Windows.Forms.TreeNode treeNode2 = new System.Windows.Forms.TreeNode("初始化數據", 1, 2);
            System.Windows.Forms.TreeNode treeNode3 = new System.Windows.Forms.TreeNode("管理員設定", 1, 2);
            System.Windows.Forms.TreeNode treeNode4 = new System.Windows.Forms.TreeNode("系統管理", new System.Windows.Forms.TreeNode[] {
            treeNode1,
            treeNode2,
            treeNode3});
            System.Windows.Forms.TreeNode treeNode5 = new System.Windows.Forms.TreeNode("添加科目信息", 1, 2);
            System.Windows.Forms.TreeNode treeNode6 = new System.Windows.Forms.TreeNode("查詢科目信息", 1, 2);
            System.Windows.Forms.TreeNode treeNode7 = new System.Windows.Forms.TreeNode("科目信息", 0, 1, new System.Windows.Forms.TreeNode[] {
            treeNode5,
            treeNode6});
            System.Windows.Forms.TreeNode treeNode8 = new System.Windows.Forms.TreeNode("總帳查詢", 1, 2);
            System.Windows.Forms.TreeNode treeNode9 = new System.Windows.Forms.TreeNode("按憑證查詢", 1, 2);
            System.Windows.Forms.TreeNode treeNode10 = new System.Windows.Forms.TreeNode("按科目查詢", 1, 2);
            System.Windows.Forms.TreeNode treeNode11 = new System.Windows.Forms.TreeNode("帳目佘額查詢", 1, 2);
            System.Windows.Forms.TreeNode treeNode12 = new System.Windows.Forms.TreeNode("帳目查詢", 0, 1, new System.Windows.Forms.TreeNode[] {
            treeNode8,
            treeNode9,
            treeNode10,
            treeNode11});
            System.Windows.Forms.TreeNode treeNode13 = new System.Windows.Forms.TreeNode("憑證錄入", 1, 2);
            System.Windows.Forms.TreeNode treeNode14 = new System.Windows.Forms.TreeNode("憑證審核", 1, 2);
            System.Windows.Forms.TreeNode treeNode15 = new System.Windows.Forms.TreeNode("憑證查詢", 1, 2);
            System.Windows.Forms.TreeNode treeNode16 = new System.Windows.Forms.TreeNode("憑證結算", 1, 2);
            System.Windows.Forms.TreeNode treeNode17 = new System.Windows.Forms.TreeNode("憑證管理", 0, 1, new System.Windows.Forms.TreeNode[] {
            treeNode13,
            treeNode14,
            treeNode15,
            treeNode16});
            System.Windows.Forms.TreeNode treeNode18 = new System.Windows.Forms.TreeNode("按憑證打印", 1, 2);
            System.Windows.Forms.TreeNode treeNode19 = new System.Windows.Forms.TreeNode("按科目打印", 1, 2);
            System.Windows.Forms.TreeNode treeNode20 = new System.Windows.Forms.TreeNode("報表打印", 0, 1, new System.Windows.Forms.TreeNode[] {
            treeNode18,
            treeNode19});
            System.Windows.Forms.TreeNode treeNode21 = new System.Windows.Forms.TreeNode("資源管理", 2, 1, new System.Windows.Forms.TreeNode[] {
            treeNode4,
            treeNode7,
            treeNode12,
            treeNode17,
            treeNode20});
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.statusStrip1 = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel2 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel3 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel4 = new System.Windows.Forms.ToolStripStatusLabel();
            this.憑證錄入ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.憑證管理ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.憑證審核ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.憑證結算ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.憑證總匯ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.憑證ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.憑證修改ToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.密碼修改ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.管理理員信息ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.系統管理ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.公司信息ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.初始化使用時間ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.初始化科目資金ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.報表ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.按科目報表ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.按憑證ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.賬目佘額ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.按科目查詢ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.退出ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.按憑證查詢ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.添加科目ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.科目信息ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.科目查詢ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.總賬遊覽ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.賬目查詢ToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip2 = new System.Windows.Forms.MenuStrip();
            this.treeView1 = new System.Windows.Forms.TreeView();
            this.imageList1 = new System.Windows.Forms.ImageList(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.statusStrip1.SuspendLayout();
            this.menuStrip2.SuspendLayout();
            this.SuspendLayout();
            // 
            // statusStrip1
            // 
            this.statusStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1,
            this.toolStripStatusLabel2,
            this.toolStripStatusLabel3,
            this.toolStripStatusLabel4});
            this.statusStrip1.Location = new System.Drawing.Point(0, 204);
            this.statusStrip1.Name = "statusStrip1";
            this.statusStrip1.Size = new System.Drawing.Size(474, 22);
            this.statusStrip1.TabIndex = 0;
            this.statusStrip1.Text = "statusStrip1";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            this.toolStripStatusLabel1.Size = new System.Drawing.Size(41, 17);
            this.toolStripStatusLabel1.Text = "狀態：";
            // 
            // toolStripStatusLabel2
            // 
            this.toolStripStatusLabel2.BorderStyle = System.Windows.Forms.Border3DStyle.RaisedOuter;
            this.toolStripStatusLabel2.Name = "toolStripStatusLabel2";
            this.toolStripStatusLabel2.Size = new System.Drawing.Size(47, 17);
            this.toolStripStatusLabel2.Text = "       ";
            // 
            // toolStripStatusLabel3
            // 
            this.toolStripStatusLabel3.BorderStyle = System.Windows.Forms.Border3DStyle.SunkenOuter;
            this.toolStripStatusLabel3.Name = "toolStripStatusLabel3";
            this.toolStripStatusLabel3.Size = new System.Drawing.Size(83, 17);
            this.toolStripStatusLabel3.Text = "操作員：Admin";
            // 
            // toolStripStatusLabel4
            // 
            this.toolStripStatusLabel4.Name = "toolStripStatusLabel4";
            this.toolStripStatusLabel4.Size = new System.Drawing.Size(77, 17);
            this.toolStripStatusLabel4.Text = "  系統時間：";
            // 
            // 憑證錄入ToolStripMenuItem
            // 
            this.憑證錄入ToolStripMenuItem.Name = "憑證錄入ToolStripMenuItem";
            this.憑證錄入ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.憑證錄入ToolStripMenuItem.Text = "憑證錄入";
            // 
            // 憑證管理ToolStripMenuItem
            // 
            this.憑證管理ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.憑證錄入ToolStripMenuItem,
            this.憑證審核ToolStripMenuItem,
            this.憑證結算ToolStripMenuItem,
            this.憑證總匯ToolStripMenuItem,
            this.憑證ToolStripMenuItem,
            this.憑證修改ToolStripMenuItem1});
            this.憑證管理ToolStripMenuItem.Name = "憑證管理ToolStripMenuItem";
            this.憑證管理ToolStripMenuItem.Size = new System.Drawing.Size(83, 20);
            this.憑證管理ToolStripMenuItem.Text = "憑證管理(&F)";
            // 
            // 憑證審核ToolStripMenuItem
            // 
            this.憑證審核ToolStripMenuItem.Name = "憑證審核ToolStripMenuItem";
            this.憑證審核ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.憑證審核ToolStripMenuItem.Text = "憑證審核";
            // 
            // 憑證結算ToolStripMenuItem
            // 
            this.憑證結算ToolStripMenuItem.Name = "憑證結算ToolStripMenuItem";
            this.憑證結算ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.憑證結算ToolStripMenuItem.Text = "憑證結算";
            // 
            // 憑證總匯ToolStripMenuItem
            // 
            this.憑證總匯ToolStripMenuItem.Name = "憑證總匯ToolStripMenuItem";
            this.憑證總匯ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.憑證總匯ToolStripMenuItem.Text = "憑證總匯";
            // 
            // 憑證ToolStripMenuItem
            // 
            this.憑證ToolStripMenuItem.Name = "憑證ToolStripMenuItem";
            this.憑證ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.憑證ToolStripMenuItem.Text = "憑證查詢";
            // 
            // 憑證修改ToolStripMenuItem1
            // 
            this.憑證修改ToolStripMenuItem1.Name = "憑證修改ToolStripMenuItem1";
            this.憑證修改ToolStripMenuItem1.Size = new System.Drawing.Size(118, 22);
            this.憑證修改ToolStripMenuItem1.Text = "憑證修改";
            // 
            // 密碼修改ToolStripMenuItem
            // 
            this.密碼修改ToolStripMenuItem.Name = "密碼修改ToolStripMenuItem";
            this.密碼修改ToolStripMenuItem.Size = new System.Drawing.Size(172, 22);
            this.密碼修改ToolStripMenuItem.Text = "密碼修改(&B)";
            // 
            // 管理理員信息ToolStripMenuItem
            // 
            this.管理理員信息ToolStripMenuItem.Name = "管理理員信息ToolStripMenuItem";
            this.管理理員信息ToolStripMenuItem.Size = new System.Drawing.Size(172, 22);
            this.管理理員信息ToolStripMenuItem.Text = "管理員信息(&W)";
            // 
            // 系統管理ToolStripMenuItem
            // 
            this.系統管理ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.公司信息ToolStripMenuItem,
            this.初始化使用時間ToolStripMenuItem,
            this.初始化科目資金ToolStripMenuItem,
            this.管理理員信息ToolStripMenuItem,
            this.密碼修改ToolStripMenuItem});
            this.系統管理ToolStripMenuItem.Name = "系統管理ToolStripMenuItem";
            this.系統管理ToolStripMenuItem.Size = new System.Drawing.Size(83, 20);
            this.系統管理ToolStripMenuItem.Text = "系統管理(&D)";
            // 
            // 公司信息ToolStripMenuItem
            // 
            this.公司信息ToolStripMenuItem.Name = "公司信息ToolStripMenuItem";
            this.公司信息ToolStripMenuItem.Size = new System.Drawing.Size(172, 22);
            this.公司信息ToolStripMenuItem.Text = "公司信息(&L)";
            // 
            // 初始化使用時間ToolStripMenuItem
            // 
            this.初始化使用時間ToolStripMenuItem.Name = "初始化使用時間ToolStripMenuItem";
            this.初始化使用時間ToolStripMenuItem.Size = new System.Drawing.Size(172, 22);
            this.初始化使用時間ToolStripMenuItem.Text = "初始化使用時間(&G)";
            // 
            // 初始化科目資金ToolStripMenuItem
            // 
            this.初始化科目資金ToolStripMenuItem.Name = "初始化科目資金ToolStripMenuItem";
            this.初始化科目資金ToolStripMenuItem.Size = new System.Drawing.Size(172, 22);
            this.初始化科目資金ToolStripMenuItem.Text = "初始化科目資金(&F)";
            // 
            // 報表ToolStripMenuItem
            // 
            this.報表ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.按科目報表ToolStripMenuItem,
            this.按憑證ToolStripMenuItem});
            this.報表ToolStripMenuItem.Name = "報表ToolStripMenuItem";
            this.報表ToolStripMenuItem.Size = new System.Drawing.Size(59, 20);
            this.報表ToolStripMenuItem.Text = "報表(&H)";
            // 
            // 按科目報表ToolStripMenuItem
            // 
            this.按科目報表ToolStripMenuItem.Name = "按科目報表ToolStripMenuItem";
            this.按科目報表ToolStripMenuItem.Size = new System.Drawing.Size(154, 22);
            this.按科目報表ToolStripMenuItem.Text = "按科目名稱報表";
            // 
            // 按憑證ToolStripMenuItem
            // 
            this.按憑證ToolStripMenuItem.Name = "按憑證ToolStripMenuItem";
            this.按憑證ToolStripMenuItem.Size = new System.Drawing.Size(154, 22);
            this.按憑證ToolStripMenuItem.Text = "按憑證號報表";
            // 
            // 賬目佘額ToolStripMenuItem
            // 
            this.賬目佘額ToolStripMenuItem.Name = "賬目佘額ToolStripMenuItem";
            this.賬目佘額ToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.賬目佘額ToolStripMenuItem.Text = "賬目餘額";
            // 
            // 按科目查詢ToolStripMenuItem
            // 
            this.按科目查詢ToolStripMenuItem.Name = "按科目查詢ToolStripMenuItem";
            this.按科目查詢ToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.按科目查詢ToolStripMenuItem.Text = "按科目查詢";
            // 
            // 退出ToolStripMenuItem
            // 
            this.退出ToolStripMenuItem.Name = "退出ToolStripMenuItem";
            this.退出ToolStripMenuItem.Size = new System.Drawing.Size(59, 20);
            this.退出ToolStripMenuItem.Text = "退出(&E)";
            // 
            // 按憑證查詢ToolStripMenuItem
            // 
            this.按憑證查詢ToolStripMenuItem.Name = "按憑證查詢ToolStripMenuItem";
            this.按憑證查詢ToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.按憑證查詢ToolStripMenuItem.Text = "按憑證查詢";
            // 
            // 添加科目ToolStripMenuItem
            // 
            this.添加科目ToolStripMenuItem.Name = "添加科目ToolStripMenuItem";
            this.添加科目ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.添加科目ToolStripMenuItem.Text = "科目信息";
            // 
            // 科目信息ToolStripMenuItem
            // 
            this.科目信息ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.添加科目ToolStripMenuItem,
            this.科目查詢ToolStripMenuItem});
            this.科目信息ToolStripMenuItem.Name = "科目信息ToolStripMenuItem";
            this.科目信息ToolStripMenuItem.Size = new System.Drawing.Size(83, 20);
            this.科目信息ToolStripMenuItem.Text = "科目信息(&T)";
            // 
            // 科目查詢ToolStripMenuItem
            // 
            this.科目查詢ToolStripMenuItem.Name = "科目查詢ToolStripMenuItem";
            this.科目查詢ToolStripMenuItem.Size = new System.Drawing.Size(118, 22);
            this.科目查詢ToolStripMenuItem.Text = "科目查詢";
            // 
            // 總賬遊覽ToolStripMenuItem
            // 
            this.總賬遊覽ToolStripMenuItem.Name = "總賬遊覽ToolStripMenuItem";
            this.總賬遊覽ToolStripMenuItem.Size = new System.Drawing.Size(130, 22);
            this.總賬遊覽ToolStripMenuItem.Text = "總賬瀏覽";
            // 
            // 賬目查詢ToolStripMenuItem
            // 
            this.賬目查詢ToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.總賬遊覽ToolStripMenuItem,
            this.按憑證查詢ToolStripMenuItem,
            this.按科目查詢ToolStripMenuItem,
            this.賬目佘額ToolStripMenuItem});
            this.賬目查詢ToolStripMenuItem.Name = "賬目查詢ToolStripMenuItem";
            this.賬目查詢ToolStripMenuItem.Size = new System.Drawing.Size(83, 20);
            this.賬目查詢ToolStripMenuItem.Text = "賬目查詢(&Q)";
            // 
            // menuStrip2
            // 
            this.menuStrip2.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.系統管理ToolStripMenuItem,
            this.憑證管理ToolStripMenuItem,
            this.科目信息ToolStripMenuItem,
            this.賬目查詢ToolStripMenuItem,
            this.報表ToolStripMenuItem,
            this.退出ToolStripMenuItem});
            this.menuStrip2.Location = new System.Drawing.Point(0, 0);
            this.menuStrip2.Name = "menuStrip2";
            this.menuStrip2.Size = new System.Drawing.Size(474, 24);
            this.menuStrip2.TabIndex = 7;
            this.menuStrip2.Text = "menuStrip2";
            // 
            // treeView1
            // 
            this.treeView1.ForeColor = System.Drawing.Color.Blue;
            this.treeView1.ImageIndex = 0;
            this.treeView1.ImageList = this.imageList1;
            this.treeView1.Location = new System.Drawing.Point(0, 27);
            this.treeView1.Name = "treeView1";
            treeNode1.ImageIndex = 1;
            treeNode1.Name = "節點9";
            treeNode1.SelectedImageIndex = 2;
            treeNode1.Text = "公司信息";
            treeNode2.ImageIndex = 1;
            treeNode2.Name = "節點10";
            treeNode2.SelectedImageIndex = 2;
            treeNode2.Text = "初始化數據";
            treeNode3.ImageIndex = 1;
            treeNode3.Name = "節點11";
            treeNode3.SelectedImageIndex = 2;
            treeNode3.Text = "管理員設定";
            treeNode4.ImageKey = "1.bmp";
            treeNode4.Name = "節點1";
            treeNode4.SelectedImageIndex = 1;
            treeNode4.Text = "系統管理";
            treeNode5.ImageIndex = 1;
            treeNode5.Name = "節點12";
            treeNode5.SelectedImageIndex = 2;
            treeNode5.Text = "添加科目信息";
            treeNode6.ImageIndex = 1;
            treeNode6.Name = "節點13";
            treeNode6.SelectedImageIndex = 2;
            treeNode6.Text = "查詢科目信息";
            treeNode7.ImageIndex = 0;
            treeNode7.Name = "節點4";
            treeNode7.SelectedImageIndex = 1;
            treeNode7.Text = "科目信息";
            treeNode8.ImageIndex = 1;
            treeNode8.Name = "節點14";
            treeNode8.SelectedImageIndex = 2;
            treeNode8.Text = "總帳查詢";
            treeNode9.ImageIndex = 1;
            treeNode9.Name = "節點15";
            treeNode9.SelectedImageIndex = 2;
            treeNode9.Text = "按憑證查詢";
            treeNode10.ImageIndex = 1;
            treeNode10.Name = "節點16";
            treeNode10.SelectedImageIndex = 2;
            treeNode10.Text = "按科目查詢";
            treeNode11.ImageIndex = 1;
            treeNode11.Name = "節點17";
            treeNode11.SelectedImageIndex = 2;
            treeNode11.Text = "帳目佘額查詢";
            treeNode12.ImageIndex = 0;
            treeNode12.Name = "節點6";
            treeNode12.SelectedImageIndex = 1;
            treeNode12.Text = "帳目查詢";
            treeNode13.ImageIndex = 1;
            treeNode13.Name = "節點18";
            treeNode13.SelectedImageIndex = 2;
            treeNode13.Text = "憑證錄入";
            treeNode14.ImageIndex = 1;
            treeNode14.Name = "節點19";
            treeNode14.SelectedImageIndex = 2;
            treeNode14.Text = "憑證審核";
            treeNode15.ImageIndex = 1;
            treeNode15.Name = "節點20";
            treeNode15.SelectedImageIndex = 2;
            treeNode15.Text = "憑證查詢";
            treeNode16.ImageIndex = 1;
            treeNode16.Name = "節點21";
            treeNode16.SelectedImageIndex = 2;
            treeNode16.Text = "憑證結算";
            treeNode17.ImageIndex = 0;
            treeNode17.Name = "節點5";
            treeNode17.SelectedImageIndex = 1;
            treeNode17.Text = "憑證管理";
            treeNode18.ImageIndex = 1;
            treeNode18.Name = "節點22";
            treeNode18.SelectedImageIndex = 2;
            treeNode18.Text = "按憑證打印";
            treeNode19.ImageIndex = 1;
            treeNode19.Name = "節點23";
            treeNode19.SelectedImageIndex = 2;
            treeNode19.Text = "按科目打印";
            treeNode20.ImageIndex = 0;
            treeNode20.Name = "節點8";
            treeNode20.SelectedImageIndex = 1;
            treeNode20.Text = "報表打印";
            treeNode21.ImageIndex = 2;
            treeNode21.Name = "節點0";
            treeNode21.SelectedImageIndex = 1;
            treeNode21.Text = "資源管理";
            this.treeView1.Nodes.AddRange(new System.Windows.Forms.TreeNode[] {
            treeNode21});
            this.treeView1.SelectedImageIndex = 0;
            this.treeView1.Size = new System.Drawing.Size(165, 175);
            this.treeView1.TabIndex = 8;
            this.treeView1.AfterSelect += new System.Windows.Forms.TreeViewEventHandler(this.treeView1_AfterSelect);
            // 
            // imageList1
            // 
            this.imageList1.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("imageList1.ImageStream")));
            this.imageList1.TransparentColor = System.Drawing.Color.Transparent;
            this.imageList1.Images.SetKeyName(0, "1.bmp");
            this.imageList1.Images.SetKeyName(1, "2.bmp");
            this.imageList1.Images.SetKeyName(2, "3.ico");
            // 
            // groupBox1
            // 
            this.groupBox1.BackgroundImage = global::TailorGuidanceInterface.Properties.Resources.c;
            this.groupBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.groupBox1.Location = new System.Drawing.Point(162, 27);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(312, 175);
            this.groupBox1.TabIndex = 9;
            this.groupBox1.TabStop = false;
            // 
            // timer1
            // 
            this.timer1.Enabled = true;
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(474, 226);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.treeView1);
            this.Controls.Add(this.menuStrip2);
            this.Controls.Add(this.statusStrip1);
            this.Name = "Form1";
            this.Text = "用TreeView控件製作導航界面";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.statusStrip1.ResumeLayout(false);
            this.statusStrip1.PerformLayout();
            this.menuStrip2.ResumeLayout(false);
            this.menuStrip2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.StatusStrip statusStrip1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel2;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel3;
        private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel4;
        private System.Windows.Forms.ToolStripMenuItem 憑證錄入ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 憑證管理ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 憑證審核ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 憑證結算ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 憑證總匯ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 憑證ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 憑證修改ToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem 密碼修改ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 管理理員信息ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 系統管理ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 公司信息ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 初始化使用時間ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 初始化科目資金ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 報表ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 按科目報表ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 按憑證ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 賬目佘額ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 按科目查詢ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 退出ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 按憑證查詢ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 添加科目ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 科目信息ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 科目查詢ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 總賬遊覽ToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem 賬目查詢ToolStripMenuItem;
        private System.Windows.Forms.MenuStrip menuStrip2;
        private System.Windows.Forms.TreeView treeView1;
        private System.Windows.Forms.ImageList imageList1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Timer timer1;
    }
}

