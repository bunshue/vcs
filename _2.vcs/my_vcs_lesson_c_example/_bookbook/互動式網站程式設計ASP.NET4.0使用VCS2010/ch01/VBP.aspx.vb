
Partial Class VBP
    Inherits System.Web.UI.Page
    Dim total As Integer
    Protected Sub Page_Load(sender As Object, e As System.EventArgs) Handles Me.Load
        total = Session("A") + Session("B")
        Session("C") = "VB回傳的結果為：" & total
        Label1.Text = total
    End Sub

    Protected Sub Button1_Click(sender As Object, e As System.EventArgs) Handles Button1.Click
        Response.Redirect("Default.aspx")
    End Sub

End Class
