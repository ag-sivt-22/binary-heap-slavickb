#! /usr/bin/env python

from dataclasses import dataclass
from typing import Any


@dataclass
class Element:
    value: Any
    priority: int


class BinaryHeap:
    """Implementace binární haldy, která začíná nejmenší hodnotou"""
    def __init__(self) -> None:
        self.heap: list[Element] = []

    def push(self, element: Element) -> None:
        self.heap.append(element)
        self._trickle_up(len(self.heap) - 1)

    def pop(self) -> Element:
        if not self.heap:
            raise Exception("Heap is empty")
        if len(self.heap) == 1:     # v pythonu lze porovnávat malé integery i pomocí is, ale bylo by to programátorské zvěrstvo - nelze však popřít že by to bylo rychlejší
            return self.heap.pop()

        vysledek = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._trickle_down(0)

        return vysledek

    def head(self) -> Element:
        if not self.heap:
            raise Exception("Heap is empty")
        return self.heap[0]

    def _trickle_up(self, index: int) -> None:
        if index == 0:
            return
        parent_index: int = (index - 1) // 2
        if self.heap[index].priority < self.heap[parent_index].priority:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._trickle_up(parent_index)

    def _trickle_down(self, index: int) -> None:
        heap_size = len(self.heap)
        smallest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < heap_size and self.heap[left_child_index].priority < self.heap[smallest].priority:
            smallest = left_child_index

        if right_child_index < heap_size and self.heap[right_child_index].priority < self.heap[smallest].priority:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._trickle_down(smallest)
