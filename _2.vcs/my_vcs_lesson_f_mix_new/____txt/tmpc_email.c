


範例四：指定不同格式的電子郵件

因應某些收件者無法顯示 HTML 內容，也可以同時提供純文字和 HTML 版本的郵件內容。

    AlternateView 類別：用來建立不同格式的郵件複本。
    MediaTypeNames 類別：指定郵件複本的媒體類型資訊。{Html,Plain,RichText,XML...}

// 設定一個HTML格式的 AlternateView 
string htmlBody = "<body><html>This message support <b>HTML</b></html></body>";
AlternateView viewHtml = AlternateView.CreateAlternateViewFromString(htmlBody, null, MediaTypeNames.Text.Html);
avHtml.LinkedResources.Add(pic1);

// 設定一個文字格式的 AlternateView
string textBody = "This message doesn't support HTML";
AlternateView viewPlain = AlternateView.CreateAlternateViewFromString(textBody, null, MediaTypeNames.Text.Plain);

// 使用 alternate views 加入訊息主體，替代 MailMessage.Body
mailmessage.AlternateViews.Add(viewHtml);
mailmessage.AlternateViews.Add(viewPlain);

SendMail(smtpclient, mailmessage);




範例五：內嵌檔案(1)

透過 LinkedResource 類別，可用來建立資源連結物件，並將該物件加入 Html 格式的 AlternateView 物件中。

給定每個 LinkedResource 一個唯一的 ContentId ，再將這個 ContentId 套用到 <img＞ 標籤的 cid 屬性的值。

// 設定連結資源檔
string sFilePath = @"D:\MCTS\MCTS2011\Practice\PracticeMCTS\bin\Debug\cloud.jpg";
LinkedResource resource1 = new LinkedResource(sFilePath, MediaTypeNames.Image.Jpeg);
resource1.ContentId = "resource_id_1";      //定義這個資源的 ContentID。

// 設定一個HTML格式的本文內容，並加入連結資源檔
string htmlBody = @"
<html><body>

<h1>資源內嵌</h1>
<img src=""cid:resource_id_1"" />

</body></html>";

AlternateView viewHtml = AlternateView.CreateAlternateViewFromString(htmlBody, null, MediaTypeNames.Text.Html);
viewHtml.LinkedResources.Add(resource1);

// 使用 alternate views 替代 MailMessage.Body
mailmessage.AlternateViews.Add(viewHtml);

SendMail(smtpclient, mailmessage);

範例六：內嵌檔案(2)

<img> 標籤中的 src 屬性，其值要等於 Attachment.Name 。

// 設定附件檔
string sFilePath2 = @"D:\MCTS\MCTS2011\Practice\PracticeMCTS\bin\Debug\cloud.jpg";
Attachment attm = new Attachment(sFilePath2);
attm.Name = Path.GetFileName(sFilePath2);
attm.NameEncoding = Encoding.GetEncoding("utf-8");
attm.TransferEncoding = TransferEncoding.Base64;

// 設定該附件為一個內嵌附件(Inline Attachment)
attm.ContentDisposition.Inline = true;                                      //附件中的內容是以內嵌方式呈現為電子郵件主體的一部分，則為 true
attm.ContentDisposition.DispositionType = DispositionTypeNames.Inline;      //附件類型 => 將附件顯示為電子郵件訊息主體的一部分
mailmessage.Attachments.Add(attm);

// 設定一個HTML格式的本文內容，並加入附件檔 
// img 標籤中的 src 屬性，其值要等於 Attachment.Name
string htmlBody = @"
<html><body>

<h3>附件內嵌(Inline Attachment)</h3>
<img src=""cloud.jpg"" />                       

</body></html>";
mailmessage.Body = htmlBody;

SendMail(smtpclient, mailmessage);











