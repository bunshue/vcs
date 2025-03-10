
C#基礎鞏固(2)-Linq To XML創建XML，

一、首先要清楚一個正確的XML基本格式是怎樣的。

 1.後綴名.xml結尾

 2.有一行描述

 3.有且僅有一個根節點。

如圖:

一個正確的xml文件能夠被浏覽器打開且顯示。所以判斷一個xml文件有沒有錯誤也可以用浏覽器打開看有沒有報錯。
二、傳統的XML創建方式。

      命名空間:System.XML 

      用到的類庫:XmlDocument -文檔

                     XmlElement  -元素

                     XmlAttribute -屬性

      代碼:

static void Main(string[] args)
        {
            TraditionalCreateXML();
        }
        
        
					        private static void TraditionalCreateXML()
					        {
					            XmlDocument xdoc = new XmlDocument();
					            //所有的元素使用文檔節點(XmlDocument)創建
					            XmlDeclaration xdec = xdoc.CreateXmlDeclaration("1.0", "gb2312", null); //xml描述
					            xdoc.AppendChild(xdec); //添加描述
					            XmlElement xele = xdoc.CreateElement("root"); //創建節點1
					            XmlElement xele2 = xdoc.CreateElement("person"); //創建節點2
					            xdoc.AppendChild(xele);  //xdoc添加節點 --根節點 
					            xele.AppendChild(xele2); //在節點1(xele)下添加一個節點2(xele2)
					            XmlAttribute xAttr = xdoc.CreateAttribute("id"); //創建屬性
					            xAttr.Value = "123";  //屬性的值
					            xele.Attributes.Append(xAttr); //把屬性插入到節點
					            XmlText txt = xdoc.CreateTextNode("我是文本節點");  //創建文本
					            xele2.AppendChild(txt); //把文本插入到節點
					            xdoc.Save("1.xml");
					        }

　 關鍵的思想是:創建元素->添加元素,執行完上面代碼 在bin->debug目錄下找到1.xml這個文件。

     內容如下:

    
三、Linq To XML創建XML

       命名空間: System.XML.Linq;

        類庫: XDocument  -文檔

                XElement -元素

                XAttribute - 屬性
   3.1 Linq To XML用法

   代碼:

 static void Main(string[] args)
        {
            LinqToXMLCreateXML();
            //TraditionalCreateXML();
        }
        private static void LinqToXMLCreateXML()
        {
            XDocument xdoc = new XDocument();
            //描述會自動創建  Encoding為UTF-8  如果想改成GB2312的  XDeclaration dec=new XDeclaration("1.0","gb2312","yes");
            XElement xRoot = new XElement("root"); //創建節點
            XElement xele2 = new XElement("person", "我是文本");
            XAttribute xAttr = new XAttribute("Id", "123"); //創建屬性
            xdoc.Add(xRoot); //添加節點
            xRoot.Add(xele2);
            xRoot.Add(xAttr); //添加屬性
            xdoc.Save("2.xml");
        }

 執行代碼,在bin->debug 目錄下找到2.xml文件

   從上面代碼可以看出，Linq TO XML的方法比傳統的方法簡單，特點有。

     1.創建元素的時候可以用 鍵/值(key/value)對的方法創建元素並賦值

     2.添加元素或者屬性的時候，都是用Add()方法。
   3.2真正的linq語法

    linq 語法主要特點： 1.基於函數式    f1().f2().f3().....

                               2.鏈式編程

    把上面3.1的代碼寫成linq語法為:

static void Main(string[] args)
        {
            LinqToXMLCreateXML2();
            //LinqToXMLCreateXML();
            //TraditionalCreateXML();
        }
        private static void LinqToXMLCreateXML2()
        {
            new XDocument(
                new XElement("root",
                    new XAttribute("Id","123"),
                    new XElement("person","我是一個文本")
                            )
                    ).Save("3.xml");
        }

 

