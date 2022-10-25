package JavaCw2;

import java.util.Random;

public class JavaRandom2DArray {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int n =50;
        double[][] wartosci = new double[4][n];
        
        Random rand = new Random();
        
        double otwarcie = 40 + (70-40) * rand.nextDouble();
        
        wartosci[0][0]=otwarcie;
        wartosci[1][0]=(otwarcie-otwarcie*0.03) + ((otwarcie+otwarcie*0.03)-(otwarcie-otwarcie*0.03)) * rand.nextDouble();
        wartosci[2][0]=(otwarcie-otwarcie*0.05) + ((otwarcie+otwarcie*0.05)-(otwarcie-otwarcie*0.05)) * rand.nextDouble();
        wartosci[3][0]=(otwarcie-otwarcie*0.05) + ((otwarcie+otwarcie*0.05)-(otwarcie-otwarcie*0.05)) * rand.nextDouble();
        if(wartosci[2][0]>wartosci[3][0])
            {
                double pomoc = wartosci[2][0];
                wartosci[2][0] = wartosci[3][0];
                wartosci[3][0] = pomoc;
            }
        for(int i=1;i<wartosci[0].length;i++)
        {
            double otwarcieNext = wartosci[1][i-1];
            wartosci[0][i]= otwarcieNext;
            wartosci[1][i]=(otwarcieNext-otwarcieNext*0.03) + ((otwarcieNext+otwarcieNext*0.05)-(otwarcieNext-otwarcieNext*0.05)) * rand.nextDouble();
            wartosci[2][i]=(otwarcieNext-otwarcieNext*0.05) + ((otwarcieNext+otwarcieNext*0.05)-(otwarcieNext-otwarcieNext*0.05)) * rand.nextDouble();
            wartosci[3][i]=(otwarcieNext-otwarcieNext*0.05) + ((otwarcieNext+otwarcieNext*0.05)-(otwarcieNext-otwarcieNext*0.05)) * rand.nextDouble();
            if(wartosci[2][i]>wartosci[3][i])
            {
                double pomoc = wartosci[2][i];
                wartosci[2][i] = wartosci[3][i];
                wartosci[3][i] = pomoc;
            }
        }
            
    }
    
}
