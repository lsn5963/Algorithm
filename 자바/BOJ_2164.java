import java.io.*;
import java.util.*;
public class BOJ_2164 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		Deque<Integer> deque = new LinkedList<>();
		for(int i = 0; i < n; i++) {
			deque.addLast(i+1);
		}
		for(int i = 0; i< n; i++) {
			deque.removeFirst();
			if (deque.size()==0) {
				System.out.println(n);
				break;
			}
			if (deque.size()==1) {
				System.out.println(deque.removeLast());
				break;
			}
			int tmp = deque.removeFirst();
			deque.addLast(tmp);
		}
	}

}
