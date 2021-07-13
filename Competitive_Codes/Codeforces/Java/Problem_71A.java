//way too long words https://codeforces.com/problemset/problem/71/A
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Problem_71A {

	public static void main(String[] args){
		FastScanner fs = new FastScanner();
		int t = fs.nextInt();
		for(int tt=0 ; tt<t; tt++) {
			
			String line = fs.next().toString();
			int a = line.length();
			System.out.println(line.charAt(0));
			if(a>10) {
				char start = line.charAt(0);
				char end = line.charAt(a);
				System.out.print(start);
				System.out.print(a-2);
				System.out.print(end);
				System.out.println();
			}
			else {
				System.out.println(line);
			}
		}
	}

	static void sort(int[] a){
		ArrayList<Integer> l = new ArrayList<Integer>();
		for(int i : a) l.add(i);
		Collections.sort(l);
		for(int i = 0 ; i< a.length; i++) a[i] = l.get(i);
	}

	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try { 
                        st=new StringTokenizer(br.readLine());				               
                    } catch (IOException e) {}
			return st.nextToken();
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		long nextLong() {
			return Long.parseLong(next());
		}
	}
}

