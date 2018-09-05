import random
class Quick(object):
    def QuickSort(self, a):
        def partition(a, lo, hi):
            def exch(a, i, j):
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
                return a

            i = lo + 1
            j = hi
            while (True):
                while a[i] < a[lo]:
                    if i == hi: break
                    i += 1
                while a[j] > a[lo]:
                    if j == lo: break
                    j -= 1
                if i >= j: break
                exch(a, i, j)

            exch(a, lo, j)
            print(j, a)
            return j

        def sort(a, lo, hi):
            if hi <= lo: return a
            j = partition(a, lo, hi)
            sort(a, lo, j-1)
            sort(a, j+1, hi)

        a = random.sample(a, len(a))
        print("a:", a)
        sort(a, 0, len(a)-1)
        print(a)



a = range(15)
run = Quick()
run.QuickSort(a)

