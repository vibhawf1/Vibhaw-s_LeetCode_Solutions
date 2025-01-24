class Solution:
    def find_profit(self, graph: Dict[str, List[Tuple[str, int]]], source: str) -> Dict[str, float]:
        dist = defaultdict(lambda : 0)
        if source not in graph:
            return dist
        
        dist[source] = 1
        pq = [(-dist[source], source)]

        while pq:
            w, u = heapq.heappop(pq)
            w = -w

            if dist[u] > w:
                continue

            for v, w_uv in graph[u]:
                if dist[v] < w * w_uv:
                    dist[v] = w * w_uv
                    heapq.heappush(pq, (-dist[v], v))

        return dist

    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        '''
        day1 -> 0+ conversions.
        day2 -> 0+ conversions.

        initialCurrency, 1 -> initialCurrency, x
        maximize x.

        profit = profit_day_1(initial_currency, some_currency) * profit_day_2(some_currency, initial_currency)

        We can try for all currency.
        Caution: If there is an arbitrage, then we can have infinite money.

        TC: V * (V * E)

        We always use modified Dijkstra, so as long as there are no cycles, we can find max path as well.
        TC: V * (V + E * logV)

        Improvement: Rather than trying for all currencies, compute max path in graph1 from source and in inverted graph2 from source.

        TC: (V + E * logV)
        '''
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        currencies = set()

        for i in range(len(pairs1)):
            u, v = pairs1[i]
            currencies.add(u)
            currencies.add(v)
            graph1[u].append((v, rates1[i]))
            graph1[v].append((u, 1 / rates1[i]))

        for i in range(len(pairs2)):
            u, v = pairs2[i]
            graph2[v].append((u, rates2[i]))
            graph2[u].append((v, 1 / rates2[i]))

        ans = 1

        dist1 = self.find_profit(graph1, initialCurrency)
        dist2 = self.find_profit(graph2, initialCurrency)
        
        for currency in currencies:
            ans = max(ans, dist1[currency] * dist2[currency])
        
        return ans
