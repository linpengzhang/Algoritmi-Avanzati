
import java.math.RoundingMode;
import java.text.DecimalFormat;
public class Point{
    private float latitude;
    private float longitude; 
    public Point(float lat, float lon){
        latitude = lat;
        longitude = lon;
    }
    public float getLatitude(){
        return latitude;
    }
    public float getLongitude(){
        return longitude;
    }
    public void setLat(float lat){
        latitude = lat;
    }
    public void setLon(float lon){
        longitude = lon;
    }
        private int truncateToInt(float val) {
        DecimalFormat df = new DecimalFormat("##");
        df.setRoundingMode(RoundingMode.DOWN);
        return Integer.parseInt(df.format(val));
    }

    private int truncateToInt(double val) {
        return truncateToInt((float) val);
    }

    private float convertToRad(float val) {
        int intVal = truncateToInt(val);
        return ((float) Math.PI) * ((intVal + 5.0f * (val - intVal)) / 3.0f) / 180.0f;
    }

    public int getDistance(Point other) {
        float thisLat = convertToRad(latitude);
        float thisLon = convertToRad(longitude);
        float otherLat = convertToRad(other.latitude);
        float otherLon = convertToRad(other.longitude);

        double q1 = Math.cos(thisLon - otherLon);
        double q2 = Math.cos(thisLat - otherLat);
        double q3 = Math.cos(thisLat + otherLat);

        return truncateToInt(6378.388 * Math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0);
    }
}