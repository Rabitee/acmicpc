import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class P2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // the number of cases, n
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++) {

            int totalSkillPoint = Integer.parseInt(br.readLine());
            int numberOfSkills = Integer.parseInt(br.readLine());
            int[][] skills = new int[numberOfSkills][2];
            for(int j=0; j<numberOfSkills; j++) {
                String[] line = br.readLine().split(" ");
                for(int k=0; k<2; k++) skills[j][k] = Integer.valueOf(line[k]);
            }
            System.out.println(Arrays.deepToString(skills));
            System.out.println(Arrays.toString(solution(totalSkillPoint, skills)));
        }

    }

    public static int[] solution(int total_sp, int[][] skills) {
        int max = -1;
        for(int i=0; i<skills.length; i++) {
            for(int j=0; j<2; j++) {
                if(skills[i][j] > max) max = skills[i][j];
            }
        }

        
        int[] count = new int[max+1];
        for(int i=0; i<skills.length; i++) {
            count[skills[i][0]]++;
        }

        
        for(int i=0; i<count.length; i++) {
            if(count[i] == 0) count[i] = 1;
        }

       
        int[] totalCount = new int[max+1];
        for(int i=0; i<skills.length; i++) {
            totalCount[skills[i][0]] += count[skills[i][1]];
        }

        
        int sum = 0;
        for(int i=1; i<totalCount.length; i++) {
            if(totalCount[i] == 0) totalCount[i] = 1;
            sum += totalCount[i];
        }
        int factor = total_sp / sum;

        for(int i=1; i<totalCount.length; i++) {
            totalCount[i] *= factor;
        }

        int[] solution = new int[max];
        for(int i=0; i<solution.length; i++) {
            solution[i] = factor * totalCount[i+1];
        }

        return solution;
    }
}
