﻿<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch7-1_1.aspx.cs" Inherits="ch7_1_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="字串資料" />
    </div>
    <p>
        <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="變數資料" />
    </p>
    <p>
        <asp:Button ID="Button3" runat="server" onclick="Button3_Click" 
            Text="字串與變數資料" />
    </p>
    </form>
</body>
</html>
