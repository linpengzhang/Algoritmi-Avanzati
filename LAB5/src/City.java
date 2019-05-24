public class City{
    private int city_id;
    private String city_name;
    private int city_population:
    private float city_latitude:
    private float city_longitude:

    public City(int id, String name, int pop, float lat, float lon){
        city_id = id;
        city_name = name;
        city_population = pop;
        city_latitude = lat;
        city_longitude = lon;
    }

    public int get_city_id(){
        return city_id;
    }

    public String get_city_name(){
        return city_name;
    }

    public int get_city_population(){
        return city_population;
    }

    public float get_city_latitude(){
        return city_latitude;
    }

    public float get_city_longitude(){
        return city_longitude;
    }

    private int truncate_to_int(float val){
        DecimalFormat df = new DecimalFormat("##");
        df.setRoundingMode(RoundingMode.DOWN);
        return (int) df.format(val);
    }

    private float convert_to_rad(float val){
        int int_val = truncate_to_int(val);
        return Math.PI * ((int_val + 5.0f * (val - int_val)) / 3.0f ) / 180.0f
    }

    public int get_distance(City other){
        DecimalFormat df = new DecimalFormat("##");
        df.setRoundingMode(RoundingMode.DOWN);

        float this_lat = convert_to_rad(city_latitude);
        float this_lon = convert_to_rad(city_longitude);
        float other_lat = convert_to_rad(other.city_latitude);
        float other_lon = convert_to_rad(other.city_longitude);

        float q1 = Math.cos(this_lon - other_lon);
        float q2 = Math.cos(this_lat - other_lat);
        float q3 = Math.cos(this_lat + other_lat);

        return truncate_to_int(6378.388 * Math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)
    }
}