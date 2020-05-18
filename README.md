# yandex-back-test

Тестовое задание в Яндекс.Практикум

## Задание

**Задача 1.** Даны два списка, вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения.

**Задача 2.** Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) дополнительной памяти.

## Решение

**Задача 1.** Для нахождения разниц во множествах идеально подходит `set`. Превратить `list` в `set` - `O(len(list))`. Опреция вычитания (разница множеств) - `O(len(left))` - то есть зависит от длины множества, из которого вычитаем. Превратить множество обратно в список - `O(len(set))`. Итоговая сложность решения - `O(max(left, right))`, иными словами `O(N)`- линейная.

**Задача 2.** Реализация за линейное время (как алгоритм из STL - `std::remove_if`). Неподходящие элементы смещаем в конец, после прохода по всему списку - делаем срез до того индекса, куда перемещали подходящие элементы.
  