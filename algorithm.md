# algorithm


## 複雜度

|             | Array  | Linked list
|-------------|--------|-------------
|記憶體配置    | 連續   |  不連續
|記憶體使用    | 彈性小 |  彈性大
|讀取資料速度  | O(1)   | O(N)
|插入資料      | O(N)   | O(N) + O(1)
|刪除資料      | O(N)   | O(N) + O(1)


|           | Stack | Queue | Binary Search Tree |Heap | Hash
|-----------|------|--------|--------|-------|----------
|找資料     |  O(N)  |  O(N)   | O(log(N)) |  O(1)      |  O(1)-O(N)
|差資料     |  O(1) |  O(1)    | O(log(N)) |  O(log(N)) |  O(1)-O(N)
|刪(取)資料 |  O(1) |  O(1) | O(log(N))  |  O(log(N))   |  O(1)-O(N)

- Hash 遇到碰撞就有可能會是 O(N)

###

- Quesiton: 從某個頂點出發到另一個頂點所經過的臨邊權重和最小路徑，稱為最短路徑
    - Dijkstra 演算法
    - Floyd 演算法
    - SPFA 演算法