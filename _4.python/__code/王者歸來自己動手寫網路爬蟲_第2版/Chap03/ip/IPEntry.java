package ip;
/**
 * <pre>
 * 一條IP範圍記錄，不僅包括國家和區域，也包括起始IP和結束IP
 * </pre>
 */
public class IPEntry {
    public String beginIp;
    public String endIp;
    public String country;
    public String area;
    
    /**
     * 建構函數
     */
    public IPEntry() {
        beginIp = endIp = country = area = "";
    }
}
