import javafx.util.Pair;
import org.knowm.xchart.BitmapEncoder;
import org.knowm.xchart.XYChart;
import org.knowm.xchart.XYChartBuilder;
import org.knowm.xchart.style.Styler;

import java.util.ArrayList;
import java.util.List;

public class PlotManager {

    private String filename;
    private XYChart plot;

    public PlotManager(String draw_title, String filename) {
        this(draw_title, filename, "X", "Y");
    }
    public PlotManager(String draw_title, String filename, String xAxisTitle, String yAxisTitle) {
        this(draw_title, filename, xAxisTitle, yAxisTitle, 1000, 800);
    }

    public PlotManager(String draw_title, String filename, int width, int height) {
        this(draw_title, filename, "X", "Y", width, height);
    }

    public PlotManager(String draw_title, String filename, String xAxisTitle, String yAxisTitle, int width, int height) {
        this.filename = filename;

        // Create Plot
        plot = new XYChartBuilder().width(width).height(height)
                .title(draw_title)
                .xAxisTitle(xAxisTitle)
                .yAxisTitle(yAxisTitle)
                .build();

        //Set legend position
        plot.getStyler().setLegendPosition(Styler.LegendPosition.OutsideS);
    }

    public PlotManager drawSeries(String name, List<Pair<Integer, Pair<Long, Long>>> values, boolean yIsKey) {
        List<Integer> xPoints = new ArrayList<>(values.size());
        List<Long> yPoints = new ArrayList<>(values.size());
        for (Pair<Integer, Pair<Long, Long>> element : values) {
            xPoints.add(element.getKey());
            if (yIsKey) {
                yPoints.add(element.getValue().getKey());
            } else {
                yPoints.add(element.getValue().getValue());
            }
        }

        plot.addSeries(name, xPoints, yPoints);
        return this;
    }
    public PlotManager drawSeriesD(String name, List<Pair<Integer, Double>> values) {
        List<Integer> xPoints = new ArrayList<>(values.size());
        List<Double> yPoints = new ArrayList<>(values.size());
        for (Pair<Integer, Double> element : values) {
            xPoints.add(element.getKey());
            yPoints.add(element.getValue());
        }
        plot.addSeries(name, xPoints, yPoints);
        return this;
    }

    public PlotManager drawSeries(String name, List<Pair<Integer, Long>> values) {
        List<Integer> xPoints = new ArrayList<>(values.size());
        List<Long> yPoints = new ArrayList<>(values.size());
        for (Pair<Integer, Long> element : values) {
            xPoints.add(element.getKey());
            yPoints.add(element.getValue());
        }
        plot.addSeries(name, xPoints, yPoints);
        return this;
    }

    public void saveToFile() {
        try {
            BitmapEncoder.saveBitmap(plot, filename, BitmapEncoder.BitmapFormat.PNG);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
