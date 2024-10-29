package it.polimi;

import com.jayway.jsonpath.Configuration;
import com.jayway.jsonpath.JsonPath;
import com.jayway.jsonpath.PathNotFoundException;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Stream;
import java.util.stream.Collectors;

public class Query {
    public static List<String> TT1(String dataset) {
        Stream<String> lines = null;
        try {
            lines = Files.lines(Paths.get(dataset)).parallel();
        } catch (IOException e) {
            System.out.println("Could not load dataset file.");
        }
        List<String> result = lines.flatMap((String x) -> {
            Object document = Configuration.defaultConfiguration().jsonProvider().parse(x);
            List<String> items = new LinkedList();
            try {
                String value = JsonPath.read(document, "$.user.lang");
                items.add(value);
            } catch (PathNotFoundException e) {}
            return items.stream();
            }).collect(Collectors.toList());
        return result;
    }

    public static List<String> TT2(String dataset) {
        Stream<String> lines = null;
        try {
            lines = Files.lines(Paths.get(dataset)).parallel();
        } catch (IOException e) {
            System.out.println("Could not load dataset file.");
        }
        List<String> result = lines.flatMap((String x) -> {
            Object document = Configuration.defaultConfiguration().jsonProvider().parse(x);
            List<String> items = new LinkedList();
            try {
                String value = JsonPath.read(document, "$.user.lang");
                items.add(value);
            } catch (PathNotFoundException e) {}
            try {
                String value = JsonPath.read(document, "$.lang");
                items.add(value);
            } catch (PathNotFoundException e) {}
            return items.stream();
        }).collect(Collectors.toList());
        return result;
    }

    public static List<String> TT3(String dataset) {
        Stream<String> lines = null;
        try {
            lines = Files.lines(Paths.get(dataset)).parallel();
        } catch (IOException e) {
            System.out.println("Could not load dataset file.");
        }
        List<String> result = lines.flatMap((String x) -> {
            Object document = Configuration.defaultConfiguration().jsonProvider().parse(x);
            List<String> value = new LinkedList();
            try {
                value = JsonPath.read(document, "$.user[?(@.lang == 'nl')].lang");
            } catch (PathNotFoundException | ClassCastException e) {}
            return value.stream();
        }).collect(Collectors.toList());
        return result;
    }

    public static List<String> TT4(String dataset) {
        Stream<String> lines = null;
        try {
            lines = Files.lines(Paths.get(dataset)).parallel();
        } catch (IOException e) {
            System.out.println("Could not load dataset file.");
        }
        List<String> result = lines.flatMap((String x) -> {
            Object document = Configuration.defaultConfiguration().jsonProvider().parse(x);
            List<String> value = new LinkedList();
            try {
                value = JsonPath.read(document, "$.user[?(@.lang == 'en')].lang");
            } catch (PathNotFoundException | ClassCastException e) {}
            return value.stream();
        }).collect(Collectors.toList());
        return result;
    }

    public static List<String> WM(String dataset) {
        Stream<String> lines = null;
        try {
            lines = Files.lines(Paths.get(dataset)).parallel();
        } catch (IOException e) {
            System.out.println("Could not load dataset file.");
        }
        List<String> result = lines.flatMap((String x) -> {
            Object document = Configuration.defaultConfiguration().jsonProvider().parse(x);
            List<String> items = new LinkedList();
            try {
                String value = JsonPath.read(document, "$.bestMarketplacePrice.price").toString();
                items.add(value);
            } catch (PathNotFoundException e) {}
            try {
                String value = JsonPath.read(document, "$.name");
                items.add(value);
            } catch (PathNotFoundException e) {}
            return items.stream();
        }).collect(Collectors.toList());
        return result;
    }

    public static List<String> BB(String dataset) {
        Stream<String> lines = null;
        try {
            lines = Files.lines(Paths.get(dataset)).parallel();
        } catch (IOException e) {
            System.out.println("Could not load dataset file.");
        }
        List<String> result = lines.flatMap((String x) -> {
        Object document = Configuration.defaultConfiguration().jsonProvider().parse(x);
        List<String> items = new LinkedList();
        try {
            items = JsonPath.read(document, "$.categoryPath[1:3].id");
        } catch (PathNotFoundException e) {}
        return items.stream();
        }).collect(Collectors.toList());
        return result;
    }
}
