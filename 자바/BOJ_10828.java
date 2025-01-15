import java.io.*;
import java.util.*;
public class BOJ_10828{
	public static void main(String args[]) throws IOException{
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int bae[] = new int[n];
		int size = 0;
		for(int i =0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			String s = st.nextToken();
			if (s.equals("push")) {
				bae[size] = Integer.parseInt(st.nextToken());
				size++;
			}else if(s.equals("pop")) {
//				System.out.println("size = " + size);
				if (size == 0) {
					System.out.println(-1);
					continue;
				}
				System.out.println(bae[size-1]);
				size --;
			}else if(s.equals("size")) {
				System.out.println(size);
			}else if(s.equals("empty")) {
				if (size == 0) {
					System.out.println(1);
				}else {
					System.out.println(0);
				}
			}else if(s.equals("top")) {
				if (size == 0) {
					System.out.println(-1);
					continue;
				}
				System.out.println(bae[size-1]);
			}
		}
	}
}
