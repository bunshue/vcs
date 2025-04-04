

XML文件
可擴展標記性語言，用來保存輕量級數據。
XML的標簽是成對出現的、並且是區分大小寫的。
XML文檔必須包含根節點，且只有一個。

創建XML文件
 1 //創建XML對象
 2 XmlDocument doc = new XmlDocument();
 3 //創建文檔描述信息
 4 XmlDeclaration dec = doc.CreateXmlDeclaration("1.0", "utf-8", null);
 5 doc.AppendChild(dec);
 6 
 7 //創建根節點
 8 XmlElement books = doc.CreateElement("Books");
 9 doc.AppendChild(books);
10 
11 //創建子節點
12 XmlElement book1 = doc.CreateElement("Book");
13 books.AppendChild(book1); //將子節點添加到books
14 
15 //給book1子節點追加子節點
16 XmlElement name1 = doc.CreateElement("Name");
17 name1.InnerText = "c#"; //賦值 文本值
18 book1.AppendChild(name1);
19 
20 XmlElement price1 = doc.CreateElement("Price");
21 price1.InnerXml = "<b>10.0</b>"; //賦值 html標簽
22 book1.AppendChild(price1);
23 
24 XmlElement items = doc.CreateElement("Items");
25 //給節點增加屬性
26 items.SetAttribute("Name", "c#");
27 items.SetAttribute("Price", "10.0");
28 book1.AppendChild(items);
29 
30 doc.Save("Books.xml"); //保存
31 
32 //創建後
33 <?xml version="1.0" encoding="utf-8"?>
34 <Books>
35   <Book>
36     <Name>c#</Name>
37     <Price>
38       <b>10.0</b>
39     </Price>
40     <Items Name="c#" Price="10.0" />
41   </Book>
42 </Books>

向已有XML文件中追加

1 XmlDocument doc = new XmlDocument();
2 if (File.Exists("Books.xml"))
3 {
4     doc.Load("Books.xml"); //加載 xml
5     XmlElement books = doc.DocumentElement; //得到根節點
6     //再建立元素進行追加
7 }

獲取XML文件

 1 XmlDocument doc = new XmlDocument();
 2 doc.Load("Books.xml");
 3 
 4 XmlElement books = doc.DocumentElement;
 5 XmlNodeList xnl = books.ChildNodes; //得到所有節點
 6 
 7 foreach (XmlNode v in xnl) //遍歷得到所有節點值
 8 {
 9     Console.WriteLine(v.InnerText);
10 }
11 
12 XmlNodeList xnl1 = doc.SelectNodes("Books/Book/Items"); //查找節點列表
13 foreach (XmlNode node in xnl1)
14 {
15     Console.WriteLine(node.Attributes["Name"].Value); //得到name屬性的值
16     Console.WriteLine(node.Attributes["Price"].Value); //得到price屬性的值
17 }

刪除XML文件

1 XmlDocument doc = new XmlDocument();
2 doc.Load("Books.xml");
3 
4 XmlNode xnl = doc.SelectSingleNode("Books/Book"); //查找單一節點
5 xnl.RemoveAll(); //刪除全部
6 doc.Save("Books.xml");
7 Console.ReadKey();

LinqToXml

 1 //兼容傳統方法創建
 2 XDocument xDoc = new XDocument();
 3 //xDoc.Declaration = new XDeclaration() 默認UTF-8 第一行不需要單獨建
 4 XElement xRoot = new XElement("root", "值"); //定義元素
 5 
 6 XElement xRoot1 = new XElement("root1");  //定義元素２
 7 xRoot1.Value = "值1";
 8 
 9 XAttribute xattr = new XAttribute("Id", "1"); //定義屬性
10 
11 xDoc.Add(xRoot); //統一使用add添加
12 xRoot.Add(xattr);
13 
14 xDoc.Save(@"d:\linqtoxml.xml");
15 
16 //真正的linq語法
17 //F#  函數式編程語言
18 new XDocument(
19     new XElement("root",
20         new XAttribute("id", "001"),
21         "值")
22     ).Save(@"d:\2.xml");
23 //鏈式編程，流水線生產 f1().f2().f3()...
24 
25 //查找xml
26 XDocument xdoc = new XDocument(new XElement("root"));//根節點
27 xdoc.Root.Add(new XElement("person",
28     new XAttribute("id", "1"),
29     new XAttribute("name", "zhangsan"),
30     new XAttribute("sex", "1")
31     )); //添加子節點
32 xdoc.Root.Add(new XElement("person",
33    new XAttribute("id", "2"),
34    new XAttribute("name", "lisi"),
35    new XAttribute("sex", "2")
36    ));
37 xdoc.Save(@"d:\2.xml");
38 
39 <?xml version="1.0" encoding="utf-8"?>
40 <root>
41   <person id="1" name="zhangsan" sex="1" />
42   <person id="2" name="lisi" sex="2" />
43 </root>
44 
45 //開始查找、修改、刪除
46 
47 XDocument xdoc = XDocument.Load(@"d:\2.xml"); //加載xml
48 foreach (XElement xlt in xdoc.Root.Elements()) //Root根節點 Elements 元素集合
49 {
50     if (xlt.Name.LocalName == "person") //Name節點名 LocalName不帶命名空間的節點名
51     {
52         if (xlt.Attribute("id").Value == "1") //判斷屬性值為1時
53         {
54             Response.Write(xlt.Attribute("name").Value); //輸出name
55             xlt.Attribute("name").Value = "newname"; //修改name
56             xlt.Remove(); //刪除此節點
57             xdoc.Save(@"d:2.xml");
58         }
59     }
60 }
61 
62 //Linq查詢語法
63 //Descendants()所有子節點 可加某節點下所有節點
64 var query = from s in xdoc.Descendants() //從集合裡找 
65             where s.Name.LocalName == "person"
66             select s;
67 foreach (XElement xlt in query)
68 {
69     Response.Write(xlt.Value);
70 }
71 
72 //Linq方法語法(lambda表達式)
73 foreach (XElement xlt in xdoc.Descendants().Where(s =>
74 {
75     if (s.Name.LocalName == "name")
76     {
77         return true;
78     }
79     return false;
80 }))
81 {
82     Response.Write(xlt.Value);
83 }


