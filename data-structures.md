# data-structures

## stack

- 序列資料結構
- First In Last Out (FILO)
- method
    - push
    - pop
    - peek
- 用途
    - Undo/Redo
    - 網頁上一頁
    - call stack

- 問題
    - array, linking list 實作 stack

## queue

- 序列資料結構
- First In First Out (FIFO)
- method
    - enqueue, 加進 queue
    - dequeue, 拿出 queue
- 用途
    - 搶票
    - 工作排程
- 問題
    - array, linking list 實作 queue

## tree

- 沒有迴路
- 一棵樹中任意兩個節點只有唯一個路徑
- 種類
    - 二元樹
    - 紅黑樹
- 問題
    - levle order: 由上往下，由左往右
    - in order: 由左往右，由上往下
    - pre order: 每次都先從左邊走到底，再走右邊
    - post order: 每次都先走最下面的點，在由左往右

## heap

- 一種完全二元樹
- 所有 parent node 一定比 child node 小
- 種類
    - 最小堆積 (min heap), python heapq
    - 最大堆積 (max heap)

## hash

- 透過 hash function 壓縮資料，建立 hash table(key, value 概念)
- 常用 hash function mod
- 碰撞解法 collison
    - close addressing: collison 發生，在同一個 key 對應到的 value 建立順序清單 linking list
    - open addressing: collison 發生，往其他 key 來找空的 value
        - linear probing，像是單純往下找
        - quadratic，類似 linear
        - double hashing，hash 裡面再建 hask
- 用途
    - map
    - 密碼
    - 檔案較驗碼，ex:md5, sha-1