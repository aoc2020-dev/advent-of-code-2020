from part1_parallel import LayoutSimulation
import timeit
import math

if __name__ == "__main__":
    with open("input", "r") as input:
        layout = input.read().splitlines()

        rounds = 11
        num_rows = len(layout)
        max_pow = int(math.log(num_rows, 2))
        size_steps = [1 << x for x in range(max_pow)]

        if size_steps[-1] < num_rows:
            size_steps.append(num_rows)

        time_table = dict()

        i = 1
        while i <= rounds:
            print("Round:", i)
            for num_workers in size_steps:
                for chunk_size in size_steps:
                    step_key = str(num_workers) + "," + str(chunk_size)

                    start = timeit.default_timer()
                    LayoutSimulation(layout, num_workers, chunk_size).simulate_until_stable()
                    stop = timeit.default_timer()

                    exec_time = stop - start

                    if step_key not in time_table:
                        time_table[step_key] = [exec_time]
                    else:
                        time_table[step_key].append(exec_time)
            i += 1

        print("== REPORT ========")
        for key in time_table:
            nmw, chn = key.split(",")
            time_list = time_table[key]

            print(f"nmw={nmw}, chn={chn} exec_times={time_list} (avg={sum(time_list)/len(time_list)})")
