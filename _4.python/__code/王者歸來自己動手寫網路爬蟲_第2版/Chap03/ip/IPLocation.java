package ip;
/** 
 * 
 * @category �Ψӫʸ�ip������T�A�ثe�u����Ӧr�q�Aip�Ҧb����a�M�a��
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
                //�p�G��������A�¯uIP�a�}�w���a�Ϸ|���CZ88.NET,�o�̧⥦�h��
		if(area.trim().equals("CZ88.NET")){
			this.area="�����Υ�����";
		}else{
			this.area = area;
		}
	}
}
