//C# Console類的具體用法

Console.Write 表示向控制台直接寫入字符串，不進行換行，可繼續接著前面的字符寫入。
Console.WriteLine 表示向控制台寫入字符串後換行。
Console.Read 表示從控制台讀取字符串，不換行。
Console.ReadLine 表示從控制台讀取字符串後進行換行。
Console.ReadKey 獲取用戶按下的下一個字符或功能鍵，按下的鍵顯示在控制台窗口中。
Console.Beep 通過控制台揚聲器播放提示音。
Console.Clear 清除控制台緩沖區和相應的控制台窗口的顯示信息。

輸出到控制台

輸出到控制台就是把數據輸出到控制台並顯示出來。.Net框架提供了console類實現這個任務，輸出方式如下：

Console.WriteLine();
Console.Write();
Console.WriteLine(輸出的值);
Console.Write(輸出的值);
Console.WriteLine("輸出的格式字符串",變量列表);
Console.Write("輸出的格式字符串",變量列表);

Console.WrietLine()和Console.Write()的唯一卻別就是前者輸出後換行，後者不換行。
Console.WriteLine("鹿鼎記中{0}的妻子有{1},{2},{3}等7個",strName[0],strName[1],strName[2],strName3]);
這種方式中包含兩個參數：“格式字符串”和變量列表。“鹿鼎記中{0}的妻子有{1},{2},{3}等7個”這是格式字符串，{0}、{1}、{2}、{3}叫做占位符，代表後面依次排列的變量表，0對應變量列表的第一個變量，1對應變量列表的第2個變量，依次類推，完成輸出。

從控制台輸入

Console類提供的輸入方法：

Console.ReadLine();

這一句代碼返回一個字符串型數據，可以把它直接賦值給字符串變量，如：
string strname=Console.ReadLine();
有時需要從控制台輸入數字，就用到前面介紹的內容，數據轉換，如：
int num=int.Pares(Console.ReadLine());
int num=Convert.ToInt32(Console.ReadLine());
上面兩句代碼效果相同，可以根據自己的習慣選擇任意一種。

注意：   

 Console.ReadLine()和Console.Read()的輸入結果完全不同，不能混用。
 Console.Read(),返回值為首字符的ASCII碼
 Console.ReadLine(),返回值為字符串
也就是說read方法只能讀取第一個字符，而ReadLine能讀多個字符也可以換行讀取 

Console.ReadKey()的作用，read是從控制台讀取，key表示按下鍵盤，那麼組合在一起的意思就是獲取用戶按下功能鍵顯示在窗口中，用在前面的代碼起到窗口暫停的功能，在調試狀態下，只有按下任意鍵後窗口才會關閉。

控制台輸入輸出

代碼如下：

using System;
using System.Collection.Generic;
using System.Linq;
using System.Text;
namespace ConsoleTest
{
class ConsoleTest
{
static void Main(string[] args)
{
Console.WriteLine("請輸入兩個學生的名字");
string name1=Console.ReadLine();
string name2=Console.ReadLine();
Console.WriteLine("請輸入兩個學生的成績");
int score1=int.Parse(Console.ReadLine());
int score2=int.Parse(Console.ReadLine());
Console.WriteLine("第一個學生的姓名{0},成績{1}",name1,score1);
Console.WriteLine("第二個學生的姓名{0},成績{1}",name2,score2);
Console.ReadKey();
}
}
}


