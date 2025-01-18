import java.io.*;
import java.util.*;
public class BOJ_20546 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int money = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int data[] = new int[14];
		for(int i = 0; i<14; i++) {
			data[i] = Integer.parseInt(st.nextToken());
		}
		int jm = money;
		int jj = 0;
		//준현 로직
		for(int i = 0; i<14; i++) {
			int n = jm/data[i];
			jj+= n;
			jm = jm%data[i];
//			System.out.println(n);
//			System.out.println(jm);
		}
//		System.out.println((jm + (jj*data[13])));
		//성민 로직
		int sm = money;
		int sj = 0;
		int harak = 0;
		int sangsoong = 0;
//		int rst = 0;
		for(int i = 0; i<13; i++) {
//			if (sm < data[i]) {
//				//1
//				continue;
//			}
			if (i >=1) {
				if (data[i-1]<data[i]) {
					//상승
					sangsoong += 1;
					harak = 0;
				}else if(data[i-1]>data[i]){
					//하락
					sangsoong = 0;
					harak += 1;
				}
				if (sangsoong == 3) {
					sangsoong -= 1;
					harak = 0;
//					System.out.println("i = " + i);
					sm += data[i]*sj;
					sj = 0;
					
				}else if(harak == 3) {
					sangsoong = 0;
					harak -= 1;
					if (sm > data[i]) {
//						System.out.println("[i] = " + i);
						sj += sm/data[i];
						sm = sm%data[i];
//						System.out.println("sm/data[i] " + sm/data[i]);
					}
				}
			}
		}
//		System.out.println("sm = " + sm);
//		System.out.println("sj = " + sj);
		
//		System.out.println(sm+(sj*data[13]));
		
		if(jm + (jj*data[13])>(sm+(sj*data[13]))) {
			System.out.println("BNP");
		}else if(jm + (jj*data[13])<(sm+(sj*data[13]))) {
			System.out.println("TIMING");
		}else {
			System.out.println("SAMESAME");
		}
		
	}

}
