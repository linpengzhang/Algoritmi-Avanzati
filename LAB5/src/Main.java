public class Main{
    public static void main(String[] args){
        ArrayList<City> cities = CityParser.parseFile("inputFiles/cities-and-towns-of-usa.csv");

        List<City> cities_250 = cities
            .stream()
            .filter(c -> c.get_city_population() > 250)
            .collect(Collectors.toList());

        List<City> cities_2000 = cities
            .stream()
            .filter(c -> c.get_city_population() > 2000)
            .collect(Collectors.toList());

        List<City> cities_5000 = cities
            .stream()
            .filter(c -> c.get_city_population() > 5000)
            .collect(Collectors.toList());

        List<City> cities_15000 = cities
            .stream()
            .filter(c -> c.get_city_population() > 15000)
            .collect(Collectors.toList());

        List<City> cities_50000 = cities
            .stream()
            .filter(c -> c.get_city_population() > 50000)
            .collect(Collectors.toList());

        List<City> cities_100000 = cities
            .stream()
            .filter(c -> c.get_city_population() > 100000)
            .collect(Collectors.toList());
    }
}