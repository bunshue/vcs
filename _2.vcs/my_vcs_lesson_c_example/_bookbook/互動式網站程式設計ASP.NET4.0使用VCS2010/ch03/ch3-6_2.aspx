<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch3-6_2.aspx.cs" Inherits="ch3_6_2" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="一、單一選擇結構" 
        Width="112px" />
    <br />
    <br />
    <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="二、雙重選擇結構" 
        Width="114px" />
    <br />
    <br />
    <asp:Button ID="Button3" runat="server" onclick="Button3_Click" 
        Text="三、多重選擇結構題目：多重選擇結構(if---else if)	" Width="325px" />
    <p>
        <asp:Button ID="Button4" runat="server" onclick="Button4_Click" 
            Text="四、多重選擇結構題目：多重選擇結構(switch)	" Width="300px" />
    </p>
    <p>
        <asp:Button ID="Button5" runat="server" onclick="Button5_Click" Text="五、巢狀選擇結構" 
            Width="117px" />
    </p>
    </form>
</body>
</html>
