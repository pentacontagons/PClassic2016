import java.util.*;
import java.io.*;
public class SudokuSolver {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new FileReader("SudokuSolverIN.txt"));
        
        int[][] puzzle = new int[9][9];
        
        while(sc.hasNext()) {
        	for(int i = 0; i < 9; i++) {
        		for(int j = 0; j < 9; j++) {
        			puzzle[i][j] = sc.nextInt();
        		}
        	}
        	
        	puzzle = sudokuSolve(puzzle);
        	
        	for(int i = 0; i < 9; i++) {
        		for(int j = 0; j < 9; j++) {
        			if(j < 8) {
        				System.out.print(puzzle[i][j] + " ");
        			} else {
        				System.out.println(puzzle[i][j] + " ");
        			}
        		}
        	}
        	
        	System.out.println("");
        	
        }
    }
    
    public static int[][] sudokuSolve(int[][] puzzle) {
    	int c = 0;
    	int[][] z = new int[2][15];
    	ArrayList<ArrayList<Integer>> fals = new ArrayList<ArrayList<Integer>>();
    	for (int i = 0; i < 9; i++){
    		for (int j = 0; j < 9; j++){
    			if (puzzle[i][j] == 0){
    				z[0][c] = i;
    				z[1][c] = j;
    				c++;
    			}
    		}
    	}
    	for (int i = 0; i < c; i++){
    		if (!(check(puzzle, z[0][i], z[1][i])>0)){
    			ArrayList<Integer> temps = new ArrayList<Integer>();
    			temps.add(z[0][i]);
    			temps.add(z[1][i]);
    			fals.add(temps);
    		}
    		else{
    			puzzle[z[0][i]][z[1][i]]=check(puzzle, z[0][i], z[1][i]);
    		}
    	}
    	while (fals.size()>0){
    		for(int i = 0; i < fals.size(); i++){
    			if(check(puzzle, fals.get(i).get(0), fals.get(i).get(1)) > 0){
    				puzzle[fals.get(i).get(0)][fals.get(i).get(1)]=check(puzzle, fals.get(i).get(0), fals.get(i).get(1));
    				fals.remove(i);
    			}
    		}
    	}
    	return puzzle;
    }
    public static int check(int[][] puzzle, int i, int j){
    	int[] temp = {1,2,3,4,5,6,7,8,9};
    	ArrayList<Integer> zz = new ArrayList<Integer>();
    	for(int l = 0; l < 9; l++){
    		for(int k = 0; k < 9; k++){
    			if(puzzle[i][l] == temp[k]){
    				temp[k] = 0;
    			}
    			if(puzzle[l][j] == temp[k]){
    				temp[k] = 0;
    			}
    		}
    	}
    	int ii = i/3;
    	ii = ii * 3;
    	int jj = j/3;
    	jj = jj * 3;
    	for(int l = 0; l < 3; l++){
    		for(int m = 0; m < 3; m++){
    			for(int k = 0; k<9; k++){
        			if(puzzle[l+ii][m+jj] == temp[k]){
        				temp[k] = 0;
        			}
    			}
    		}
    	}
    	for(int k = 0; k<9;k++){
    		if(temp[k]>0){
    			zz.add(temp[k]);
    		}
    	}
    	if (zz.size() == 1){
    		return zz.get(0);
    	}
    	else{
    		return 0;
    	}
    }
    
}
