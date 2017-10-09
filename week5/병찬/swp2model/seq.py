import typecheck as tc
from llist import dllist
import collections


class RecurrenceSeq:
    @tc.typecheck
    def __init__(self, *init_terms, calc: callable, init_idx: int):
        '''
        :param init_terms:
            Initial terms. _calc requires init_terms to calculate
            the next term of this explicit Initial terms.

        :param calc:

            :param #0: next index
            :param #1:
                Part of consecutive terms that will be used in calculating the next term;
                In other words, material of recurrence relation.
            :return next term

        :param init_idx:
            Initial index. The index of init_terms[0] is interpret as _init_idx.
            No limitation exists except its type is int. Even being negative is allowed logically.

        :type calc: (int, tuple) -> Any; with only positional args.
        '''

        self._init_idx = init_idx
        self._idx = init_idx
        self._part_terms = dllist(init_terms)
        self._calc = calc

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def part_terms(self) -> dllist:
        return self._part_terms

    @part_terms.setter
    @tc.typecheck
    def part_terms(self, part_terms: collections.Iterable):
        self._part_terms = dllist(part_terms)

    def chk_rel_idx(self) -> (int, bool):
        '''
        Relative index is logical virtual current index on the assumption seeing as if _init_idx = 0
        :return: relative index and whether the element of current index is in init_terms
        :rtype: (int, bool)
        '''
        rel_idx = self._idx - self._init_idx
        return (rel_idx, rel_idx < len(self._part_terms))

    def current(self):
        '''
        :return sequence value on current index
        '''
        rel_idx_chked = self.chk_rel_idx()
        if rel_idx_chked[1]:
            node = self._part_terms.nodeat(rel_idx_chked[0])
        else:
            node = self._part_terms.last
        return node.value

    def next(self):
        '''
        calculate next term,
        and increase current index.
        '''
        self._idx += 1
        rel_idx_chked = self.chk_rel_idx()
        if not rel_idx_chked[1]:
            next_val = self._calc(self._idx, tuple(self._part_terms))
            self._part_terms.appendright(next_val)
            self._part_terms.popleft()
        return self.current()

    @tc.typecheck
    def get(self, idx: int):
        '''
        :param idx: index to get value
        :return sequence value on the given index
        :raise ValueError if given index is less than current index of the object
        '''
        if self._idx > idx:
            raise ValueError("Current _idx is larger than the given _idx; current %d, given %d"
                             % (self._idx, idx))
        for i in range(self._idx, idx):
            self.next()
        return self.current()


@tc.typecheck
def fibo_recur(n: int) -> int:
    if n < 0:
        raise ValueError("The term index 'n' have to be positive integer.")
    return n if n <= 1 else fibo_recur(n - 1) + fibo_recur(n - 2)


@tc.typecheck
def fibo_iter(n: int) -> int:
    rseq = RecurrenceSeq(0, 1, calc=lambda nextidx, parts: sum(parts), init_idx=0)
    return rseq.get(n)
