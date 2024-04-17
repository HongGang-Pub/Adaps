import concurrent.futures


def thread_function(age):
    # return  age + 1
    print(age)
    for i in age:
        yield i+1

def run_thread_pool(target, args, max_work_count=6):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_work_count) as t:
        res = t.map(target, args)
        return res

if __name__ == '__main__':
    ages = [1, 3, 4]
    # 2222
    res = run_thread_pool(target=thread_function, args=(ages,))
    for j in res:
        for i in j:
            print (i)