import java.io.IOException;
import java.io.*;
public class BOJ_4659 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			String tmp = br.readLine();
			if (tmp.equals("end")) {
				break;
			}
			char rst[] = new char[tmp.length()];
			for(int i =0; i<tmp.length(); i++) {
				rst[i] = tmp.charAt(i);
			}
			char prev = tmp.charAt(0);
			int m = 0;
			int j = 0;
			boolean real = true;
			boolean mouen = false;
			for(int i = 0; i<tmp.length(); i++) {
				if (rst[i] == 'a' || rst[i] == 'e' || rst[i] == 'i' || rst[i] == 'o' || rst[i] == 'u') {
					mouen = true;
					m ++;
					j=0;
					if (m>=3) {
						//실패
						real = false;
						break;
					}
				}
				else {
					j++;
					m=0;
					if (j>=3) {
						real = false;
						break;
					}
				}
				if (i>=1) {
					if(rst[i] == rst[i-1]&&rst[i]!='e'&&rst[i]!='o') {
						real = false;
						break;
					}
				}
			}
			if (real == true && mouen == true) {
				System.out.println("<"+tmp+">"+" is acceptable.");
			}else {
				System.out.println("<"+tmp+">"+" is not acceptable.");
			}
//			tmp = br.readLine()
//			System.out.println("tmp = " + tmp);
		}
	}
}
