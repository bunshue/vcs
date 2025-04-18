//C# .net 抓取網頁內容

/*
1、抓取一般內容

需要三個類：WebRequest、WebResponse、StreamReader

所需命名空間：System.Net、System.IO

核心代碼：

      WebRequest 類的 Create 為靜態方法，參數為要抓取的網頁的網址；

      Encoding 指定編碼，Encoding 中有屬性 ASCII、UTF32、UTF8 等全球通用的編碼，但沒有 gb2312 這個編碼屬性，所以我們使用 GetEncoding 獲得 gb2312 編碼。

*/
 
private string GetGeneralContent(string strUrl)
    {
        string strMsg = string.Empty;
        try
        {
            WebRequest request = WebRequest.Create(strUrl);
            WebResponse response = request.GetResponse();
            StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.GetEncoding("gb2312"));

            strMsg = reader.ReadToEnd();

            reader.Close();
            reader.Dispose();
            response.Close();
        }
        catch
        { }
        return strMsg;
    }

/*
2、抓取圖片或其它二進制文件（如文件） 需要四個類：WebRequest、WebResponse、Stream、FileStream 所需命名空間：System.Net、System.IO 核心代碼：用Stream讀取
*/

private string GetFileContent(string strUrl)
    {
        string strMsg = string.Empty;
        try
        {
            WebRequest request = WebRequest.Create(strUrl); 
            WebResponse response = request.GetResponse(); 
            Stream reader = response.GetResponseStream(); 
            
            //可根據實際保存為具體文件
            FileStream writer = new FileStream("D:\\logo.gif", FileMode.OpenOrCreate, FileAccess.Write); 
            byte[] buff = new byte[512]; 
            int c = 0; //實際讀取的字節數 
            while ((c=reader.Read(buff, 0, buff.Length)) > 0) 
            { 
                writer.Write(buff, 0, c); 
            } 
            writer.Close(); 
            writer.Dispose(); 
             
            reader.Close(); 
            reader.Dispose(); 
            response.Close();

            strMsg = "保存成功";
        }
        catch
        { }
        return strMsg;
    }

 
/*
3、抓取網頁內容 POST方式 在抓取網頁時，有時候，需要將某些數據通過 Post 的方式發送到服務器，將以下代碼添加在網頁抓取的程序中，以實現將用戶名和密碼 Post 到服務器：
*/

 private string GetPostContent(string strUrl)
    {
        string strMsg = string.Empty;
        try
        {
            string data = "userName=admin&passwd=admin888"; 
            byte[] requestBuffer = System.Text.Encoding.GetEncoding("gb2312").GetBytes(data);

            WebRequest request = WebRequest.Create(strUrl);
            request.Method = "POST"; 
            request.ContentType = "application/x-www-form-urlencoded"; 
            request.ContentLength = requestBuffer.Length;
            using (Stream requestStream = request.GetRequestStream()) 
            { 
                requestStream.Write(requestBuffer, 0, requestBuffer.Length); 
                requestStream.Close(); 
            }

            WebResponse response = request.GetResponse();
            using (StreamReader reader = new StreamReader(response.GetResponseStream(), Encoding.GetEncoding("gb2312"))) 
            {
                strMsg = reader.ReadToEnd(); 
                reader.Close(); 
            }
        }
        catch
        { }
        return strMsg;
    }

 

4、ASP.NET 抓取網頁內容－防止重定向 在抓取網頁時，成功登錄服務器應用系統後，應用系統可能會通過 Response.Redirect 將網頁進行重定向，如果不需要響應這個重定向，那麼，我們就不要把 reader.ReadToEnd() 給 Response.Write 出來，就可以了。 5、ASP.NET 抓取網頁內容－保持登錄狀態 利用 Post 數據成功登錄服務器應用系統後，就可以抓取需要登錄的頁面了，那麼我們就可能需要在多個 Request 間保持登錄狀態。 首先，我們要使用 HttpWebRequest，而不是 WebRequest。 與 WebRequest 相比，變化的代碼是：
HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(strUrl);

 

注意：HttpWebRequest.Create 返回的類型仍是 WebRequest，所以要轉化一下。 其次，使用 CookieContainer。
System.Net.CookieContainer cc = new System.Net.CookieContainer(); 
request.CookieContainer = cc; 
request2.CookieContainer = cc;

 這樣 request 和 request2 之間就使用了相同的 Session，如果 request 登錄了，那麼 request2 也是登錄狀態。

 最後，如何在不同的頁面間使用同一個 CookieContainer。

 要在不同的頁面間使用同一個 CookieContainer，只有把 CookieContainer 加入 Session。
Session.Add("ccc", cc); //存 
CookieContainer cc = (CookieContainer)Session["ccc"]; //取Session

 如：
HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(strUrl);
            
            //同一頁面
            //HttpWebRequest request2 = (HttpWebRequest)HttpWebRequest.Create(strUrl);
            //System.Net.CookieContainer cc = new CookieContainer();
            //request.CookieContainer = cc;
            //request2.CookieContainer = cc;
            //不同頁面,具體使用時需要將request,request2分開
            object obj = Session["ccc"];
            if (obj == null)
            {
                CookieContainer cc = new CookieContainer();
                //requestr的保存
                Session.Add("ccc", cc);
            }
            string strUrl2 = "";
            HttpWebRequest request2 = (HttpWebRequest)HttpWebRequest.Create(strUrl2);
            //取出來
            CookieContainer cc2 = (CookieContainer)Session["ccc"];
            request2.CookieContainer = cc2;
            //再進行下一步處理

 6、ASP.NET 抓取網頁內容－把當前會話帶到 WebRequest 中

 比如說浏覽器 B1 去訪問服務器端 S1，這會產生一個會話，而服務器端 S2 再用 WebRequest 去訪問服務器端 S1，這又會產生一個會話。現在的需求是讓 WebRequest 使用浏覽器 B1 與 S1 之間的會話，也就是說要讓 S1 認為是 B1 在訪問 S1，而不是 S2 在訪問 S1。

這就要利用 Cookie 了，先在 S1 中取得與 B1 的 SessionID 的 Cookie，再將這個 Cookie 告訴 S2，S2 再將 Cookie 寫在 WebRequest 中。
 WebRequest request = WebRequest.Create("url");
 request.Headers.Add(HttpRequestHeader.Cookie, "ASPSESSIONIDSCATBTAD=KNNDKCNBONBOOBIHHHHAOKDM;");
 WebResponse response = request.GetResponse();
 StreamReader reader = new StreamReader(response.GetResponseStream(), System.Text.Encoding.GetEncoding("gb2312"));
 Response.Write(reader.ReadToEnd());
 reader.Close();
 reader.Dispose();
 response.Close();

 要說明的是：

        本文並不是 Cookie 欺騙，因為 SessionID 是 S1 告訴 S2 的，並不是 S2 竊取的，雖然有些古怪，但這可能在一些特定的應用系統中會有用。
        S1 必須要向 B1 寫 Session，這樣 SessionID 才會保存到 Cookie 中，並且 SessionID 才會保持不變。
        在 ASP.NET 中取 Cookie 用 Request.Cookies，本文假設 Cookie 已經取出來。
        不同的服務器端語言，SessionID 在 Cookie 中上名稱並不一樣，本文是 ASP 的 SessionID。
        S1 可能不僅僅依靠 SessionID 來判斷當前登錄，它可能還會輔助於 Referer、User-Agent 等，這取決於 S1 端程序的設計。
        其實本文算是本連載中“保持登錄狀態”的另一種方法。

7、ASP.NET 抓取網頁內容－如何更改來源 Referer 和 UserAgent
HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create("http://127.0.0.1/index.htm"); 
request.Referer = "http://hovertree.com/";
request.UserAgent = "要設置的標頭";
//下一步的處理 

 



