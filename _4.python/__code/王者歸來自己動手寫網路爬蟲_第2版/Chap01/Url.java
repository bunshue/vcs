

import java.sql.Timestamp;
import java.util.Date;

public class Url {
	// ��lurl���ȡA�D�������O��W
	private String oriUrl;
	// url���ȡA�D�������OIP,���F����ƥD�����X�{
	private String url;
	//URL NUM
	private int urlNo;
	// ��oURL�Ǧ^�����G�X
	private int statusCode;
	// ��URL�Q�O���峹�ѦҪ�����
	private int hitNum;
	// ��URL�����峹������r�ѽX
	private String charSet;
	// �峹�K�n
	private String abstractText;
	// �@��
	private String author;
	// �峹���v���]�]�t�ɦV������T�^
	private int weight;
	// �峹���y�z
	private String description;
	// �峹�j�p
	private int fileSize;
	// �̫�ק�ɶ�
	private Timestamp lastUpdateTime;
	// �L���ɶ�
	private Date timeToLive;
	// �峹�W��
	private String title;
	// �峹����
	private String type;
	// �ѦҪ��챵
	private String[] urlRefrences;
    //���������h�A�q�ؤl�}�l�A�̦�����0�h�A��1�h...
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
