

import java.util.Set;

public class MyCrawler {
	/**
	 * �ϥκؤl��l�� URL ���C
	 * @return
	 * @param seeds �ؤlURL
	 */ 
	private void initCrawlerWithSeeds(String[] seeds)
	{
		for(int i=0;i<seeds.length;i++)
			LinkQueue.addUnvisitedUrl(seeds[i]);
	}	
	/**
	 * ����L�{
	 * @return
	 * @param seeds
	 */
	public void crawling(String[] seeds)
	{   //�w�q�L�o���A���R�Hhttp://www.lietu.com�}�Y���챵
		LinkFilter filter = new LinkFilter(){
			public boolean accept(String url) {
				if(url.startsWith("http://www.lietu.com"))
					return true;
				else
					return false;
			}
		};
		//��l�� URL ���C
		initCrawlerWithSeeds(seeds);
		//�`������G�ݧ�����챵���ťB������������h��1000
		while(!LinkQueue.unVisitedUrlsEmpty()&&LinkQueue.getVisitedUrlNum()<=1000)
		{
			//���YURL�X���C
			String visitUrl=(String)LinkQueue.unVisitedUrlDeQueue();
			if(visitUrl==null)
				continue;
			DownLoadFile downLoader=new DownLoadFile();
			//�U������
			downLoader.downloadFile(visitUrl);
			//�� url ��J��w�s���� URL ��
			LinkQueue.addVisitedUrl(visitUrl);
			//���R�X�U���������� URL
			
			Set<String> links=HtmlParserTool.extracLinks(visitUrl,filter);
			//�s�����s���� URL �J��
			for(String link:links)
			{
					LinkQueue.addUnvisitedUrl(link);
			}
		}
	}
	//main ��k�J�f
	public static void main(String[]args)
	{
		MyCrawler crawler = new MyCrawler();
		crawler.crawling(new String[]{"http://www.twt.edu.cn"});
	}

}
