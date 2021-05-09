<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch3-1_2.aspx.cs" Inherits="ch3_1_2" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form2" runat="server">
    <div>
        題目：<span style="font-size:12.0pt;font-family:新細明體;
mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;;
mso-bidi-font-family:&quot;Times New Roman&quot;;mso-font-kerning:1.0pt;mso-ansi-language:
EN-US;mso-fareast-language:ZH-TW;mso-bidi-language:AR-SA">計算學生的學業成績<br />
        姓名：<span 
            style="font-size: 12.0pt; font-family: 新細明體; mso-ascii-font-family: &quot;Times New Roman&quot;; mso-hansi-font-family: &quot;Times New Roman&quot;; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-font-kerning: 1.0pt; mso-ansi-language: EN-US; mso-fareast-language: ZH-TW; mso-bidi-language: AR-SA"><asp:TextBox 
            ID="TextBox1" runat="server" Width="88px"></asp:TextBox>
        </span>
        <br />
        國文：<span 
            style="font-size: 12.0pt; font-family: 新細明體; mso-ascii-font-family: &quot;Times New Roman&quot;; mso-hansi-font-family: &quot;Times New Roman&quot;; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-font-kerning: 1.0pt; mso-ansi-language: EN-US; mso-fareast-language: ZH-TW; mso-bidi-language: AR-SA"><asp:TextBox 
            ID="TextBox2" runat="server" Width="88px"></asp:TextBox>
        </span>
        <br />
        英文：<span 
            style="font-size: 12.0pt; font-family: 新細明體; mso-ascii-font-family: &quot;Times New Roman&quot;; mso-hansi-font-family: &quot;Times New Roman&quot;; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-font-kerning: 1.0pt; mso-ansi-language: EN-US; mso-fareast-language: ZH-TW; mso-bidi-language: AR-SA"><asp:TextBox 
            ID="TextBox3" runat="server" Width="88px"></asp:TextBox>
        </span>
        <br />
        平均成績：<asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
        <br />
        </span>
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="計算" />
</form>
</body>
</html>
