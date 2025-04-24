class Solution {
    public int maxProfit(int[] prices) {
        // List<Integer> l2rMin = new ArrayList<>();
        // IntStream.range(0, prices.length).forEach(i -> {
        //     if (i == 0) l2rMin.add(prices[0]);
        //     else l2rMin.add(Math.min(l2rMin.get(i - 1), prices[i]));
        // });

        // // Right-to-left maximum list
        // List<Integer> r2lMax = new ArrayList<>(Collections.nCopies(prices.length, 0));
        // for (int i = prices.length - 1; i >= 0; i--) {
        //     if (i == prices.length - 1) r2lMax.set(i, prices[i]);
        //     else r2lMax.set(i, Math.max(r2lMax.get(i + 1), prices[i]));
        // }

        // // Zip and calculate max profit
        // return IntStream.range(0, prices.length)
        //         .map(i -> r2lMax.get(i) - l2rMin.get(i))
        //         .max()
        //         .orElse(0);


        List<Integer> l2rMin = new ArrayList<>();
        IntStream.range(0, prices.length).forEach(i -> {
            if(i==0) l2rMin.add(prices[0]);
            else l2rMin.add(Math.min(prices[i], l2rMin.get(i-1)));
        });

        List<Integer> r2lMax = new ArrayList<>();
        for(int i =prices.length-1; i>=0; i--) {
            if (i==prices.length-1) r2lMax.add(prices[i]);
            else r2lMax.add(Math.max(prices[i], r2lMax.get(prices.length - 2 - i)));
        }
        Collections.reverse(r2lMax);

        return IntStream.range(0, prices.length)
                .map( i-> r2lMax.get(i)-l2rMin.get(i))
                .max()
                .orElse(0);
    }
}

