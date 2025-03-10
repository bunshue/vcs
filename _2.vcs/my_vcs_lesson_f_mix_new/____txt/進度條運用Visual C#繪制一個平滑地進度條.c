//運用Visual C#繪制一個平滑地進度條

　　本文描述了如何建立一個簡單的、自定義的用戶控件——一個平滑的進度條。

　　在早先的進度條控件版本中，例如在 Microsoft Windows Common Controls ActiveX 控件中提供的版本，您可以看到進度條有兩種不同的視圖。您可以通過設定 Scrolling 屬性來設定 Standard 視圖或是 Smooth 視圖。 Smooth 視圖提供了一個區域來平滑的顯示進度， Standard 試圖則看上去是由一個一個方塊來表示進度的。

　　在 Visual C# .NET 中提供的進度條控件只支持 Standard 視圖。

　　本文的代碼樣例揭示了如何建立一個有如下屬性的控件：

　　　Minimum。該屬性表示了進度條的最小值。默認情況下是 0 ；您不能將該屬性設為負值。

　　　Maximum。該屬性表示了進度條的最大值。默認情況下是 100 。

　　　Value。該屬性表示了進度條的當前值。該值必須介於 Minimum 和 Maximum 之間。

　　　ProgressBarColor。該屬性表示了進度條的顏色。



　　建立一個自定義的進度條控件

　　1、按著下面的步驟，在 Visual C# .NET 中建立一個 Windows Control Library 項目：

　　a、打開 Microsoft Visual Studio .NET。

　　b、點擊 File 菜單，點擊 New ，再點擊 Project 。

　　c、在 New Project 對話框中，在 Project Types 中選擇 Visual C# Projects，然後在 Templates 中選擇 Windows Control Library 。

　　d、在 Name 框中，填上 SmoothProgressBar ，並點擊 OK 。

　　e、在 Project Explorer 中，重命名缺省的 class module ，將 UserControl1.cs 改為 SmoothProgressBar.cs 。

　　f、在該 UserControl 對象的 Property 窗口中，將其 Name 屬性從 UserControl1 改為 SmoothProgressBar 。

　　2、此時，您已經從 control 類繼承了一個新類，並可以添加新的功能。但是，ProgressBar累是密封(sealed)的，不能再被繼承。因此，您必須從頭開始建立這個控件。

　　將下面的代碼添加到UserControl模塊中，就在“Windows Form Designer generated code”之後：

int min = 0; // Minimum value for progress range
int max = 100; // Maximum value for progress range
int val = 0; // Current progress
Color BarColor = Color.Blue; // Color of progress meter

protected override void OnResize(EventArgs e)
{
　// Invalidate the control to get a repaint.
　this.Invalidate();
}

protected override void OnPaint(PaintEventArgs e)
{
　Graphics g = e.Graphics;
　SolidBrush brush = new SolidBrush(BarColor);
　float percent = (float)(val - min) / (float)(max - min);
　Rectangle rect = this.ClientRectangle;

　// Calculate area for drawing the progress.
　rect.Width = (int)((float)rect.Width * percent);

　// Draw the progress meter.
　g.FillRectangle(brush, rect);

　// Draw a three-dimensional border around the control.
　Draw3DBorder(g);

　// Clean up.
　brush.Dispose();
　g.Dispose();
}

public int Minimum
{
　get
　{
　　return min;
　}

　set
　{
　　// Prevent a negative value.
　　if (value < 0)
　　{
　　　min = 0;
　　}

　　// Make sure that the minimum value is never set higher than the maximum value.
　　if (value > max)
　　{
　　　min = value;
　　　min = value;
　　}

　　// Ensure value is still in range
　　if (val < min)
　　{
　　　val = min;
　　}

　　// Invalidate the control to get a repaint.
　　this.Invalidate();
　}
}

public int Maximum
{
　get
　{
　　return max;
　}

　set
　{
　　// Make sure that the maximum value is never set lower than the minimum value.
　　if (value < min)
　　{
　　　min = value;
　　}

　　max = value;

　　// Make sure that value is still in range.
　　if (val > max)
　　{
　　　val = max;
　　}

　　// Invalidate the control to get a repaint.
　　this.Invalidate();
　}
}

public int Value
{
　get
　{
　　return val;
　}

　set
　{
　　int oldValue = val;

　　// Make sure that the value does not stray outside the valid range.
　　if (value < min)
　　{
　　　val = min;
　　}
　　else if (value > max)
　　{
　　　val = max;
　　}
　　else
　　{
　　　val = value;
　　}

　　// Invalidate only the changed area.
　　float percent;

　　Rectangle newValueRect = this.ClientRectangle;
　　Rectangle oldValueRect = this.ClientRectangle;

　　// Use a new value to calculate the rectangle for progress.
　　percent = (float)(val - min) / (float)(max - min);
　　newValueRect.Width = (int)((float)newValueRect.Width * percent);

　　// Use an old value to calculate the rectangle for progress.
　　percent = (float)(oldValue - min) / (float)(max - min);
　　oldValueRect.Width = (int)((float)oldValueRect.Width * percent);

　　Rectangle updateRect = new Rectangle();

　　// Find only the part of the screen that must be updated.
　　if (newValueRect.Width > oldValueRect.Width)
　　{
　　　updateRect.X = oldValueRect.Size.Width;
　　　updateRect.Width = newValueRect.Width - oldValueRect.Width;
　　}
　　else
　　{
　　　updateRect.X = newValueRect.Size.Width;
　　　updateRect.Width = oldValueRect.Width - newValueRect.Width;
　　}

　　updateRect.Height = this.Height;

　　// Invalidate the intersection region only.
　　this.Invalidate(updateRect);
　}
}

public Color ProgressBarColor
{
　get
　{
　　return BarColor;
　}

　set
　{
　　BarColor = value;

　　// Invalidate the control to get a repaint.
　　this.Invalidate();
　}
}

private void Draw3DBorder(Graphics g)
{
　int PenWidth = (int)Pens.White.Width;

　g.DrawLine(Pens.DarkGray, new Point(this.ClientRectangle.Left, this.ClientRectangle.Top),
new Point(this.ClientRectangle.Width - PenWidth, this.ClientRectangle.Top));
　g.DrawLine(Pens.DarkGray, new Point(this.ClientRectangle.Left, this.ClientRectangle.Top), new Point(this.ClientRectangle.Left, this.ClientRectangle.Height - PenWidth));
　g.DrawLine(Pens.White, new Point(this.ClientRectangle.Left, this.ClientRectangle.Height - PenWidth),
new Point(this.ClientRectangle.Width - PenWidth, this.ClientRectangle.Height - PenWidth));
g.DrawLine(Pens.White, new Point(this.ClientRectangle.Width - PenWidth, this.ClientRectangle.Top),
new Point(this.ClientRectangle.Width - PenWidth, this.ClientRectangle.Height - PenWidth));
}

　　3、在 Build 菜單中，點擊 Build Solution 來編譯整個項目。

　　建立一個簡單的客戶端應用

　　1、在 File 菜單中，點擊 New ，再點擊Project。

　　2、在 Add New Project 對話框中，在 Project Types 中點擊 Visual C# Projects，在 Templates 中點擊 Windows Application，並點擊 OK。

　　3、按照下面的步驟，在 Form 上添加兩個 SmoothProgressBar 實例：

　　a、在 Tools 菜單上，點擊 Customize Toolbox。

　　b、點擊 .NET Framework Components 頁。

　　c、點擊 Browse，然後選中你在 Create a Custom ProgressBar Control 段中建立的 SmoothProgressBar.dll 文件。

　　d、點擊 OK。您可以看到在 toolbox 中已經有 SmoothProgressBar 控件了。

　　e、從 toolbox 中拖兩個 SmoothProgressBar 控件的實例到該 Windows Application 項目中的默認 form 上。

　　4、從 toolbox 頁中拖一個 Timer 控件到 form 上。

　　5、將下面的代碼添加到 Timer 控件的 Tick 事件中：

if (this.smoothProgressBar1.Value > 0)
{
　this.smoothProgressBar1.Value--;
　this.smoothProgressBar2.Value++;
}
else
{
　this.timer1.Enabled = false;
}
　　6、從 toolbox 頁中拖一個 Button 控件到 form 上。

　　7、將下面的代碼添加到 Button 控件的 Click 事件中：

this.smoothProgressBar1.Value = 100;
this.smoothProgressBar2.Value = 0;

this.timer1.Interval = 1;
this.timer1.Enabled = true;
　　8、在 Debug 菜單中，點擊 Start 來運行樣例項目。

　　9、點擊Button。注意觀察那兩個進度指示器。一個逐漸減小，另一個逐漸增加。







