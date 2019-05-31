import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class CityParser {
    public static List<City> parseFile(String filename) {
        ArrayList<City> cities = new ArrayList<City>();

        //try-with-resources to read the file
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            line = br.readLine(); // Skip the first line
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                cities.add(new City(
                        Integer.parseInt(parts[0]),
                        parts[1],
                        Integer.parseInt(parts[2]),
                        Float.parseFloat(parts[3]),
                        Float.parseFloat(parts[4])
                ));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return cities;
    }
}