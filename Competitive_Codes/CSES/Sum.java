import java.util.*;
public class Sum{
	public static void main(String[] args){
		Long n;
		Scanner cin = new Scanner(System.in);
		n = cin.nextLong();
		System.out.print(n);
	while(n>1){
		if(n%2==0)
			n/=2;
		else
			n=3*n+1;
		System.out.print(" " + n);
	}
	}
}