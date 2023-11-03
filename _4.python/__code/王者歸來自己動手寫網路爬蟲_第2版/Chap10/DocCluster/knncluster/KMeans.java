package knncluster;

import java.lang.Math;

public class KMeans {
	//private static int[] CenterId;
	//to computer the EuclideanDistance
	private static double euDistance(double array1[], double array2[]) {
		double Dist = 0.0;
		if (array1.length != array2.length) {
			System.out.println("the number of the arrary is ineql");
		}
		
		for (int i = 0; i < array2.length; i++) {
			Dist += (array1[i] - array2[i]) * (array1[i] - array2[i]);
		}
		return Math.sqrt(Dist);
	}
	
	//to print the int Array
	private static void printArray(int array[]) {
		System.out.print('[');
		for (int i = 0; i < array.length; i++) {
			System.out.print(array[i]);
			if ((i + 1) < array.length) {
				System.out.print(", ");
			}
		}
		System.out.println(']');
	}
	
	//傳回一個M個元素組成的隨機整數陣列，其中每個元素的取值範圍從0到n-1
	public static int[] randperm(int N,int M){
		double[]  permF=new double[N];
		int[]     permI=new int[N];
		int[]     sampleResult=new int[M];
		double tempF;
		int    tempI;
		for(int i=0; i<N; i++){
			permF[i]=Math.random();
			permI[i]=i;			
		}
		//透過排序把陣列permI隨機化
		for(int i=0; i<N-1; i++){
			for(int j=i+1; j<N; j++){
				if(permF[i]<permF[j]){
					tempF=permF[i];
					tempI=permI[i];
					permF[i]=permF[j];
					permI[i]=permI[j];
					permF[j]=tempF;
					permI[j]=tempI;					
				}
			}
		}
		//取前m個值傳回
		for(int i=0; i<M; i++){
			sampleResult[i]=permI[i];
		}
		return sampleResult;
	}
	
	//the judge the equal two Array
	private static boolean isEqual(int Array1[],int Array2[]){
		for(int i=0; i<Array1.length; i++){
			if(Array1[i]!=Array2[i]){
				return false;
			}
		}
		return true;		
	}
	
	//get the location of min element from the Array
	private static int minLocation(double Array[]){
		int Location;
		double Min;
		//initial
		Min=Array[0];
		Location=0;
		//Iteration
		for(int i=1; i<Array.length; i++){
			if(Array[i]<Min){
				Location=i;
				Min=Array[i];			  
			}
		}
		return Location;
	}
	
	private static boolean isInArray(int[] Array,int elem){
		for(int i=0;i<Array.length;i++){
			if(Array[i]==elem){
				return true;
			}
		}
		return false;
	}
	
	//public static int[] GetInitCluster(){
	//	return CenterId;
	//}
	
	public static int[] minMaxInitCluster(double matrix[][],int row,int col,int clusterNum){
		int i,j,r,c;
		r=c=0; //所有對象中相距最遠的兩個對像編號
		int [] result=new int[clusterNum];//聚點結果陣列
		for(i=0;i<clusterNum;i++){
			result[i]=-2;
		}
		double[][]  distMatrix=new double[row][row];//距離矩陣
		double max=0.0;
		
		//發現所有對象中相距最遠的兩個對像
		for(i=0; i<row; i++){
			for( j=0; j<row; j++){
				//發現第i個和第j個對象之間的距離
				distMatrix[i][j]=euDistance(matrix[i],matrix[j]);
				distMatrix[j][i]=distMatrix[i][j];
				if(i>j){
					if(distMatrix[i][j]>max){
						max=distMatrix[i][j];
						r=i;
						c=j;
					}
				}
			}
		}
		
		int num=2;
		result[0]=r;
		result[1]=c;
		int next=-1; //記錄下一個聚點編號
		while(num<clusterNum){
			max=0.0;
			for(i=0;i<row;i++){
				if( !isInArray(result,i)){
					//找出和所有已知聚點最近的聚點中最遠的點
					double min=Double.MAX_VALUE;
					for(j=0;j<num;j++){
						if(distMatrix[i][result[j]]<min){
							min=distMatrix[i][result[j]];
						}
					}
					if(min>max){
						max=min;
						next=i;
					}
				}
			}
			result[num]=next;
			num++;
		}
		return result;
	}
	
	//to clustering the data Matrix
	public static int[] kCluster(double matrix[][], int clusterNum){
		int row = matrix.length;//行數，也就是點的個數
		int col = matrix[0].length;//列數，也就是特徵個數
		int[] centerId=new int[clusterNum];//初始聚點編號
    	int[]  cId=new int[row];//聚類結果
    	
    	int[]  oldCid=new int[row];//上次聚類結果
    	int[]  numOfEveryCluster=new int[clusterNum];
    	double[][]  clusterCenter=new double[clusterNum][col];//聚點
    	double[]  centerDist=new double[clusterNum];
    	//初始化聚類中心
    	centerId= minMaxInitCluster(matrix, row, col,clusterNum);
    	/*	System.out.println("Init cluster center is :");
    	for(int k=0;k<CenterId.length;k++){
    		System.out.print(CenterId[k]+" 	");
    	}*/
    	System.out.println();
    	for(int i=0; i<clusterNum; i++){
    		for(int j=0; j<col; j++){
    			 clusterCenter[i][j]=matrix[ centerId[i] ][j];    		
    		}
    	}
    	
    	int maxIter=100;//最大疊代次數
    	int iter=1;
    	
    	while( !isEqual(cId,oldCid) && iter < maxIter){
    		System.arraycopy(cId, 0, oldCid, 0, cId.length);
    		
    		//檢查每個點，發現它到每一個聚點的距離
    		for(int i=0;i<row;i++){
    			for(int j=0; j<clusterNum;j++){
    				centerDist[j]=euDistance(matrix[i], clusterCenter[j] );
    			}
    			//將點歸類給距離最近的簇
    			cId[i]=minLocation(centerDist);    			
    		}
    		
    		//得到每個簇擁有的點數
    		for(int j=0; j<clusterNum; j++){
    			numOfEveryCluster[j]=0;
    			for(int i=0; i<row; i++){
    				if(cId[i]==j){
    					numOfEveryCluster[j]++;    					
    				}    			
    		    }
    		}
    		
    		//計算新的聚點
    		//求和
    		for(int j=0; j<clusterNum; j++){
    			for(int k=0; k<col; k++){
    				clusterCenter[j][k]=0.0;
    				for(int i=0; i<row; i++){
    					if(cId[i]==j){
    						clusterCenter[j][k]+=matrix[i][k];
    					}
    				}
    			}
    	    }
       	    //求平均值
       	    for(int j=0; j<clusterNum; j++){
       	    	for(int k=0; k<col; k++){
       	    		clusterCenter[j][k]=clusterCenter[j][k]/(double)numOfEveryCluster[j];
       	    	}
       	    }
       		++iter;//疊代次數
    	}
    	
    	return cId;
    }
    	
    //main to test the KMeans
  public static void main(String[] args) {
    	int Matrix_row;
    	int Matrix_col;
    	int ClusterNum;
    	Matrix_col=1000;
    	Matrix_row=1000;
    	ClusterNum=15;
		double[][]  Matrix = new double[Matrix_row][Matrix_col];
		int[]  List=new int[Matrix_row];
	
		for(int i=0; i<Matrix_row; i++){
			for(int j=0; j<Matrix_col; j++){
				Matrix[i][j]=10*Math.random();
			}
		}
		
	    List=kCluster(Matrix, ClusterNum);
	    System.out.println("The result of clustering, value of No.i means the ith belong to the No.value cluster");
	    printArray(List);
	}
}