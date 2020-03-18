import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) {
    
        int N = 0;
        int last = 0;
        int cnt = 1;
        int[][] l = null;
        try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in)))
        {
            N = Integer.parseInt(br.readLine());
            l = new int[N][2];
            for(int i=0; i<N; i++)
            {
                StringTokenizer st = new StringTokenizer(br.readLine());
                l[i][0] = Integer.parseInt(st.nextToken());
                l[i][1] = Integer.parseInt(st.nextToken());
            }
        }
        catch(IOException e)
        {

        }

        Arrays.sort(l, new Comparator<int[]>() {
           public int compare(int[] o1, int[] o2)
           {
               if(o1[1] == o2[1])
               {
                   return Integer.compare(o1[0], o2[0]);
               }
               else
               {
                   return Integer.compare(o1[1], o2[1]);
               }
           }
        });

        last = l[0][1];
        if(l[0][0] == l[0][1])
        {
            cnt = 0;
        }

        for(int[] e : l)
        {
            if(last <= e[0])
            {
                last = e[1];
                cnt++;
            }
        }

        System.out.println(cnt);
    }
}