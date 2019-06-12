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
        this.filename = filename;

        // Create Plot
        plot = new XYChartBuilder().width(600).height(500)
                .title(draw_title)
                .xAxisTitle(xAxisTitle)
                .yAxisTitle(yAxisTitle)
                .build();

        //Set legend position
        plot.getStyler().setLegendPosition(Styler.LegendPosition.InsideNE);
    }

    public void drawSeries(String name, List<Pair<Integer, Pair<Long, Long>>> values, boolean yIsKey) {
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
    }

    public void drawSeries(String name, List<Pair<Integer, Long>> values) {
        List<Integer> xPoints = new ArrayList<>(values.size());
        List<Long> yPoints = new ArrayList<>(values.size());
        for (Pair<Integer, Long> element : values) {
            xPoints.add(element.getKey());
            yPoints.add(element.getValue());
        }
        plot.addSeries(name, xPoints, yPoints);
    }

    public void saveToFile() {
        try {
            BitmapEncoder.saveBitmap(plot, filename, BitmapEncoder.BitmapFormat.PNG);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
