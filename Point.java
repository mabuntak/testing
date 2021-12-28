public class Point {
    private int x;
    private int y;

    public Point() {
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public double distance()
    {
        return Math.sqrt(this.x*this.x+this.y*this.y);
    }

    public double distance(int bx, int by)
    {
        return Math.sqrt((bx-this.x)*(bx-this.x)+(by-this.y)*(by-this.y));
    }

    public double distance(Point xy)
    {
        return Math.sqrt((xy.x-this.x)*(xy.x-this.x)+(xy.y-this.y)*(xy.y-this.y));
    }


}


