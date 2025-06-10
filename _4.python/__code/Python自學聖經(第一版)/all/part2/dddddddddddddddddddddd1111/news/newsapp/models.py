from django.db import models

class NewsUnit(models.Model):  #新聞資料表
	catego =  models.CharField(max_length=10, null=False)  #類別關聯
	nickname = models.CharField(max_length=20, null=False)  #暱稱
	title = models.CharField(max_length=50, null=False)  #標題
	message = models.TextField(null=False)  #內容
	pubtime = models.DateTimeField(auto_now=True)  #發布時間
	enabled = models.BooleanField(default=False)  #是否顯示
	press = models.IntegerField(default=0)  #點擊次數
	def __str__(self):
		return self.title
