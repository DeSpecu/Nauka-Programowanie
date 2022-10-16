package Java;

import java.util.Random;
import java.util.Scanner;

public class StringGen{

    public static void main(String[] Args){

            Scanner wejscie = new Scanner(System.in);
            
            String linia = wejscie.nextLine();
            char c;
            Random rand = new Random();
            int dlugosc,litera;
            String slowo="";
            String[] listaSlow = {};
            do{
                dlugosc = rand.nextInt(1,21);
                for(int i=0; i<dlugosc;i++)
                {
                    litera = rand.nextInt(97,123);
                    slowo+=litera;
                }
                System.out.println("Czy" + slowo + "jest słowem? t/n");
                linia = wejscie.nextLine();
                while (linia.length()!=1){
                    System.out.print("Podaj t lub n");
                    linia = wejscie.nextLine();
                }
                c = linia.charAt(0);
                for(String s : listaSlow){
                    if(slowo==s){
                        break;
                    }
                }
            }
            while(c=='t');
            wejscie.close();

            

    }
}