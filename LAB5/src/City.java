import java.math.RoundingMode;
import java.text.DecimalFormat;

public class City {
    private int cityId;
    private String cityName;
    private int cityPopulation;
    private float cityLatitude;
    private float cityLongitude;

    public City(int id, String name, int pop, float lat, float lon) {
        cityId = id;
        cityName = name;
        cityPopulation = pop;
        cityLatitude = lat;
        cityLongitude = lon;
    }

    public int getCityId() {
        return cityId;
    }

    public String getCityName() {
        return cityName;
    }

    public int getCityPopulation() {
        return cityPopulation;
    }

    public float getCityLatitude() {
        return cityLatitude;
    }

    public float getCityLongitude() {
        return cityLongitude;
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

    public int getDistance(City other) {
        float thisLat = convertToRad(cityLatitude);
        float thisLon = convertToRad(cityLongitude);
        float otherLat = convertToRad(other.cityLatitude);
        float otherLon = convertToRad(other.cityLongitude);

        double q1 = Math.cos(thisLon - otherLon);
        double q2 = Math.cos(thisLat - otherLat);
        double q3 = Math.cos(thisLat + otherLat);

        return truncateToInt(6378.388 * Math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0);
    }
}