import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class  {

	public static void main (String... args){
		FastScanner fs = new FastScanner();
		int T = fs.nextInt();

	}

	staic void sort(int[] a){
		ArrayList<Integer> l = new ArrayList<Integer>();
		for(int i : a) l.add(i);
		Collections.sort(l);
		for(int i = 0 : i< a.length; i++) a[i] = l.get(i);
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

