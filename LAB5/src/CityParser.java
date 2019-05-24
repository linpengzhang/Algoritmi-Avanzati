import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class CityParser{
    public static ArrayList<City> parseFile(String filename){
        ArrayList<City> cities = new ArrayList<City>();

        //read file into stream, try-with-resources
		try (Stream<String> stream = Files.lines(Paths.get(filename))) {
			String line;
            br.readLine();
			while ((line = br.readLine()) != null) {
				String[] parts = string.split(",");
                cities.append(new City(parts[0], parts[1], parts[2], parts[3], parts[4]))
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

        return cities;
    }
}