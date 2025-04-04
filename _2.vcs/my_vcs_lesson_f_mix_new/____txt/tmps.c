//C# WinForm窗口最小化到系統托盤2


1.設置WinForm窗體屬性showinTask=false
2.加notifyicon控件notifyIcon1，為控件notifyIcon1的屬性Icon添加一個icon圖標。
3.添加窗體最小化事件(首先需要添加事件引用)：


this.SizeChanged += new System.EventHandler(this.Form1_SizeChanged);
//上面一行是主窗體InitializeComponent()方法中需要添加的引用
private void Form1_SizeChanged(object sender, EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.Hide();
this.notifyIcon1.Visible=true;
}
}

4.添加點擊圖標事件(首先需要添加事件引用)：

private void notifyIcon1_Click(object sender, EventArgs e)
{
this.Visible = true;
this.WindowState = FormWindowState.Normal;
this.notifyIcon1.Visible = false;
}

5.可以給notifyIcon添加右鍵菜單：
主窗體中拖入一個ContextMenu控件NicontextMenu，點中控件，在上下文菜單中添加菜單，notifyIcon1的ContextMenu行為中選中NicontextMenu 作為上下文菜單。
代碼如下：

this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
this.NicontextMenu = new System.Windows.Forms.ContextMenu();
this.menuItem_Hide = new System.Windows.Forms.MenuItem();

this.menuItem_Show = new System.Windows.Forms.MenuItem();
this.menuItem_Aubot = new System.Windows.Forms.MenuItem();
this.menuItem_Exit = new System.Windows.Forms.MenuItem();
this.notifyIcon1.ContextMenu = this.NicontextMenu;
this.notifyIcon1.Icon = ((System.Drawing.Icon)(resources.GetObject( "NotifyIcon.Icon ")));
this.notifyIcon1.Text = " ";
this.notifyIcon1.Visible = true;
this.notifyIcon1.DoubleClick += new System.EventHandler(this.notifyIcon1_DoubleClick);
this.notifyIcon1.Click += new System.EventHandler(this.notifyIcon1_Click);
this.NicontextMenu.MenuItems.AddRange(
new System.Windows.Forms.MenuItem[]
{
this.menuItem_Hide,
this.menuItem_Show,
this.menuItem_Aubot,
this.menuItem_Exit
}
);
//
// menuItem_Hide
//
this.menuItem_Hide.Index = 0;
this.menuItem_Hide.Text = "隱藏 ";
this.menuItem_Hide.Click += new System.EventHandler(this.menuItem_Hide_Click);
//
// menuItem_Show
//
this.menuItem_Show.Index = 1;
this.menuItem_Show.Text = "顯示 ";
this.menuItem_Show.Click += new System.EventHandler(this.menuItem_Show_Click);
//
// menuItem_Aubot
//
this.menuItem_Aubot.Index = 2;
this.menuItem_Aubot.Text = "關於 ";
this.menuItem_Aubot.Click += new System.EventHandler(this.menuItem_Aubot_Click);
//
// menuItem_Exit
//
this.menuItem_Exit.Index = 3;
this.menuItem_Exit.Text = "退出 ";
this.menuItem_Exit.Click += new System.EventHandler(this.menuItem_Exit_Click);
protected override void OnClosing(CancelEventArgs e)
{
this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
protected override void OnClosing(CancelEventArgs e)
{
//this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
private void CloseCtiServer()
{
timer.Enabled = false;
DJ160API.DisableCard();
this.NotifyIcon.Visible = false;
this.Close();
this.Dispose();
Application.Exit();
}
private void HideCtiServer()
{
this.Hide();
}
private void ShowCtiServer()
{
this.Show();
this.WindowState = FormWindowState.Normal;
this.Activate();
}
private void CtiManiForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Show_Click(object sender, System.EventArgs e)
{
this.ShowCtiServer();
}
private void menuItem_Aubot_Click(object sender, System.EventArgs e)
{
}
private void menuItem_Exit_Click(object sender, System.EventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Hide_Click(object sender, System.EventArgs e)
{
this.HideCtiServer();
}
private void CtiManiForm_SizeChanged(object sender, System.EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.HideCtiServer();
}
}
private void notifyIcon1_DoubleClick(object sender,System.EventArgs e)
{
this.ShowCtiServer();
}



