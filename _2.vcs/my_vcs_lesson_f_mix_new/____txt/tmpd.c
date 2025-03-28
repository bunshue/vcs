var urlFormat = @"


http://maps.google.com/maps/api/staticmap?center={0},           
 
    {1}&size=640x640&format=jpg&sensor=false&markers=color:red%7Csize:mid%7Clabel:A%7C{0},{1}";
https://maps.googleapis.com/maps/api/staticmap?parameters





http://maps.google.com/maps/api/staticmap?parameters

https://maps.googleapis.com/maps/api/staticmap?parameters


如何抓取Google Static Map

https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318
&markers=color:red%7Clabel:C%7C40.718217,-73.998284
&key=AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY




AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY



        private const string mapurl = "http://maps.google.com/mapdata?latitude_e6={0}&longitude_e6={1}&zm={2}&w={3}&h={4}&cc=&min_priority=2";

string.Format(mapurl, this.Latitude, this.Longitude, this.Zoom, this.Width.Value, this.Height.Value)
			
			url : http://maps.google.com/mapdata?latitude_e6=100&longitude_e6=123&zm=200&w=640&h=480&cc=&min_priority=2





範例網址：
http://maps.google.com/mapdata?Point=b&Point.latitude_e6=23000944&Point.longitude_e6=120180160&Point.iconid=17&Point=e&zm=33900&w=113&h=113&cc=&min_priority=3&client=internal-mobilefe&zl=7

參數說明：
Point=b和Point=e：代表一個點的開始和結尾
Point.latitude_e6：緯度 (無小數點，小數取到第六位)
Point.longitude_e6：經度(無小數點，小數取到第六位)
w：取得的圖片寬度
h：取得的圖片高度
cc：目前好像沒用
min_priority：試著去改過，不過好像沒什麼作用
client：照著輸入即可
zl：縮放比例 (0~17)
zm：應該是Zoom Meter，計算方式為 (zl + 1) * w 




http://maps.google.com/mapdata?latitude_e6=51600117&longitude_e6=
 4293842485&zm=9600&w=600&h=400&cc=&min_priority=2