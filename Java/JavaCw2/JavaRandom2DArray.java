/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package javaapplication1;

import java.util.Random;
/**
 *
 * @author Student8
 */
public class JavaApplication1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int n =50;
        double[][] wartosci = new double[4][n];
        
        Random rand = new Random();
        
        double otwarcie = 40 + (70-40) * rand.nextDouble();
        
        wartosci[0][1]=otwarcie;
        wartosci[0][2]=(otwarcie-otwarcie*0.03) + ((otwarcie+otwarcie*0.03)-(otwarcie-otwarcie*0.03)) * rand.nextDouble();
        wartosci[0][3]=(otwarcie-otwarcie*0.05) + ((otwarcie+otwarcie*0.05)-(otwarcie-otwarcie*0.05)) * rand.nextDouble();
        wartosci[0][4]=(otwarcie-otwarcie*0.05) + ((otwarcie+otwarcie*0.05)-(otwarcie-otwarcie*0.05)) * rand.nextDouble();
        
        for(int i=0;i<wartosci.length(1);i++)
        {
            wartosci[0][i]= 40 + (70-40) * rand.nextDouble();
            
        }
            
    }
    
}
