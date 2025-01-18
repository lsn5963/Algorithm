import java.io.*;
import java.util.*;
public class BOJ_9375 {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		for(int i = 0; i<tc; i++) {
			int n = Integer.parseInt(br.readLine());
			Map<String,Integer> m = new HashMap<>();
			for(int j = 0; j<n; j++) {
				StringTokenizer st = new StringTokenizer(br.readLine()," ");
				String a = st.nextToken();
				String b = st.nextToken();
				if (m.containsKey(b)) {
					m.put(b,m.get(b)+1);
				}else {
					m.put(b,1);
				}
			}
			int answer = 1;
			for(int rst : m.values()) {
				answer *= (rst+1);
			}
			System.out.println(answer-1);
		}
	}

}
