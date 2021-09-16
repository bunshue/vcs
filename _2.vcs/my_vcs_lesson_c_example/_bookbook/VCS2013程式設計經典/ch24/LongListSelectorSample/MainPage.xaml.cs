using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Navigation;
using Microsoft.Phone.Controls;
using Microsoft.Phone.Shell;
using LongListSelectorSample.Resources;

namespace LongListSelectorSample
{
    public partial class MainPage : PhoneApplicationPage
    {
        // 建構函式
        public MainPage()
        {
            InitializeComponent();


            Loaded += MainPage_Loaded;
            MainLongListSelector.SelectionChanged += MainLongListSelector_SelectionChanged;
        }
        // 頁面載入時執行
        void MainPage_Loaded(object sender, RoutedEventArgs e)
        {
            Book[] bk = new Book[]
            {
                new Book(){ Id="AEL014200", BkName="Visual C# 2012 程式設計經典", Price=650, Img="images/cs2012.jpg"},
                new Book(){ Id="AEL009400", BkName="Visual C# 2012 基礎必修課", Price=520, Img="images/cs2010.jpg"},
                new Book(){ Id="AEL009500", BkName="Visual Basic 2010 程式設計經典", Price=520, Img="images/vb2010.jpg"}
            };
            MainLongListSelector.ItemsSource = bk;
        }
        //選取清單中的項目時執行
        void MainLongListSelector_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            Book selBook = (Book)MainLongListSelector.SelectedItem;
            string msg = "書號：" + selBook.Id +
                "\n書名：" + selBook.BkName +
                "\n單價：" + selBook.Price.ToString();
            MessageBox.Show(msg );
        }
    }
}