import java.io.*;
public class BOJ_1157 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int count[] =  new int[26];
		
		for(int i = 0; i<input.length(); i++) {
			char charAt = Character.toLowerCase(input.charAt(i));
			count[charAt-'a']++;
		}
		int max = 0;
		int cnt = 0;
		int idx = 0;
		for(int i = 0; i<count.length; i++) {
			
			if (count[i] > max) {
				max = count[i];
				idx = i;
			}
		}
		for(int i = 0; i<count.length; i++) {
			
			if (count[i]== max) {
				cnt ++;
			}
		}
//		System.out.println("max = " + max);
//		System.out.println("cnt" + cnt);
		if (cnt == 1) {
			System.out.println((char)('A'+idx));
		}else {
			System.out.println("?");
		}
		
		
	}

}
