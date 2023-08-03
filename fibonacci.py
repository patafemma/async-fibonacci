import sys
from random import random
from asyncio import sleep, run, gather
from typing import Callable, Coroutine, TypeVar
from time import time

T = TypeVar("T")

MAX_DELAY_SEC = 1.0


async def fib(n: int) -> int:
    """Get a number from fibonacci sequence, iterative implementation"""
    await sleep(random() * MAX_DELAY_SEC)
    if n < 0:
        raise Exception("n must be positive")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n2, n1 = 0, 1
        for _ in range(n - 1):
            result = n1 + n2
            n2, n1 = n1, result

    return result


async def recursive_fib(n: int) -> int:
    """Get a number from fibonacci sequence, recursive implementation"""
    await sleep(random() * MAX_DELAY_SEC)
    if n < 0:
        raise Exception("n must be positive")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n2, n1 = await gather(recursive_fib(n - 2), recursive_fib(n - 1))
        return n2 + n1


async def with_run_time(coro: Coroutine[any, any, T]) -> tuple[T, float]:
    """Execute a coroutine and return its result and run time"""
    t0 = time()
    return await coro, time() - t0


def get_positive_int() -> int:
    """Get positive integer from stdin"""
    n = 0
    while n <= 0:
        try:
            n = int(input("Input a positive integer (greater than 0):"))
        except EOFError:
            exit(0)
        except:
            pass

    return n


async def run_concurrent_fib(fib_func: Callable[[int], int]):
    """Run given fibonacci function twice concurrently and print results"""
    n = get_positive_int()
    func_name = fib_func.__name__

    print(f'Calling function "{func_name}(n={n})" concurrently...')
    timed_results = await gather(with_run_time(fib_func(n)), with_run_time(fib_func(n)))

    print(f"Result: {timed_results[0][0]}")
    for i, (_, run_time) in enumerate(timed_results):
        print(f"Call #{i} returned in {run_time:.3f} seconds")

    fastest_result = min(timed_results, key=lambda result: result[1])
    fastest_result_idx = timed_results.index(fastest_result)
    print(f"Call #{fastest_result_idx} finished first")


if __name__ == "__main__":
    fib_func = recursive_fib if "--recursive" in sys.argv else fib
    run(run_concurrent_fib(fib_func))
