<%@ Page Title="" Language="C#" MasterPageFile="~/ch12.master" AutoEventWireup="true" CodeFile="ch12.aspx.cs" Inherits="ch12" %>

<asp:Content ID="Content1" ContentPlaceHolderID="head" Runat="Server">
</asp:Content>
<asp:Content ID="Content2" ContentPlaceHolderID="ContentPlaceHolder1" Runat="Server">
    <br />
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" 
        Text="透過控制項右鍵產生" />
&nbsp;&nbsp;
    <asp:Button ID="Button2" runat="server" Text="由方案總管產生" 
        onclick="Button2_Click" />
    <br />
    <br />
</asp:Content>

