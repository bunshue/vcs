<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-11_1.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
    </div>
    <asp:Wizard ID="Wizard1" runat="server" ActiveStepIndex="0" BackColor="#EFF3FB" 
        BorderColor="#B5C7DE" BorderWidth="1px" Font-Names="Verdana" Font-Size="Small" 
        Height="136px" Width="249px">
        <StepStyle Font-Size="0.8em" ForeColor="#333333" />
        <WizardSteps>
            <asp:WizardStep runat="server" StepType="Start" Title="Start">
                歡迎來到「e-Learing」上線學習之學員註冊系統！</asp:WizardStep>
            <asp:WizardStep runat="server" title="Step 1">
                學員請註冊<br />
                學號：<asp:TextBox ID="TextBox1" runat="server" Width="83px"></asp:TextBox>
                <br />
                姓名：<asp:TextBox ID="TextBox2" runat="server" Width="83px"></asp:TextBox>
                <br />
                想閱讀課程名稱：<br />
                <asp:DropDownList ID="DropDownList1" runat="server">
                    <asp:ListItem>資料庫課程</asp:ListItem>
                    <asp:ListItem>程式設計課程</asp:ListItem>
                </asp:DropDownList>
            </asp:WizardStep>
            <asp:WizardStep runat="server" title="Step 2">
                請輸入學員帳號：<br />
                <br />
                <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
            </asp:WizardStep>
            <asp:WizardStep runat="server" Title="Step 3">
                學員密碼：<asp:TextBox ID="TextBox4" runat="server" Width="69px"></asp:TextBox>
                <br />
                再輸一次：<asp:TextBox ID="TextBox5" runat="server" Width="69px"></asp:TextBox>
            </asp:WizardStep>
            <asp:WizardStep runat="server" StepType="Finish" Title="Finish">
                您已經填寫完成學員註冊之步驟，請按「完成」，可以真正成為e-Learning會員！</asp:WizardStep>
            <asp:WizardStep runat="server" StepType="Complete" Title="Complete">
                恭喜您！註冊成功！<br />
                您的註冊相關資料如下：<br />
                <br />
                <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
            </asp:WizardStep>
        </WizardSteps>
        <SideBarButtonStyle BackColor="#507CD1" Font-Names="Verdana" 
            ForeColor="White" />
        <NavigationButtonStyle BackColor="White" BorderColor="#507CD1" 
            BorderStyle="Solid" BorderWidth="1px" Font-Names="Verdana" Font-Size="0.8em" 
            ForeColor="#284E98" />
        <SideBarStyle BackColor="#507CD1" Font-Size="0.9em" VerticalAlign="Top" />
        <HeaderStyle BackColor="#284E98" BorderColor="#EFF3FB" BorderStyle="Solid" 
            BorderWidth="2px" Font-Bold="True" Font-Size="0.9em" ForeColor="White" 
            HorizontalAlign="Center" />
        <HeaderTemplate>
            <span lang="EN-US" style="font-size:12.0pt;font-family:
&quot;Times New Roman&quot;;mso-fareast-font-family:新細明體;mso-font-kerning:1.0pt;
mso-ansi-language:EN-US;mso-fareast-language:ZH-TW;mso-bidi-language:AR-SA">e-Learning</span><span style="font-size:12.0pt;font-family:新細明體;mso-ascii-font-family:&quot;Times New Roman&quot;;
mso-hansi-font-family:&quot;Times New Roman&quot;;mso-bidi-font-family:&quot;Times New Roman&quot;;
mso-font-kerning:1.0pt;mso-ansi-language:EN-US;mso-fareast-language:ZH-TW;
mso-bidi-language:AR-SA">學員註冊系統</span>
        </HeaderTemplate>
    </asp:Wizard>
    
    </div>
    </form>
</body>
</html>
