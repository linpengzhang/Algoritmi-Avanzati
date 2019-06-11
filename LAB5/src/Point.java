public class Point {
    private double latitude;
    private double longitude;

    public Point(double lat, double lon) {
        latitude = lat;
        longitude = lon;
    }

    public double getLatitude() {
        return latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    public void setLatitude(double lat) {
        latitude = lat;
    }

    public void setLongitude(double lon) {
        longitude = lon;
    }

    private double convertToRad(double val) {
        int intVal = (int) val;
        return (Math.PI) * ((intVal + 5.0d * (val - intVal)) / 3.0d) / 180.0d;
    }

    public int getDistance(Point other) {
        double thisLat = convertToRad(latitude);
        double thisLon = convertToRad(longitude);
        double otherLat = convertToRad(other.latitude);
        double otherLon = convertToRad(other.longitude);

        double q1 = Math.cos(thisLon - otherLon);
        double q2 = Math.cos(thisLat - otherLat);
        double q3 = Math.cos(thisLat + otherLat);

        return (int)(6378.388 * Math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0);
    }
}