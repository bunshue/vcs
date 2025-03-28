//C#中加強ListView控件的功能


首先是實現ListView控件的自定義排序,訂閱ListVIEw控件的ColumnClick事件
private void listView1_ColumnClick(object sender, ColumnClickEventArgs e)
{
    if (this.listView1.Columns[e.Column].Tag == null)
        this.listView1.Columns[e.Column].Tag = true;
    bool tabK = (bool)this.listView1.Columns[e.Column].Tag;
    if (tabK)
        this.listView1.Columns[e.Column].Tag = false;
    else
        this.listView1.Columns[e.Column].Tag = true;
    this.listView1.ListViewItemSorter = new ListViewSort(e.Column, this.listView1.Columns[e.Column].Tag);
    //指定排序器並傳送列索引與升序降序關鍵字
    this.listView1.Sort();//對列表進行自定義排序
}

 
排序類的定義:

 1/**////
 2///自定義ListVIEw控件排序函數
 3///
 4class ListVIEwSort : IComparer
 5{
 6    private int col;
 7    private bool descK;
 8
 9   public ListVIEwSort()
10    {
11        col = 0;
12    }
13    public ListVIEwSort(int column, object Desc)
14    {
15        descK = (bool)Desc;
16        col = column; //當前列,0,1,2...,參數由ListVIEw控件的ColumnClick事件傳遞
17    }
18    public int Compare(object x, object y)
19    {
20        int tempInt = String.Compare(((ListViewItem)x).SubItems[col].Text, ((ListVIEwItem)y).SubItems[col].Text);
21        if (descK) return -tempInt;
22        else return tempInt;
23    }
24}
 
上面的ListView控件的自定義排列，即單擊ListVIEw控件的標題時進行排序
下面將實現ListVIEw控件的最後一列的去除,即自動調整合適的大小
首先寫一個調整ListVIEw控件列寬的函數


1/**////
2///自動調整listVIEw控件最後一列的列寬
3///
4private void 調整LV列寬()
5{
6    listView1.ColumnWidthChanged -= new ColumnWidthChangedEventHandler(listView1_ColumnWidthChanged);
7    備注.AutoResize(ColumnHeaderAutoResizeStyle.HeaderSize);
8    listView1.ColumnWidthChanged += new ColumnWidthChangedEventHandler(listView1_ColumnWidthChanged);
9}
 
上面的備注列是listview控件的最後一列的名稱，而listview控件的實例名為listView1
然後訂閱ListVIEw控件的ColumnWidthChanged事件，即列寬改變時自動調整列寬


1/**////
2/// listvIEw列寬改變事件函數
3///
4void listView1_ColumnWidthChanged(object sender, ColumnWidthChangedEventArgs e)
5{
6    調整LV列寬();
7}
 
再訂閱ListVIEw控件的Size_Change事件，即窗口大小被改變時調整列寬


1void listView1_SizeChanged(object sender, EventArgs e)
2{
3 調整LV列寬();
4}
 
最後在窗體的Shown事件中調整ListVIEw控件的列寬，即第一次顯示的時候馬上調整列寬


1private void 商品管理_Shown(object sender, EventArgs e)
2{
3    調整LV列寬();
4} 




