import java.util.*;
public class Main{
	public static void main(String args[]){
	Scanner scan = new Scanner(System.in);
	int n=scan.nextInt();
	System.out.println(fib(n));
	}
	static int fib(int n){
	    if(n==1)
	    return 1;
	    else if(n==0)
	    return 0;
	    
	    return fib(n-1)+fib(n-2);
	}
}
