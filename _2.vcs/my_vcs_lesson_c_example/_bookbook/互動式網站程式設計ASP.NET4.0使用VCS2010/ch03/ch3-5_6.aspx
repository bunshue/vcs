<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch3-5_6.aspx.cs" Inherits="ch3_5_6" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form2" runat="server">
    <div>
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="字串與變數" />
    <p>
        <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="字串與字串" />
    </p>
    <p>
        <asp:Button ID="Button3" runat="server" onclick="Button3_Click" 
            Text="字串與算術運算式" />
    </p>
    <p>
        <asp:Button ID="Button4" runat="server" onclick="Button4_Click" 
            Text="運算元都是數值" />
    </p>
    <p>
        <asp:Button ID="Button5" runat="server" onclick="Button5_Click" 
            Text="運算元都是字串" />
    </p>
    </form>
</body>
</html>
