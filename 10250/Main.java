// https://www.acmicpc.net/problem/10250

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int T = 0;
		
		try(BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)))
		{
			T = Integer.parseInt(bf.readLine());
			for(int i=0; i<T; i++)
			{
				int H = 0, W = 0, N = 0;
				StringTokenizer st = new StringTokenizer(bf.readLine());
				H = Integer.parseInt(st.nextToken());
				W = Integer.parseInt(st.nextToken());
				N = Integer.parseInt(st.nextToken());
				
				
				int x = N / H;
				int y = N % H;
				
				if(y == 0)
				{
					x = x - 1;
					y = H;
				}
				if(H >= N)
				{
					y = N;
				}
				System.out.printf("%d%02d\n", y, x + 1);
			}
		}
		catch(IOException e)
		{
			
		}
	}

}
