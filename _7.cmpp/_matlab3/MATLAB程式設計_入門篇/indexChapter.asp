<%@language=jscript%>
<%
fso=Server.CreateObject("Scripting.FileSystemObject");
parentPath=fso.GetParentFolderName(Request.ServerVariables("URL"));
title=fso.GetFileName(parentPath);
%>
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
absTopPath = Server.MapPath(".");
fd=fso.GetFolder(absTopPath);
%>
<table border=1 align=center>
<tr>
<th>Files</th>
<th>Last modified</th>
<%
var fileList=new Enumerator(fd.files);
for (fileList.moveFirst(); !fileList.atEnd(); fileList.moveNext()){
	fileName=fileList.item().name;
	extName=fso.GetExtensionName(fileName);
	if (extName=="asp") continue;
	dateLastModified=new Date(fileList.item().DateLastModified+"");
	Response.Write("<tr>");
	Response.Write("<td><a href=\"" + fileName + "\">" + fileName + "</a></td>");
	Response.Write("<td>" + dateLastModified.toLocaleString() + "</td>");
	Response.Write("</tr>\n");
}
%>
</table>

<hr>

<script language="JavaScript">
document.write("Last updated on " + document.lastModified + ".")
</script>

</font>
</body>
</html>
