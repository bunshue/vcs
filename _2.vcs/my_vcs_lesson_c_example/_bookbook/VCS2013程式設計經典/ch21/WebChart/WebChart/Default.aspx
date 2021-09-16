<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="WebChart.Default" %>

<%@ Register assembly="System.Web.DataVisualization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" namespace="System.Web.UI.DataVisualization.Charting" tagprefix="asp" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <img  src="charttitle.jpg" /><br />
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT 產品類別.類別名稱, COUNT(產品資料.產品編號) AS 產品總類 FROM 產品資料
INNER JOIN 產品類別 ON 產品資料.類別編號 = 產品類別.類別編號 
GROUP BY 產品類別.類別名稱"></asp:SqlDataSource>
        <br />
        <asp:Chart ID="Chart1" runat="server" DataSourceID="SqlDataSource1">
            <series>
                <asp:Series Name="Series1" XValueMember="類別名稱" YValueMembers="產品總類">
                </asp:Series>
            </series>
            <chartareas>
                <asp:ChartArea Name="ChartArea1">
                </asp:ChartArea>
            </chartareas>
        </asp:Chart>
        <br />
        <br />
        <br />
        <asp:Chart ID="Chart2" runat="server" DataSourceID="SqlDataSource1">
            <series>
                <asp:Series ChartType="Pie" Name="Series1" XValueMember="類別名稱" YValueMembers="產品總類">
                </asp:Series>
            </series>
            <chartareas>
                <asp:ChartArea Name="ChartArea1">
                </asp:ChartArea>
            </chartareas>
        </asp:Chart>
    
    </div>
    </form>
</body>
</html>
