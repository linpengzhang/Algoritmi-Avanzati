public class SerialClustering{
    
    private int get_min_centroid(List<City> centroid, City min){
        int min_distance = centroid[0].get_distance(min);
        int pos = 0;
        for(int i=1; i < centroid.size(); i++){
            if(centroid[i].get_distance(min) < min_distance){
                min_distance = centroid[i].get_distance(min);
                pos = i;
            }
        }
        return pos;
    }

    private center(List<City> cities){
        
    }

    public k_means_clustering(List<City> cities, int clust_number, int iterations){
        int number_of_cities = cities.size();

        List<City> centroid = cities.stream().sorted(Comparator.comparing(City::get_city_population)).limit(clust_number).toList();

        for(int i=0; i < iterations; i++){
            List<List<City>>> clusters = new ArrayList<List<City>>(clust_number);

            for(int j = 0; j < number_of_cities; j++){
                int min_pos = get_min_centroid(centroid, cities[j]);

                clusters[min_pos].append(cities[j]);
            }

            for(int j = 0 ; j < clust_number; j++){
                centroid[j] = 
            }
        } 
    }
}