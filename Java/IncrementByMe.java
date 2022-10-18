package Java;

import java.util.Scanner;
public class IncrementByMe {
    public static String Increment(String s)
    {
        int i = s.length();
        char c = s.charAt(i-1);
        if(c!='9'){
            c += 1;
            String end = s.substring(0, i-1);
            return end+c;
        }
        
        else{
            String nowys="";
            for(int j=0; j<s.length();j++){
                char ch=s.charAt(j);
                nowys=ch+nowys;
            }
            char[] litery = nowys.toCharArray();


            for(int y=0; y<litery.length;y++){
                if(litery[y]=='9')
                    litery[y]='0';
                else{
                    litery[y]+=1;
                    break;
                }
            }
            
            String wyjscie="";
            for(int j=0; j<litery.length;j++){
                char ch = litery[j];
                wyjscie=ch+wyjscie;
            }
            if(litery[litery.length-1]=='0'){
                wyjscie = '1'+wyjscie;
            }
            return wyjscie;
        }
    }
    
    public static void main(String[] args) {

        Scanner wejscie = new Scanner(System.in);
        String liczba = wejscie.nextLine();
        System.out.println(Increment(liczba));
        wejscie.close();
       
    }
    
}
