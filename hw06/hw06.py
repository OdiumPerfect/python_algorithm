from random import randint
from pympler import asizeof, tracker
tr = tracker.ObjectTracker()
tr_1 = tracker.SummaryTracker()
def task_2_1(i):
    a = [x for x in range(i * 4)]
    a[1] = 0
    m = 2
    while m < i * 4:
        if a[m] != 0:
            j = m * 2
            while j < i * 4:
                a[j] = 0
                j = j + m
        m += 1
    b = [x for x in a if x != 0]
    return b[i - 1]


print(asizeof.asizeof(task_2_1(10)))




def task_3():
    rand_list = [randint(1, 100) for x in range(10)]
    print(rand_list)
    idx_max = rand_list.index(max(rand_list))
    idx_min = rand_list.index(min(rand_list))
    rand_list[idx_max], rand_list[idx_min] = rand_list[idx_min], rand_list[idx_max]
    print(rand_list)

tr.print_diff()
tr_1.print_diff()

# Вторая функция более затратна, происходит генерация более крупного списка и более крупная работа с ним.