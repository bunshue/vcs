<!DOCTYPE html>
<html lang='zh-Hant-TW'>
<head>
<title>Python Mysql測試網頁</title>
</head>
<body>
<table align='center' width='60%' bgcolor='#cccccc' cellpadding=5 cellspacing=2>
<caption align='center'>中油最近20週油價</caption>
<tr><th>公告日期</th><th>92無鉛</th><th>95無鉛</th><th>98無鉛</th></tr>
<?php
  $dbuser='ptest';
  $dbname='ptest';
  $dbhost = 'db4free.net';
  $dbpasswd = '******';

  $conn = mysql_connect($dbhost, $dbuser, $dbpasswd) or die ('connect error');
  mysql_select_db($dbname);
  $res = mysql_query('select * from PRICES order by gdate desc limit 20;');
  $i=0;
  while($row = mysql_fetch_array($res)) {
    $i++;
    if($i%2)
      echo '<tr bgcolor=#ccffcc>';
    else
      echo '<tr bgcolor=#ffccff>';
    echo '<td width=200 align=center>' . $row[0] . '</td>' . 
         '<td align=center>' . $row[1] . '元</td>' . 
         '<td align=center>' . $row[2] . '元</td>' . 
         '<td align=center>' . $row[3] . '元</td>';
    echo '</tr>';
  }
  mysql_close($conn);
?>
</table>
</body>
</html>
