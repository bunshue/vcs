
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class HITS {

	/** �x�sweb�Ϫ���Ƶ��c */
	private WebGraphMemory graph;

	/** �]�t�C�Ӻ��������� */
	private Map<Integer,Double> hubScores; //<id,value>
	
	/** �]�t�C�Ӻ�����Authority  */
	private Map<Integer,Double> authorityScores;//<id,value>
	
	/** 
	 *�غc���
	 */
	public HITS ( WebGraphMemory graph ) {
		this.graph = graph;
		this.hubScores = new HashMap<Integer,Double>();
		this.authorityScores = new HashMap<Integer,Double>();
		int numLinks = graph.numNodes();
		for(int i=1; i<=numLinks; i++) { 
			hubScores.put(new Integer(i),new Double(1));
			authorityScores.put(new Integer(i),new Double(1));
		}
		computeHITS();
	}

	/**
	 * �p������� Hub �M Authority scores 
		 */
	public void computeHITS() {
		computeHITS(25);
	}
	
	/**
	 *�p������� Hub �M Authority scores
	 * 
     */
	public void computeHITS(int numIterations) {
		
		while(numIterations-->0 ) {
			for (int i = 1; i <= graph.numNodes(); i++) {
				Map<Integer,Double> inlinks    = graph.inLinks(new Integer(i));
				Map<Integer,Double> outlinks  = graph.outLinks(new Integer(i));
				double authorityScore = 0;
				double hubScore = 0;
				for (Integer id:inlinks.keySet()) {
					authorityScore += (hubScores.get(id)).doubleValue();
				}
				
				for (Integer id:outlinks.keySet()) {
					hubScore += (authorityScores.get(id)).doubleValue();
				}
				
				authorityScores.put(new Integer(i),new Double(authorityScore));
				hubScores.put(new Integer(i),new Double(hubScore));
			}
			normalize(authorityScores);
			normalize(hubScores);
		}
	}
	
	public void computeWeightedHITS(int numIterations) {
		while(numIterations-->0 ) {
			for (int i = 1; i <= graph.numNodes(); i++) {
				Map<Integer,Double> inlinks    = graph.inLinks(new Integer(i));
				Map<Integer,Double> outlinks  = graph.outLinks(new Integer(i));
				double authorityScore = 0;
				double hubScore = 0;
				for (Map.Entry<Integer,Double> in:inlinks.entrySet()) {
					authorityScore += (hubScores.get(in.getKey())).doubleValue() * in.getValue();
				}
				
				for (Map.Entry<Integer,Double> out:outlinks.entrySet()) {
					hubScore += (authorityScores.get(out.getKey())).doubleValue() * out.getValue();
				}
				
				authorityScores.put(new Integer(i),new Double(authorityScore));
				hubScores.put(new Integer(i),new Double(hubScore));
			}
			normalize(authorityScores);
			normalize(hubScores);
		}
	}
	
	/**
	 * Normalize the set 
	 */
	private void normalize(Map<Integer,Double> scoreSet)
	{
		Iterator<Integer> iter = scoreSet.keySet().iterator();
		double summation = 0.0;
		while (iter.hasNext())
			summation += ((scoreSet.get((Integer)(iter.next())))).doubleValue();
		
		iter = scoreSet.keySet().iterator();
		while (iter.hasNext())
		{
			Integer id = iter.next();
			scoreSet.put(id , (scoreSet.get(id)).doubleValue()/summation);
		}
	}
	
	/**
	 *  �Ǧ^�P���w�챵���p��Hub score 
	 */
	public Double hubScore(String link) {
		return hubScore(graph.URLToIdentifyer(link));	
	}
	
	/**
	 *�Ǧ^�P���w�챵���p��Hub score 

	 */
	private Double hubScore(Integer id) {
		return (Double)(hubScores.get(id));
	}

	/**
	 *��l�ƻP���w�챵���p��Hub score 
	 */
	public void initializeHubScore(String link, double value) {
		Integer id = graph.URLToIdentifyer(link);
		if(id!=null) hubScores.put(id,new Double(value));	
	}
	
	/**
	 *��l�ƻP���w�챵���p��Hub score
	 */
	public void initializeHubScore(Integer id, double value) {
		if(id!=null) hubScores.put(id,new Double(value));	
	}

	/**
	 *�Ǧ^�P���w�챵���p�� Authority score	 
	 */
	public Double authorityScore(String link) {
		return authorityScore(graph.URLToIdentifyer(link));	
	}
	
	/**
	 *�Ǧ^�P���w�챵���p�� Authority score	
	 */
	private Double authorityScore(Integer id) {
		return (Double)(authorityScores.get(id));
	}

	/**
	 *��l�ƻP���w�챵���p�� Authority score	
	 */
	public void initializeAuthorityScore(String link, double value) {
		Integer id = graph.URLToIdentifyer(link);
		if(id!=null) authorityScores.put(id,new Double(value));	
	}
	
	/**
	 *��l�ƻP���w�챵���p�� Authority score	
	 */
	public void initializeAuthorityScore(Integer id, double value) {
		if(id!=null) authorityScores.put(id,new Double(value));	
	}

}

