class Node:
    #класс представляет узел в связанном списке со значением данных и ссылкой на следующий узел
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    #функция перебирает связанный список и удаляет дубликаты, обновляя ссылку на текущий узел
    current = head
    while current.next:
        if current.data == current.next.data:
            temp = current.next
            current.next = current.next.next
            temp.next = None
        else:
            current = current.next


def print_list(head):
    #функци печатает значения узлов в связанном списке
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print("")


#пример создания и использования связанного списка
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(3)

print("До удаления дубликатов: ", end="")
print_list(head)

remove_duplicates(head)

print("После удаления дубликатов: ", end="")
print_list(head)
