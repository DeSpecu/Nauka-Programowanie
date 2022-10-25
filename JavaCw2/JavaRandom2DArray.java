package JavaCw2;

import java.util.Random;

public class JavaRandom2DArray {

    public static void main(String[] args) {
        int n =50;
        double[][] wartosci = new double[4][n];
        double pomoc;
        Random rand = new Random();
        
        double otwarcie = 40 + (70-40) * rand.nextDouble();
        
        wartosci[0][0]=otwarcie;
        wartosci[1][0]=(otwarcie-otwarcie*0.03) + ((otwarcie+otwarcie*0.03)-(otwarcie-otwarcie*0.03)) * rand.nextDouble();
        do{
            wartosci[2][0]=(otwarcie-otwarcie*0.05) + ((otwarcie+otwarcie*0.05)-(otwarcie-otwarcie*0.05)) * rand.nextDouble();
        }
        while(wartosci[1][0]<wartosci[2][0]);
        
        do{
            wartosci[3][0]=(otwarcie-otwarcie*0.05) + ((otwarcie+otwarcie*0.05)-(otwarcie-otwarcie*0.05)) * rand.nextDouble();
        }
        while(wartosci[1][0]>wartosci[3][0]);

        if(wartosci[2][0]>wartosci[3][0])
            {
                pomoc = wartosci[2][0];
                wartosci[2][0] = wartosci[3][0];
                wartosci[3][0] = pomoc;
            }
        
        
        for(int i=1;i<wartosci[0].length;i++)
        {
            double otwarcieNext = wartosci[1][i-1];
            wartosci[0][i]= otwarcieNext;
            wartosci[1][i]=(otwarcieNext-otwarcieNext*0.03) + ((otwarcieNext+otwarcieNext*0.03)-(otwarcieNext-otwarcieNext*0.03)) * rand.nextDouble();
            do{
                wartosci[2][i]=(otwarcieNext-otwarcieNext*0.05) + ((otwarcieNext+otwarcieNext*0.05)-(otwarcieNext-otwarcieNext*0.05)) * rand.nextDouble();
            }
            while(wartosci[1][i]<wartosci[2][i]);

            do{
                wartosci[3][i]=(otwarcieNext-otwarcieNext*0.05) + ((otwarcieNext+otwarcieNext*0.05)-(otwarcieNext-otwarcieNext*0.05)) * rand.nextDouble();
            }
            while(wartosci[1][i]>wartosci[3][i]);
            if(wartosci[2][i]>wartosci[3][i])
            {
                pomoc = wartosci[2][i];
                wartosci[2][i] = wartosci[3][i];
                wartosci[3][i] = pomoc;
            }
        }

        for(int i=1; i<wartosci[0].length;i++)
        {
            System.out.println("Open: "+wartosci[0][i]);
            System.out.println("Close: "+wartosci[1][i]);
            System.out.println("Min: "+wartosci[2][i]);
            System.out.println("Max: "+wartosci[3][i]);
        }
            
    }
    
}
