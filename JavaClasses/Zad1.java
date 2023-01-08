package JavaClasses;

class Punkt3D{

    int x, y, z;

    public Punkt3D(){
        x=0;
        y=0;
        z=0;
    }

    public Punkt3D(int x, int y, int z){
        this.x=x;
        this.y=y;
        this.z=z;
    }

    public int getX(){
        return x;
    }

    public int getY(){
        return y;
    }

    public int getZ(){
        return z;
    }

    public void setX(int x){
        this.x = x;
    }

    public void setY(int y){
        this.y = y;
    }

    public void setZ(int z){
        this.z = z;
    }

    public double odlegosc(){
        double result;
        result = Math.pow(x,2)+Math.pow(y,2)+Math.pow(z,2);
        return java.lang.Math.sqrt(result);
    }
}

public class Zad1 {
    public static void main(String[] args){

        Punkt3D d = new Punkt3D(1,2,3);
        double wynik = d.odlegosc();
        System.out.println(wynik);
    }
    
}
