package it.polimi;
import java.util.List;

public class Batch1 {
    interface I {
        public List<String> query(String dataset);
    }

    public static void main(String[] args) {
        Execute exe = new Execute();
        exe.init(args);

        String twitter_small = "twitter_small_records.json";
        String bestbuy_small = "bestbuy_small_records.json";
        String walmart_small = "walmart_small_records.json";

        exe.execute(twitter_small, Query::TT1, "TT1");
        exe.execute(twitter_small, Query::TT2, "TT2");
        exe.execute(twitter_small, Query::TT3, "TT3");
        exe.execute(twitter_small, Query::TT4, "TT4");

        exe.execute(walmart_small, Query::WM, "WM");

        exe.execute(bestbuy_small, Query::BB, "BB");
    }
}