import java.io.*;
import java.util.Stack;
public class BOJ_3986 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int cnt = 0;
		for(int i =0; i<n; i++) {
			String s = br.readLine();
			char data[] = new char[s.length()];
			for(int j =0; j<s.length(); j++) {
				data[j] = s.charAt(j);
			}
			Stack<Character> ta = new Stack<>();
//			char rst[] = new char[s.length()];
			for(int j =0; j<s.length(); j++) {
				if (ta.size()>0&&ta.peek() == data[j]) {
					ta.pop();
				}else {
					ta.push(data[j]);
				}
			}
			if (ta.size() == 0) {
				cnt += 1;
			}
		}
		System.out.println(cnt);
	}

}
