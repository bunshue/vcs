package ip;
/** 
 * 
 * @category 用來封裝ip相關資訊，目前只有兩個字段，ip所在的國家和地區
 */

public class IPLocation {
	private String country;
	private String area;
	
	public IPLocation() {
	    country = area = "";
	}
	
	public IPLocation getCopy() {
	    IPLocation ret = new IPLocation();
	    ret.country = country;
	    ret.area = area;
	    return ret;
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
	}

	public String getArea() {
		return area;
	}

	public void setArea(String area) {
                //如果為局域網，純真IP地址庫的地區會顯示CZ88.NET,這裡把它去掉
		if(area.trim().equals("CZ88.NET")){
			this.area="本機或本網絡";
		}else{
			this.area = area;
		}
	}
}
