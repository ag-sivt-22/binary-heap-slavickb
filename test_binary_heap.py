from binary_heap import BinaryHeap, Element


def push(heap: BinaryHeap, priority: int) -> None:
    heap.push(Element(priority, priority))


def test_push() -> None:
    heap = BinaryHeap()
    push(heap, 5)
    assert heap.head().priority == 5
    push(heap, 8)
    assert heap.head().priority == 5
    push(heap, 4)
    assert heap.head().priority == 4
    push(heap, 7)
    assert heap.head().priority == 4
    push(heap, 10)
    assert heap.head().priority == 4
    push(heap, 2)
    assert heap.head().priority == 2


def test_push_pop() -> None:
    heap = BinaryHeap()
    push(heap, 5)
    push(heap, 8)
    push(heap, 4)
    assert heap.pop().priority == 4
    assert heap.head().priority == 5

    # another push round
    push(heap, 7)
    push(heap, 10)
    push(heap, 2)
    assert heap.pop().priority == 2
    assert heap.pop().priority == 5
    assert heap.pop().priority == 7
    assert heap.pop().priority == 8
    assert heap.pop().priority == 10
