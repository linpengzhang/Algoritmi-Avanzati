import java.awt.Color;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class Main {
    public static void main(String[] args) {
        final int number_of_iter = 5;
        System.out.println("Script start");
        System.out.println("Parsing file...");
        List<City> cities = CityParser.parseFile("./inputFiles/cities-and-towns-of-usa.csv");
        System.out.println("Creating population arrays...");
        List<City> cities_250 = cities.stream().filter(c -> c.getPopulation() > 250).collect(Collectors.toList());
        List<City> cities_2000 = cities.stream().filter(c -> c.getPopulation() > 2000).collect(Collectors.toList());
        List<City> cities_5000 = cities.stream().filter(c -> c.getPopulation() > 5000).collect(Collectors.toList());
        List<City> cities_15000 = cities.stream().filter(c -> c.getPopulation() > 15000).collect(Collectors.toList());
        List<City> cities_50000 = cities.stream().filter(c -> c.getPopulation() > 50000).collect(Collectors.toList());
        List<City> cities_100000 = cities.stream().filter(c -> c.getPopulation() > 100000).collect(Collectors.toList());


        //test(A, B, cities_15000);
        List<Pair<Integer, List<City>>> cities_list = new ArrayList<>();
        cities_list.add(new Pair<>(250, cities_250));
        cities_list.add(new Pair<>(2000, cities_2000));
        cities_list.add(new Pair<>(5000, cities_5000));
        cities_list.add(new Pair<>(15000, cities_15000));
        cities_list.add(new Pair<>(50000, cities_50000));
        cities_list.add(new Pair<>(100000, cities_100000));
        cities_list.add(new Pair<>(38183, cities));

        List<Pair<Integer, Pair<Long, Long>>> values = new ArrayList<>();
        for (Pair<Integer, List<City>> couple: cities_list){
            long inizio = System.currentTimeMillis();
            List<List<City>> A = SerialClustering.kMeansClustering(couple.getValue(), 50, number_of_iter);
            long fine = System.currentTimeMillis();
            long seriale = fine - inizio;
            inizio = System.currentTimeMillis();
            List<Integer> B = new ParallelClustering().parallelKMeansClustering(couple.getValue(), 50, number_of_iter, 1);
            fine = System.currentTimeMillis();
            long parallelo = fine - inizio;
            Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
            Pair<Integer, Pair<Long, Long>> punto = new Pair<>(couple.getKey(), tempi);
            values.add(punto);
        }
        Plot plot = Plot.plot(null)
                            .series("Seriale", Plot.data()
                            .xy(values.get(0).getKey(), values.get(0).getValue().getKey())
                            .xy(values.get(1).getKey(), values.get(1).getValue().getKey())
                            .xy(values.get(2).getKey(), values.get(2).getValue().getKey())
                            .xy(values.get(3).getKey(), values.get(3).getValue().getKey())
                            .xy(values.get(4).getKey(), values.get(4).getValue().getKey())
                            .xy(values.get(5).getKey(), values.get(5).getValue().getKey())
                            .xy(values.get(6).getKey(), values.get(6).getValue().getKey())
                            , Plot.seriesOpts().marker(Plot.Marker.DIAMOND).markerColor(Color.BLACK).color(Color.BLUE));
        plot = plot
                            .series("Parallelo", Plot.data()
                            .xy(values.get(0).getKey(), values.get(0).getValue().getValue())
                            .xy(values.get(1).getKey(), values.get(1).getValue().getValue())
                            .xy(values.get(2).getKey(), values.get(2).getValue().getValue())
                            .xy(values.get(3).getKey(), values.get(3).getValue().getValue())
                            .xy(values.get(4).getKey(), values.get(4).getValue().getValue())
                            .xy(values.get(5).getKey(), values.get(5).getValue().getValue())
                            .xy(values.get(6).getKey(), values.get(6).getValue().getValue())
                            , Plot.seriesOpts().marker(Plot.Marker.DIAMOND).markerColor(Color.GREEN).color(Color.RED));
        try {
            plot.save("es1", "png");
        } catch (Exception e) {
            System.out.println(e);
        }

        //ES 2
        values = new ArrayList<>();
        for(int i=10;i<100;i++){
            long inizio = System.currentTimeMillis();
            List<List<City>> A = SerialClustering.kMeansClustering(cities, i, number_of_iter);
            long fine = System.currentTimeMillis();
            long seriale = fine - inizio;
            inizio = System.currentTimeMillis();
            List<Integer> B = new ParallelClustering().parallelKMeansClustering(cities, i, number_of_iter, 1);
            fine = System.currentTimeMillis();
            long parallelo = fine - inizio;
            Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
            Pair<Integer, Pair<Long, Long>> punto = new Pair<>(i, tempi);
            values.add(punto);
        }

        //ES 3
        values = new ArrayList<>();
        for(int i=10;i<1000;i++){
            long inizio = System.currentTimeMillis();
            List<List<City>> A = SerialClustering.kMeansClustering(cities, 50 , i);
            long fine = System.currentTimeMillis();
            long seriale = fine - inizio;
            inizio = System.currentTimeMillis();
            List<Integer> B = new ParallelClustering().parallelKMeansClustering(cities, 50, i, 1);
            fine = System.currentTimeMillis();
            long parallelo = fine - inizio;
            Pair<Long, Long> tempi = new Pair<>(seriale, parallelo);
            Pair<Integer, Pair<Long, Long>> punto = new Pair<>(i, tempi);
            values.add(punto);
        }
        //ES 4
        List<Pair<Integer, Long>> values_es_four = new ArrayList<>();
        for(int i=1;i<100;i++){
            long inizio = System.currentTimeMillis();
            List<Integer> B = new ParallelClustering().parallelKMeansClustering(cities, 50, number_of_iter, i);
            long fine = System.currentTimeMillis();
            Pair<Integer, Long> punto = new Pair<>(i, fine - inizio);
            values_es_four.add(punto);
        }
        /*
        //grafico
        Plot plotp = Plot.plot(null);
        Plot actual = plotp.series("lol", Plot.data().xy(3, 4).xy(5,9), Plot.seriesOpts().color(Color.red));
        plotp.series("lol2", Plot.data().xy(5, 4).xy(6,9), Plot.seriesOpts().color(Color.blue));

                
        try {
            plotp.save("sample_minimal", "png");
        } catch (Exception e) {
            System.out.println(e);
        }    
        */
    }

    private static void test(List<List<City>> clustering_1, List<Integer> clustering_2, List<City> cities){
        int clustNumber = clustering_1.size();
        List<List<City>> n_clustering_2 = new ArrayList<>();
        for (int j = 0; j < clustNumber; j++) {
            n_clustering_2.add(j, new ArrayList<City>());
        }
        for (int i = 0; i < clustering_2.size(); i++) {
            n_clustering_2.get(clustering_2.get(i)).add(cities.get(i));
        }

        for (int j = 0; j < clustNumber; j++) {
            int s1 = clustering_1.get(j).size();
            int s2 = n_clustering_2.get(j).size();
            if(s1 != s2)
                System.out.println("W: Cluster " + j + ": " + s1 + " - " + s2);
            else
                System.out.println("Cluster " + j + ": " + s1);
        }
    }
}