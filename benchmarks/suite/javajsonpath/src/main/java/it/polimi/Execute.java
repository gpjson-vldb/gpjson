package it.polimi;

import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Execute {
    private int warmup = 5;
    private int repeat = 10;
    private String baseDir = "/home/ubuntu/datasets/";

    public void execute(String dataset, Batch1.I func, String query) {
        List<String> result = new ArrayList();
        for (int i=0; i < warmup; i++)
            result = func.query(baseDir + dataset);
        int numResults = result.size();
        long start = 0;
        double[] delays = new double[repeat];
        for (int i=0; i < repeat; i++) {
            start = System.currentTimeMillis();
            func.query(baseDir + dataset);
            delays[i] = System.currentTimeMillis() - start;
        }
        double average = Arrays.stream(delays).sum() / repeat;
        double std = Math.sqrt(Arrays.stream(delays).reduce(0, (tot, elem) -> tot + (elem-average)*(elem-average) / (repeat-1)));
        System.out.println("javajsonpath,"+baseDir+dataset+","+query+","+average+","+std+","+numResults+","+warmup+","+repeat);
    }

    public void init(String[] args) {
        for (int i=0; i<args.length; i++) {
            if (args[i].contains("datasets=")) {
                this.baseDir = args[i].substring(9);
            }
            else if (args[i].contains("warmup=")) {
                warmup = Integer.parseInt(args[i].substring(7));
            }
            else if (args[i].contains("repeat=")) {
                repeat = Integer.parseInt(args[i].substring(7));
            }
            else if (args[i].contains("threads=")) {
                System.setProperty("java.util.concurrent.ForkJoinPool.common.parallelism", args[i].substring(8));
            }
        }
    }
}
