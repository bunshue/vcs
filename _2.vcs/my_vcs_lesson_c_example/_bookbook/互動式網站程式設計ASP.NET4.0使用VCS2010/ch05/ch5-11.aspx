<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-11.aspx.cs" Inherits="ch5_1" %>

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
    <asp:Wizard ID="Wizard1" runat="server">
        <WizardSteps>
            <asp:WizardStep runat="server" StepType="Start" Title="Start">
            </asp:WizardStep>
            <asp:WizardStep runat="server" title="Step 1">
            </asp:WizardStep>
            <asp:WizardStep runat="server" title="Step 2">
            </asp:WizardStep>
            <asp:WizardStep runat="server" Title="Step 3">
            </asp:WizardStep>
            <asp:WizardStep runat="server" StepType="Finish" Title="Finish">
            </asp:WizardStep>
            <asp:WizardStep runat="server" StepType="Complete" Title="Complete">
            </asp:WizardStep>
        </WizardSteps>
    </asp:Wizard>
    
    </div>
    </form>
</body>
</html>
