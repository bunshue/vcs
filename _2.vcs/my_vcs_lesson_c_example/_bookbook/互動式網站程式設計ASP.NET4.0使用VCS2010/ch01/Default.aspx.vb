
Partial Class _Default
    Inherits System.Web.UI.Page
    Dim A, B As Integer
    Protected Sub Page_Load(sender As Object, e As System.EventArgs) Handles Me.Load
        Session("A") = 10
        Session("B") = 20
        Label1.Text = Session("C")

    End Sub

    Protected Sub Button1_Click(sender As Object, e As System.EventArgs) Handles Button1.Click
        Response.Redirect("CSP.aspx")
    End Sub

    Protected Sub Button2_Click(sender As Object, e As System.EventArgs) Handles Button2.Click
        Response.Redirect("VBP.aspx")
    End Sub

    Protected Sub Button3_Click(sender As Object, e As System.EventArgs) Handles Button3.Click
        Session.Clear()
        Response.Redirect("Default.aspx")
    End Sub
End Class
