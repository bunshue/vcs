

import java.sql.Timestamp;
import java.util.Date;

public class Url {
	// 原始url的值，主機部分是域名
	private String oriUrl;
	// url的值，主機部分是IP,為了防止重複主機的出現
	private String url;
	//URL NUM
	private int urlNo;
	// 獲得URL傳回的結果碼
	private int statusCode;
	// 此URL被別的文章參考的次數
	private int hitNum;
	// 此URL對應文章的中文字解碼
	private String charSet;
	// 文章摘要
	private String abstractText;
	// 作者
	private String author;
	// 文章的權重（包含導向詞的資訊）
	private int weight;
	// 文章的描述
	private String description;
	// 文章大小
	private int fileSize;
	// 最後修改時間
	private Timestamp lastUpdateTime;
	// 過期時間
	private Date timeToLive;
	// 文章名稱
	private String title;
	// 文章類型
	private String type;
	// 參考的鏈接
	private String[] urlRefrences;
    //爬取的階層，從種子開始，依次為第0層，第1層...
	private int layer;
	public String getOriUrl() {
		return oriUrl;
	}

	public void setOriUrl(String oriUrl) {
		this.oriUrl = oriUrl;
	}

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	public int getUrlNo() {
		return urlNo;
	}

	public void setUrlNo(int urlNo) {
		this.urlNo = urlNo;
	}

	public int getStatusCode() {
		return statusCode;
	}

	public void setStatusCode(int statusCode) {
		this.statusCode = statusCode;
	}

	public int getHitNum() {
		return hitNum;
	}

	public void setHitNum(int hitNum) {
		this.hitNum = hitNum;
	}

	public String getCharSet() {
		return charSet;
	}

	public void setCharSet(String charSet) {
		this.charSet = charSet;
	}

	public String getAbstractText() {
		return abstractText;
	}

	public void setAbstractText(String abstractText) {
		this.abstractText = abstractText;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public int getWeight() {
		return weight;
	}

	public void setWeight(int weight) {
		this.weight = weight;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public int getFileSize() {
		return fileSize;
	}

	public void setFileSize(int fileSize) {
		this.fileSize = fileSize;
	}
	public Timestamp getLastUpdateTime() {
		return lastUpdateTime;
	}

	public void setLastUpdateTime(Timestamp lastUpdateTime) {
		this.lastUpdateTime = lastUpdateTime;
	}

	public Date getTimeToLive() {
		return timeToLive;
	}

	public void setTimeToLive(Date timeToLive) {
		this.timeToLive = timeToLive;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String[] getUrlRefrences() {
		return urlRefrences;
	}

	public void setUrlRefrences(String[] urlRefrences) {
		this.urlRefrences = urlRefrences;
	}
}
