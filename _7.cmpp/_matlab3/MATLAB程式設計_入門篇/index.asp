<%@language=jscript%>
<% title="MATLAB�{���]�p�m�J���g�n�G�{���d��" %>
<html>
<head>
	<title><%=title%></title>
	<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=big5">
	<meta HTTP-EQUIV="Expires" CONTENT="0">
	<style>
		td {font-family: "�з���", "helvetica,arial", "Tahoma"}
		A:link {text-decoration: none}
		A:hover {text-decoration: underline}
	</style>
</head>

<body background="/jang/graphics/background/yellow.gif">
<font face="�з���">
<h2 align=center><%=title%></h2>
<h3 align=center><a href="mirlab.org/jang">�i���P</a></h3>
<hr>

<%
fso = Server.CreateObject("Scripting.FileSystemObject");
absTopPath = Server.MapPath(".");
fd = fso.GetFolder(absTopPath);
%>
<table border=1 align=center>
<tr>
<th>�U���D�D</th>
<%
var subFolderList=new Enumerator(fd.SubFolders);
for (subFolderList.moveFirst(); !subFolderList.atEnd(); subFolderList.moveNext()){
	folderName=subFolderList.item().name;
	Response.Write("<tr>");
	Response.Write("<td><a target=_blank href=\"" + folderName + "\">" + folderName + "</a></td>");
	Response.Write("</tr>\n");
}
%>
</table>

<hr>

<!--
<script language="JavaScript">
document.write("Last updated on " + document.lastModified + ".")
</script>
-->

</font>
</body>
</html>
