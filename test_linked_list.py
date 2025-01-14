import pytest
import linked_list as l


def test_create_linked_list():
    new_linked_list = l.LinkedList()
    assert new_linked_list


def test_create_and_insert_single_value_into_linked_list():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(20)
    assert new_linked_list
    assert new_linked_list.head.val == 20


def test_insert_at_start():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(1)
    new_linked_list.insert_at_start(2)
    new_linked_list.insert_at_start(3)
    new_linked_list.insert_at_start(4)
    new_linked_list.insert_at_start(5)
    assert new_linked_list
    assert new_linked_list.head.val == 5
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 4
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 3
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 2
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 1


def test_insert_at_end():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_end(1)
    new_linked_list.insert_at_end(2)
    new_linked_list.insert_at_end(3)
    assert new_linked_list
    assert new_linked_list.head.val == 1
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 2
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 3
    new_linked_list.head = new_linked_list.head.next


def test_insert_at_start_and_end():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(1)
    new_linked_list.insert_at_end(2)
    new_linked_list.insert_at_start(3)
    assert new_linked_list
    assert new_linked_list.head.val == 3
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 1
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 2
    new_linked_list.head = new_linked_list.head.next


def test_insert_after_item():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(1)
    new_linked_list.insert_at_start(2)
    new_linked_list.insert_at_start(3)  # 3 2 1
    new_linked_list.insert_after_item(2, 4)  # 3 2 4 1
    assert new_linked_list
    assert new_linked_list.head.val == 3
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 2
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 4
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 1
    new_linked_list.head = new_linked_list.head.next


def test_insert_before_item():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(1)
    new_linked_list.insert_at_start(2)
    new_linked_list.insert_at_start(3)  # 3 2 1
    new_linked_list.insert_before_item(2, 4)  # 3 4 2 1
    assert new_linked_list
    assert new_linked_list.head.val == 3
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 4
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 2
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 1
    new_linked_list.head = new_linked_list.head.next


def test_insert_at_index():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(1)
    new_linked_list.insert_at_start(2)
    new_linked_list.insert_at_start(3)
    new_linked_list.insert_at_start(4)
    new_linked_list.insert_at_start(5)  # 5 4 3 2 1
    new_linked_list.insert_at_index(3, 6)
    assert new_linked_list
    assert new_linked_list.head.val == 5
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 4
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 3
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 6
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 2
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 1


def test_insert_all_functions():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_end(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.insert_at_start(20)
    new_linked_list.insert_after_item(10, 17)
    new_linked_list.insert_before_item(17, 25)
    new_linked_list.insert_at_index(2, 8)
    assert new_linked_list.get_count() == 7
    assert new_linked_list
    assert new_linked_list.head.val == 20
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 5
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 8
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 10
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 25
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 17
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 15


def test_delete_at_start_and_end():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.insert_at_end(20)
    new_linked_list.insert_at_end(25)
    new_linked_list.delete_at_start()
    new_linked_list.delete_at_end()
    new_linked_list.delete_element_by_value(15)
    assert new_linked_list
    assert new_linked_list.head.val == 10
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 20


def test_reverse_linkedlist():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.insert_at_end(20)
    new_linked_list.insert_at_end(25)
    new_linked_list.reverse_linkedlist()
    assert new_linked_list
    assert new_linked_list.head.val == 25
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 20
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 15
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 10
    new_linked_list.head = new_linked_list.head.next
    assert new_linked_list.head.val == 5
    new_linked_list.head = new_linked_list.head.next


def test_check_if_palindrome():
    new_linked_list = l.LinkedList()
    new_linked_list.insert_at_start(5)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(15)
    new_linked_list.insert_at_end(20)
    new_linked_list.insert_at_end(25)
    new_linked_list.insert_at_end(20)
    new_linked_list.insert_at_end(15)
    new_linked_list.insert_at_end(10)
    new_linked_list.insert_at_end(5)
    check = new_linked_list.check_if_palindrome()
    assert check
    new_linked_list.delete_at_start()
    assert new_linked_list.head.val == 10
    check = new_linked_list.check_if_palindrome()
    assert not check
    new_linked_list.delete_at_end()
    check = new_linked_list.check_if_palindrome()
    assert check
