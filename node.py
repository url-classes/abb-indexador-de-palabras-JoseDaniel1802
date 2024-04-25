from typing import Generic, TypeVar, Literal

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def hos_children(self) -> Literal["left", "right", "both", "none"]:
        if self.left is None and self.right is None:
            return "none"
        elif self.left is not None and self.right is not None:
            return "both"
        elif self.left is not None and self.right is None:
            return "left"
        elif self.left is None and self.right is not None:
            return "right"

    def __str__(self):
        return str(self.data)